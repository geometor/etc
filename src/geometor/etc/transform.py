"""Transform parsed ETC center and preamble structures into semantic ReStructuredText."""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Any

from .glossary import (
    _apply_outside_rst_spans,
    filter_center_refs,
    wrap_glossary_terms,
    wrap_persons_and_citations,
)
from .parser import parse_preamble


def format_rst_header(title: str, char: str = "=") -> str:
    """Create an RST section header with matching underline length."""
    line = char * max(4, len(title))
    return f"{title}\n{line}\n\n"


def wrap_refs(
    text: str, valid_centers: set[int] | None = None
) -> str:
    """Wrap X(n) and X[n] references in `:ref:`X(n) <X(n)>`` outside existing RST roles."""
    if not text:
        return ""

    pattern = re.compile(r"(?<![a-z])X[\(\[](\d+)[\)\]]")

    def _repl_seg(seg: str) -> str:
        out: list[str] = []
        last_idx = 0
        for m in pattern.finditer(seg):
            num_str = m.group(1)
            num = int(num_str)
            start, end = m.start(), m.end()
            out.append(seg[last_idx:start])
            if valid_centers is not None and num not in valid_centers:
                out.append(f"X({num_str})")
            else:
                prev_ch = seg[start - 1] if start > 0 else " "
                next_ch = seg[end] if end < len(seg) else " "
                need_pre = (prev_ch not in " \t\n-:/'\"<([{") and not (
                    last_idx == start and out and out[-1].endswith(r"\ ")
                )
                need_post = next_ch not in " \t\n-.,:;!?/'\")>]}"
                prefix = r"\ " if need_pre else ""
                suffix = r"\ " if need_post else ""
                out.append(f"{prefix}:ref:`X({num_str}) <X({num_str})>`{suffix}")
            last_idx = end
        out.append(seg[last_idx:])
        return "".join(out)

    return _apply_outside_rst_spans(text, _repl_seg)


def _wrap_relation_tuples(
    rel_text: str, valid_centers: set[int] | None = None
) -> str:
    """Wrap bare integer tuples after 'for these (i,j):' into clickable `:ref:` links."""
    colon_match = re.search(
        r"(for\s+these\s+[^:]+:\s*)(.+)$",
        rel_text,
        flags=re.DOTALL | re.IGNORECASE,
    )
    if not colon_match:
        return rel_text

    prefix = rel_text[: colon_match.end(1)]
    tail = colon_match.group(2)

    def _fmt_num(n_str: str) -> str:
        n_int = int(n_str)
        if valid_centers is None or n_int in valid_centers:
            return f":ref:`{n_str} <X({n_str})>`"
        return n_str

    def _tuple_repl(m: re.Match) -> str:
        open_br, inner, close_br = m.group(1), m.group(2), m.group(3)
        nums = [n.strip() for n in inner.split(",") if n.strip().isdigit()]
        if not nums:
            return m.group(0)
        linked = ", ".join(_fmt_num(n) for n in nums)
        return f"{open_br}{linked}{close_br}"

    linked_tail = re.sub(
        r"([\(\{])\s*(\d+(?:\s*,\s*\d+)+)\s*([\)\}])",
        _tuple_repl,
        tail,
    )
    return f"{prefix}{linked_tail}"


def _enrich_text(
    text: str,
    glossary_terms: dict[str, Any] | list[str] | None,
    seen_terms: set[str],
    seen_persons: set[str],
    seen_cites: set[str],
    valid_centers: set[int] | None = None,
) -> str:
    """Apply X(n) reference linking, glossary `:term:` linking, and `:person:`/`:cite:` linking."""
    text = wrap_refs(text, valid_centers=valid_centers)
    if glossary_terms:
        text = wrap_glossary_terms(text, glossary_terms, seen_slugs=seen_terms)
    text = wrap_persons_and_citations(
        text, seen_persons=seen_persons, seen_cites=seen_cites
    )
    return filter_center_refs(text, valid_centers)


def _extract_primary_enunciation(
    notes: list[str], relations: list[str]
) -> tuple[str, list[str]]:
    """Extract a concise primary defining statement for ``.. enunciation::`` and return remaining notes."""
    skip_prefixes = (
        "as a point on the euler line",
        "barycentrics ",
        "trilinears ",
        "tripolars ",
        "*",
    )
    remaining = list(notes)

    for idx, note in enumerate(remaining):
        s = note.strip()
        if not s:
            continue
        low = s.lower()
        if any(low.startswith(p) for p in skip_prefixes):
            continue
        if "\n" not in s and len(s) > 10:
            del remaining[idx]
            return s, remaining

    for idx, note in enumerate(remaining):
        paras = [p.strip() for p in note.split("\n\n") if p.strip()]
        if not paras:
            continue
        first_p = paras[0]
        low = first_p.lower()
        if any(low.startswith(p) for p in skip_prefixes):
            continue
        if "\n" not in first_p and len(first_p) > 10:
            if len(paras) == 1:
                del remaining[idx]
            else:
                remaining[idx] = "\n\n".join(paras[1:])
            return first_p, remaining

    for idx, note in enumerate(remaining):
        s = note.strip()
        if s and "\n" not in s and not s.startswith("*"):
            del remaining[idx]
            return s, remaining

    for rel in relations:
        r_s = rel.strip()
        if r_s and "for these" not in r_s.lower() and "\n" not in r_s:
            return r_s, remaining

    return "", remaining


def transform_center_to_rst(
    data: dict[str, Any],
    glossary_terms: dict[str, Any] | list[str] | None = None,
    preambles: list[dict[str, Any]] | None = None,
    valid_centers: set[int] | None = None,
    figure_uri: str | None = None,
    kimberling_figure_uri: str | None = None,
    search_value: float | None = None,
    include_model_py: bool = False,
) -> str:
    """Transform a parsed center dictionary into the Book Codex Overview track (`index.rst`)."""
    if not data or not data.get("key"):
        return ""

    key = data["key"]
    title = data.get("title", "")
    num = data.get("num")
    if num is None:
        try:
            num = int(key.replace("X(", "").replace(")", ""))
        except ValueError:
            num = 0

    lines: list[str] = [
        f":order: {num}",
        ":type: center",
        f":canonical_id: {key}",
    ]

    aliases = data.get("aliases") or []
    if aliases:
        lines.append(f":aliases: {', '.join(aliases)}")

    if data.get("dependencies"):
        lines.append(f":dependencies: {', '.join(data['dependencies'])}")

    lines.append("")

    # Anchors
    lines.append(f".. _X({num}):")
    anchor_id = data.get("anchor_id")
    if anchor_id and anchor_id != f"X({num})":
        lines.append(f".. _{anchor_id}:")
    lines.append("")

    # Document Title (=)
    full_title = f"{key} = {title}" if title else key
    lines.append(full_title)
    lines.append("=" * max(4, len(full_title)))
    lines.append("")

    if aliases:
        lines.append(f".. rubric:: {' • '.join(aliases)}")
        lines.append("")

    seen_terms: set[str] = set()
    seen_persons: set[str] = set()
    seen_cites: set[str] = set()

    raw_notes = data.get("notes") or []
    raw_relations = data.get("relations") or []
    enun_raw, remaining_notes = _extract_primary_enunciation(
        raw_notes, raw_relations
    )

    if enun_raw:
        enriched_enun = _enrich_text(
            enun_raw,
            glossary_terms,
            seen_terms,
            seen_persons,
            seen_cites,
            valid_centers=valid_centers,
        )
        lines.append(".. enunciation::")
        lines.append("")
        for e_ln in enriched_enun.splitlines():
            lines.append(f"   {e_ln}" if e_ln.strip() else "")
        lines.append("")

    # Optional preceding inter-center group preamble(s)
    if preambles:
        for p_item in preambles:
            parsed_p = parse_preamble(p_item.get("html", ""))
            p_title = parsed_p["title"] or p_item.get("title", "Preamble")
            p_paras = parsed_p["paragraphs"]
            p_id = p_item.get("id")
            if p_id:
                lines.append(f".. _{p_id}:")
                lines.append("")
            if p_paras:
                lines.append(f".. admonition:: Group Preamble — {p_title}")
                lines.append("   :class: note")
                lines.append("")
                for para in p_paras:
                    enriched_para = _enrich_text(
                        para,
                        glossary_terms,
                        seen_terms,
                        seen_persons,
                        seen_cites,
                        valid_centers=valid_centers,
                    )
                    for p_ln in enriched_para.splitlines():
                        lines.append(f"   {p_ln}" if p_ln.strip() else "")
                    lines.append("")
            else:
                lines.append(".. admonition:: Group Preamble")
                lines.append("   :class: note")
                lines.append("")
                enriched_title = _enrich_text(
                    p_title,
                    glossary_terms,
                    seen_terms,
                    seen_persons,
                    seen_cites,
                    valid_centers=valid_centers,
                )
                for p_ln in enriched_title.splitlines():
                    lines.append(f"   {p_ln}" if p_ln.strip() else "")
                lines.append("")

    # 1. Primary Geometric Construction Figure (4-Tab Interactive Panel)
    if figure_uri:
        lines.append(f".. figure:: {figure_uri}")
        lines.append(f"   :alt: {full_title}")
        lines.append("   :align: center")
        lines.append("")
        lines.append(
            f"   **{full_title}** constructed on acute reference triangle "
            r":math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`."
        )
        lines.append("")

    # 2. Compact Coordinate Signature Card (.. signature:: center) + Alternate Coordinates
    has_coords = any(
        data.get(k) for k in ("trilinears", "barycentrics", "tripolars")
    )
    alt_coord_bullets: list[str] = []
    if has_coords or (search_value is not None and abs(search_value) > 1e-12):
        lines.append(".. signature:: center")
        lines.append("")
        for coord_key, coord_label in (
            ("trilinears", "Trilinears"),
            ("barycentrics", "Barycentrics"),
            ("tripolars", "Tripolars"),
        ):
            items = data.get(coord_key) or []
            if not items:
                continue
            enriched_items = []
            for item in items:
                enr = _enrich_text(
                    " ".join(item.splitlines()).strip(),
                    glossary_terms,
                    seen_terms,
                    seen_persons,
                    seen_cites,
                    valid_centers=valid_centers,
                )
                if enr:
                    enriched_items.append(enr)
            if not enriched_items:
                continue
            lines.append(f"   | **{coord_label}:** {enriched_items[0]}")
            rest_start = 1
            if len(enriched_items) > 1 and enriched_items[1].lower().startswith(
                "where"
            ):
                lines.append(f"   |   {enriched_items[1]}")
                rest_start = 2
            for extra_it in enriched_items[rest_start:]:
                alt_coord_bullets.append(f"**{coord_label}:** {extra_it}")

        if search_value is not None and abs(search_value) > 1e-12:
            lines.append(
                f"   | **Search Value (6, 9, 13):** :math:`{search_value:.12f}`"
            )
        lines.append("")

    if alt_coord_bullets:
        n_alt = len(alt_coord_bullets)
        alt_badge = "1 form" if n_alt == 1 else f"{n_alt} forms"
        lines.append(".. collapse:: Alternate Coordinates")
        lines.append(f"   :badge: {alt_badge}")
        lines.append("")
        for b_line in alt_coord_bullets:
            lines.append(f"   * {b_line}")
        lines.append("")

    # 3. Collapsible Linear Combinations
    combos = data.get("combinations") or []
    if combos:
        n_combos = len(combos)
        combo_badge = (
            "1 combination" if n_combos == 1 else f"{n_combos} combinations"
        )
        lines.append(".. collapse:: Linear Combinations")
        lines.append(f"   :badge: {combo_badge}")
        lines.append("")
        for combo in combos:
            enriched_combo = _enrich_text(
                combo,
                glossary_terms,
                seen_terms,
                seen_persons,
                seen_cites,
                valid_centers=valid_centers,
            )
            combo_lines = [
                ln.strip() for ln in enriched_combo.splitlines() if ln.strip()
            ]
            if combo_lines:
                lines.append(f"   * {' '.join(combo_lines)}")
        lines.append("")

    # 4. Incidence (Curves visible + Collapsible Incident Central Lines)
    incidences = data.get("incidences") or []
    if incidences:
        for inc in incidences:
            if isinstance(inc, dict):
                line_pairs = inc.get("lines") or []
                curves_prefix = inc.get("curves_prefix", "")
                if line_pairs:
                    enriched_prefix = _enrich_text(
                        curves_prefix,
                        glossary_terms,
                        seen_terms,
                        seen_persons,
                        seen_cites,
                        valid_centers=valid_centers,
                    ).strip()
                    is_bare_key = bool(
                        re.match(
                            r"^(?::ref:`X\(\d+\) <X\(\d+\)>`|X\(\d+\))\s*$",
                            enriched_prefix,
                        )
                    )
                    if enriched_prefix and not is_bare_key:
                        lines.append(".. container:: note-item")
                        lines.append("")
                        for c_ln in f"{enriched_prefix}.".splitlines():
                            lines.append(f"   {c_ln}" if c_ln.strip() else "")
                        lines.append("")

                    def _fmt_inc_pt(pt: int) -> str:
                        if valid_centers is None or pt in valid_centers:
                            return f":ref:`{pt} <X({pt})>`"
                        return str(pt)

                    formatted_pairs = [
                        f"{{{_fmt_inc_pt(i)}, {_fmt_inc_pt(j)}}}"
                        for i, j in line_pairs
                    ]
                    n_lines = len(line_pairs)
                    badge_lbl = "1 line" if n_lines == 1 else f"{n_lines} lines"
                    lines.append(".. collapse:: Incident Central Lines")
                    lines.append(f"   :badge: {badge_lbl}")
                    lines.append("   :class: line-catalog")
                    lines.append("")
                    lines.append(f"   {', '.join(formatted_pairs)}")
                    lines.append("")
                else:
                    raw_inc = _enrich_text(
                        inc.get("raw_rst", ""),
                        glossary_terms,
                        seen_terms,
                        seen_persons,
                        seen_cites,
                        valid_centers=valid_centers,
                    ).strip()
                    if raw_inc:
                        lines.append(".. container:: note-item")
                        lines.append("")
                        for r_ln in raw_inc.splitlines():
                            lines.append(f"   {r_ln}" if r_ln.strip() else "")
                        lines.append("")
            else:
                str_inc = _enrich_text(
                    str(inc),
                    glossary_terms,
                    seen_terms,
                    seen_persons,
                    seen_cites,
                    valid_centers=valid_centers,
                ).strip()
                if str_inc:
                    lines.append(".. container:: note-item")
                    lines.append("")
                    for s_ln in str_inc.splitlines():
                        lines.append(f"   {s_ln}" if s_ln.strip() else "")
                    lines.append("")

    # 5. Collapsible Functional Relations
    if raw_relations:
        n_rels = len(raw_relations)
        rel_badge = "1 relation" if n_rels == 1 else f"{n_rels} relations"
        lines.append(".. collapse:: Functional Relations")
        lines.append(f"   :badge: {rel_badge}")
        lines.append("")
        for rel in raw_relations:
            rel_with_tuples = _wrap_relation_tuples(
                rel, valid_centers=valid_centers
            )
            enriched_rel = _enrich_text(
                rel_with_tuples,
                glossary_terms,
                seen_terms,
                seen_persons,
                seen_cites,
                valid_centers=valid_centers,
            )
            rel_lines = [ln.strip() for ln in enriched_rel.splitlines() if ln.strip()]
            if rel_lines:
                lines.append(f"   * {' '.join(rel_lines)}")
        lines.append("")

    # 6. Remaining Notes
    if remaining_notes:
        lines.append("Notes")
        lines.append("-----")
        lines.append("")

        def _fmt_circle_idx(m: re.Match) -> str:
            idx_str = m.group(1)
            idx_int = int(idx_str)
            if valid_centers is None or idx_int in valid_centers:
                return f":ref:`{idx_str} <X({idx_str})>`"
            return idx_str

        for note in remaining_notes:
            enriched_note = _enrich_text(
                note,
                glossary_terms,
                seen_terms,
                seen_persons,
                seen_cites,
                valid_centers=valid_centers,
            )
            lines.append(".. container:: note-item")
            lines.append("")
            for n_ln in enriched_note.splitlines():
                if n_ln.strip().startswith("* (") and ";" in n_ln:
                    n_ln = re.sub(
                        r"(?<=[;,]\s)(\d+)\b",
                        _fmt_circle_idx,
                        n_ln,
                    )
                lines.append(f"   {n_ln}" if n_ln.strip() else "")
            lines.append("")

    # 7. Companion Code Track Toctree
    if include_model_py:
        lines.append(".. toctree::")
        lines.append("   :hidden:")
        lines.append("")
        lines.append("   code")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def transform_center_to_code_rst(
    data: dict[str, Any],
    glossary_terms: dict[str, Any] | list[str] | None = None,
    valid_centers: set[int] | None = None,
    figure_uri: str | None = None,
) -> str:
    """Transform a parsed center dictionary into the companion Code track (`code.rst`)."""
    if not data or not data.get("key"):
        return ""

    key = data["key"]
    title = data.get("title", "")
    full_title = f"{key} = {title}" if title else key
    code_heading = f"{full_title} — Code"

    lines: list[str] = [
        f":canonical_id: {key}",
        ":type: code",
        "",
        code_heading,
        "=" * max(4, len(code_heading)),
        "",
    ]

    aliases = data.get("aliases") or []
    if aliases:
        lines.append(f".. rubric:: {' • '.join(aliases)}")
        lines.append("")

    enun_raw, _ = _extract_primary_enunciation(
        data.get("notes") or [], data.get("relations") or []
    )
    if enun_raw:
        enriched_enun = _enrich_text(
            enun_raw,
            glossary_terms,
            set(),
            set(),
            set(),
            valid_centers=valid_centers,
        )
        lines.append(".. enunciation::")
        lines.append("")
        for e_ln in enriched_enun.splitlines():
            lines.append(f"   {e_ln}" if e_ln.strip() else "")
        lines.append("")

    if figure_uri:
        lines.append(f".. figure:: {figure_uri}")
        lines.append(f"   :alt: {full_title}")
        lines.append("   :align: center")
        lines.append("")
        lines.append(
            f"   **{full_title}** constructed on acute reference triangle "
            r":math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`."
        )
        lines.append("")

    lines.append(".. literalinclude:: model.py")
    lines.append("   :language: python")
    lines.append("")

    return "\n".join(lines).rstrip() + "\n"


_SHARED_GEN_STATE: dict[str, Any] = {}


def _process_center_index(idx: int) -> None:
    """Worker function for fork-based parallel center folder generation."""
    state = _SHARED_GEN_STATE
    center = state["centers"][idx]
    if not center:
        return

    out_path: Path = state["out_path"]
    acute_reg = state["acute_reg"]
    right_reg = state["right_reg"]
    kepler_reg = state["kepler_reg"]
    kimb_reg = state["kimb_reg"]
    kimb_ctx = state["kimb_ctx"]
    render_graphics: bool = state["render_graphics"]
    glossary_terms = state["glossary_terms"]
    preambles_by_center = state["preambles_by_center"]
    valid_centers = state["valid_centers"]
    build_center_model = state["build_center_model"]
    generate_center_model_py = state["generate_center_model_py"]
    write_center_svg = state["write_center_svg"]

    key = center["key"]
    num = center.get("num")
    if num is None:
        try:
            num = int(key.replace("X(", "").replace(")", ""))
        except ValueError:
            num = 0

    folder_name = f"x-{num:05d}" if num > 0 else key
    entry_dir = out_path / folder_name
    entry_dir.mkdir(parents=True, exist_ok=True)
    filepath = entry_dir / "index.rst"
    code_rst_path = entry_dir / "code.rst"
    model_py_path = entry_dir / "model.py"

    figure_uri: str | None = None
    search_val: float | None = None
    has_model_py = False

    if num in kimb_reg.bary_cache:
        kb = kimb_reg.bary_cache[num]
        if abs(sum(kb)) > 1e-6:
            search_val = kimb_ctx.kimberling_search_value(*kb)

    svg_name = f"x-{num:05d}.svg"
    right_svg_name = f"x-{num:05d}-right.svg"
    kepler_svg_name = f"x-{num:05d}-kepler.svg"
    kimb_svg_name = f"x-{num:05d}-kimberling.svg"

    if num in acute_reg.xy_cache:
        model_py_code = generate_center_model_py(center, acute_reg)
        model_py_path.write_text(model_py_code, encoding="utf-8")
        has_model_py = True

    if render_graphics and num in acute_reg.xy_cache:
        model_acute = build_center_model(center, acute_reg)
        write_center_svg(
            model_acute,
            entry_dir / svg_name,
            subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
        )
        model_acute.save(str(entry_dir / f"x-{num:05d}.json"))
        figure_uri = svg_name

        if num in right_reg.xy_cache:
            model_right = build_center_model(center, right_reg)
            write_center_svg(
                model_right,
                entry_dir / right_svg_name,
                subtitle="(a, b, c) = (3, 4, 5) | AB = 1",
            )

        if num in kepler_reg.xy_cache:
            model_kepler = build_center_model(center, kepler_reg)
            write_center_svg(
                model_kepler,
                entry_dir / kepler_svg_name,
                subtitle="Kepler (1, √φ, φ) | AB = 1",
            )

        if num in kimb_reg.xy_cache:
            model_kimb = build_center_model(center, kimb_reg)
            write_center_svg(
                model_kimb,
                entry_dir / kimb_svg_name,
                subtitle="Kimberling (6, 9, 13) | AB = 1",
            )
    else:
        if (entry_dir / svg_name).exists():
            figure_uri = svg_name
        if model_py_path.exists():
            has_model_py = True

    center_preambles = (
        preambles_by_center.get(key) if preambles_by_center else None
    )
    rst_content = transform_center_to_rst(
        center,
        glossary_terms=glossary_terms,
        preambles=center_preambles,
        valid_centers=valid_centers,
        figure_uri=figure_uri,
        search_value=search_val,
        include_model_py=has_model_py,
    )
    filepath.write_text(rst_content, encoding="utf-8")

    if has_model_py:
        code_rst_content = transform_center_to_code_rst(
            center,
            glossary_terms=glossary_terms,
            valid_centers=valid_centers,
            figure_uri=figure_uri,
        )
        code_rst_path.write_text(code_rst_content, encoding="utf-8")
    elif code_rst_path.exists():
        code_rst_path.unlink()


def generate_rst_files(
    centers: list[dict[str, Any]],
    output_dir: str | Path,
    glossary_terms: dict[str, Any] | list[str] | None = None,
    preambles_by_center: dict[str, list[dict[str, Any]]] | None = None,
    valid_centers: set[int] | None = None,
    render_graphics: bool = True,
    constructions_dir: str | Path | None = None,
) -> None:
    """Generate per-center folders (`x-NNNNN/`) with `index.rst`, `code.rst`, `model.py`, SVGs, and `geometor.model` JSONs."""
    import concurrent.futures
    import multiprocessing

    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    if valid_centers is None:
        valid_centers = set()
        for c in centers:
            if not c:
                continue
            cnum = c.get("num")
            if cnum is None and c.get("key"):
                try:
                    cnum = int(c["key"].replace("X(", "").replace(")", ""))
                except ValueError:
                    cnum = None
            if cnum:
                valid_centers.add(int(cnum))

    from .construct import (
        TRIANGLE_PRESETS,
        CenterRegistry,
        TriangleContext,
        build_center_model,
        generate_center_model_py,
    )
    from .glossary import _get_glossary_lookup_and_pattern
    from .render import write_center_svg

    if glossary_terms:
        _get_glossary_lookup_and_pattern(glossary_terms)

    # Build coordinate and construction registries on (5, 6, 7), (3, 4, 5), Kepler, and Kimberling (6, 9, 13)
    print(f"Resolving coordinates and incidences for {len(centers)} centers...", flush=True)
    acute_ctx = TriangleContext(*TRIANGLE_PRESETS["acute"])
    acute_reg = CenterRegistry(centers, acute_ctx)
    right_ctx = TriangleContext(*TRIANGLE_PRESETS["right"])
    right_reg = CenterRegistry(centers, right_ctx)
    kepler_ctx = TriangleContext(*TRIANGLE_PRESETS["kepler"])
    kepler_reg = CenterRegistry(centers, kepler_ctx)
    kimb_ctx = TriangleContext(*TRIANGLE_PRESETS["kimberling"])
    kimb_reg = CenterRegistry(centers, kimb_ctx)
    print(f"Resolved {len(acute_reg.xy_cache)} / {len(centers)} centers.", flush=True)

    index_lines = [
        ":navigation: header",
        ":order: 1",
        ":layout: book",
        ":book_title: Encyclopedia of Triangle Centers",
        "",
        "Encyclopedia of Triangle Centers",
        "================================",
        "",
        ".. collection::",
        "   :type: center",
        "   :sort: order",
        "",
    ]

    _SHARED_GEN_STATE.clear()
    _SHARED_GEN_STATE.update(
        {
            "centers": centers,
            "out_path": out_path,
            "acute_reg": acute_reg,
            "right_reg": right_reg,
            "kepler_reg": kepler_reg,
            "kimb_reg": kimb_reg,
            "kimb_ctx": kimb_ctx,
            "render_graphics": render_graphics,
            "glossary_terms": glossary_terms,
            "preambles_by_center": preambles_by_center,
            "valid_centers": valid_centers,
            "build_center_model": build_center_model,
            "generate_center_model_py": generate_center_model_py,
            "write_center_svg": write_center_svg,
        }
    )

    total = len(centers)
    if total > 200:
        mp_ctx = multiprocessing.get_context("fork")
        with concurrent.futures.ProcessPoolExecutor(mp_context=mp_ctx) as pool:
            for done_idx, _ in enumerate(
                pool.map(_process_center_index, range(total), chunksize=64), 1
            ):
                if done_idx % 2000 == 0 or done_idx == total:
                    print(
                        f"Generated {done_idx} / {total} center folders...",
                        flush=True,
                    )
    else:
        for idx in range(total):
            _process_center_index(idx)

    _SHARED_GEN_STATE.clear()
    (out_path / "index.rst").write_text("\n".join(index_lines), encoding="utf-8")




