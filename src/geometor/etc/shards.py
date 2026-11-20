"""Parallel exact-symbolic JSON shard builder for GEOMETOR ETC.

Compiles parsed ETC center HTML files across all 7 canonical reference triangles
using :mod:`geometor.etc.field_eval` into compact 100-center JSON shards,
a shared companion-center lookup table (``core-centers.json``), a fast search
index (``search-index.json``), and a manifest with exact projective collinearity
audit metrics (``manifest.json``).

Usage::

    uv run --no-sync python -m geometor.etc.shards --end 4000
    uv run --no-sync python -m geometor.etc.shards --end 53144
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import math
import multiprocessing
import re
import time
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from .field_eval import (
    _CANONICAL_TRIANGLE_ORDER,
    ExactCorpusResolver,
    ExactEvalResult,
    get_triangle_field,
)
from .parser import parse_center
from .transform import (
    THEMATIC_COLLECTIONS,
    _extract_primary_enunciation,
    get_collection_folder_name,
    get_collection_spec,
)

_REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_SPLIT_DIR = _REPO_ROOT / "resources" / "split"
DEFAULT_DATA_DIR = _REPO_ROOT / ".cache" / "etc_data"
SHARD_SIZE = 100


# ---------------------------------------------------------------------------
# Fork-Parallel Worker Helpers
# ---------------------------------------------------------------------------


_WORKER_CENTERS: dict[int, dict[str, Any]] = {}
_WORKER_CACHE_DIR: Path | None = None
_WORKER_CORPUS_SIG: str = ""


def _parse_one_split(path_str: str) -> dict[str, Any] | None:
    p = Path(path_str)
    return parse_center(p.read_text(encoding="utf-8"))


def _resolve_one_triangle(
    tri_key: str,
) -> tuple[str, dict[int, dict[str, Any]], dict[str, Any], dict[str, Any], float]:
    import gzip

    cache_path = (
        _WORKER_CACHE_DIR / f"{tri_key}.json.gz"
        if _WORKER_CACHE_DIR is not None
        else None
    )
    if cache_path is not None and cache_path.is_file():
        t_load = time.perf_counter()
        try:
            with gzip.open(cache_path, "rt", encoding="utf-8") as fh:
                cached = json.load(fh)
            sig = str(cached.get("sig") or "")
            if sig == _WORKER_CORPUS_SIG:
                packed_map = {int(k): v for k, v in cached["packed"].items()}
                dt_load = time.perf_counter() - t_load
                print(
                    f"[shards]   {tri_key:11s}: loaded {len(packed_map)} centers from checkpoint in {dt_load:.2f}s",
                    flush=True,
                )
                return (
                    tri_key,
                    packed_map,
                    cached["stats"],
                    cached.get("audit") or {},
                    cached["stats"].get("seconds", dt_load),
                )
            sig_m = re.match(r"^v2:n=(\d+):max=(\d+)$", sig)
            if sig_m:
                old_n = int(sig_m.group(1))
                packed_map = {int(k): v for k, v in cached["packed"].items()}
                if abs(len(_WORKER_CENTERS) - old_n) <= 50 and len(packed_map) >= int(
                    0.90 * len(_WORKER_CENTERS)
                ):
                    stale = [k for k in packed_map if k not in _WORKER_CENTERS]
                    for k in stale:
                        del packed_map[k]
                    # Patch newly recovered/fixed centers (e.g. upstream anchor typos)
                    patch_nums = {
                        k
                        for k in (57621, 57622, 60349, 68618, 71412)
                        if k in _WORKER_CENTERS
                    }
                    if patch_nums:
                        # Seed with nearby centers + core hubs so relations/incidences resolve cleanly
                        seed_nums = set(range(1, 250)) | patch_nums
                        for pn in patch_nums:
                            for inc in _WORKER_CENTERS[pn].get("incidences") or []:
                                for i_n, j_n in inc.get("lines") or []:
                                    if i_n in _WORKER_CENTERS:
                                        seed_nums.add(i_n)
                                    if j_n in _WORKER_CENTERS:
                                        seed_nums.add(j_n)
                        sub_centers = {k: _WORKER_CENTERS[k] for k in seed_nums if k in _WORKER_CENTERS}
                        sub_res = ExactCorpusResolver(sub_centers, tri_key).resolve_all()
                        include_search = tri_key == "kimberling"
                        for pn in patch_nums:
                            if pn in sub_res:
                                packed_map[pn] = _pack_eval_result(
                                    sub_res[pn], include_search=include_search
                                )
                    stats_new = {
                        "seconds": cached["stats"].get("seconds", 0.0),
                        "exact": sum(1 for v in packed_map.values() if v.get("p") == "e"),
                        "mp50": sum(1 for v in packed_map.values() if v.get("p") == "m"),
                        "indeterminate": sum(1 for v in packed_map.values() if v.get("st") == "0"),
                        "ideal": sum(1 for v in packed_map.values() if v.get("st") == "i"),
                        "unresolved": len(_WORKER_CENTERS) - len(packed_map),
                    }
                    tmp_path = cache_path.with_suffix(".gz.tmp")
                    with gzip.open(tmp_path, "wt", encoding="utf-8", compresslevel=3) as fh:
                        json.dump(
                            {
                                "sig": _WORKER_CORPUS_SIG,
                                "stats": stats_new,
                                "audit": cached.get("audit") or {},
                                "packed": {str(k): v for k, v in packed_map.items()},
                            },
                            fh,
                            separators=(",", ":"),
                            ensure_ascii=False,
                        )
                    tmp_path.replace(cache_path)
                    dt_load = time.perf_counter() - t_load
                    print(
                        f"[shards]   {tri_key:11s}: patched {len(patch_nums)} centers onto checkpoint in {dt_load:.2f}s",
                        flush=True,
                    )
                    return (
                        tri_key,
                        packed_map,
                        stats_new,
                        cached.get("audit") or {},
                        stats_new["seconds"],
                    )
        except (OSError, ValueError, KeyError):
            pass

    t0 = time.perf_counter()
    resolver = ExactCorpusResolver(_WORKER_CENTERS, tri_key)
    results = resolver.resolve_all()
    audit: dict[str, Any] = {}
    if tri_key in {"heronian", "kimberling"}:
        audit = resolver.audit_exact_collinearity(max_lines_per_center=4)

    include_search = tri_key == "kimberling"
    n_exact = 0
    n_mp = 0
    n_indet = 0
    n_ideal = 0
    packed: dict[int, dict[str, Any]] = {}
    for num, res in results.items():
        if res.precision == "exact":
            n_exact += 1
        elif res.precision == "mpmath-50":
            n_mp += 1
        if res.is_indeterminate:
            n_indet += 1
        if res.is_ideal:
            n_ideal += 1
        packed[num] = _pack_eval_result(res, include_search=include_search)

    dt = time.perf_counter() - t0
    stats = {
        "seconds": round(dt, 2),
        "exact": n_exact,
        "mp50": n_mp,
        "indeterminate": n_indet,
        "ideal": n_ideal,
        "unresolved": len(_WORKER_CENTERS) - len(results),
    }

    # Atomically persist per-triangle checkpoint so interrupted runs resume cleanly
    if cache_path is not None:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        tmp_path = cache_path.with_suffix(".gz.tmp")
        with gzip.open(tmp_path, "wt", encoding="utf-8", compresslevel=3) as fh:
            json.dump(
                {
                    "sig": _WORKER_CORPUS_SIG,
                    "stats": stats,
                    "audit": audit,
                    "packed": {str(k): v for k, v in packed.items()},
                },
                fh,
                separators=(",", ":"),
                ensure_ascii=False,
            )
        tmp_path.replace(cache_path)

    return (tri_key, packed, stats, audit, dt)


# ---------------------------------------------------------------------------
# Clean RST/LaTeX String Stripping for Client-Side Browser Rendering
# ---------------------------------------------------------------------------


_ROLE_REF_RE = re.compile(r":(?:ref|term|person|cite|doc|g):`([^`<]+?)(?:\s*<([^>]+)>)?`")
_MATH_ROLE_RE = re.compile(r":math:`([^`]+)`")
_SUP_ROLE_RE = re.compile(r":sup:`([^`]+)`")
_SUB_ROLE_RE = re.compile(r":sub:`([^`]+)`")
_X_PLAIN_RE = re.compile(r"\bX\((\d+)\)")


def _rst_to_display_text(text: str) -> str:
    """Convert RST inline markup cleanly into browser-ready plain text + TeX ``\\(...\\)``."""
    if not text:
        return ""
    s = text.replace("\\ ", " ").replace(r"\*", "*")
    s = _MATH_ROLE_RE.sub(lambda m: f"\\({m.group(1)}\\)", s)
    s = _ROLE_REF_RE.sub(lambda m: m.group(1).strip(), s)
    s = _SUP_ROLE_RE.sub(lambda m: f"^{m.group(1)}", s)
    s = _SUB_ROLE_RE.sub(lambda m: f"_{m.group(1)}", s)
    s = _X_PLAIN_RE.sub(r"X_\1", s)
    return " ".join(s.split()).strip()


def _coord_entry_to_json(raw_rst: str) -> dict[str, str]:
    """Extract clean formula LaTeX (or prose) + optional trailing where/attribution note."""
    s = raw_rst.strip()
    m = re.match(r"^:math:`([^`]+)`(.*)$", s, flags=re.DOTALL)
    if m:
        ltx = m.group(1).strip()
        tail = _rst_to_display_text(m.group(2).strip().lstrip(",; "))
        out: dict[str, str] = {"m": ltx}
        if tail:
            out["w"] = tail
        return out
    return {"t": _rst_to_display_text(s)}


def _round_xy(xy: tuple[float, float]) -> list[float] | None:
    if not (math.isfinite(xy[0]) and math.isfinite(xy[1])):
        return None
    return [round(xy[0], 6), round(xy[1], 6)]


def _round_bary(b: tuple[float, float, float]) -> list[float] | None:
    if not all(math.isfinite(v) for v in b):
        return None
    return [round(b[0], 7), round(b[1], 7), round(b[2], 7)]


def _pack_eval_result(res: ExactEvalResult, *, include_search: bool = False) -> dict[str, Any]:
    st = "0" if res.is_indeterminate else ("i" if res.is_ideal else "f")
    item: dict[str, Any] = {
        "p": "e" if res.precision == "exact" else "m",
        "st": st,
        "f": res.field_tag,
    }
    if st == "f":
        xy = _round_xy(res.approx_xy)
        if xy is not None:
            item["xy"] = xy
    b = _round_bary(res.approx_bary)
    if b is not None and st != "0":
        item["b"] = b
    if res.bary_latex:
        item["bl"] = res.bary_latex
    if res.trilinear_latex:
        item["tl"] = res.trilinear_latex
    if res.xy_latex:
        item["xyl"] = res.xy_latex
    if include_search and res.search_latex:
        item["sl"] = res.search_latex
    if include_search and math.isfinite(res.approx_search):
        item["sv"] = round(res.approx_search, 12)
    if res.symmetry_note:
        item["sn"] = res.symmetry_note
    return item


def _build_triangles_meta() -> dict[str, Any]:
    meta: dict[str, Any] = {}
    for key in _CANONICAL_TRIANGLE_ORDER:
        tf = get_triangle_field(key)
        meta[key] = {
            "key": key,
            "label": tf.label,
            "field": tf.field_latex,
            "sides": [round(tf.a.to_float(), 8), round(tf.b.to_float(), 8), round(tf.c.to_float(), 8)],
            "area": round(tf.area.to_float(), 8),
            "area_latex": tf.area.to_latex(),
            "verts": {
                "A": [round(tf.A_xy[0].to_float(), 8), round(tf.A_xy[1].to_float(), 8)],
                "B": [round(tf.B_xy[0].to_float(), 8), round(tf.B_xy[1].to_float(), 8)],
                "C": [round(tf.C_xy[0].to_float(), 8), round(tf.C_xy[1].to_float(), 8)],
            },
            "is_right": tf.is_right,
            "is_isosceles": tf.is_isosceles,
            "is_equilateral": tf.is_equilateral,
        }
    return meta


def build_shards(
    *,
    split_dir: Path = DEFAULT_SPLIT_DIR,
    output_dir: Path = DEFAULT_DATA_DIR,
    end: int = 4000,
    workers: int | None = None,
    core_hub_count: int = 600,
) -> dict[str, Any]:
    """Parse, evaluate across all 7 canonical triangles, verify, and emit compact JSON shards."""
    global _WORKER_CENTERS

    t_start = time.perf_counter()
    output_dir.mkdir(parents=True, exist_ok=True)
    shards_dir = output_dir / "shards"
    shards_dir.mkdir(parents=True, exist_ok=True)

    all_files = sorted(split_dir.glob("x-*.html"))
    if end > 0:
        all_files = all_files[:end]
    total_files = len(all_files)
    max_workers = workers or min(8, multiprocessing.cpu_count() or 4)
    print(f"[shards] Parsing {total_files} center HTML files using {max_workers} workers...", flush=True)

    t0 = time.perf_counter()
    centers_by_num: dict[int, dict[str, Any]] = {}
    file_strs = [str(p) for p in all_files]
    if total_files > 200:
        mp_ctx = multiprocessing.get_context("fork")
        with concurrent.futures.ProcessPoolExecutor(
            max_workers=max_workers, mp_context=mp_ctx
        ) as pool:
            for cdata in pool.map(_parse_one_split, file_strs, chunksize=128):
                if cdata and cdata.get("num"):
                    centers_by_num[int(cdata["num"])] = cdata
    else:
        for fs in file_strs:
            cdata = _parse_one_split(fs)
            if cdata and cdata.get("num"):
                centers_by_num[int(cdata["num"])] = cdata
    t_parse = time.perf_counter() - t0
    print(f"[shards] Parsed {len(centers_by_num)} centers in {t_parse:.2f}s.", flush=True)

    # Evaluate all 7 canonical triangles concurrently via fork (zero serialization overhead!)
    global _WORKER_CACHE_DIR, _WORKER_CORPUS_SIG
    _WORKER_CENTERS = centers_by_num
    _WORKER_CACHE_DIR = output_dir / "tri_cache"
    _WORKER_CORPUS_SIG = f"v2:n={len(centers_by_num)}:max={max(centers_by_num) if centers_by_num else 0}"
    tri_results: dict[str, dict[int, dict[str, Any]]] = {}
    tri_stats: dict[str, dict[str, Any]] = {}
    collinearity_audits: dict[str, Any] = {}

    t1 = time.perf_counter()
    mp_ctx = multiprocessing.get_context("fork")
    worker_errors: list[tuple[str, BaseException]] = []
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=min(len(_CANONICAL_TRIANGLE_ORDER), max_workers),
        mp_context=mp_ctx,
    ) as pool:
        futs = {pool.submit(_resolve_one_triangle, tk): tk for tk in _CANONICAL_TRIANGLE_ORDER}
        for fut in concurrent.futures.as_completed(futs):
            tk_req = futs[fut]
            try:
                tk, packed_map, stats, audit, dt = fut.result()
            except Exception as exc:  # noqa: BLE001
                import traceback

                print(f"[shards] ERROR in triangle {tk_req!r}: {exc!r}", flush=True)
                traceback.print_exc()
                worker_errors.append((tk_req, exc))
                continue
            tri_results[tk] = packed_map
            tri_stats[tk] = stats
            if audit:
                collinearity_audits[tk] = audit
            n_exact = stats["exact"]
            n_mp = stats["mp50"]
            n_indet = stats["indeterminate"]
            n_ideal = stats["ideal"]
            n_miss = stats["unresolved"]
            print(
                f"[shards]   {tk:11s}: {dt:6.2f}s | exact={n_exact:5d} ({100*n_exact/max(1,len(centers_by_num)):5.1f}%) "
                f"| mp50={n_mp:5d} | indet={n_indet:5d} | ideal={n_ideal:5d} | miss={n_miss:5d}",
                flush=True,
            )
    if worker_errors:
        failed_names = ", ".join(tk for tk, _ in worker_errors)
        raise RuntimeError(f"Triangle evaluation failed for: {failed_names}") from worker_errors[0][1]
    t_eval = time.perf_counter() - t1
    print(f"[shards] Resolved all 7 canonical triangles in {t_eval:.2f}s wall-clock.", flush=True)

    # Identify top referenced companion hub centers for shared core-centers.json
    partner_freq: Counter[int] = Counter()
    center_lines_map: dict[int, list[list[int]]] = {}
    for num, cdata in centers_by_num.items():
        lines_list: list[list[int]] = []
        seen_l: set[tuple[int, int]] = set()
        for inc in cdata.get("incidences") or []:
            for i_n, j_n in inc.get("lines") or []:
                pair = (min(i_n, j_n), max(i_n, j_n))
                if pair not in seen_l:
                    seen_l.add(pair)
                    lines_list.append([pair[0], pair[1]])
                    partner_freq[pair[0]] += 1
                    partner_freq[pair[1]] += 1
        center_lines_map[num] = lines_list
        for rel in cdata.get("relations") or []:
            for xm in re.finditer(r"\bX[\(_](\d+)", rel):
                k = int(xm.group(1))
                if k != num:
                    partner_freq[k] += 1

    # Always include X_1..X_150 plus top referenced hubs
    core_nums: set[int] = {n for n in range(1, 151) if n in centers_by_num}
    for k, _ in partner_freq.most_common(core_hub_count):
        if k in centers_by_num:
            core_nums.add(k)

    def _xy_map_for(k: int) -> dict[str, list[float]]:
        out_xy: dict[str, list[float]] = {}
        for tk in _CANONICAL_TRIANGLE_ORDER:
            r = tri_results[tk].get(k)
            if r is not None and r.get("st") == "f" and "xy" in r:
                out_xy[tk] = r["xy"]
        return out_xy

    core_centers_payload: dict[str, Any] = {}
    for k in sorted(core_nums):
        cdata = centers_by_num[k]
        core_centers_payload[str(k)] = {
            "t": cdata.get("title") or f"X_{k}",
            "xy": _xy_map_for(k),
        }
    (output_dir / "core-centers.json").write_text(
        json.dumps(core_centers_payload, separators=(",", ":"), ensure_ascii=False),
        encoding="utf-8",
    )

    # Emit 100-center JSON shards + compact search index + collection summary
    default_fields = {
        tk: get_triangle_field(tk).field_latex for tk in _CANONICAL_TRIANGLE_ORDER
    }
    boilerplate_sn = {
        "Coalesces to symmetry center O under equilateral D₃ symmetry",
        "Ideal point on the line at infinity (u + v + w = 0)",
        "Indeterminate (0 : 0 : 0) under equilateral D₃ symmetry",
        "Indeterminate homogeneous triple (0 : 0 : 0)",
        "Indeterminate / pole under equilateral D₃ symmetry (a = b = c)",
        "Indeterminate / pole under isosceles symmetry (a = b)",
        "Indeterminate / pole under right-angle degeneracy (∠A = 90°)",
        "Indeterminate algebraic pole (0 / 0)",
        "Indeterminate (0 : 0 : 0)",
    }

    sorted_nums = sorted(centers_by_num)
    max_num = sorted_nums[-1] if sorted_nums else 0
    search_rows: list[list[Any]] = []
    collections_map: dict[str, dict[str, Any]] = {}
    shard_count = 0
    shard_bytes = 0

    for shard_start in range(1, max_num + 1, SHARD_SIZE):
        shard_end = shard_start + SHARD_SIZE - 1
        shard_centers: dict[str, Any] = {}
        shard_partners: dict[str, Any] = {}
        for num in range(shard_start, shard_end + 1):
            cdata = centers_by_num.get(num)
            if cdata is None:
                continue
            c_start, c_end, c_title, c_summary = get_collection_spec(num)
            c_slug = get_collection_folder_name(c_start, c_end)
            if c_slug not in collections_map:
                collections_map[c_slug] = {
                    "slug": c_slug,
                    "start": c_start,
                    "end": c_end,
                    "title": c_title,
                    "summary": c_summary,
                    "count": 0,
                }
            collections_map[c_slug]["count"] += 1

            raw_notes = cdata.get("notes") or []
            raw_rels = cdata.get("relations") or []
            enun_raw, rem_notes = _extract_primary_enunciation(
                raw_notes, raw_rels, num=num, title=cdata.get("title") or ""
            )

            tris_packed: dict[str, Any] = {}
            for tk in _CANONICAL_TRIANGLE_ORDER:
                r = tri_results[tk].get(num)
                if r is not None:
                    compact_r = dict(r)
                    if compact_r.get("f") == default_fields[tk]:
                        compact_r.pop("f", None)
                    if compact_r.get("sn") in boilerplate_sn:
                        compact_r.pop("sn", None)
                    tris_packed[tk] = compact_r

            lines_all = center_lines_map.get(num) or []
            lines_head = lines_all[:36]

            # Deduplicate up to 10 non-core external partner coordinates at shard level
            partner_cands: list[int] = []
            for p_i, p_j in lines_head[:8]:
                partner_cands.extend((p_i, p_j))
            for rel in raw_rels[:8]:
                for xm in re.finditer(r"\bX[\(_](\d+)", rel):
                    partner_cands.append(int(xm.group(1)))
            added_for_center = 0
            for pk in partner_cands:
                if (
                    pk == num
                    or pk in core_nums
                    or (shard_start <= pk <= shard_end)
                    or str(pk) in shard_partners
                ):
                    continue
                if pk in centers_by_num and added_for_center < 10:
                    pxy = _xy_map_for(pk)
                    if pxy:
                        shard_partners[str(pk)] = {
                            "t": centers_by_num[pk].get("title") or f"X_{pk}",
                            "xy": pxy,
                        }
                        added_for_center += 1

            entry: dict[str, Any] = {
                "n": num,
                "t": cdata.get("title") or f"X_{num}",
                "col": c_slug,
                "tris": tris_packed,
            }
            if cdata.get("aliases"):
                entry["al"] = cdata["aliases"][:6]
            if enun_raw:
                entry["en"] = _rst_to_display_text(enun_raw)
            if cdata.get("trilinears"):
                entry["tr"] = [_coord_entry_to_json(x) for x in cdata["trilinears"][:8]]
            if cdata.get("barycentrics"):
                entry["ba"] = [_coord_entry_to_json(x) for x in cdata["barycentrics"][:8]]
            if cdata.get("tripolars"):
                entry["tp"] = [_coord_entry_to_json(x) for x in cdata["tripolars"][:4]]
            if cdata.get("combinations"):
                entry["co"] = [_rst_to_display_text(x) for x in cdata["combinations"][:10]]
            if lines_head:
                entry["li"] = lines_head
                if len(lines_all) > len(lines_head):
                    entry["lt"] = len(lines_all)
            if raw_rels:
                entry["re"] = [_rst_to_display_text(x) for x in raw_rels[:40]]
                if len(raw_rels) > 40:
                    entry["rt"] = len(raw_rels)
            if rem_notes:
                entry["no"] = [_rst_to_display_text(x) for x in rem_notes[:12]]

            shard_centers[str(num)] = entry

            # Search index row: [num, title, kimb_search_val, precision_code, col_slug]
            kr = tri_results["kimberling"].get(num)
            hr = tri_results["heronian"].get(num)
            sv_flt = round(kr["sv"], 9) if (kr is not None and "sv" in kr) else None
            prec_code = hr["p"] if hr is not None else "u"
            search_rows.append([num, entry["t"], sv_flt, prec_code, c_slug])

        if shard_centers:
            shard_name = f"s-{shard_start:05d}-{shard_end:05d}.json"
            shard_payload: dict[str, Any] = {
                "schema": 1,
                "range": [shard_start, shard_end],
                "centers": shard_centers,
            }
            if shard_partners:
                shard_payload["partners"] = shard_partners
            shard_txt = json.dumps(
                shard_payload,
                separators=(",", ":"),
                ensure_ascii=False,
            )
            (shards_dir / shard_name).write_text(shard_txt, encoding="utf-8")
            shard_count += 1
            shard_bytes += len(shard_txt.encode("utf-8"))

    (output_dir / "search-index.json").write_text(
        json.dumps(search_rows, separators=(",", ":"), ensure_ascii=False),
        encoding="utf-8",
    )

    manifest = {
        "schema": 1,
        "generated_at": datetime.now(UTC).isoformat(),
        "total_centers": len(centers_by_num),
        "max_center": max_num,
        "shard_size": SHARD_SIZE,
        "shard_count": shard_count,
        "shards_total_mb": round(shard_bytes / (1024 * 1024), 2),
        "core_centers_count": len(core_centers_payload),
        "triangles": _build_triangles_meta(),
        "collections": sorted(collections_map.values(), key=lambda c: c["start"]),
        "stats": tri_stats,
        "collinearity_audits": collinearity_audits,
        "elapsed_seconds": round(time.perf_counter() - t_start, 2),
    }
    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(
        f"[shards] Done in {manifest['elapsed_seconds']:.2f}s -> {shard_count} shards "
        f"({manifest['shards_total_mb']} MB), core={len(core_centers_payload)}, "
        f"search={len(search_rows)} rows in {output_dir}",
        flush=True,
    )
    if collinearity_audits:
        for tk, ca in collinearity_audits.items():
            pct = 100.0 * ca["passed_centers"] / max(1, ca["tested_centers"])
            print(
                f"[shards] Exact Collinearity Audit ({tk}): "
                f"{ca['passed_centers']}/{ca['tested_centers']} ({pct:.2f}%) passed "
                f"(failed={ca['failed_count']})",
                flush=True,
            )
    build_families_json(split_dir=split_dir, output_dir=output_dir)
    return manifest


def _clean_preamble_paragraphs(raw_html: str, max_chars: int = 1600) -> list[str]:
    """Convert raw ETC preamble HTML into clean display paragraphs (XSS-safe text)."""
    import html as _html

    if not raw_html or not raw_html.strip():
        return []
    txt = raw_html
    # Drop <header> title boilerplate when pulling from preambles.json
    txt = re.sub(r"<header\b[^>]*>.*?</header>", "", txt, flags=re.DOTALL | re.IGNORECASE)
    txt = re.sub(r"<p[^>]*class=[\"']?preamble-title[\"']?[^>]*>.*?</p>", "", txt, flags=re.DOTALL | re.IGNORECASE)
    txt = re.sub(r"<br\s*/?>", "\n", txt, flags=re.IGNORECASE)
    txt = re.sub(r"</(?:p|div|li|tr|h[1-6]|blockquote)>", "\n\n", txt, flags=re.IGNORECASE)
    txt = re.sub(r"<li\b[^>]*>", "• ", txt, flags=re.IGNORECASE)
    txt = re.sub(r"<sup\b[^>]*>(.*?)</sup>", r"^\1", txt, flags=re.DOTALL | re.IGNORECASE)
    txt = re.sub(r"<sub\b[^>]*>(.*?)</sub>", r"_\1", txt, flags=re.DOTALL | re.IGNORECASE)
    txt = re.sub(r"<[^>]+>", "", txt)
    txt = _html.unescape(txt)
    paras: list[str] = []
    total_len = 0
    for chunk in re.split(r"\n{2,}", txt):
        cleaned = " ".join(chunk.split()).strip()
        if not cleaned:
            continue
        if total_len + len(cleaned) > max_chars and paras:
            paras.append("…")
            break
        paras.append(cleaned[:max_chars])
        total_len += len(cleaned)
    return paras


def build_families_json(
    *,
    split_dir: Path = DEFAULT_SPLIT_DIR,
    output_dir: Path = DEFAULT_DATA_DIR,
) -> dict[str, Any]:
    """Export all 62 curated thematic collections and all 925 ETC preamble families into ``families.json``."""
    output_dir.mkdir(parents=True, exist_ok=True)

    collections_list: list[dict[str, Any]] = []
    for s_num, e_num, title, summary in THEMATIC_COLLECTIONS:
        collections_list.append(
            {
                "slug": get_collection_folder_name(s_num, e_num),
                "start": s_num,
                "end": e_num,
                "title": title,
                "summary": summary,
            }
        )

    # Index full volume preambles by before_num for enriching Part 1..37 guide entries
    vol_preambles_by_num: dict[int, list[str]] = {}
    preambles_path = split_dir / "preambles.json"
    if preambles_path.is_file():
        raw_pre = json.loads(preambles_path.read_text(encoding="utf-8"))
        by_c = raw_pre.get("by_center", raw_pre) if isinstance(raw_pre, dict) else {}
        if isinstance(by_c, dict):
            for p_list in by_c.values():
                if not isinstance(p_list, list):
                    continue
                for item in p_list:
                    bn = item.get("before_num")
                    if isinstance(bn, int) and item.get("html"):
                        vol_preambles_by_num.setdefault(bn, []).append(item["html"])

    families_list: list[dict[str, Any]] = []
    guide_path = split_dir / "preambles_guide.json"
    if guide_path.is_file():
        guide_data = json.loads(guide_path.read_text(encoding="utf-8"))
        entries = guide_data.get("entries", []) if isinstance(guide_data, dict) else guide_data
        for entry in entries:
            idx = int(entry.get("index") or (len(families_list) + 1))
            s_num = int(entry.get("start_num") or 0)
            e_num = int(entry.get("end_num") or s_num)
            if s_num <= 0:
                continue
            if e_num < s_num:
                s_num, e_num = e_num, s_num
            title = (entry.get("title") or entry.get("header") or f"Family X_{s_num}–X_{e_num}").strip()
            body_html = entry.get("html") or ""
            if not body_html.strip():
                # Pull matching volume preamble essay if guide entry has empty body
                for cand_n in (s_num, *(entry.get("nums") or [])):
                    if cand_n in vol_preambles_by_num:
                        body_html = vol_preambles_by_num[cand_n][0]
                        break
            paras = _clean_preamble_paragraphs(body_html)
            fam_rec: dict[str, Any] = {
                "id": f"f-{idx:04d}",
                "idx": idx,
                "part": int(entry.get("part") or 1),
                "start": s_num,
                "end": e_num,
                "title": title,
            }
            if paras:
                fam_rec["p"] = paras
            families_list.append(fam_rec)

    payload = {
        "schema": 1,
        "collections_count": len(collections_list),
        "families_count": len(families_list),
        "collections": collections_list,
        "families": families_list,
    }
    out_path = output_dir / "families.json"
    out_txt = json.dumps(payload, separators=(",", ":"), ensure_ascii=False)
    out_path.write_text(out_txt, encoding="utf-8")
    print(
        f"[shards] Wrote {out_path.name} ({len(out_txt) / 1024:.1f} KB): "
        f"{len(collections_list)} curated collections + {len(families_list)} ETC preamble families",
        flush=True,
    )
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build exact symbolic JSON shards for GEOMETOR ETC"
    )
    parser.add_argument("--split-dir", type=Path, default=DEFAULT_SPLIT_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--end", type=int, default=4000, help="Number of centers (0 = all)")
    parser.add_argument("--workers", type=int, default=None)
    parser.add_argument(
        "--families-only",
        action="store_true",
        help="Only build families.json (62 collections + 925 ETC preamble families)",
    )
    args = parser.parse_args()
    if args.families_only:
        build_families_json(split_dir=args.split_dir, output_dir=args.output_dir)
        return
    build_shards(
        split_dir=args.split_dir,
        output_dir=args.output_dir,
        end=args.end,
        workers=args.workers,
    )


if __name__ == "__main__":
    main()
