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
    """Transform a parsed center dictionary into a rich semantic RST document."""
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

    if data.get("aliases"):
        lines.append(f":aliases: {', '.join(data['aliases'])}")

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

    seen_terms: set[str] = set()
    seen_persons: set[str] = set()
    seen_cites: set[str] = set()

    # Optional preceding inter-center group preamble(s)
    if preambles:
        for p_item in preambles:
            parsed_p = parse_preamble(p_item.get("html", ""))
            p_title = parsed_p["title"] or p_item.get("title", "Preamble")
            p_id = p_item.get("id")
            if p_id:
                lines.append(f".. _{p_id}:")
                lines.append("")
            lines.append(f".. admonition:: Group Preamble — {p_title}")
            lines.append("   :class: note")
            lines.append("")
            for para in parsed_p["paragraphs"]:
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

    # Primary Geometric Construction Figure
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

    # 1. Coordinates Section (-)
    has_coords = any(
        data.get(k) for k in ("trilinears", "barycentrics", "tripolars")
    )
    if has_coords or search_value is not None:
        lines.append("Coordinates")
        lines.append("-----------")
        lines.append("")

        for coord_key, coord_label in (
            ("trilinears", "Trilinears"),
            ("barycentrics", "Barycentrics"),
            ("tripolars", "Tripolars"),
        ):
            items = data.get(coord_key) or []
            if not items:
                continue
            lines.append(coord_label)
            lines.append("~" * len(coord_label))
            lines.append("")
            for item in items:
                enriched_item = _enrich_text(
                    item,
                    glossary_terms,
                    seen_terms,
                    seen_persons,
                    seen_cites,
                    valid_centers=valid_centers,
                )
                lines.append(f"* {enriched_item}")
            lines.append("")

        if search_value is not None and abs(search_value) > 1e-12:
            lines.append(
                f"* **Kimberling (6, 9, 13) Search Value:** :math:`{search_value:.12f}`"
            )
            lines.append("")

    # 2. Linear Combinations Section (-)
    combos = data.get("combinations") or []
    if combos:
        lines.append("Linear Combinations")
        lines.append("-------------------")
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
            lines.append(f"* {enriched_combo}")
        lines.append("")

    # 3. Notes Section (-)
    notes = data.get("notes") or []
    if notes:
        lines.append("Notes")
        lines.append("-----")
        lines.append("")

        def _fmt_circle_idx(m: re.Match) -> str:
            idx_str = m.group(1)
            idx_int = int(idx_str)
            if valid_centers is None or idx_int in valid_centers:
                return f":ref:`{idx_str} <X({idx_str})>`"
            return idx_str

        for note in notes:
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

    # 4. Incidence Section (-)
    incidences = data.get("incidences") or []
    if incidences:
        lines.append("Incidence")
        lines.append("---------")
        lines.append("")
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
                    )
                    if re.match(
                        r"^(?::ref:`X\(\d+\) <X\(\d+\)>`|X\(\d+\))\s*$",
                        enriched_prefix.strip(),
                    ):
                        intro_line = f"{enriched_prefix.strip()} lies on these lines:"
                    else:
                        intro_line = f"{enriched_prefix.strip()} and on these lines:"
                    lines.append(intro_line)
                    lines.append("")

                    def _fmt_inc_pt(pt: int) -> str:
                        if valid_centers is None or pt in valid_centers:
                            return f":ref:`{pt} <X({pt})>`"
                        return str(pt)

                    formatted_pairs = [
                        f"{{{_fmt_inc_pt(i)}, {_fmt_inc_pt(j)}}}"
                        for i, j in line_pairs
                    ]
                    lines.append(", ".join(formatted_pairs))
                    lines.append("")
                else:
                    lines.append(
                        _enrich_text(
                            inc.get("raw_rst", ""),
                            glossary_terms,
                            seen_terms,
                            seen_persons,
                            seen_cites,
                            valid_centers=valid_centers,
                        )
                    )
                    lines.append("")
            else:
                lines.append(
                    _enrich_text(
                        str(inc),
                        glossary_terms,
                        seen_terms,
                        seen_persons,
                        seen_cites,
                        valid_centers=valid_centers,
                    )
                )
                lines.append("")

    # 5. Relations Section (-)
    relations = data.get("relations") or []
    if relations:
        lines.append("Relations")
        lines.append("---------")
        lines.append("")
        for rel in relations:
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
            lines.append(f"* {enriched_rel}")
        lines.append("")

    # 6. Symbolic Construction Code Section (-)
    if include_model_py:
        lines.append("Construction")
        lines.append("------------")
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


def generate_rst_files(
    centers: list[dict[str, Any]],
    output_dir: str | Path,
    glossary_terms: dict[str, Any] | list[str] | None = None,
    preambles_by_center: dict[str, list[dict[str, Any]]] | None = None,
    valid_centers: set[int] | None = None,
    render_graphics: bool = True,
    constructions_dir: str | Path | None = None,
) -> None:
    """Generate per-center folders (`x-NNNNN/`) with `index.rst`, `model.py`, SVGs, and `geometor.model` JSONs."""
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



