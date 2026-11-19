"""Generalized 5-Track Tabular Book Codex generator for GEOMETOR ETC centers.

Splits each center with a full symbolic plate suite (Collection 1 ``X_1``–``X_19`` and any
future multi-plate center) into five fast, focused, tabular Book Codex tracks:

- ``index.rst`` (Overview): Identity strip, enunciation, primary viewer, ordered Homogeneous
  Coordinates table, Four-Triangle Symbolic Invariants table, Heronian Coordinate Decomposition
  table, Constructed Elements table, and Linear Combinations table.
- ``lines.rst`` (Lines): Central Lines viewer (4-triangle tabs), Principal Central Lines table
  with exact Cartesian equations and spreads, incident curves/cubics, and full line catalog.
- ``relations.rst`` (Relations): Relations viewer, Canonical Algebraic Operators table, and
  categorized Functional Relations tables (Unary, Binary, Perspectors/Derived Triangles).
- ``notes.rst`` (Notes): Construction viewer, structured metric/excenter identities where
  present, geometric constructions, historical citations, and companion topic guides.
- ``code.rst`` (Code): Construction viewer (4-triangle tabs) alongside exact symbolic ``model.py``.

Zero center-specific hardcoding; every table derives from ``CenterSymbolicRegistry``,
``CenterRelationsBundle``, the exact symbolic ``Model``, and parsed ETC apparatus records.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

TRACKS_FRONTMATTER = (
    "Overview: index | Lines: lines | Relations: relations | Notes: notes | Code: code"
)

_BINARY_REL_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("Midpoint of (X_i, X_j)", re.compile(r"\bmidpoint of\b", re.IGNORECASE)),
    ("Reflection of X_i in X_j", re.compile(r"\breflection of\b", re.IGNORECASE)),
    ("Ceva Conjugate", re.compile(r"\bceva conjugate\b", re.IGNORECASE)),
    ("Cevapoint", re.compile(r"\bcevapoint\b", re.IGNORECASE)),
    ("Cross Conjugate", re.compile(r"\bcross conjugate\b", re.IGNORECASE)),
    ("Crosspoint", re.compile(r"\bcrosspoint\b", re.IGNORECASE)),
    ("Crosssum", re.compile(r"\bcrosssum\b", re.IGNORECASE)),
    ("Crossdifference", re.compile(r"\bcrossdifference\b", re.IGNORECASE)),
    ("Hirst Inverse", re.compile(r"\bhirst inverse\b", re.IGNORECASE)),
    ("Line Conjugate", re.compile(r"\bline conjugate\b", re.IGNORECASE)),
    ("Aleph Conjugate", re.compile(r"\baleph conjugate\b", re.IGNORECASE)),
    ("Beth Conjugate", re.compile(r"\bbeth conjugate\b", re.IGNORECASE)),
    ("Harmonic Conjugate", re.compile(r"\bharmonic conjugate\b", re.IGNORECASE)),
]

_UNARY_REL_RE = re.compile(
    r"\b(?:isogonal conjugate|isotomic conjugate|cyclocevian conjugate|"
    r"complement|anticomplement|complementary conjugate|anticomplementary conjugate|"
    r"inverse-in-|circle-inverse|antigonal image|eigencenter|trilinear pole|"
    r"pole wrt|isoconjugate|vertex conjugate|Miquel associate|Dao image|"
    r"similarity image|barycentric image|functional image|trilinear image)\b",
    re.IGNORECASE,
)


def _rst_cell(text: str) -> str:
    """Normalize a single-paragraph cell string cleanly for ``.. list-table::``."""
    return " ".join(str(text or "—").splitlines()).strip() or "—"


def _append_list_table(
    lines: list[str],
    caption: str,
    headers: list[str],
    rows: list[list[str | list[str]]],
    *,
    css_classes: str = "etc-table",
    widths: str | None = None,
) -> None:
    """Append a clean ReStructuredText ``.. list-table::`` block (supporting multi-paragraph cells)."""
    if not rows:
        return
    lines.append(f".. list-table:: {caption}" if caption else ".. list-table::")
    lines.append("   :header-rows: 1")
    lines.append(f"   :class: {css_classes}")
    if widths:
        lines.append(f"   :widths: {widths}")
    lines.append("")
    for idx, hdr in enumerate(headers):
        hdr_txt = " ".join(str(hdr).splitlines()).strip()
        if idx == 0:
            lines.append(f"   * - {hdr_txt}" if hdr_txt else "   * -")
        else:
            lines.append(f"     - {hdr_txt}" if hdr_txt else "     -")
    for row in rows:
        for idx, cell in enumerate(row):
            prefix = "   * - " if idx == 0 else "     - "
            if isinstance(cell, list):
                paras = [_rst_cell(p) for p in cell if str(p).strip()]
                if not paras:
                    lines.append(f"{prefix}—")
                else:
                    lines.append(f"{prefix}{paras[0]}")
                    for extra_p in paras[1:]:
                        lines.append("")
                        lines.append(f"       {extra_p}")
            else:
                lines.append(f"{prefix}{_rst_cell(cell)}")
    lines.append("")


def _build_identity_bar(
    num: int,
    concordance: Any,
    exact_search_ltx: str,
    approx_search: float,
) -> list[str]:
    if not concordance:
        return []
    search_part = (
        rf" • **Search** :math:`(6,9,13)`: :math:`{exact_search_ltx} \approx {approx_search:.12f}`"
        if exact_search_ltx
        else (rf" • **Search** :math:`(6,9,13)`: :math:`{approx_search:.12f}`" if abs(approx_search) > 1e-12 else "")
    )
    return [
        ".. container:: etc-identity-bar",
        "",
        f"   ``{concordance.signature}`` • **{concordance.classical_ref}** • **Kimberling** ``X({num})``{search_part}",
        "",
    ]


_CYC_LOWER = {"a": "b", "b": "c", "c": "a"}
_CYC_UPPER = {"A": "B", "B": "C", "C": "A"}

_LATEX_CYC_TOKEN_RE = re.compile(
    r"(\\operatorname\{[^}]+\}|\\text\{[^}]+\}|\\mathrm\{[^}]+\}|"
    r"\\[A-Za-z]+|"
    r"(?<![A-Za-z\\])(?:Area|area|ABC)(?![A-Za-z])|"
    r"(?<![A-Za-z\\])(?:S|r)_\{?[ABCabc]\}?|"
    r"(?<![A-Za-z\\])[ABC](?=[PU]\()|"
    r"(?<![A-Za-z\\])[abc]+(?![A-Za-z])|"
    r"(?<![A-Za-z\\])[ABC](?![A-Za-z]))"
)


def _cyclic_permute_latex(expr: str, steps: int = 1) -> str:
    """Cyclically permute triangle variables ``(a,b,c)`` and ``(A,B,C)`` inside a LaTeX expression.

    Preserves LaTeX commands (``\\sin``, ``\\cos``, ``\\operatorname{area}``), symmetric invariants
    (``ABC``, ``Area``, ``S``, ``S_{\\omega}``, ``r``, ``R``, ``s``, ``abc``), and handles
    multi-letter products (``bc -> ca -> ab``), digit-prefixed angles (``2A -> 2B -> 2C``),
    subscripts (``S_{A} -> S_{B}``, ``r_{a} -> r_{b}``), and vertex distances (``AP(1) -> BP(1)``).
    """
    steps = steps % 3
    if steps == 0 or not expr:
        return expr

    def _perm_char(ch: str) -> str:
        out = ch
        for _ in range(steps):
            if out in _CYC_LOWER:
                out = _CYC_LOWER[out]
            elif out in _CYC_UPPER:
                out = _CYC_UPPER[out]
        return out

    def _repl(m: re.Match[str]) -> str:
        tok = m.group(1)
        if tok.startswith("\\") or tok in {"Area", "area", "ABC", "abc"}:
            return tok
        if len(tok) >= 3 and tok[0] in {"S", "r"} and tok[1] == "_":
            return tok[:2] + "".join(_perm_char(ch) for ch in tok[2:])
        return "".join(_perm_char(ch) for ch in tok)

    return _LATEX_CYC_TOKEN_RE.sub(_repl, expr)


def _cyclic_permute_prose(text: str, steps: int = 1) -> str:
    """Cyclically permute prose coordinate descriptors like ``A-Soddy ellipse``."""
    steps = steps % 3
    if steps == 0 or not text:
        return text

    def _repl(m: re.Match[str]) -> str:
        ch = m.group(1)
        for _ in range(steps):
            ch = _CYC_UPPER[ch]
        return f"{ch}-"

    return re.sub(r"\b([ABC])-", _repl, text)


def _split_top_level_colons(latex_expr: str) -> list[str]:
    """Split a LaTeX homogeneous triple on top-level ``:`` separators."""
    parts: list[str] = []
    buf: list[str] = []
    depth = 0
    for ch in latex_expr:
        if ch in "({[":
            depth += 1
            buf.append(ch)
        elif ch in ")}]":
            depth = max(0, depth - 1)
            buf.append(ch)
        elif ch == ":" and depth == 0:
            parts.append("".join(buf).strip())
            buf = []
        else:
            buf.append(ch)
    parts.append("".join(buf).strip())
    return [p for p in parts if p]


def _extract_coordinate_triple(
    raw_item: str, enrich_fn: Any
) -> tuple[tuple[str, str, str], str]:
    """Parse one raw ETC coordinate entry into 3 component RST strings plus an optional note.

    Splits explicit ``e1 : e2 : e3`` triples and expands cyclic shorthand ``e1 : :`` so every
    component sits cleanly in its own table row without colon separators.
    """
    raw = " ".join(str(raw_item or "").splitlines()).strip()
    if not raw:
        return (("—", "—", "—"), "")

    # Normalize Kimberling inline function-definition forms like `f(a,b,c) : f(b,c,a) : f(c,a,b), where f(a,b,c) = ...`
    m_fn = re.match(
        r"^:math:`f\(a,\s*b,\s*c\)\s*:\s*f\(b,\s*c,\s*a\)\s*:\s*f\(c,\s*a,\s*b\)`,\s*where\s+:math:`f\(a,\s*b,\s*c\)\s*=\s*(.+)$",
        raw,
    )
    if m_fn:
        body = m_fn.group(1).strip()
        body = re.sub(r"`\\?\s*:math:`", " ", body)
        body = body.replace("`", "").replace(r"\*", " ").replace("*", " ").replace("\\ ", " ")
        body = re.sub(r"\bArea\(ABC\)", r"\\operatorname{area}(ABC)", body)
        body = re.sub(r"\s+", " ", body).strip()
        if body.endswith("))") and body.count("(") < body.count(")"):
            body = body[:-1]
        e1 = body
        e2 = _cyclic_permute_latex(e1, 1)
        e3 = _cyclic_permute_latex(e1, 2)
        return ((f":math:`{e1}`", f":math:`{e2}`", f":math:`{e3}`"), "")

    # Primary math form at the start of the item, plus optional trailing prose note (`, where ...`)
    m_math = re.match(r"^:math:`([^`]+)`(.*)$", raw)
    if m_math:
        math_inner = m_math.group(1).strip()
        tail_raw = m_math.group(2).strip().lstrip(",").strip()
        note = enrich_fn(tail_raw) if tail_raw else ""

        parts = _split_top_level_colons(math_inner)
        if len(parts) >= 3:
            e1, e2, e3 = parts[0], parts[1], parts[2]
        else:
            e1 = parts[0]
            e2 = _cyclic_permute_latex(e1, 1)
            e3 = _cyclic_permute_latex(e1, 2)
        return ((f":math:`{e1}`", f":math:`{e2}`", f":math:`{e3}`"), note)

    # Prose-only coordinate descriptor (e.g., `semi-major axis of A-Soddy ellipse : :`)
    clean_prose = re.sub(r"\s*:\s*:\s*$", "", raw).strip()
    p1 = enrich_fn(clean_prose)
    p2 = enrich_fn(_cyclic_permute_prose(clean_prose, 1))
    p3 = enrich_fn(_cyclic_permute_prose(clean_prose, 2))
    return ((p1, p2, p3), "")


def _format_ordered_coordinates_table(
    data: dict[str, Any],
    exact_search_ltx: str,
    approx_search: float,
    enrich_fn: Any,
    num: int = 0,
) -> list[str]:
    """Render Trilinears, Barycentrics, and Tripolars as vertical 3-row component tables.

    Each system renders one row per coordinate axis (``α, β, γ``; ``u, v, w``; ``PA, PB, PC``)
    wired with ``:g:`` links to the exact struts, sub-triangles, and vertex spokes in
    ``02_coordinates.svg`` for two-way table ↔ graphic highlighting.
    """
    out: list[str] = []
    if num > 0:
        tri_axes = (
            f":g:`α </ X_{num} T_a />`",
            f":g:`β </ X_{num} T_b />`",
            f":g:`γ </ X_{num} T_c />`",
        )
        bary_axes = (
            f":g:`u << X_{num} B C >>`",
            f":g:`v << X_{num} C A >>`",
            f":g:`w << X_{num} A B >>`",
        )
        trip_axes = (
            f":g:`PA </ X_{num} A />`",
            f":g:`PB </ X_{num} B />`",
            f":g:`PC </ X_{num} C />`",
        )
        table_cls = "etc-table etc-coord-table etc-mode-coordinates"
    else:
        tri_axes = (r":math:`\alpha`", r":math:`\beta`", r":math:`\gamma`")
        bary_axes = (r":math:`u`", r":math:`v`", r":math:`w`")
        trip_axes = (r":math:`PA`", r":math:`PB`", r":math:`PC`")
        table_cls = "etc-table etc-coord-table"

    coord_specs = [
        ("trilinears", "Trilinears", tri_axes),
        ("barycentrics", "Barycentrics", bary_axes),
        ("tripolars", "Tripolars", trip_axes),
    ]

    for c_key, caption, axis_labels in coord_specs:
        raw_items = [x for x in (data.get(c_key) or []) if str(x).strip()]
        if not raw_items:
            continue

        # Merge standalone trailing `where ...` items onto notes instead of repeating 3 times
        parsed_entries: list[tuple[tuple[str, str, str], str]] = []
        notes: list[str] = []
        for raw_item in raw_items:
            stripped = " ".join(str(raw_item).splitlines()).strip()
            if stripped.lower().startswith("where ") and parsed_entries:
                enr_note = enrich_fn(stripped)
                if enr_note:
                    notes.append(enr_note)
                continue
            triple, note = _extract_coordinate_triple(stripped, enrich_fn)
            parsed_entries.append((triple, note))
            if note:
                notes.append(note)

        if not parsed_entries:
            continue

        canon_triple = parsed_entries[0][0]
        alt_triples = [entry[0] for entry in parsed_entries[1:]]

        rows: list[list[str | list[str]]] = []
        for comp_idx, axis_lbl in enumerate(axis_labels):
            canon_val = canon_triple[comp_idx]
            alt_cell: str | list[str] = [t[comp_idx] for t in alt_triples] if alt_triples else "—"
            rows.append([axis_lbl, canon_val, alt_cell])

        _append_list_table(
            out,
            "",
            [caption, "Canonical", "Alternates"],
            rows,
            css_classes=table_cls,
            widths="18 41 41",
        )
        if notes:
            out.append(".. container:: etc-coord-notes")
            out.append("")
            for note_txt in notes:
                out.append(f"   *Note:* {note_txt}")
                out.append("")

    return out


def _format_four_triangle_table_tabular(num: int) -> list[str]:
    """Build the 7-row Canonical Triangle Symbolic Invariants table with clickable panel :g: links."""
    from .plates import CIRCLE_CENTER_SPECS
    from .symbolic_cache import CenterSymbolicRegistry, format_symbolic_latex
    from .triangles import CANONICAL_TRIANGLES

    tri_specs = [
        ("heronian", r":g:`Heronian (15, 13, 14) <panel-heronian>`"),
        ("right", r":g:`Right (3, 4, 5) <panel-right>`"),
        ("kepler", r":g:`Kepler (1, √φ, φ) <panel-kepler>`"),
        ("kimberling", r":g:`Kimberling (6, 9, 13) <panel-kimberling>`"),
        ("golden", r":g:`Golden (φ, φ, 1) <panel-golden>`"),
        ("gnomon", r":g:`Gnomon (1, 1, φ) <panel-gnomon>`"),
        ("equilateral", "**Equilateral (2, 2, 2)**"),
    ]
    c_spec = CIRCLE_CENTER_SPECS.get(num)
    dist_col = (
        c_spec.table_header
        if c_spec is not None
        else r"Directed Trilinear :math:`(d_a,\, Q_a)`"
    )
    rows: list[list[str | list[str]]] = []
    for t_key, t_label in tri_specs:
        tri = CANONICAL_TRIANGLES[t_key]
        rec = CenterSymbolicRegistry(tri).get(num)
        if rec is None:
            continue
        kp = rec.is_kepler
        f_latex = f":math:`{tri.coordinate_field_latex([*rec.xy, *rec.bary])}`"

        if rec.is_indeterminate:
            xy_cell: str | list[str] = ["*indeterminate*", r"*(D₃ symmetry)*"]
            tri_cell: str | list[str] = [r":math:`\alpha = 0`", r":math:`\beta = 0`", r":math:`\gamma = 0`"]
            bary_cell: str | list[str] = [":math:`u = 0`", ":math:`v = 0`", ":math:`w = 0`"]
            sa_cell: str | list[str] = ["—"]
            dq_cell: str | list[str] = ["—"]
        else:
            x_ltx = format_symbolic_latex(rec.xy[0], kepler_phi=kp)
            y_ltx = format_symbolic_latex(rec.xy[1], kepler_phi=kp)
            xy_cell = [f":math:`x = {x_ltx}`", f":math:`y = {y_ltx}`"]

            tri_parts = _split_top_level_colons(rec.trilinear_latex())
            tri_cell = (
                [
                    rf":math:`\alpha = {tri_parts[0]}`",
                    rf":math:`\beta = {tri_parts[1]}`",
                    rf":math:`\gamma = {tri_parts[2]}`",
                ]
                if len(tri_parts) == 3
                else f":math:`{rec.trilinear_latex()}`"
            )

            bary_parts = _split_top_level_colons(rec.bary_latex())
            bary_cell = (
                [
                    f":math:`u = {bary_parts[0]}`",
                    f":math:`v = {bary_parts[1]}`",
                    f":math:`w = {bary_parts[2]}`",
                ]
                if len(bary_parts) == 3
                else f":math:`{rec.bary_latex()}`"
            )

            sa_parts = [format_symbolic_latex(sa, kepler_phi=kp) for sa in rec.sub_areas]
            sa_cell = [
                rf":math:`\Delta_a = {sa_parts[0]}`",
                rf":math:`\Delta_b = {sa_parts[1]}`",
                rf":math:`\Delta_c = {sa_parts[2]}`",
            ]

            if c_spec is not None:
                d_val = c_spec.radius_fn(tri)
                q_val = tri.simplify(d_val * d_val)
                d_ltx = format_symbolic_latex(d_val, kepler_phi=kp)
                q_ltx = format_symbolic_latex(q_val, kepler_phi=kp)
                dq_cell = [
                    f":math:`{c_spec.r_sym} = {d_ltx}`",
                    f":math:`{c_spec.q_sym} = {q_ltx}`",
                ]
            else:
                d_val = rec.search_value
                q_val = tri.simplify(d_val * d_val)
                d_ltx = format_symbolic_latex(d_val, kepler_phi=kp)
                q_ltx = format_symbolic_latex(q_val, kepler_phi=kp)
                dq_cell = [
                    f":math:`d_a = {d_ltx}`",
                    f":math:`Q_a = {q_ltx}`",
                ]
        rows.append(
            [
                t_label,
                f_latex,
                xy_cell,
                tri_cell,
                bary_cell,
                sa_cell,
                dq_cell,
            ]
        )

    out: list[str] = []
    _append_list_table(
        out,
        "Canonical Triangle Symbolic Invariants",
        [
            "Triangle",
            "Field",
            r"Cartesian",
            r"Trilinears",
            r"Barycentrics",
            r"Sub-Areas",
            dist_col,
        ],
        rows,
        css_classes="etc-table etc-mode-four-triangles",
    )
    return out


def _format_coordinate_decomposition_table(num: int) -> list[str]:
    """Tabular Heronian trilinear struts, pedal touchpoints, and signed barycentric sub-areas."""
    import sympy as sp

    from .plates import CIRCLE_CENTER_SPECS, exact_pedal_foot_and_param
    from .symbolic_cache import CenterSymbolicRegistry, format_symbolic_latex
    from .triangles import CANONICAL_TRIANGLES

    tri = CANONICAL_TRIANGLES["heronian"]
    rec = CenterSymbolicRegistry(tri).get(num)
    if rec is None:
        return []
    key = f"X_{num}"

    pa_ex, _ = exact_pedal_foot_and_param(rec.xy, tri.B_xy, tri.C_xy, tri)
    pb_ex, _ = exact_pedal_foot_and_param(rec.xy, tri.C_xy, tri.A_xy, tri)
    pc_ex, _ = exact_pedal_foot_and_param(rec.xy, tri.A_xy, tri.B_xy, tri)
    sa, sb, sc = rec.sub_areas

    def _pt_ltx(pt: tuple[sp.Expr, sp.Expr]) -> str:
        return rf"\left({format_symbolic_latex(pt[0])},\; {format_symbolic_latex(pt[1])}\right)"

    side_specs = [
        ("BC", "[ B C ]", "a", tri.a, "T_a", pa_ex, "B C", sa, "a"),
        ("CA", "[ C A ]", "b", tri.b, "T_b", pb_ex, "C A", sb, "b"),
        ("AB", "[ A B ]", "c", tri.c, "T_c", pc_ex, "A B", sc, "c"),
    ]
    rows: list[list[str]] = []
    for s_disp, s_ref, s_sym, s_len, f_id, foot_xy, sub_verts, area_v, idx_l in side_specs:
        d_val = tri.simplify(sp.Integer(2) * area_v / s_len)
        q_val = tri.simplify(d_val * d_val)
        d_ltx = format_symbolic_latex(d_val)
        q_ltx = format_symbolic_latex(q_val)
        a_ltx = format_symbolic_latex(area_v)
        sub_disp = f"△{key}{s_disp}"
        rows.append(
            [
                f":g:`{s_disp} <{s_ref}>` (:math:`{s_sym} = {format_symbolic_latex(s_len)}`)",
                f":g:`{f_id} <{f_id}>` = :math:`{_pt_ltx(foot_xy)}`",
                rf":g:`{key}{f_id} </ {key} {f_id} />` (:math:`d_{idx_l} = {d_ltx},\; Q = {q_ltx}`)",
                f":g:`{sub_disp} << {key} {sub_verts} >>`",
                rf":math:`\Delta_{idx_l} = {a_ltx}`",
            ]
        )

    c_spec = CIRCLE_CENTER_SPECS.get(num)
    summary_note = (
        rf"Barycentric sum :math:`\Delta_a + \Delta_b + \Delta_c = 84 = \Delta` "
        rf"(:math:`u : v : w = {rec.bary_latex()}`); trilinear ratio :math:`\alpha : \beta : \gamma = {rec.trilinear_latex()}`"
    )
    if c_spec is not None:
        r_val = c_spec.radius_fn(tri)
        q_r = tri.simplify(r_val * r_val)
        summary_note += (
            f"; :g:`{c_spec.circle_label.lower()} <{c_spec.circle_id}>` "
            rf":math:`{c_spec.r_sym} = {format_symbolic_latex(r_val)},\; {c_spec.q_sym} = {format_symbolic_latex(q_r)}`"
        )
    summary_note += "."

    out: list[str] = []
    _append_list_table(
        out,
        f"Coordinate Decomposition of {key} on Heronian (15, 13, 14)",
        [
            "Sideline",
            "Pedal Foot",
            "Trilinear Strut",
            "Sub-Triangle",
            "Signed Area",
        ],
        rows,
        css_classes="etc-table etc-mode-coordinates",
    )
    out.extend(
        [
            ".. container:: etc-mode-coordinates",
            "",
            f"   {summary_note}",
            "",
        ]
    )
    return out


def _format_constructed_elements_table(
    model: Any,
    data: dict[str, Any],
    enun_raw: str,
    valid_centers: set[int] | None,
) -> list[str]:
    """Convert ``_format_constructed_elements_rst`` bullet semantics into a clean 3-column table."""
    from .transform import _format_constructed_elements_rst

    raw_admon = _format_constructed_elements_rst(
        model, data, enun_raw, valid_centers=valid_centers
    )
    if not raw_admon:
        return []
    rows: list[list[str]] = []
    for ln in raw_admon:
        s = ln.strip()
        if not s.startswith("* **"):
            continue
        m = re.match(r"^\*\s+\*\*([^*]+?):\*\*\s*(.+)$", s)
        if not m:
            continue
        role, rest = m.group(1).strip(), m.group(2).strip()
        if " — " in rest:
            els_part, prop_part = rest.split(" — ", 1)
        else:
            els_part, prop_part = rest, "—"
        rows.append([f"**{role}**", els_part.strip(), prop_part.strip()])

    if not rows:
        return raw_admon
    out: list[str] = []
    _append_list_table(
        out,
        "Constructed Geometric Elements",
        ["Role", "Elements", "Property"],
        rows,
        css_classes="etc-table",
        widths="24 38 38",
    )
    return out


def _format_central_lines_table(
    num: int,
    model: Any,
    svg_03_refs: set[str],
    valid_centers: set[int] | None = None,
) -> list[str]:
    """Format Principal Central Lines through ``X_num`` as a crisp, hover-linked table."""
    import sympy.geometry as spg
    from geometor.model import line_spread, zero_test

    from .plates import _exact_line_eq_pair
    from .render import _load_center_names, model_to_elements_list
    from .symbolic_cache import (
        EXACT_CYCLIC_BARYCENTRICS,
        CenterSymbolicRegistry,
        format_symbolic_latex,
    )
    from .transform import _classify_central_line_name, _short_center_title
    from .triangles import CANONICAL_TRIANGLES

    if model is None:
        return []
    tri = CANONICAL_TRIANGLES["heronian"]
    reg = CenterSymbolicRegistry(tri)
    center_names = _load_center_names()
    elements = model_to_elements_list(model)

    plotted_centers: set[int] = set()
    for el in elements:
        if el["type"] == "point":
            m_x = re.match(r"^X_(\d+)$", el["ID"])
            if m_x:
                plotted_centers.add(int(m_x.group(1)))

    ab_el = model.get_element_by_ID("[ A B ]")
    rows: list[list[str]] = []

    for el in elements:
        if el["type"] != "line":
            continue
        lid = el["ID"]
        m_cl = re.match(r"^\{\s*(\d+)\s*,\s*(\d+)\s*\}$", lid)
        if not m_cl or lid not in svg_03_refs:
            continue
        i_n, j_n = int(m_cl.group(1)), int(m_cl.group(2))
        if i_n not in EXACT_CYCLIC_BARYCENTRICS or j_n not in EXACT_CYCLIC_BARYCENTRICS:
            continue
        rec_i = reg.get(i_n)
        rec_j = reg.get(j_n)

        col_nums: list[int] = []
        for cand in sorted(plotted_centers | {num, i_n, j_n}):
            if cand not in EXACT_CYCLIC_BARYCENTRICS:
                continue
            rc = reg.get(cand)
            det = (
                (rec_j.xy[0] - rec_i.xy[0]) * (rc.xy[1] - rec_i.xy[1])
                - (rec_j.xy[1] - rec_i.xy[1]) * (rc.xy[0] - rec_i.xy[0])
            )
            if zero_test(det):
                col_nums.append(cand)

        line_name = _classify_central_line_name(set(col_nums), i_n, j_n, center_names)
        set_disp = "{" + ", ".join(str(k) for k in col_nums) + "}"

        pt_parts: list[str] = []
        for k in col_nums:
            xk = f"X_{k}"
            if k == num:
                pt_parts.append(f":g:`{xk} <{xk}>`")
                continue
            rk = reg.get(k)
            t_short = _short_center_title(center_names.get(str(k), xk))
            can_ref = valid_centers is None or k in valid_centers
            if xk in svg_03_refs:
                head = f":g:`{xk} <{xk}>`"
                if can_ref:
                    pt_parts.append(f"{head} (:ref:`{t_short} <{xk}>`, :math:`{rk.xy_latex()}`)")
                else:
                    pt_parts.append(f"{head} (*{t_short}*, :math:`{rk.xy_latex()}`)")
            elif can_ref:
                pt_parts.append(f":ref:`{xk} <{xk}>` (*{t_short}*, :math:`{rk.xy_latex()}`)")
            else:
                pt_parts.append(f"**{xk}** (*{t_short}*, :math:`{rk.xy_latex()}`)")

        eq_ltx, _ = _exact_line_eq_pair(rec_i.xy, rec_j.xy, tri)
        line_geom = spg.Line(spg.Point(*rec_i.xy), spg.Point(*rec_j.xy))
        if isinstance(ab_el, spg.Line):
            spr = tri.simplify(line_spread(ab_el, line_geom))
            spr_ltx = format_symbolic_latex(spr)
            if zero_test(spr):
                spr_cell = "0 *(parallel to* :g:`AB <[ A B ]>` *)*"
            elif zero_test(spr - 1):
                spr_cell = "1 *(perp. to* :g:`AB <[ A B ]>` *)*"
            else:
                spr_cell = rf":math:`{spr_ltx}`"
        else:
            spr_cell = "—"

        rows.append(
            [
                f"**{line_name}**",
                f":g:`{set_disp} <{lid}>`",
                ", ".join(pt_parts),
                f":math:`{eq_ltx}`",
                spr_cell,
            ]
        )

    out: list[str] = []
    _append_list_table(
        out,
        f"Principal Central Lines Through X_{num} on Heronian (15, 13, 14)",
        ["Central Line", "Indices", "Collinear Centers", "Exact Equation", "Spread vs AB"],
        rows,
        css_classes="etc-table etc-mode-lines",
    )
    return out


def _format_algebraic_operators_table(
    num: int,
    svg_04_refs: set[str],
    valid_centers: set[int] | None = None,
) -> list[str]:
    """Format Canonical Algebraic Operators on ``X_num`` as a structured table."""
    import sympy as sp

    from .plates import AlgebraicPartnerInfo, build_center_relations_bundle
    from .render import _load_center_names
    from .symbolic_cache import CenterSymbolicRegistry, format_symbolic_latex
    from .transform import _short_center_title
    from .triangles import CANONICAL_TRIANGLES

    tri = CANONICAL_TRIANGLES["heronian"]
    reg = CenterSymbolicRegistry(tri)
    rec = reg.get(num)
    bundle = build_center_relations_bundle(num, preset="heronian")
    center_names = _load_center_names()
    key = f"X_{num}"

    def _xy_cell(xy: tuple[sp.Expr, sp.Expr] | None) -> str:
        if xy is None:
            return "—"
        return rf":math:`\left({format_symbolic_latex(xy[0])},\; {format_symbolic_latex(xy[1])}\right)`"

    def _bary_cell(bary: tuple[sp.Expr, sp.Expr, sp.Expr] | None) -> str:
        if bary is None:
            return "—"
        return ":math:`" + " : ".join(format_symbolic_latex(c) for c in bary) + "`"

    def _partner_cell(info: AlgebraicPartnerInfo) -> tuple[str, str]:
        pnum = info.partner_num
        if pnum is None:
            return ("Ideal point" if info.is_ideal else "Algebraic point", "")
        px = f"X_{pnum}"
        t_short = _short_center_title(info.partner_title or center_names.get(str(pnum), px))
        can_ref = valid_centers is None or pnum in valid_centers
        pair_lid = f"{{ {min(num, pnum)}, {max(num, pnum)} }}"
        ray_txt = (
            f" along :g:`{{{min(num, pnum)}, {max(num, pnum)}}} <{pair_lid}>`"
            if pair_lid in svg_04_refs
            else ""
        )
        if px in svg_04_refs:
            chip = f":ref:`{t_short} <{px}>`" if can_ref else f"*{t_short}*"
            return (f":g:`{px} <{px}>` ({chip})", ray_txt)
        if can_ref:
            return (f":ref:`{px} <{px}>` (*{t_short}*)", ray_txt)
        return (f"**{px}** (*{t_short}*)", ray_txt)

    rows: list[list[str]] = []

    # 1. Isogonal Conjugate
    ig = bundle.isogonal
    if ig.is_self:
        rows.append(
            [
                "**Isogonal Conjugate**",
                f":g:`{key} <{key}>` *(self)*",
                f":math:`{rec.xy_latex()}`",
                f":math:`{rec.bary_latex()}`",
                rf"Fixed point of :term:`isogonal conjugate <isogonal-conjugate>` (:math:`{rec.trilinear_latex()}`)",
            ]
        )
    elif ig.is_ideal:
        rows.append(
            [
                "**Isogonal Conjugate**",
                "Line at infinity",
                "—",
                _bary_cell(ig.bary),
                r"Ideal point on :math:`u + v + w = 0`",
            ]
        )
    else:
        p_cell, ray = _partner_cell(ig)
        rows.append(
            [
                "**Isogonal Conjugate**",
                p_cell,
                _xy_cell(ig.xy),
                _bary_cell(ig.bary),
                rf":term:`Isogonal <isogonal-conjugate>` :math:`a^2 vw : b^2 wu : c^2 uv`{ray}",
            ]
        )

    # 2. Isotomic Conjugate
    it = bundle.isotomic
    if it.is_self:
        rows.append(
            [
                "**Isotomic Conjugate**",
                f":g:`{key} <{key}>` *(self)*",
                f":math:`{rec.xy_latex()}`",
                f":math:`{rec.bary_latex()}`",
                r"Identity of :term:`isotomic conjugate <isotomic-conjugate>`",
            ]
        )
    elif it.is_ideal:
        rows.append(
            [
                "**Isotomic Conjugate**",
                "Line at infinity",
                "—",
                _bary_cell(it.bary),
                r"Ideal point on :math:`u + v + w = 0`",
            ]
        )
    else:
        p_cell, ray = _partner_cell(it)
        rows.append(
            [
                "**Isotomic Conjugate**",
                p_cell,
                _xy_cell(it.xy),
                _bary_cell(it.bary),
                rf":term:`Isotomic <isotomic-conjugate>` :math:`vw : wu : uv`{ray}",
            ]
        )

    # 3. Complement & Anticomplement
    x2_chip = ":g:`X_2 <X_2>`" if "X_2" in svg_04_refs else ":ref:`X_2 <X_2>`"
    comp = bundle.complement
    anti = bundle.anticomplement
    if comp.is_self and anti.is_self:
        rows.append(
            [
                "**Complement / Anticomplement**",
                f":g:`{key} <{key}>` *(fixed center)*",
                f":math:`{rec.xy_latex()}`",
                f":math:`{rec.bary_latex()}`",
                r"Fixed center of :term:`complement <complement>` (:math:`-\frac{1}{2}`) & :term:`anticomplement <anticomplement>` (:math:`-2`)",
            ]
        )
    else:
        cp_cell, c_ray = _partner_cell(comp)
        rows.append(
            [
                "**Complement**",
                cp_cell,
                _xy_cell(comp.xy),
                _bary_cell(comp.bary),
                rf":term:`Complement <complement>` from {x2_chip} (scale :math:`-\frac{{1}}{{2}}`){c_ray}",
            ]
        )
        ap_cell, a_ray = _partner_cell(anti)
        rows.append(
            [
                "**Anticomplement**",
                ap_cell,
                _xy_cell(anti.xy),
                _bary_cell(anti.bary),
                rf":term:`Anticomplement <anticomplement>` from {x2_chip} (scale :math:`-2`){a_ray}",
            ]
        )

    # 4. Circumcircle Inversion
    ci = bundle.circumcircle_inverse
    x3_chip = ":g:`X_3 <X_3>`" if "X_3" in svg_04_refs else ":ref:`X_3 <X_3>`"
    circ_chip = ":g:`circumcircle <circumcircle>`" if "circumcircle" in svg_04_refs else "the circumcircle"
    if ci.is_center_of_inversion:
        rows.append(
            [
                "**Circumcircle Inversion**",
                "Line at infinity",
                "—",
                "—",
                rf"Center of {circ_chip} (:math:`R = \frac{{65}}{{8}},\; Q_R = \frac{{4225}}{{64}}`)",
            ]
        )
    else:
        p_cell, _ = _partner_cell(ci)
        q_op_ltx = format_symbolic_latex(ci.inversion_quadrance) if ci.inversion_quadrance is not None else ""
        sc_ltx = format_symbolic_latex(ci.inversion_scale) if ci.inversion_scale is not None else ""
        ray_id = f"{{ {min(num, 3)}, {max(num, 3)} }}"
        ray_txt = (
            f" along :g:`{{{min(num, 3)}, {max(num, 3)}}} <{ray_id}>`"
            if ray_id in svg_04_refs
            else ""
        )
        rows.append(
            [
                "**Circumcircle Inverse**",
                p_cell,
                _xy_cell(ci.xy),
                _bary_cell(ci.bary),
                rf"Inversion in {circ_chip} at {x3_chip}{ray_txt} (:math:`Q = {q_op_ltx},\; Q_R/Q = {sc_ltx}`)",
            ]
        )

    # 5. Quadratic sqrt(3) Galois Conjugate (X_13..X_18)
    if bundle.galois_conjugate is not None:
        gp_cell, g_ray = _partner_cell(bundle.galois_conjugate)
        rows.append(
            [
                r"**Galois** :math:`\sqrt{3}` **Conjugate**",
                gp_cell,
                _xy_cell(bundle.galois_conjugate.xy),
                _bary_cell(bundle.galois_conjugate.bary),
                rf"Automorphism :math:`\sqrt{{3}} \mapsto -\sqrt{{3}}` over :math:`\mathbb{{Q}}(\sqrt{{3}})`{g_ray}",
            ]
        )

    # 6. Feuerbach Harmonic Conjugate (X_11 <-> X_12)
    if bundle.harmonic_feuerbach_partner is not None:
        h_k = bundle.harmonic_feuerbach_partner
        hk_rec = reg.get(h_k)
        hk_id = f"X_{h_k}"
        hk_title = _short_center_title(center_names.get(str(h_k), hk_id))
        hk_chip = (
            f":g:`{hk_id} <{hk_id}>` (:ref:`{hk_title} <{hk_id}>`)"
            if hk_id in svg_04_refs
            else f":ref:`{hk_id} <{hk_id}>` (*{hk_title}*)"
        )
        x1_c = ":g:`X_1 <X_1>`" if "X_1" in svg_04_refs else ":ref:`X_1 <X_1>`"
        x5_c = ":g:`X_5 <X_5>`" if "X_5" in svg_04_refs else ":ref:`X_5 <X_5>`"
        rows.append(
            [
                "**Feuerbach Harmonic**",
                hk_chip,
                f":math:`{hk_rec.xy_latex()}`",
                f":math:`{hk_rec.bary_latex()}`",
                rf"Divides {x1_c} and {x5_c} harmonically (:math:`(X_1, X_5; X_{{11}}, X_{{12}}) = -1`)",
            ]
        )

    out: list[str] = []
    _append_list_table(
        out,
        f"Canonical Algebraic Operators on {key} (Heronian 15, 13, 14)",
        ["Operator", "Partner", r"Cartesian :math:`(x, y)`", r"Barycentrics :math:`u : v : w`", "Transformation Law"],
        rows,
        css_classes="etc-table etc-mode-relations",
    )
    return out


def _categorize_functional_relations(
    raw_relations: list[str],
    enrich_rel_fn: Any,
) -> tuple[list[list[str]], list[list[str]], list[list[str]]]:
    """Group ETC functional relations into (binary_rows, unary_rows, triangle_rows)."""
    binary_rows: list[list[str]] = []
    unary_rows: list[list[str]] = []
    triangle_rows: list[list[str]] = []

    for rel in raw_relations:
        enr = enrich_rel_fn(rel)
        flat = " ".join(ln.strip() for ln in enr.splitlines() if ln.strip())
        if not flat:
            continue
        # Strip leading "X_n = " prefix inside structured table cells
        rhs = re.sub(r"^(?::ref:`X_\d+ <X_\d+>`|X_\d+)\s*=\s*", "", flat, count=1)

        matched_bin = None
        for label, rx in _BINARY_REL_PATTERNS:
            if rx.search(rel):
                matched_bin = label
                break
        if matched_bin is not None:
            binary_rows.append([f"**{matched_bin}**", rhs])
        elif _UNARY_REL_RE.search(rel):
            unary_rows.append([rhs])
        else:
            triangle_rows.append([rhs])

    return binary_rows, unary_rows, triangle_rows


def _format_notes_structured(
    remaining_notes: list[str],
    enrich_fn: Any,
    valid_centers: set[int] | None,
) -> list[str]:
    """Format curated notes, elevating clean multi-item excenter/trilinear definitions into tables."""
    out: list[str] = []

    def _fmt_circle_idx(m: re.Match) -> str:
        idx_str = m.group(1)
        idx_int = int(idx_str)
        if valid_centers is None or idx_int in valid_centers:
            return f":ref:`{idx_str} <X_{idx_str}>`"
        return idx_str

    for note in remaining_notes:
        # Detect structured A/B/C excenter coordinate notes cleanly without hardcoding center numbers
        if "A-excenter" in note and "B-excenter" in note and "C-excenter" in note:
            exc_rows: list[list[str]] = []
            for vtx, trilin, exrad in (
                (":g:`A <A>`-excenter", r":math:`-1 : 1 : 1`", r":math:`r_a = \frac{2\Delta}{-a+b+c}`"),
                (":g:`B <B>`-excenter", r":math:`1 : -1 : 1`", r":math:`r_b = \frac{2\Delta}{a-b+c}`"),
                (":g:`C <C>`-excenter", r":math:`1 : 1 : -1`", r":math:`r_c = \frac{2\Delta}{a+b-c}`"),
            ):
                exc_rows.append([vtx, trilin, exrad])
            _append_list_table(
                out,
                "Excenters & Associated Exradii",
                ["Excenter", r"Trilinears :math:`\alpha : \beta : \gamma`", "Exradius Formula"],
                exc_rows,
                css_classes="etc-table",
                widths="26 32 42",
            )
            continue

        enriched_note = enrich_fn(note)
        out.append(".. container:: note-item")
        out.append("")
        for n_ln in enriched_note.splitlines():
            if n_ln.strip().startswith("* (") and ";" in n_ln:
                n_ln = re.sub(r"(?<=[;,]\s)(\d+)\b", _fmt_circle_idx, n_ln)
            out.append(f"   {n_ln}" if n_ln.strip() else "")
        out.append("")

    return out


def format_multitrack_center_rsts(
    data: dict[str, Any],
    entry_dir: Path,
    glossary_terms: dict[str, Any] | list[str] | None = None,
    preambles: list[dict[str, Any]] | None = None,
    valid_centers: set[int] | None = None,
    figure_uri: str | None = None,
    search_value: float | None = None,
    include_model_py: bool = False,
    model: Any = None,
) -> dict[str, str]:
    """Generate the complete 5-track tabular Book Codex RST mapping for a symbolic center.

    Returns a dict mapping filename (``"index.rst"``, ``"lines.rst"``, ``"relations.rst"``,
    ``"notes.rst"``) to its verified ReStructuredText source.
    """
    from .ops import get_center_concordance
    from .parser import parse_preamble
    from .plates import CIRCLE_CENTER_SPECS
    from .symbolic_cache import CenterSymbolicRegistry, format_symbolic_latex
    from .transform import (
        _COLLECTION_1_TOPIC_GUIDES,
        _enrich_text,
        _extract_primary_enunciation,
        _format_act5_prose_rst,
        _reconcile_g_roles_with_svgs,
        _wrap_relation_tuples,
        extract_svg_element_refs,
    )
    from .triangles import CANONICAL_TRIANGLES

    key = data["key"]
    title = data.get("title", "")
    num = int(data.get("num") or re.sub(r"[^0-9]", "", key) or 0)
    if num > 0:
        key = f"X_{num}"

    concordance = get_center_concordance(num)
    hero_tri = CANONICAL_TRIANGLES["heronian"]
    hero_rec = CenterSymbolicRegistry(hero_tri).get(num)
    kimb_tri = CANONICAL_TRIANGLES["kimberling"]
    kimb_rec = CenterSymbolicRegistry(kimb_tri).get(num)
    exact_search_ltx = kimb_rec.search_latex() if kimb_rec is not None else ""
    approx_search = (
        kimb_rec.approx_search_value()
        if kimb_rec is not None
        else (search_value or 0.0)
    )

    alt_title = f"{key} — {title}" if title and title != key else key
    cap_title = f"**{key}** (*{title}*)" if title and title != key else f"**{key}**"
    fig_file = figure_uri or f"x-{num:05d}.svg"

    r_act1 = extract_svg_element_refs(entry_dir / fig_file)
    r_act2 = extract_svg_element_refs(entry_dir / "02_coordinates.svg")
    r_act3 = extract_svg_element_refs(entry_dir / "03_central_lines.svg")
    r_act4 = extract_svg_element_refs(entry_dir / "04_relations.svg")
    r_act5 = extract_svg_element_refs(entry_dir / "05_four_triangles.svg")

    raw_notes = data.get("notes") or []
    raw_relations = data.get("relations") or []
    enun_raw, remaining_notes = _extract_primary_enunciation(
        raw_notes, raw_relations, num=num, title=title
    )

    def _make_enrich():
        seen_t: set[str] = set()
        seen_p: set[str] = set()
        seen_c: set[str] = set()

        def _fn(txt: str) -> str:
            return _enrich_text(
                txt, glossary_terms, seen_t, seen_p, seen_c, valid_centers=valid_centers
            )

        return _fn

    identity_bar = _build_identity_bar(num, concordance, exact_search_ltx, approx_search)

    # ==================================================================
    # Track 1: Overview (index.rst)
    # ==================================================================
    enrich_ov = _make_enrich()
    ov: list[str] = [
        f":order: {num}",
        f":canonical_id: {key}",
    ]
    if title and title != key:
        ov.append(f":subtitle: {title}")
    ov.append(f":tracks: {TRACKS_FRONTMATTER}")
    aliases = data.get("aliases") or []
    if aliases:
        ov.append(f":aliases: {', '.join(aliases)}")
    if data.get("dependencies"):
        ov.append(f":dependencies: {', '.join(data['dependencies'])}")
    ov.append("")

    ov.append(f".. _X_{num}:")
    anchor_id = data.get("anchor_id")
    seen_anchors = {f"x_{num}"}
    if anchor_id and anchor_id.lower() not in seen_anchors and anchor_id not in {f"X_{num}", f"X({num})"}:
        ov.append(f".. _{anchor_id}:")
        seen_anchors.add(anchor_id.lower())
    if concordance and concordance.function_name.lower() not in seen_anchors:
        ov.append(f".. _{concordance.function_name}:")
    ov.append("")

    ov.extend([key, "=" * max(4, len(key)), ""])
    if title and title != key:
        ov.extend([f".. rubric:: {title}", ""])
    ov.extend(identity_bar)

    if enun_raw:
        ov.extend([".. enunciation::", ""])
        for e_ln in enrich_ov(enun_raw).splitlines():
            ov.append(f"   {e_ln}" if e_ln.strip() else "")
        ov.append("")

    if preambles:
        for p_item in preambles:
            parsed_p = parse_preamble(p_item.get("html", ""))
            p_title = parsed_p["title"] or p_item.get("title", "Preamble")
            p_paras = parsed_p["paragraphs"]
            if p_item.get("id"):
                ov.extend([f".. _{p_item['id']}:", ""])
            ov.extend([f".. admonition:: Group Preamble — {p_title}", "   :class: note", ""])
            for para in p_paras or [p_title]:
                for p_ln in enrich_ov(para).splitlines():
                    ov.append(f"   {p_ln}" if p_ln.strip() else "")
                ov.append("")

    # Single primary figure (becomes the sticky .etc-viewer with Mode + 4-Triangle tabs)
    h_field = hero_tri.coordinate_field_latex([*hero_rec.xy, *hero_rec.bary])
    field_adj = "exact rational" if h_field == r"\mathbb{Q}" else "exact algebraic"
    c_spec = CIRCLE_CENTER_SPECS.get(num)
    circle_clause = ""
    if c_spec is not None:
        r_ltx = format_symbolic_latex(c_spec.radius_fn(hero_tri))
        circle_clause = rf", and {c_spec.circle_label.lower()} radius :math:`{c_spec.r_sym} = {r_ltx}`"
    ov.extend(
        [
            f".. figure:: {fig_file}",
            f"   :alt: {alt_title}",
            "   :align: center",
            "",
            (
                f"   {cap_title} constructed at :g:`{key} <{key}>` = :math:`{hero_rec.xy_latex()}` in {field_adj} "
                f"coordinates on Heronian :math:`(15, 13, 14)` over :math:`{h_field}` with vertices "
                f":g:`A <A>` = :math:`(0, 0)`, :g:`B <B>` = :math:`(14, 0)`, :g:`C <C>` = :math:`(5, 12)`, "
                rf"area :math:`\Delta = 84`{circle_clause}. Switch view modes or reference triangles above."
            ),
            "",
        ]
    )

    # Ordered Homogeneous Coordinates Table
    ov.extend(["Homogeneous Coordinates", "-----------------------", ""])
    ov.extend(
        _format_ordered_coordinates_table(
            data, exact_search_ltx, approx_search, enrich_ov, num=num
        )
    )
    ov.extend(_format_four_triangle_table_tabular(num))
    act5_lines = _format_act5_prose_rst(num)
    if act5_lines:
        ov.extend([".. container:: etc-mode-four-triangles", ""])
        for a5 in act5_lines:
            ov.append(f"   {a5}" if a5.strip() else "")
    ov.extend(_format_coordinate_decomposition_table(num))

    if model is not None:
        ov.extend(["Constructed Elements", "--------------------", ""])
        ov.extend(_format_constructed_elements_table(model, data, enun_raw, valid_centers))

    combos = data.get("combinations") or []
    if combos:
        combo_rows = []
        for combo in combos:
            enr_c = " ".join(ln.strip() for ln in enrich_ov(combo).splitlines() if ln.strip())
            if enr_c:
                if ", where " in enr_c:
                    expr_p, where_p = enr_c.split(", where ", 1)
                    combo_rows.append([expr_p.strip(), f"where {where_p.strip()}"])
                else:
                    combo_rows.append([enr_c, "—"])
        if combo_rows:
            n_c = len(combo_rows)
            ov.extend(
                [
                    ".. collapse:: Linear Combinations",
                    f"   :badge: {'1 combination' if n_c == 1 else f'{n_c} combinations'}",
                    "",
                ]
            )
            tbl_lines: list[str] = []
            _append_list_table(
                tbl_lines,
                f"Barycentric & Vector Linear Combinations of {key}",
                ["Expression", "Definitions"],
                combo_rows,
                css_classes="etc-table",
                widths="55 45",
            )
            for tl in tbl_lines:
                ov.append(f"   {tl}" if tl else "")
            ov.append("")

    if num in _COLLECTION_1_TOPIC_GUIDES:
        ov.extend(
            [
                ".. admonition:: Related Collection 1 Topic Guides",
                "   :class: tip",
                "",
                f"   {_COLLECTION_1_TOPIC_GUIDES[num]}",
                "",
            ]
        )

    toc_entries = ["lines", "relations", "notes"]
    if include_model_py:
        toc_entries.append("code")
    ov.extend([".. toctree::", "   :hidden:", ""])
    for te in toc_entries:
        ov.append(f"   {te}")
    ov.append("")

    ov_rst = _reconcile_g_roles_with_svgs(
        "\n".join(ov).rstrip() + "\n", r_act1 | r_act2 | r_act5
    )

    # ==================================================================
    # Track 2: Lines (lines.rst)
    # ==================================================================
    enrich_ln = _make_enrich()
    ln_doc: list[str] = [
        f":canonical_id: {key}",
        f":subtitle: {title} — Central Lines" if title and title != key else "Central Lines",
        f":tracks: {TRACKS_FRONTMATTER}",
        "",
        key,
        "=" * max(4, len(key)),
        "",
        f".. rubric:: {title} — Incident Central Lines" if title and title != key else ".. rubric:: Incident Central Lines",
        "",
        *identity_bar,
        f".. figure:: {fig_file}",
        f"   :alt: {alt_title} — Incident Central Lines",
        "   :align: center",
        "",
        f"   **Principal Central Lines Through {key}** on Heronian :math:`(15, 13, 14)`. Hover any line or row to illuminate exact equations and collinear centers; switch tabs above for Right, Kepler, and Kimberling.",
        "",
        "Principal Central Lines",
        "-----------------------",
        "",
    ]
    ln_doc.extend(_format_central_lines_table(num, model, r_act3 | r_act1, valid_centers=valid_centers))

    incidences = data.get("incidences") or []
    for inc in incidences:
        if not isinstance(inc, dict):
            continue
        line_pairs = inc.get("lines") or []
        curves_prefix = inc.get("curves_prefix", "")
        if line_pairs:
            enriched_prefix = enrich_ln(curves_prefix).strip()
            is_bare_key = bool(
                re.match(
                    r"^(?::ref:`X(?:_|\()\d+\)? <X(?:_|\()\d+\)?>`|X(?:_|\()\d+\)?)\s*$",
                    enriched_prefix,
                )
            )
            if enriched_prefix and not is_bare_key:
                ln_doc.extend([".. container:: note-item", ""])
                for c_ln in f"{enriched_prefix}.".splitlines():
                    ln_doc.append(f"   {c_ln}" if c_ln.strip() else "")
                ln_doc.append("")

            def _fmt_inc_pt(pt: int) -> str:
                if valid_centers is None or pt in valid_centers:
                    return f":ref:`{pt} <X_{pt}>`"
                return str(pt)

            formatted_pairs = [f"{{{_fmt_inc_pt(i)}, {_fmt_inc_pt(j)}}}" for i, j in line_pairs]
            n_lines = len(line_pairs)
            ln_doc.extend(
                [
                    "Complete Incident Line Catalog",
                    "------------------------------",
                    "",
                    ".. collapse:: Full Incident Central Line Catalog",
                    f"   :badge: {'1 line' if n_lines == 1 else f'{n_lines} lines'}",
                    "   :class: line-catalog",
                    "",
                    f"   {', '.join(formatted_pairs)}",
                    "",
                ]
            )

    lines_rst = _reconcile_g_roles_with_svgs(
        "\n".join(ln_doc).rstrip() + "\n", r_act3 | r_act1
    )

    # ==================================================================
    # Track 3: Relations (relations.rst)
    # ==================================================================
    enrich_rel = _make_enrich()
    rel_doc: list[str] = [
        f":canonical_id: {key}",
        f":subtitle: {title} — Functional Relations" if title and title != key else "Functional Relations",
        f":tracks: {TRACKS_FRONTMATTER}",
        "",
        key,
        "=" * max(4, len(key)),
        "",
        f".. rubric:: {title} — Functional Relations & Conjugates" if title and title != key else ".. rubric:: Functional Relations & Conjugates",
        "",
        *identity_bar,
        ".. figure:: 04_relations.svg",
        f"   :alt: {alt_title} — Functional Relations and Conjugates",
        "   :align: center",
        "",
        f"   **Conjugate & Homothetic Partners of {key}** on Heronian :math:`(15, 13, 14)`. Hover any plotted partner, connecting ray, or operator row for two-way highlighting.",
        "",
        "Canonical Algebraic Operators",
        "-----------------------------",
        "",
    ]
    rel_doc.extend(_format_algebraic_operators_table(num, r_act4, valid_centers=valid_centers))

    if raw_relations:
        def _enrich_single_rel(r_str: str) -> str:
            return enrich_rel(_wrap_relation_tuples(r_str, valid_centers=valid_centers))

        bin_rows, unary_rows, tri_rows = _categorize_functional_relations(
            raw_relations, _enrich_single_rel
        )
        rel_doc.extend(["Functional Relations Catalog", "----------------------------", ""])

        if unary_rows:
            n_u = len(unary_rows)
            rel_doc.extend(
                [
                    ".. collapse:: Unary Conjugates, Inverses & Images",
                    f"   :badge: {'1 relation' if n_u == 1 else f'{n_u} relations'}",
                    "",
                ]
            )
            utbl: list[str] = []
            _append_list_table(
                utbl,
                f"Unary Conjugates, Inverses & Images of {key}",
                ["Relation"],
                unary_rows,
                css_classes="etc-table",
            )
            for tl in utbl:
                rel_doc.append(f"   {tl}" if tl else "")
            rel_doc.append("")

        if bin_rows:
            n_b = len(bin_rows)
            rel_doc.extend(
                [
                    ".. collapse:: Binary Center Operations",
                    f"   :badge: {'1 group' if n_b == 1 else f'{n_b} groups'}",
                    "",
                ]
            )
            btbl: list[str] = []
            _append_list_table(
                btbl,
                f"Binary Center Operations Producing {key}",
                ["Operator", "Center Pairs & Parameters"],
                bin_rows,
                css_classes="etc-table",
                widths="24 76",
            )
            for tl in btbl:
                rel_doc.append(f"   {tl}" if tl else "")
            rel_doc.append("")

        if tri_rows:
            n_t = len(tri_rows)
            rel_doc.extend(
                [
                    ".. collapse:: Perspectors, Homotheties & Derived-Triangle Centers",
                    f"   :badge: {'1 relation' if n_t == 1 else f'{n_t} relations'}",
                    "",
                ]
            )
            ttbl: list[str] = []
            _append_list_table(
                ttbl,
                f"Derived-Triangle & Perspector Relations of {key}",
                ["Geometric Relation"],
                tri_rows,
                css_classes="etc-table",
            )
            for tl in ttbl:
                rel_doc.append(f"   {tl}" if tl else "")
            rel_doc.append("")

    relations_rst = _reconcile_g_roles_with_svgs(
        "\n".join(rel_doc).rstrip() + "\n", r_act4 | r_act1
    )

    # ==================================================================
    # Track 4: Notes (notes.rst)
    # ==================================================================
    enrich_nt = _make_enrich()
    nt_doc: list[str] = [
        f":canonical_id: {key}",
        f":subtitle: {title} — Notes" if title and title != key else "Notes",
        f":tracks: {TRACKS_FRONTMATTER}",
        "",
        key,
        "=" * max(4, len(key)),
        "",
        f".. rubric:: {title} — Notes & Constructions" if title and title != key else ".. rubric:: Notes & Constructions",
        "",
        *identity_bar,
        f".. figure:: {fig_file}",
        f"   :alt: {alt_title} — Construction Reference",
        "   :align: center",
        "",
        f"   **{key}** (*{title}*) — interactive reference diagram synchronized with geometric references in the notes below."
        if title and title != key
        else f"   **{key}** — interactive reference diagram synchronized with geometric references in the notes below.",
        "",
    ]

    if remaining_notes:
        nt_doc.extend(["Notes & Constructions", "---------------------", ""])
        nt_doc.extend(_format_notes_structured(remaining_notes, enrich_nt, valid_centers))
    else:
        nt_doc.extend(
            [
                "Notes & Constructions",
                "---------------------",
                "",
                f"All defining properties of :g:`{key} <{key}>` are tabulated on the Overview, Lines, and Relations tracks.",
                "",
            ]
        )

    if num in _COLLECTION_1_TOPIC_GUIDES:
        nt_doc.extend(
            [
                ".. admonition:: Related Collection 1 Topic Guides",
                "   :class: tip",
                "",
                f"   {_COLLECTION_1_TOPIC_GUIDES[num]}",
                "",
            ]
        )

    notes_rst = _reconcile_g_roles_with_svgs(
        "\n".join(nt_doc).rstrip() + "\n", r_act1
    )

    return {
        "index.rst": ov_rst,
        "lines.rst": lines_rst,
        "relations.rst": relations_rst,
        "notes.rst": notes_rst,
    }
