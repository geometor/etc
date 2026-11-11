"""Visual coordinate diagram generators and dual-format (9:16 + 16:9) video compiler for ETC centers.

Each per-center video focuses strictly on a single center X_n and its relations across 5 visual facets:

1. PRIMARY VIEW & ENUNCIATION (Thumbnail & Slide 1) — Exact primary construction SVG from the web page
2. HOMOGENEOUS COORDINATES OF X_n (Slide 2) — Trilinear distances (alpha : beta : gamma) and Barycentric sub-areas (u : v : w)
3. INCIDENT CENTRAL LINES (Slide 3) — Primary SVG with .show-lines active, revealing collinear centers and central lines
4. FUNCTIONAL RELATIONS & CONJUGATES (Slide 4) — Explorer-styled model plotting X_n with its conjugates and homothetic partners
5. FOUR REFERENCE TRIANGLES (Slide 5) — 2x2 invariance showcase across Heronian, Right, Kepler, and Kimberling triangles
"""

from __future__ import annotations

import html
import json
import math
import re
from pathlib import Path
from typing import Any

import sympy as sp
from geometor.model import Model

from .construct import (
    CenterRegistry,
    TriangleContext,
    _add_circle,
    _add_line,
    _add_point,
    _add_polygon,
)
from .ops import (
    add_circle,
    add_line,
    add_point,
    construct_reference_triangle,
    create_model,
    midpoint,
    perpendicular_foot,
    promote_point_to_top,
)
from .palette import (
    PARTNER_COLOR_RING,
    REFERENCE_TRIANGLE_COLORS,
    get_central_line_color_token,
    get_circle_color_token,
    token_hex,
)
from .render import EXPLORER_SVG_CSS, INTERACTIVE_SVG_JS, render_model_svg
from .symbolic_cache import (
    CenterSymbolicRegistry,
    format_symbolic_latex,
    format_symbolic_pretty,
)
from .triangles import CANONICAL_TRIANGLES, SymbolicTriangle


def _svg_x(num: int | str, suffix: str = "") -> str:
    """Return SVG `<tspan>` subscript markup for `X_n` followed by optional `suffix`."""
    if suffix:
        return f'X<tspan dy="0.28em" font-size="74%">{num}</tspan><tspan dy="-0.28em">{html.escape(suffix)}</tspan>'
    return f'X<tspan dy="0.28em" font-size="74%">{num}</tspan>'


def _to_screen(pt: tuple[float, float], scale: float, ox: float, oy: float) -> tuple[float, float]:
    """Map mathematical (x, y) coordinates (y up) to SVG screen coordinates (y down)."""
    return (ox + pt[0] * scale, oy - pt[1] * scale)


def _foot_on_line(
    p: tuple[float, float],
    q1: tuple[float, float],
    q2: tuple[float, float],
) -> tuple[float, float]:
    """Return the orthogonal projection (pedal foot) of point `p` onto line `q1-q2`."""
    dx = q2[0] - q1[0]
    dy = q2[1] - q1[1]
    denom = dx * dx + dy * dy
    if denom < 1e-15:
        return q1
    t = ((p[0] - q1[0]) * dx + (p[1] - q1[1]) * dy) / denom
    return (q1[0] + t * dx, q1[1] + t * dy)


def _right_angle_path(
    foot_s: tuple[float, float],
    p_s: tuple[float, float],
    q_s: tuple[float, float],
    size: float = 14.0,
) -> str:
    """Return an SVG path string drawing a crisp right-angle square at `foot_s`."""
    vx = p_s[0] - foot_s[0]
    vy = p_s[1] - foot_s[1]
    v_len = math.hypot(vx, vy)
    ux = q_s[0] - foot_s[0]
    uy = q_s[1] - foot_s[1]
    u_len = math.hypot(ux, uy)
    if v_len < 1e-6 or u_len < 1e-6:
        return ""
    vx, vy = (vx / v_len) * size, (vy / v_len) * size
    ux, uy = (ux / u_len) * size, (uy / u_len) * size
    p1 = (foot_s[0] + ux, foot_s[1] + uy)
    p2 = (foot_s[0] + ux + vx, foot_s[1] + uy + vy)
    p3 = (foot_s[0] + vx, foot_s[1] + vy)
    return f"M {p1[0]:.1f},{p1[1]:.1f} L {p2[0]:.1f},{p2[1]:.1f} L {p3[0]:.1f},{p3[1]:.1f}"


def _clean_formula(s: str) -> str:
    """Strip RST :math:`...` or :term:`...` markup from a coordinate formula string."""
    s = re.sub(r":math:`([^`]+)`", r"\1", s)
    s = re.sub(r":term:`([^`<]+?)(?:\s*<[^>]+>)?`", r"\1", s)
    s = s.replace("\\cdot", "·").replace("\\pi", "π").replace("\\cos", "cos").replace("\\sin", "sin")
    s = s.replace("\\tan", "tan").replace("\\sec", "sec").replace("\\csc", "csc").replace("\\cot", "cot")
    s = re.sub(r"\^\{([^}]+)\}", r"^\1", s)
    s = re.sub(r"_\{([^}]+)\}", r"_\1", s)
    return s.strip()


def _fit_points_to_box(
    pts: list[tuple[float, float]],
    box_x: float,
    box_y: float,
    box_w: float,
    box_h: float,
) -> tuple[float, float, float]:
    """Compute `(scale, ox, oy)` mapping `pts` cleanly inside `[box_x, box_x+box_w] x [box_y, box_y+box_h]`."""
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    span_x = max(max_x - min_x, 0.35)
    span_y = max(max_y - min_y, 0.35)
    scale = min(box_w / span_x, box_h / span_y)
    cx = 0.5 * (min_x + max_x)
    cy = 0.5 * (min_y + max_y)
    ox = box_x + 0.5 * box_w - cx * scale
    oy = box_y + 0.5 * box_h + cy * scale
    return (scale, ox, oy)


def _safe_meta_json(catalog: dict[str, Any]) -> str:
    """Serialize an ``etc-elements-meta`` catalog so XML parsers never trip on ``<``, ``>``, or ``&``."""
    return (
        json.dumps(catalog, ensure_ascii=True, separators=(",", ":"))
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("&", "\\u0026")
    )


def _exact_pedal_foot(
    p_xy: tuple[sp.Expr, sp.Expr],
    q1_xy: tuple[sp.Expr, sp.Expr],
    q2_xy: tuple[sp.Expr, sp.Expr],
    tri: SymbolicTriangle,
) -> tuple[sp.Expr, sp.Expr]:
    """Compute the exact orthogonal projection of ``p_xy`` onto line ``q1_xy-q2_xy`` in ``tri``'s field."""
    dx = tri.simplify(q2_xy[0] - q1_xy[0])
    dy = tri.simplify(q2_xy[1] - q1_xy[1])
    denom = tri.simplify(dx * dx + dy * dy)
    if denom == 0:
        return q1_xy
    t = tri.simplify(((p_xy[0] - q1_xy[0]) * dx + (p_xy[1] - q1_xy[1]) * dy) / denom)
    return (
        tri.simplify(q1_xy[0] + t * dx),
        tri.simplify(q1_xy[1] + t * dy),
    )


def _exact_sub_area(
    p1: tuple[sp.Expr, sp.Expr],
    p2: tuple[sp.Expr, sp.Expr],
    p3: tuple[sp.Expr, sp.Expr],
    tri: SymbolicTriangle,
) -> sp.Expr:
    """Compute exact unsigned area of sub-triangle ``p1 p2 p3`` in ``tri``'s field."""
    det = tri.simplify(
        (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])
    )
    val = det / sp.Integer(2)
    return tri.simplify(-val if float(val.evalf(20)) < 0 else val)


def _exact_line_eq_pair(
    q1: tuple[sp.Expr, sp.Expr],
    q2: tuple[sp.Expr, sp.Expr],
    tri: SymbolicTriangle,
) -> tuple[str, str]:
    """Return ``(latex_eq, pretty_eq)`` for the exact line through ``q1`` and ``q2``."""
    x_sym, y_sym = sp.Symbol("x"), sp.Symbol("y")
    a_c = tri.simplify(q1[1] - q2[1])
    b_c = tri.simplify(q2[0] - q1[0])
    c_c = tri.simplify(q1[0] * q2[1] - q2[0] * q1[1])
    if float(a_c.evalf(20)) < -1e-15 or (
        abs(float(a_c.evalf(20))) <= 1e-15 and float(b_c.evalf(20)) < -1e-15
    ):
        a_c, b_c, c_c = -a_c, -b_c, -c_c
    if all(isinstance(v, sp.Rational) for v in (a_c, b_c, c_c)):
        lcm_d = sp.ilcm(a_c.q, b_c.q, c_c.q)
        ia = int(a_c * lcm_d)
        ib = int(b_c * lcm_d)
        ic = int(c_c * lcm_d)
        g = math.gcd(math.gcd(abs(ia), abs(ib)), abs(ic)) or 1
        a_c = sp.Integer(ia // g)
        b_c = sp.Integer(ib // g)
        c_c = sp.Integer(ic // g)
    lhs = a_c * x_sym + b_c * y_sym + c_c
    return (
        f"{format_symbolic_latex(lhs)} = 0",
        f"{format_symbolic_pretty(lhs)} = 0",
    )


def _pt_meta_entry(
    eid: str,
    name: str,
    color: str,
    pt_ex: tuple[sp.Expr, sp.Expr],
    bary_latex: str = "",
    bary_pretty: str = "",
    tri_latex: str = "",
    tri_pretty: str = "",
    kepler_phi: bool = False,
) -> dict[str, Any]:
    """Build an ``etc-elements-meta`` point entry with exact symbolic rows."""
    px_f = float(pt_ex[0].evalf(20))
    py_f = float(pt_ex[1].evalf(20))
    c_ltx = (
        f"\\left({format_symbolic_latex(pt_ex[0], kepler_phi=kepler_phi)},\\; "
        f"{format_symbolic_latex(pt_ex[1], kepler_phi=kepler_phi)}\\right)"
    )
    c_prt = (
        f"({format_symbolic_pretty(pt_ex[0], kepler_phi=kepler_phi)}, "
        f"{format_symbolic_pretty(pt_ex[1], kepler_phi=kepler_phi)})"
    )
    sym_rows: list[dict[str, str]] = [
        {"label": "(x, y)", "latex": c_ltx, "pretty": c_prt}
    ]
    if tri_latex:
        sym_rows.append({"label": "trilinear", "latex": tri_latex, "pretty": tri_pretty})
    if bary_latex:
        sym_rows.append({"label": "bary", "latex": bary_latex, "pretty": bary_pretty})
    return {
        "ID": eid,
        "type": "point",
        "color": color,
        "name": name,
        "symbolic_rows": sym_rows,
        "approx": f"≈ ({px_f:.6f}, {py_f:.6f})",
        "related_points": [eid],
    }


def generate_symbolic_coordinates_svg(
    num: int = 1,
    title: str = "",
    trilinear_formula: str = "1 : 1 : 1",
    barycentric_formula: str = "a : b : c",
    preset: str = "heronian",
) -> str:
    """Generate an interactive 1000x760 SVG for Act 2 showing exact symbolic Trilinear struts and Barycentric sub-areas."""
    tri = CANONICAL_TRIANGLES.get(preset, CANONICAL_TRIANGLES["heronian"])
    sym_reg = CenterSymbolicRegistry(tri)
    rec = sym_reg.get(num)
    if rec is None:
        raise ValueError(f"Center X_{num} could not be evaluated symbolically on {preset}")

    A_ex, B_ex, C_ex = tri.A_xy, tri.B_xy, tri.C_xy
    P_ex = rec.xy
    Pa_ex = _exact_pedal_foot(P_ex, B_ex, C_ex, tri)
    Pb_ex = _exact_pedal_foot(P_ex, C_ex, A_ex, tri)
    Pc_ex = _exact_pedal_foot(P_ex, A_ex, B_ex, tri)

    A = (float(A_ex[0].evalf(20)), float(A_ex[1].evalf(20)))
    B = (float(B_ex[0].evalf(20)), float(B_ex[1].evalf(20)))
    C = (float(C_ex[0].evalf(20)), float(C_ex[1].evalf(20)))
    P = (float(P_ex[0].evalf(20)), float(P_ex[1].evalf(20)))
    Pa = (float(Pa_ex[0].evalf(20)), float(Pa_ex[1].evalf(20)))
    Pb = (float(Pb_ex[0].evalf(20)), float(Pb_ex[1].evalf(20)))
    Pc = (float(Pc_ex[0].evalf(20)), float(Pc_ex[1].evalf(20)))

    scale, ox, oy = _fit_points_to_box([A, B, C, P, Pa, Pb, Pc], 110.0, 48.0, 780.0, 646.0)

    As = _to_screen(A, scale, ox, oy)
    Bs = _to_screen(B, scale, ox, oy)
    Cs = _to_screen(C, scale, ox, oy)
    Ps = _to_screen(P, scale, ox, oy)
    Pas = _to_screen(Pa, scale, ox, oy)
    Pbs = _to_screen(Pb, scale, ox, oy)
    Pcs = _to_screen(Pc, scale, ox, oy)

    ra_a = _right_angle_path(Pas, Ps, Bs, size=14.0)
    ra_b = _right_angle_path(Pbs, Ps, Cs, size=14.0)
    ra_c = _right_angle_path(Pcs, Ps, As, size=14.0)

    ma = ((Ps[0] + Pas[0]) * 0.5 + 18, (Ps[1] + Pas[1]) * 0.5 - 6)
    mb = ((Ps[0] + Pbs[0]) * 0.5 - 26, (Ps[1] + Pbs[1]) * 0.5 - 6)
    mc = ((Ps[0] + Pcs[0]) * 0.5 + 20, (Ps[1] + Pcs[1]) * 0.5 + 6)

    fa_id, fb_id, fc_id = ("T_a", "T_b", "T_c") if num == 1 else ("P_a", "P_b", "P_c")
    sa_id = f"/ X_{num} {fa_id} /"
    sb_id = f"/ X_{num} {fb_id} /"
    sc_id = f"/ X_{num} {fc_id} /"
    sub_a_id = f"< X_{num} B C >"
    sub_b_id = f"< X_{num} C A >"
    sub_c_id = f"< X_{num} A B >"
    sub_a_esc = html.escape(sub_a_id, quote=True)
    sub_b_esc = html.escape(sub_b_id, quote=True)
    sub_c_esc = html.escape(sub_c_id, quote=True)

    # Exact symbolic invariants for catalog
    area_a = _exact_sub_area(P_ex, B_ex, C_ex, tri)
    area_b = _exact_sub_area(P_ex, C_ex, A_ex, tri)
    area_c = _exact_sub_area(P_ex, A_ex, B_ex, tri)
    qa_s = tri.simplify((Pa_ex[0] - P_ex[0]) ** 2 + (Pa_ex[1] - P_ex[1]) ** 2)
    qb_s = tri.simplify((Pb_ex[0] - P_ex[0]) ** 2 + (Pb_ex[1] - P_ex[1]) ** 2)
    qc_s = tri.simplify((Pc_ex[0] - P_ex[0]) ** 2 + (Pc_ex[1] - P_ex[1]) ** 2)
    la_s = tri.simplify(sp.sqrt(qa_s))
    lb_s = tri.simplify(sp.sqrt(qb_s))
    lc_s = tri.simplify(sp.sqrt(qc_s))

    catalog: dict[str, Any] = {
        "A": _pt_meta_entry("A", "Vertex A", "#66ff66", A_ex, "1 : 0 : 0", "1 : 0 : 0"),
        "B": _pt_meta_entry("B", "Vertex B", "#66ff66", B_ex, "0 : 1 : 0", "0 : 1 : 0"),
        "C": _pt_meta_entry("C", "Vertex C", "#f8f6f0", C_ex, "0 : 0 : 1", "0 : 0 : 1"),
        f"X_{num}": _pt_meta_entry(
            f"X_{num}",
            title or ("INCENTER" if num == 1 else f"Center X_{num}"),
            "#ffd700",
            P_ex,
            rec.bary_latex(),
            rec.bary_pretty(),
            rec.trilinear_latex(),
            rec.trilinear_pretty(),
        ),
        fa_id: _pt_meta_entry(
            fa_id,
            f"Right-Spread Pedal Foot {fa_id} on BC",
            "#e8b85a",
            Pa_ex,
        ),
        fb_id: _pt_meta_entry(
            fb_id,
            f"Right-Spread Pedal Foot {fb_id} on CA",
            "#38bdf8",
            Pb_ex,
        ),
        fc_id: _pt_meta_entry(
            fc_id,
            f"Right-Spread Pedal Foot {fc_id} on AB",
            "#5ec27e",
            Pc_ex,
        ),
    }

    for sid, p1_e, p2_e, s_len, s_col, s_lbl in [
        ("[ B C ]", B_ex, C_ex, tri.a, "#cbd5e1", "Sideline BC (Side a)"),
        ("[ C A ]", C_ex, A_ex, tri.b, "#cbd5e1", "Sideline CA (Side b)"),
        ("[ A B ]", A_ex, B_ex, tri.c, "#cbd5e1", "Sideline AB (Side c)"),
    ]:
        eq_l, eq_p = _exact_line_eq_pair(p1_e, p2_e, tri)
        q_side = tri.simplify(s_len * s_len)
        catalog[sid] = {
            "ID": sid,
            "type": "line",
            "color": s_col,
            "name": s_lbl,
            "symbolic_rows": [
                {"label": "eq", "latex": eq_l, "pretty": eq_p},
                {
                    "label": "length",
                    "latex": format_symbolic_latex(s_len),
                    "pretty": format_symbolic_pretty(s_len),
                },
                {
                    "label": "Q",
                    "latex": format_symbolic_latex(q_side),
                    "pretty": format_symbolic_pretty(q_side),
                },
            ],
            "approx": f"≈ length {float(s_len.evalf(20)):.6f}",
        }

    for st_id, st_len, st_q, st_col, st_sym, side_nm in [
        (sa_id, la_s, qa_s, "#e8b85a", "\\alpha", "BC"),
        (sb_id, lb_s, qb_s, "#38bdf8", "\\beta", "CA"),
        (sc_id, lc_s, qc_s, "#5ec27e", "\\gamma", "AB"),
    ]:
        catalog[st_id] = {
            "ID": st_id,
            "type": "segment",
            "color": st_col,
            "name": f"Orthogonal Trilinear Strut ⊥ {side_nm}",
            "symbolic_rows": [
                {
                    "label": "d",
                    "latex": f"{st_sym}_0 = {format_symbolic_latex(st_len)}",
                    "pretty": format_symbolic_pretty(st_len),
                },
                {
                    "label": "Q",
                    "latex": format_symbolic_latex(st_q),
                    "pretty": format_symbolic_pretty(st_q),
                },
                {"label": "spread", "latex": "1 \\;(\\perp)", "pretty": "1 (⊥)"},
            ],
            "approx": f"≈ {float(st_len.evalf(20)):.6f}",
        }

    for spk_id, v_ex, v_nm in [
        (f"/ X_{num} A /", A_ex, "A"),
        (f"/ X_{num} B /", B_ex, "B"),
        (f"/ X_{num} C /", C_ex, "C"),
    ]:
        q_spk = tri.simplify((v_ex[0] - P_ex[0]) ** 2 + (v_ex[1] - P_ex[1]) ** 2)
        l_spk = tri.simplify(sp.sqrt(q_spk))
        catalog[spk_id] = {
            "ID": spk_id,
            "type": "segment",
            "color": "#cbd5e1",
            "name": f"Barycentric Partition Spoke X_{num}{v_nm}",
            "symbolic_rows": [
                {
                    "label": "length",
                    "latex": format_symbolic_latex(l_spk),
                    "pretty": format_symbolic_pretty(l_spk),
                },
                {
                    "label": "Q",
                    "latex": format_symbolic_latex(q_spk),
                    "pretty": format_symbolic_pretty(q_spk),
                },
            ],
            "approx": f"≈ {float(l_spk.evalf(20)):.6f}",
        }

    for poly_id, sub_area, p_col, sym_u, opp_v in [
        (sub_a_id, area_a, "#e8b85a", "u", "BC"),
        (sub_b_id, area_b, "#38bdf8", "v", "CA"),
        (sub_c_id, area_c, "#5ec27e", "w", "AB"),
    ]:
        share = tri.simplify(sub_area / tri.area)
        pct = 100.0 * float(share.evalf(20))
        catalog[poly_id] = {
            "ID": poly_id,
            "type": "polygon",
            "color": p_col,
            "name": f"Barycentric Sub-Triangle △X_{num}{opp_v}",
            "symbolic_rows": [
                {
                    "label": "Δ",
                    "latex": format_symbolic_latex(sub_area),
                    "pretty": format_symbolic_pretty(sub_area),
                },
                {
                    "label": f"{sym_u} / Δ",
                    "latex": format_symbolic_latex(share),
                    "pretty": format_symbolic_pretty(share),
                },
                {
                    "label": "bary",
                    "latex": rec.bary_latex(),
                    "pretty": rec.bary_pretty(),
                },
            ],
            "approx": f"≈ {float(sub_area.evalf(20)):.4f} ({pct:.1f}% of Δ)",
        }

    incircle_svg = ""
    if num == 1:
        r_scr = float(tri.r.evalf(20)) * scale
        q_r = tri.simplify(tri.r * tri.r)
        x_sym, y_sym = sp.Symbol("x"), sp.Symbol("y")
        eq_lhs = (x_sym - P_ex[0]) ** 2 + (y_sym - P_ex[1]) ** 2
        eq_ltx = f"{format_symbolic_latex(eq_lhs)} = {format_symbolic_latex(q_r)}"
        eq_prt = f"{format_symbolic_pretty(eq_lhs)} = {format_symbolic_pretty(q_r)}"
        catalog["incircle"] = {
            "ID": "incircle",
            "type": "circle",
            "color": "#f472b6",
            "name": "Inscribed Circle (Incircle)",
            "symbolic_rows": [
                {"label": "eq", "latex": eq_ltx, "pretty": eq_prt},
                {
                    "label": "r",
                    "latex": format_symbolic_latex(tri.r),
                    "pretty": format_symbolic_pretty(tri.r),
                },
                {
                    "label": "Q_r",
                    "latex": format_symbolic_latex(q_r),
                    "pretty": format_symbolic_pretty(q_r),
                },
            ],
            "approx": f"r ≈ {float(tri.r.evalf(20)):.6f}",
        }
        incircle_svg = (
            f'  <circle id="incircle" data-id="incircle" data-ref="incircle" class="etc-plate-circle" '
            f'cx="{Ps[0]:.1f}" cy="{Ps[1]:.1f}" r="{r_scr:.1f}" '
            f'fill="none" stroke="rgba(244, 114, 182, 0.52)" stroke-width="2.2" stroke-dasharray="6,5" />\n'
        )

    sub_caption = (
        f"{tri.label} • Δ = {format_symbolic_pretty(tri.area)}, r = {format_symbolic_pretty(tri.r)}"
    )
    meta_json = _safe_meta_json(catalog)

    return f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg class="geometor-etc-drawing" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 760" data-initial-viewbox="0 0 1000 760" data-triangle="{html.escape(preset)}" width="100%" height="100%" preserveAspectRatio="xMidYMid meet">
  <style>{EXPLORER_SVG_CSS}</style>
  <defs>
    <filter id="glow-coord" filterUnits="userSpaceOnUse" x="-100" y="-100" width="1200" height="960">
      <feGaussianBlur stdDeviation="4.5" result="blur" />
      <feMerge><feMergeNode in="blur" /><feMergeNode in="SourceGraphic" /></feMerge>
    </filter>
  </defs>

  <!-- Shaded Barycentric Sub-Triangles: u = Area(X_n BC), v = Area(X_n CA), w = Area(X_n AB) -->
  <polygon id="{sub_a_esc}" data-id="{sub_a_esc}" data-ref="{sub_a_esc}" class="etc-plate-poly"
           points="{Ps[0]:.1f},{Ps[1]:.1f} {Bs[0]:.1f},{Bs[1]:.1f} {Cs[0]:.1f},{Cs[1]:.1f}"
           fill="#e8b85a" fill-opacity="0.19" stroke="none" />
  <polygon id="{sub_b_esc}" data-id="{sub_b_esc}" data-ref="{sub_b_esc}" class="etc-plate-poly"
           points="{Ps[0]:.1f},{Ps[1]:.1f} {Cs[0]:.1f},{Cs[1]:.1f} {As[0]:.1f},{As[1]:.1f}"
           fill="#38bdf8" fill-opacity="0.17" stroke="none" />
  <polygon id="{sub_c_esc}" data-id="{sub_c_esc}" data-ref="{sub_c_esc}" class="etc-plate-poly"
           points="{Ps[0]:.1f},{Ps[1]:.1f} {As[0]:.1f},{As[1]:.1f} {Bs[0]:.1f},{Bs[1]:.1f}"
           fill="#5ec27e" fill-opacity="0.17" stroke="none" />

{incircle_svg}  <!-- Extended sidelines (when pedal feet fall outside segment) -->
  <line x1="{Bs[0]:.1f}" y1="{Bs[1]:.1f}" x2="{Pas[0]:.1f}" y2="{Pas[1]:.1f}" stroke="#64748b" stroke-width="1.8" stroke-dasharray="5,5" pointer-events="none" />
  <line x1="{Cs[0]:.1f}" y1="{Cs[1]:.1f}" x2="{Pbs[0]:.1f}" y2="{Pbs[1]:.1f}" stroke="#64748b" stroke-width="1.8" stroke-dasharray="5,5" pointer-events="none" />
  <line x1="{As[0]:.1f}" y1="{As[1]:.1f}" x2="{Pcs[0]:.1f}" y2="{Pcs[1]:.1f}" stroke="#64748b" stroke-width="1.8" stroke-dasharray="5,5" pointer-events="none" />

  <!-- Reference Triangle Sidelines BC, CA, AB -->
  <line id="[ B C ]" data-id="[ B C ]" data-ref="[ B C ]" class="etc-plate-line"
        x1="{Bs[0]:.1f}" y1="{Bs[1]:.1f}" x2="{Cs[0]:.1f}" y2="{Cs[1]:.1f}"
        stroke="#cbd5e1" stroke-width="2.8" stroke-dasharray="2, 4.5" stroke-linecap="round" />
  <line id="[ C A ]" data-id="[ C A ]" data-ref="[ C A ]" class="etc-plate-line"
        x1="{Cs[0]:.1f}" y1="{Cs[1]:.1f}" x2="{As[0]:.1f}" y2="{As[1]:.1f}"
        stroke="#cbd5e1" stroke-width="2.8" stroke-dasharray="2, 4.5" stroke-linecap="round" />
  <line id="[ A B ]" data-id="[ A B ]" data-ref="[ A B ]" class="etc-plate-line"
        x1="{As[0]:.1f}" y1="{As[1]:.1f}" x2="{Bs[0]:.1f}" y2="{Bs[1]:.1f}"
        stroke="#cbd5e1" stroke-width="2.8" stroke-dasharray="2, 4.5" stroke-linecap="round" />

  <!-- Barycentric partition spokes (dash-dot) from X_n to vertices A, B, C -->
  <line id="/ X_{num} A /" data-id="/ X_{num} A /" data-ref="/ X_{num} A /" class="etc-plate-line"
        x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{As[0]:.1f}" y2="{As[1]:.1f}" stroke="#cbd5e1" stroke-width="2.2" stroke-dasharray="10,5,2.5,5" opacity="0.65" />
  <line id="/ X_{num} B /" data-id="/ X_{num} B /" data-ref="/ X_{num} B /" class="etc-plate-line"
        x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{Bs[0]:.1f}" y2="{Bs[1]:.1f}" stroke="#cbd5e1" stroke-width="2.2" stroke-dasharray="10,5,2.5,5" opacity="0.65" />
  <line id="/ X_{num} C /" data-id="/ X_{num} C /" data-ref="/ X_{num} C /" class="etc-plate-line"
        x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{Cs[0]:.1f}" y2="{Cs[1]:.1f}" stroke="#cbd5e1" stroke-width="2.2" stroke-dasharray="10,5,2.5,5" opacity="0.65" />

  <!-- Right-angle markers at pedal feet -->
  <path d="{ra_a}" fill="none" stroke="#e8b85a" stroke-width="2.4" opacity="0.9" pointer-events="none" />
  <path d="{ra_b}" fill="none" stroke="#38bdf8" stroke-width="2.4" opacity="0.9" pointer-events="none" />
  <path d="{ra_c}" fill="none" stroke="#5ec27e" stroke-width="2.4" opacity="0.9" pointer-events="none" />

  <!-- Three Directed Perpendicular Struts (alpha, beta, gamma) -->
  <line id="{sa_id}" data-id="{sa_id}" data-ref="{sa_id}" class="etc-plate-strut"
        x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{Pas[0]:.1f}" y2="{Pas[1]:.1f}"
        stroke="#e8b85a" stroke-width="5.2" stroke-linecap="round" filter="url(#glow-coord)" />
  <line id="{sb_id}" data-id="{sb_id}" data-ref="{sb_id}" class="etc-plate-strut"
        x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{Pbs[0]:.1f}" y2="{Pbs[1]:.1f}"
        stroke="#38bdf8" stroke-width="5.2" stroke-linecap="round" filter="url(#glow-coord)" />
  <line id="{sc_id}" data-id="{sc_id}" data-ref="{sc_id}" class="etc-plate-strut"
        x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{Pcs[0]:.1f}" y2="{Pcs[1]:.1f}"
        stroke="#5ec27e" stroke-width="5.2" stroke-linecap="round" filter="url(#glow-coord)" />

  <!-- Pedal feet -->
  <circle id="{fa_id}" data-id="{fa_id}" data-ref="{fa_id}" class="etc-plate-pt"
          cx="{Pas[0]:.1f}" cy="{Pas[1]:.1f}" r="6.2" fill="#e8b85a" stroke="#0d111a" stroke-width="2" />
  <circle id="{fb_id}" data-id="{fb_id}" data-ref="{fb_id}" class="etc-plate-pt"
          cx="{Pbs[0]:.1f}" cy="{Pbs[1]:.1f}" r="6.2" fill="#38bdf8" stroke="#0d111a" stroke-width="2" />
  <circle id="{fc_id}" data-id="{fc_id}" data-ref="{fc_id}" class="etc-plate-pt"
          cx="{Pcs[0]:.1f}" cy="{Pcs[1]:.1f}" r="6.2" fill="#5ec27e" stroke="#0d111a" stroke-width="2" />

  <!-- Vertices A, B, C -->
  <circle id="A" data-id="A" data-ref="A" class="etc-plate-pt"
          cx="{As[0]:.1f}" cy="{As[1]:.1f}" r="7.2" fill="#66ff66" stroke="#0d111a" stroke-width="2.2" />
  <circle id="B" data-id="B" data-ref="B" class="etc-plate-pt"
          cx="{Bs[0]:.1f}" cy="{Bs[1]:.1f}" r="7.2" fill="#66ff66" stroke="#0d111a" stroke-width="2.2" />
  <circle id="C" data-id="C" data-ref="C" class="etc-plate-pt"
          cx="{Cs[0]:.1f}" cy="{Cs[1]:.1f}" r="7.2" fill="#f8f6f0" stroke="#0d111a" stroke-width="2.2" />

  <g pointer-events="none">
    <text x="{As[0] - 32:.1f}" y="{As[1] + 26:.1f}" fill="#88ff88" font-family="Georgia, serif" font-size="28" font-weight="bold">A</text>
    <text x="{Bs[0] + 16:.1f}" y="{Bs[1] + 26:.1f}" fill="#88ff88" font-family="Georgia, serif" font-size="28" font-weight="bold">B</text>
    <text x="{Cs[0] - 10:.1f}" y="{Cs[1] - 18:.1f}" fill="#f8f6f0" font-family="Georgia, serif" font-size="28" font-weight="bold">C</text>
    <text x="{Pas[0] + 12:.1f}" y="{Pas[1] - 8:.1f}" fill="#e8b85a" font-family="Georgia, serif" font-size="19" font-weight="bold">{fa_id[0]}<tspan dy="0.28em" font-size="74%">{fa_id[-1]}</tspan></text>
    <text x="{Pbs[0] - 34:.1f}" y="{Pbs[1] - 8:.1f}" fill="#38bdf8" font-family="Georgia, serif" font-size="19" font-weight="bold">{fb_id[0]}<tspan dy="0.28em" font-size="74%">{fb_id[-1]}</tspan></text>
    <text x="{Pcs[0] + 10:.1f}" y="{Pcs[1] + 26:.1f}" fill="#5ec27e" font-family="Georgia, serif" font-size="19" font-weight="bold">{fc_id[0]}<tspan dy="0.28em" font-size="74%">{fc_id[-1]}</tspan></text>
  </g>

  <!-- Strut Labels alpha, beta, gamma -->
  <g font-family="Georgia, serif" font-size="26" font-weight="bold" pointer-events="none">
    <rect x="{ma[0] - 8:.1f}" y="{ma[1] - 24:.1f}" width="34" height="30" rx="6" fill="rgba(13, 17, 26, 0.86)" />
    <text x="{ma[0]:.1f}" y="{ma[1]:.1f}" fill="#e8b85a">α</text>
    <rect x="{mb[0] - 8:.1f}" y="{mb[1] - 24:.1f}" width="34" height="30" rx="6" fill="rgba(13, 17, 26, 0.86)" />
    <text x="{mb[0]:.1f}" y="{mb[1]:.1f}" fill="#38bdf8">β</text>
    <rect x="{mc[0] - 8:.1f}" y="{mc[1] - 24:.1f}" width="34" height="30" rx="6" fill="rgba(13, 17, 26, 0.86)" />
    <text x="{mc[0]:.1f}" y="{mc[1]:.1f}" fill="#5ec27e">γ</text>
  </g>

  <!-- Center X_n -->
  <circle id="X_{num}" data-id="X_{num}" data-ref="X_{num}" class="etc-plate-pt"
          cx="{Ps[0]:.1f}" cy="{Ps[1]:.1f}" r="10.5" fill="#ffd700" stroke="#00ffff" stroke-width="3" filter="url(#glow-coord)" />
  <g pointer-events="none">
    <rect x="{Ps[0] - 34:.1f}" y="{Ps[1] - 46:.1f}" width="68" height="30" rx="6" fill="rgba(13, 17, 26, 0.92)" stroke="#e8b85a" stroke-width="1.5" />
    <text x="{Ps[0]:.1f}" y="{Ps[1] - 25:.1f}" text-anchor="middle" fill="#ffd700" font-family="JetBrains Mono, monospace" font-size="19" font-weight="bold">{_svg_x(num)}</text>
    <text x="976" y="742" text-anchor="end" fill="#94a3b8" font-family="JetBrains Mono, monospace" font-size="14">{html.escape(sub_caption)}</text>
  </g>
  <script type="application/json" class="etc-elements-meta">{meta_json}</script>
  <script>//<![CDATA[
{INTERACTIVE_SVG_JS}
//]]></script>
</svg>"""


def generate_center_coordinates_svg(
    num: int,
    title: str,
    trilinear_formula: str,
    barycentric_formula: str,
    ctx: TriangleContext | None = None,
    reg: CenterRegistry | None = None,
    preset: str = "heronian",
) -> str:
    """Generate a 1000x760 SVG showing both Trilinear struts and Barycentric sub-areas for X_n."""
    tri = CANONICAL_TRIANGLES.get(preset, CANONICAL_TRIANGLES["heronian"])
    if ctx is None or reg is None or CenterSymbolicRegistry(tri).get(num) is not None:
        return generate_symbolic_coordinates_svg(
            num=num,
            title=title,
            trilinear_formula=trilinear_formula,
            barycentric_formula=barycentric_formula,
            preset=preset,
        )
    A, B, C = ctx.A_xy, ctx.B_xy, ctx.C_xy
    P = reg.xy_cache.get(num, (0.5, 0.25))
    Pa = _foot_on_line(P, B, C)
    Pb = _foot_on_line(P, C, A)
    Pc = _foot_on_line(P, A, B)
    scale, ox, oy = _fit_points_to_box([A, B, C, P, Pa, Pb, Pc], 110.0, 48.0, 780.0, 664.0)
    As = _to_screen(A, scale, ox, oy)
    Bs = _to_screen(B, scale, ox, oy)
    Cs = _to_screen(C, scale, ox, oy)
    Ps = _to_screen(P, scale, ox, oy)
    Pas = _to_screen(Pa, scale, ox, oy)
    Pbs = _to_screen(Pb, scale, ox, oy)
    Pcs = _to_screen(Pc, scale, ox, oy)
    ra_a = _right_angle_path(Pas, Ps, Bs, size=14.0)
    ra_b = _right_angle_path(Pbs, Ps, Cs, size=14.0)
    ra_c = _right_angle_path(Pcs, Ps, As, size=14.0)
    ma = ((Ps[0] + Pas[0]) * 0.5 + 18, (Ps[1] + Pas[1]) * 0.5 - 6)
    mb = ((Ps[0] + Pbs[0]) * 0.5 - 26, (Ps[1] + Pbs[1]) * 0.5 - 6)
    mc = ((Ps[0] + Pcs[0]) * 0.5 + 20, (Ps[1] + Pcs[1]) * 0.5 + 6)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 760" width="100%" height="100%">
  <polygon points="{Ps[0]:.1f},{Ps[1]:.1f} {Bs[0]:.1f},{Bs[1]:.1f} {Cs[0]:.1f},{Cs[1]:.1f}" fill="rgba(232, 184, 90, 0.19)" stroke="none" />
  <polygon points="{Ps[0]:.1f},{Ps[1]:.1f} {Cs[0]:.1f},{Cs[1]:.1f} {As[0]:.1f},{As[1]:.1f}" fill="rgba(56, 189, 248, 0.17)" stroke="none" />
  <polygon points="{Ps[0]:.1f},{Ps[1]:.1f} {As[0]:.1f},{As[1]:.1f} {Bs[0]:.1f},{Bs[1]:.1f}" fill="rgba(94, 194, 126, 0.17)" stroke="none" />
  <polygon points="{As[0]:.1f},{As[1]:.1f} {Bs[0]:.1f},{Bs[1]:.1f} {Cs[0]:.1f},{Cs[1]:.1f}" fill="none" stroke="#cbd5e1" stroke-width="2.6" stroke-dasharray="2, 4.5" />
  <path d="{ra_a}" fill="none" stroke="#e8b85a" stroke-width="2.4" />
  <path d="{ra_b}" fill="none" stroke="#38bdf8" stroke-width="2.4" />
  <path d="{ra_c}" fill="none" stroke="#5ec27e" stroke-width="2.4" />
  <line x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{Pas[0]:.1f}" y2="{Pas[1]:.1f}" stroke="#e8b85a" stroke-width="5.0" stroke-linecap="round" />
  <line x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{Pbs[0]:.1f}" y2="{Pbs[1]:.1f}" stroke="#38bdf8" stroke-width="5.0" stroke-linecap="round" />
  <line x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{Pcs[0]:.1f}" y2="{Pcs[1]:.1f}" stroke="#5ec27e" stroke-width="5.0" stroke-linecap="round" />
  <circle cx="{Ps[0]:.1f}" cy="{Ps[1]:.1f}" r="10.5" fill="#ffd700" stroke="#00ffff" stroke-width="3" />
  <text x="{ma[0]:.1f}" y="{ma[1]:.1f}" fill="#e8b85a" font-size="26">α</text>
  <text x="{mb[0]:.1f}" y="{mb[1]:.1f}" fill="#38bdf8" font-size="26">β</text>
  <text x="{mc[0]:.1f}" y="{mc[1]:.1f}" fill="#5ec27e" font-size="26">γ</text>
</svg>"""


def generate_central_lines_svg(primary_svg_text: str) -> str:
    """Return the primary web-page SVG with `.show-lines` active so all incident central lines and collinear centers appear."""
    return primary_svg_text.replace(
        'class="geometor-etc-drawing"',
        'class="geometor-etc-drawing show-lines"',
        1,
    )


def generate_symbolic_relations_svg(
    num: int = 1,
    partner_nums: list[int] | None = None,
    preset: str = "heronian",
) -> str:
    """Build and render an exact symbolic Explorer-styled ``Model`` SVG plotting ``X_num`` and its conjugate/homothetic partners."""
    tri = CANONICAL_TRIANGLES.get(preset, CANONICAL_TRIANGLES["heronian"])
    sym_reg = CenterSymbolicRegistry(tri)
    partners = list(partner_nums) if partner_nums is not None else [8, 10, 75]

    model = create_model(f"X_{num} Functional Relations")
    A, B, C = construct_reference_triangle(model, preset, show_guides=False)

    tri_xs = [float(p[0].evalf(20)) for p in (tri.A_xy, tri.B_xy, tri.C_xy)]
    tri_ys = [float(p[1].evalf(20)) for p in (tri.A_xy, tri.B_xy, tri.C_xy)]
    min_x, max_x = min(tri_xs), max(tri_xs)
    min_y, max_y = min(tri_ys), max(tri_ys)
    span = max(max_x - min_x, max_y - min_y, 1.0)
    cx = 0.5 * (min_x + max_x)
    cy = 0.5 * (min_y + max_y)

    pts_map: dict[int, Any] = {}

    def get_exact_pt(c_num: int, is_target: bool = False, as_guide: bool = False) -> Any:
        if c_num in pts_map:
            return pts_map[c_num]
        rec = sym_reg.get(c_num)
        if rec is None:
            return None
        cls = (
            ["selected", "target"]
            if is_target
            else (["guide"] if as_guide else ["center"])
        )
        pt = add_point(
            model,
            rec.xy[0],
            rec.xy[1],
            ID=f"X_{c_num}",
            classes=cls,
            parents=[A, B, C],
            guide=as_guide and not is_target,
        )
        pts_map[c_num] = pt
        return pt

    valid_partners: list[int] = []
    for k in partners:
        if k == num:
            continue
        rec_k = sym_reg.get(k)
        if rec_k is None:
            continue
        kx, ky = rec_k.approx_xy()
        if abs(kx - cx) <= 1.85 * span and abs(ky - cy) <= 1.85 * span:
            get_exact_pt(k, is_target=False, as_guide=False)
            valid_partners.append(k)

    # Homothetic dilation center X_2 when complement/anticomplement partners are displayed
    if num == 1 and 2 not in valid_partners:
        get_exact_pt(2, is_target=False, as_guide=True)

    X3 = get_exact_pt(3, is_target=(num == 3), as_guide=(3 not in valid_partners and num != 3))
    if X3 is not None:
        add_circle(model, X3, A, ID="circumcircle", classes=["circumcircle"])

    X1 = get_exact_pt(1, is_target=(num == 1), as_guide=(1 not in valid_partners and num != 1))
    if X1 is not None:
        Tc = perpendicular_foot(model, X1, A, B, ID="T_c", classes=["foot", "guide"], guide=True)
        add_circle(model, X1, Tc, ID="incircle", classes=["incircle"])

    if num in {5, 11, 12} or 5 in valid_partners:
        X5 = get_exact_pt(5, is_target=(num == 5), as_guide=(5 not in valid_partners and num != 5))
        if X5 is not None:
            Mc = midpoint(model, A, B, ID="M_c", classes=["foot", "guide"], guide=True)
            add_circle(model, X5, Mc, ID="nine_point_circle", classes=["nine_point_circle"])

    target_pt = get_exact_pt(num, is_target=True, as_guide=False)

    if target_pt is not None:
        for k in valid_partners[:4]:
            pk = pts_map.get(k)
            if pk is not None:
                add_line(
                    model,
                    target_pt,
                    pk,
                    ID=f"{{ {min(num, k)}, {max(num, k)} }}",
                    classes=["central_line"],
                )
        if num == 1 and X3 is not None:
            add_line(model, target_pt, X3, ID="{ 1, 3 }", classes=["central_line"])
        promote_point_to_top(model, target_pt)

    return render_model_svg(model, subtitle=f"{tri.label} | Functional Relations")


def generate_relations_svg(
    num: int,
    partner_nums: list[int],
    reg: CenterRegistry | None = None,
    preset: str = "heronian",
) -> str:
    """Build and render an Explorer-styled ``Model`` SVG plotting ``X_n`` and its functional-relation partner centers."""
    tri = CANONICAL_TRIANGLES.get(preset, CANONICAL_TRIANGLES["heronian"])
    if reg is None or CenterSymbolicRegistry(tri).get(num) is not None:
        return generate_symbolic_relations_svg(
            num=num, partner_nums=partner_nums, preset=preset
        )

    ctx = reg.ctx
    model = Model(f"X_{num} Functional Relations", auto_intersect=False)
    A = _add_point(model, 0.0, 0.0, ID="A", classes=["given", "vertex"])
    B = _add_point(model, 1.0, 0.0, ID="B", classes=["given", "vertex"])
    C = _add_point(model, ctx.C_xy[0], ctx.C_xy[1], ID="C", classes=["vertex"])
    _add_line(model, A, B, ID="[ A B ]", classes=["given", "sideline"])
    _add_line(model, B, C, ID="[ B C ]", classes=["sideline"])
    _add_line(model, C, A, ID="[ C A ]", classes=["sideline"])
    _add_polygon(model, [A, B, C], ID="< A B C >", classes=["reference"])

    pts_map: dict[int, Any] = {}

    def get_pt(c_num: int, is_target: bool = False, as_guide: bool = False) -> Any:
        if c_num in pts_map:
            return pts_map[c_num]
        xy = reg.xy_cache.get(c_num)
        if xy is None:
            return None
        cls = ["selected", "target"] if is_target else (["guide"] if as_guide else ["center"])
        pt = _add_point(model, xy[0], xy[1], ID=f"X_{c_num}", classes=cls, guide=as_guide and not is_target)
        pts_map[c_num] = pt
        return pt

    valid_partners: list[int] = []
    for k in partner_nums:
        if k != num and k in reg.xy_cache:
            xy_k = reg.xy_cache[k]
            if -1.4 <= xy_k[0] <= 2.4 and -1.4 <= xy_k[1] <= 2.0:
                get_pt(k, is_target=False, as_guide=False)
                valid_partners.append(k)

    X3 = get_pt(3, is_target=(num == 3), as_guide=(3 not in valid_partners and num != 3))
    if X3 is not None:
        _add_circle(model, X3, A, ID="circumcircle", classes=["circumcircle"])
    X1 = get_pt(1, is_target=(num == 1), as_guide=(1 not in valid_partners and num != 1))
    if X1 is not None:
        r_in = ctx.r * ctx.scale
        _add_circle(model, X1, r_in, ID="incircle", classes=["incircle"])

    target_pt = get_pt(num, is_target=True, as_guide=False)
    if target_pt is not None:
        for k in valid_partners[:4]:
            pk = pts_map.get(k)
            if pk is not None:
                _add_line(model, target_pt, pk, ID=f"{{ {min(num, k)}, {max(num, k)} }}", classes=["central_line"])
        promote_point_to_top(model, target_pt)

    return render_model_svg(model)


def generate_trilinear_picture_svg(
    num: int,
    title: str,
    trilinear_formula: str,
    ctx: TriangleContext,
    reg: CenterRegistry,
) -> str:
    """Generate a 1000x760 SVG demonstrating Trilinear Coordinates (alpha : beta : gamma) in pictures."""
    trilinear_formula = _clean_formula(trilinear_formula)
    A, B, C = ctx.A_xy, ctx.B_xy, ctx.C_xy
    P = reg.xy_cache.get(num, (0.5, 0.25))
    bary = reg.bary_cache.get(num, (ctx.raw_a, ctx.raw_b, ctx.raw_c))
    a_r, b_r, c_r = ctx.raw_a, ctx.raw_b, ctx.raw_c

    Pa = _foot_on_line(P, B, C)
    Pb = _foot_on_line(P, C, A)
    Pc = _foot_on_line(P, A, B)

    raw_tri = (bary[0] / a_r, bary[1] / b_r, bary[2] / c_r)
    sum_abs_tri = sum(abs(x) for x in raw_tri) or 1.0
    norm_tri = [abs(x) / sum_abs_tri for x in raw_tri]
    min_pos = min((abs(x) for x in raw_tri if abs(x) > 1e-9), default=1.0)
    disp_tri = [x / min_pos for x in raw_tri]

    scale = 610.0
    ox = 195.0
    oy = 505.0

    As = _to_screen(A, scale, ox, oy)
    Bs = _to_screen(B, scale, ox, oy)
    Cs = _to_screen(C, scale, ox, oy)
    Ps = _to_screen(P, scale, ox, oy)
    Pas = _to_screen(Pa, scale, ox, oy)
    Pbs = _to_screen(Pb, scale, ox, oy)
    Pcs = _to_screen(Pc, scale, ox, oy)

    ra_a = _right_angle_path(Pas, Ps, Bs, size=14.0)
    ra_b = _right_angle_path(Pbs, Ps, Cs, size=14.0)
    ra_c = _right_angle_path(Pcs, Ps, As, size=14.0)

    ma = ((Ps[0] + Pas[0]) * 0.5 + 18, (Ps[1] + Pas[1]) * 0.5 - 8)
    mb = ((Ps[0] + Pbs[0]) * 0.5 - 26, (Ps[1] + Pbs[1]) * 0.5 - 8)
    mc = ((Ps[0] + Pcs[0]) * 0.5 + 22, (Ps[1] + Pcs[1]) * 0.5 + 4)

    extra_circle = ""
    if num == 1:
        r_scr = math.hypot(Ps[0] - Pcs[0], Ps[1] - Pcs[1])
        extra_circle = (
            f'<circle cx="{Ps[0]:.1f}" cy="{Ps[1]:.1f}" r="{r_scr:.1f}" '
            f'fill="rgba(232, 184, 90, 0.05)" stroke="#e8b85a" stroke-width="2" stroke-dasharray="7,5" opacity="0.75" />'
        )

    max_bar_w = 220.0
    max_t = max(norm_tri) or 1.0
    wa = max(18.0, max_bar_w * (norm_tri[0] / max_t))
    wb = max(18.0, max_bar_w * (norm_tri[1] / max_t))
    wc = max(18.0, max_bar_w * (norm_tri[2] / max_t))

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 760" width="100%" height="100%">
  <defs>
    <filter id="glow-gold" filterUnits="userSpaceOnUse" x="-100" y="-100" width="1200" height="960">
      <feGaussianBlur stdDeviation="5" result="blur" />
      <feMerge><feMergeNode in="blur" /><feMergeNode in="SourceGraphic" /></feMerge>
    </filter>
  </defs>

  <polygon points="{As[0]:.1f},{As[1]:.1f} {Bs[0]:.1f},{Bs[1]:.1f} {Cs[0]:.1f},{Cs[1]:.1f}"
           fill="rgba(214, 207, 197, 0.04)" stroke="#d6cfc5" stroke-width="3.2" stroke-linejoin="round" />

  {extra_circle}

  <path d="{ra_a}" fill="none" stroke="#e8b85a" stroke-width="2.4" opacity="0.9" />
  <path d="{ra_b}" fill="none" stroke="#38bdf8" stroke-width="2.4" opacity="0.9" />
  <path d="{ra_c}" fill="none" stroke="#5ec27e" stroke-width="2.4" opacity="0.9" />

  <line x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{Pas[0]:.1f}" y2="{Pas[1]:.1f}"
        stroke="#e8b85a" stroke-width="5" stroke-linecap="round" filter="url(#glow-gold)" />
  <line x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{Pbs[0]:.1f}" y2="{Pbs[1]:.1f}"
        stroke="#38bdf8" stroke-width="5" stroke-linecap="round" filter="url(#glow-gold)" />
  <line x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{Pcs[0]:.1f}" y2="{Pcs[1]:.1f}"
        stroke="#5ec27e" stroke-width="5" stroke-linecap="round" filter="url(#glow-gold)" />

  <circle cx="{Pas[0]:.1f}" cy="{Pas[1]:.1f}" r="5.5" fill="#e8b85a" stroke="#0d111a" stroke-width="2" />
  <circle cx="{Pbs[0]:.1f}" cy="{Pbs[1]:.1f}" r="5.5" fill="#38bdf8" stroke="#0d111a" stroke-width="2" />
  <circle cx="{Pcs[0]:.1f}" cy="{Pcs[1]:.1f}" r="5.5" fill="#5ec27e" stroke="#0d111a" stroke-width="2" />

  <circle cx="{As[0]:.1f}" cy="{As[1]:.1f}" r="6.5" fill="#f8f6f0" stroke="#0d111a" stroke-width="2.2" />
  <circle cx="{Bs[0]:.1f}" cy="{Bs[1]:.1f}" r="6.5" fill="#f8f6f0" stroke="#0d111a" stroke-width="2.2" />
  <circle cx="{Cs[0]:.1f}" cy="{Cs[1]:.1f}" r="6.5" fill="#f8f6f0" stroke="#0d111a" stroke-width="2.2" />

  <circle cx="{Ps[0]:.1f}" cy="{Ps[1]:.1f}" r="9.5" fill="#e8b85a" stroke="#ffffff" stroke-width="2.8" filter="url(#glow-gold)" />

  <text x="{As[0] - 28:.1f}" y="{As[1] + 24:.1f}" fill="#f8f6f0" font-family="Georgia, serif" font-size="26" font-weight="bold">A</text>
  <text x="{Bs[0] + 16:.1f}" y="{Bs[1] + 24:.1f}" fill="#f8f6f0" font-family="Georgia, serif" font-size="26" font-weight="bold">B</text>
  <text x="{Cs[0] - 8:.1f}" y="{Cs[1] - 18:.1f}" fill="#f8f6f0" font-family="Georgia, serif" font-size="26" font-weight="bold">C</text>

  <text x="{(Bs[0] + Cs[0]) * 0.5 + 34:.1f}" y="{(Bs[1] + Cs[1]) * 0.5 - 6:.1f}" fill="#cbd5e1" font-family="JetBrains Mono, monospace" font-size="20" font-weight="600">a = 5</text>
  <text x="{(Cs[0] + As[0]) * 0.5 - 88:.1f}" y="{(Cs[1] + As[1]) * 0.5 - 6:.1f}" fill="#cbd5e1" font-family="JetBrains Mono, monospace" font-size="20" font-weight="600">b = 6</text>
  <text x="{(As[0] + Bs[0]) * 0.5 - 26:.1f}" y="{As[1] + 38:.1f}" fill="#cbd5e1" font-family="JetBrains Mono, monospace" font-size="20" font-weight="600">c = 7</text>

  <g font-family="Georgia, serif" font-size="26" font-weight="bold">
    <rect x="{ma[0] - 8:.1f}" y="{ma[1] - 24:.1f}" width="34" height="30" rx="6" fill="rgba(13, 17, 26, 0.85)" />
    <text x="{ma[0]:.1f}" y="{ma[1]:.1f}" fill="#e8b85a">α</text>
    <rect x="{mb[0] - 8:.1f}" y="{mb[1] - 24:.1f}" width="34" height="30" rx="6" fill="rgba(13, 17, 26, 0.85)" />
    <text x="{mb[0]:.1f}" y="{mb[1]:.1f}" fill="#38bdf8">β</text>
    <rect x="{mc[0] - 8:.1f}" y="{mc[1] - 24:.1f}" width="34" height="30" rx="6" fill="rgba(13, 17, 26, 0.85)" />
    <text x="{mc[0]:.1f}" y="{mc[1]:.1f}" fill="#5ec27e">γ</text>
  </g>

  <rect x="{Ps[0] - 32:.1f}" y="{Ps[1] - 44:.1f}" width="64" height="28" rx="6" fill="rgba(13, 17, 26, 0.9)" stroke="#e8b85a" stroke-width="1.2" />
  <text x="{Ps[0]:.1f}" y="{Ps[1] - 24:.1f}" text-anchor="middle" fill="#e8b85a" font-family="JetBrains Mono, monospace" font-size="18" font-weight="bold">{_svg_x(num)}</text>

  <g transform="translate(55, 575)">
    <rect x="0" y="0" width="890" height="158" rx="14" fill="rgba(11, 14, 21, 0.92)" stroke="rgba(232, 184, 90, 0.35)" stroke-width="1.5" />
    <text x="24" y="34" fill="#94a3b8" font-family="JetBrains Mono, monospace" font-size="15" font-weight="bold" letter-spacing="1.2">DIRECTED PERPENDICULAR DISTANCES TO SIDELINES</text>
    <text x="866" y="34" text-anchor="end" fill="#e8b85a" font-family="JetBrains Mono, monospace" font-size="18" font-weight="bold">α : β : γ = {html.escape(trilinear_formula[:28])}</text>

    <text x="24" y="72" fill="#e8b85a" font-family="JetBrains Mono, monospace" font-size="18" font-weight="bold">α ⊥ BC (a=5)</text>
    <rect x="180" y="55" width="{wa:.1f}" height="20" rx="5" fill="#e8b85a" />
    <text x="{192 + wa:.1f}" y="71" fill="#f8f6f0" font-family="JetBrains Mono, monospace" font-size="17">{disp_tri[0]:.3g}</text>

    <text x="24" y="106" fill="#38bdf8" font-family="JetBrains Mono, monospace" font-size="18" font-weight="bold">β ⊥ CA (b=6)</text>
    <rect x="180" y="89" width="{wb:.1f}" height="20" rx="5" fill="#38bdf8" />
    <text x="{192 + wb:.1f}" y="105" fill="#f8f6f0" font-family="JetBrains Mono, monospace" font-size="17">{disp_tri[1]:.3g}</text>

    <text x="24" y="140" fill="#5ec27e" font-family="JetBrains Mono, monospace" font-size="18" font-weight="bold">γ ⊥ AB (c=7)</text>
    <rect x="180" y="123" width="{wc:.1f}" height="20" rx="5" fill="#5ec27e" />
    <text x="{192 + wc:.1f}" y="139" fill="#f8f6f0" font-family="JetBrains Mono, monospace" font-size="17">{disp_tri[2]:.3g}</text>

    <rect x="520" y="52" width="346" height="92" rx="10" fill="rgba(232, 184, 90, 0.08)" stroke="rgba(232, 184, 90, 0.3)" />
    <text x="693" y="84" text-anchor="middle" fill="#f8f6f0" font-family="Georgia, serif" font-size="20">d({_svg_x(num, ", BC")}) : d({_svg_x(num, ", CA")}) : d({_svg_x(num, ", AB")})</text>
    <text x="693" y="118" text-anchor="middle" fill="#e8b85a" font-family="JetBrains Mono, monospace" font-size="21" font-weight="bold">= {disp_tri[0]:.3g} : {disp_tri[1]:.3g} : {disp_tri[2]:.3g}</text>
  </g>
</svg>"""


def generate_barycentric_picture_svg(
    num: int,
    title: str,
    barycentric_formula: str,
    ctx: TriangleContext,
    reg: CenterRegistry,
) -> str:
    """Generate a 1000x760 SVG demonstrating Barycentric Coordinates (u : v : w = a*alpha : b*beta : c*gamma) in pictures."""
    barycentric_formula = _clean_formula(barycentric_formula)
    A, B, C = ctx.A_xy, ctx.B_xy, ctx.C_xy
    P = reg.xy_cache.get(num, (0.5, 0.25))
    bary = reg.bary_cache.get(num, (ctx.raw_a, ctx.raw_b, ctx.raw_c))

    sum_bary = sum(abs(x) for x in bary) or 1.0
    pcts = [100.0 * abs(x) / sum_bary for x in bary]
    min_pos = min((abs(x) for x in bary if abs(x) > 1e-9), default=1.0)
    disp_bary = [x / min_pos for x in bary]
    if all(abs(x * 5 - round(x * 5)) < 1e-4 for x in disp_bary) and not all(
        abs(x - round(x)) < 1e-4 for x in disp_bary
    ):
        disp_bary = [x * 5 for x in disp_bary]

    scale = 610.0
    ox = 195.0
    oy = 505.0

    As = _to_screen(A, scale, ox, oy)
    Bs = _to_screen(B, scale, ox, oy)
    Cs = _to_screen(C, scale, ox, oy)
    Ps = _to_screen(P, scale, ox, oy)

    ga = ((0.7 * Ps[0] + 1.45 * Bs[0] + 1.45 * Cs[0]) / 3.6 + 18.0, (0.7 * Ps[1] + 1.45 * Bs[1] + 1.45 * Cs[1]) / 3.6 - 6.0)
    gb = ((0.7 * Ps[0] + 1.45 * Cs[0] + 1.45 * As[0]) / 3.6 - 18.0, (0.7 * Ps[1] + 1.45 * Cs[1] + 1.45 * As[1]) / 3.6 - 6.0)
    gc = ((Ps[0] + As[0] + Bs[0]) / 3.0, (Ps[1] + As[1] + Bs[1]) / 3.0 + 18.0)

    ra_mass = 12.0 + 18.0 * math.sqrt(pcts[0] / 100.0)
    rb_mass = 12.0 + 18.0 * math.sqrt(pcts[1] / 100.0)
    rc_mass = 12.0 + 18.0 * math.sqrt(pcts[2] / 100.0)

    total_bar_w = 842.0
    w_u = max(40.0, total_bar_w * (pcts[0] / 100.0))
    w_v = max(40.0, total_bar_w * (pcts[1] / 100.0))
    w_w = max(40.0, total_bar_w - w_u - w_v)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 760" width="100%" height="100%">
  <defs>
    <filter id="glow-bary" filterUnits="userSpaceOnUse" x="-100" y="-100" width="1200" height="960">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feMerge><feMergeNode in="blur" /><feMergeNode in="SourceGraphic" /></feMerge>
    </filter>
  </defs>

  <polygon points="{Ps[0]:.1f},{Ps[1]:.1f} {Bs[0]:.1f},{Bs[1]:.1f} {Cs[0]:.1f},{Cs[1]:.1f}"
           fill="rgba(232, 184, 90, 0.24)" stroke="none" />
  <polygon points="{Ps[0]:.1f},{Ps[1]:.1f} {Cs[0]:.1f},{Cs[1]:.1f} {As[0]:.1f},{As[1]:.1f}"
           fill="rgba(56, 189, 248, 0.22)" stroke="none" />
  <polygon points="{Ps[0]:.1f},{Ps[1]:.1f} {As[0]:.1f},{As[1]:.1f} {Bs[0]:.1f},{Bs[1]:.1f}"
           fill="rgba(94, 194, 126, 0.22)" stroke="none" />

  <polygon points="{As[0]:.1f},{As[1]:.1f} {Bs[0]:.1f},{Bs[1]:.1f} {Cs[0]:.1f},{Cs[1]:.1f}"
           fill="none" stroke="#f8f6f0" stroke-width="3.2" stroke-linejoin="round" />

  <line x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{As[0]:.1f}" y2="{As[1]:.1f}" stroke="#e8b85a" stroke-width="3.2" stroke-dasharray="12,5,2.5,5" stroke-linecap="round" />
  <line x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{Bs[0]:.1f}" y2="{Bs[1]:.1f}" stroke="#38bdf8" stroke-width="3.2" stroke-dasharray="12,5,2.5,5" stroke-linecap="round" />
  <line x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{Cs[0]:.1f}" y2="{Cs[1]:.1f}" stroke="#5ec27e" stroke-width="3.2" stroke-dasharray="12,5,2.5,5" stroke-linecap="round" />

  <circle cx="{As[0]:.1f}" cy="{As[1]:.1f}" r="{ra_mass:.1f}" fill="rgba(232, 184, 90, 0.22)" stroke="#e8b85a" stroke-width="2.4" />
  <circle cx="{Bs[0]:.1f}" cy="{Bs[1]:.1f}" r="{rb_mass:.1f}" fill="rgba(56, 189, 248, 0.22)" stroke="#38bdf8" stroke-width="2.4" />
  <circle cx="{Cs[0]:.1f}" cy="{Cs[1]:.1f}" r="{rc_mass:.1f}" fill="rgba(94, 194, 126, 0.22)" stroke="#5ec27e" stroke-width="2.4" />

  <circle cx="{As[0]:.1f}" cy="{As[1]:.1f}" r="6" fill="#f8f6f0" stroke="#0d111a" stroke-width="2" />
  <circle cx="{Bs[0]:.1f}" cy="{Bs[1]:.1f}" r="6" fill="#f8f6f0" stroke="#0d111a" stroke-width="2" />
  <circle cx="{Cs[0]:.1f}" cy="{Cs[1]:.1f}" r="6" fill="#f8f6f0" stroke="#0d111a" stroke-width="2" />

  <g transform="translate({ga[0]:.1f}, {ga[1]:.1f})">
    <rect x="-72" y="-26" width="144" height="50" rx="8" fill="rgba(13, 17, 26, 0.90)" stroke="#e8b85a" stroke-width="1.5" />
    <text x="0" y="-4" text-anchor="middle" fill="#e8b85a" font-family="JetBrains Mono, monospace" font-size="16" font-weight="bold">u = a·α ({disp_bary[0]:.3g})</text>
    <text x="0" y="17" text-anchor="middle" fill="#f8f6f0" font-family="JetBrains Mono, monospace" font-size="15">△{_svg_x(num, f"BC • {pcts[0]:.1f}%")}</text>
  </g>
  <g transform="translate({gb[0]:.1f}, {gb[1]:.1f})">
    <rect x="-72" y="-26" width="144" height="50" rx="8" fill="rgba(13, 17, 26, 0.90)" stroke="#38bdf8" stroke-width="1.5" />
    <text x="0" y="-4" text-anchor="middle" fill="#38bdf8" font-family="JetBrains Mono, monospace" font-size="16" font-weight="bold">v = b·β ({disp_bary[1]:.3g})</text>
    <text x="0" y="17" text-anchor="middle" fill="#f8f6f0" font-family="JetBrains Mono, monospace" font-size="15">△{_svg_x(num, f"CA • {pcts[1]:.1f}%")}</text>
  </g>
  <g transform="translate({gc[0]:.1f}, {gc[1]:.1f})">
    <rect x="-72" y="-26" width="144" height="50" rx="8" fill="rgba(13, 17, 26, 0.90)" stroke="#5ec27e" stroke-width="1.5" />
    <text x="0" y="-4" text-anchor="middle" fill="#5ec27e" font-family="JetBrains Mono, monospace" font-size="16" font-weight="bold">w = c·γ ({disp_bary[2]:.3g})</text>
    <text x="0" y="17" text-anchor="middle" fill="#f8f6f0" font-family="JetBrains Mono, monospace" font-size="15">△{_svg_x(num, f"AB • {pcts[2]:.1f}%")}</text>
  </g>

  <circle cx="{Ps[0]:.1f}" cy="{Ps[1]:.1f}" r="9.5" fill="#e8b85a" stroke="#ffffff" stroke-width="2.8" filter="url(#glow-bary)" />
  <rect x="{Ps[0] - 32:.1f}" y="{Ps[1] - 42:.1f}" width="64" height="26" rx="6" fill="rgba(13, 17, 26, 0.92)" stroke="#e8b85a" stroke-width="1.2" />
  <text x="{Ps[0]:.1f}" y="{Ps[1] - 24:.1f}" text-anchor="middle" fill="#e8b85a" font-family="JetBrains Mono, monospace" font-size="17" font-weight="bold">{_svg_x(num)}</text>

  <text x="{As[0] - 42:.1f}" y="{As[1] + 32:.1f}" fill="#e8b85a" font-family="Georgia, serif" font-size="25" font-weight="bold">A (u)</text>
  <text x="{Bs[0] + 24:.1f}" y="{Bs[1] + 32:.1f}" fill="#38bdf8" font-family="Georgia, serif" font-size="25" font-weight="bold">B (v)</text>
  <text x="{Cs[0] - 28:.1f}" y="{Cs[1] - 28:.1f}" fill="#5ec27e" font-family="Georgia, serif" font-size="25" font-weight="bold">C (w)</text>

  <g transform="translate(55, 575)">
    <rect x="0" y="0" width="890" height="158" rx="14" fill="rgba(11, 14, 21, 0.92)" stroke="rgba(232, 184, 90, 0.35)" stroke-width="1.5" />
    <text x="24" y="34" fill="#94a3b8" font-family="JetBrains Mono, monospace" font-size="15" font-weight="bold" letter-spacing="1.0">SUB-TRIANGLE AREA PARTITION • (u : v : w) = (aα : bβ : cγ)</text>
    <text x="866" y="34" text-anchor="end" fill="#e8b85a" font-family="JetBrains Mono, monospace" font-size="18" font-weight="bold">u : v : w = {html.escape(barycentric_formula[:28])}</text>

    <rect x="24" y="54" width="{w_u:.1f}" height="42" rx="6" fill="#e8b85a" />
    <rect x="{24 + w_u:.1f}" y="54" width="{w_v:.1f}" height="42" fill="#38bdf8" />
    <rect x="{24 + w_u + w_v:.1f}" y="54" width="{w_w:.1f}" height="42" rx="6" fill="#5ec27e" />

    <text x="{24 + w_u * 0.5:.1f}" y="81" text-anchor="middle" fill="#0d111a" font-family="JetBrains Mono, monospace" font-size="17" font-weight="bold">u: {pcts[0]:.1f}%</text>
    <text x="{24 + w_u + w_v * 0.5:.1f}" y="81" text-anchor="middle" fill="#0d111a" font-family="JetBrains Mono, monospace" font-size="17" font-weight="bold">v: {pcts[1]:.1f}%</text>
    <text x="{24 + w_u + w_v + w_w * 0.5:.1f}" y="81" text-anchor="middle" fill="#0d111a" font-family="JetBrains Mono, monospace" font-size="17" font-weight="bold">w: {pcts[2]:.1f}%</text>

    <text x="445" y="132" text-anchor="middle" fill="#f8f6f0" font-family="Georgia, serif" font-size="21">
      Area(△{_svg_x(num, "BC")}) : Area(△{_svg_x(num, "CA")}) : Area(△{_svg_x(num, f"AB) = ½aα : ½bβ : ½cγ = {disp_bary[0]:.3g} : {disp_bary[1]:.3g} : {disp_bary[2]:.3g}")}
    </text>
  </g>
</svg>"""


def generate_coordinate_trio_svg(
    ctx: TriangleContext,
    reg: CenterRegistry,
) -> str:
    """Generate a 1000x760 SVG comparing X_1 (Incenter), X_2 (Centroid), and X_6 (Symmedian) in pictures."""
    A, B, C = ctx.A_xy, ctx.B_xy, ctx.C_xy
    cards = [
        (
            1,
            f'{_svg_x(1, " • Incenter")}',
            "Equal Distances (r)",
            "α : β : γ = 1 : 1 : 1",
            "Perpendiculars: (1 : 1 : 1)",
            "u : v : w = a : b : c",
            "Sub-Areas: (5 : 6 : 7)",
            "#e8b85a",
            35.0,
        ),
        (
            2,
            f'{_svg_x(2, " • Centroid")}',
            "Equal Sub-Areas (⅓)",
            "α : β : γ = 1/a : 1/b : 1/c",
            "Perpendiculars: (42 : 35 : 30)",
            "u : v : w = 1 : 1 : 1",
            "Sub-Areas: (1 : 1 : 1)",
            "#38bdf8",
            355.0,
        ),
        (
            6,
            f'{_svg_x(6, " • Symmedian")}',
            "Side-Proportional",
            "α : β : γ = a : b : c",
            "Perpendiculars: (5 : 6 : 7)",
            "u : v : w = a² : b² : c²",
            "Sub-Areas: (25 : 36 : 49)",
            "#5ec27e",
            675.0,
        ),
    ]

    panels = []
    scale = 235.0
    for c_num, c_title_svg, c_tag, tri_lbl, tri_sub, bary_lbl, bary_sub, accent, x_off in cards:
        P = reg.xy_cache.get(c_num, (0.5, 0.25))
        ox = x_off + 28.0
        oy = 365.0
        As = _to_screen(A, scale, ox, oy)
        Bs = _to_screen(B, scale, ox, oy)
        Cs = _to_screen(C, scale, ox, oy)
        Ps = _to_screen(P, scale, ox, oy)
        Pa = _to_screen(_foot_on_line(P, B, C), scale, ox, oy)
        Pb = _to_screen(_foot_on_line(P, C, A), scale, ox, oy)
        Pc = _to_screen(_foot_on_line(P, A, B), scale, ox, oy)

        panels.append(f"""
  <g>
    <rect x="{x_off:.1f}" y="26" width="290" height="708" rx="16" fill="rgba(13, 17, 26, 0.92)" stroke="{accent}" stroke-width="2" />
    <text x="{x_off + 145:.1f}" y="68" text-anchor="middle" fill="{accent}" font-family="Georgia, serif" font-size="25" font-weight="bold">{c_title_svg}</text>
    <text x="{x_off + 145:.1f}" y="98" text-anchor="middle" fill="#cbd5e1" font-family="JetBrains Mono, monospace" font-size="15" font-weight="bold">{html.escape(c_tag)}</text>

    <polygon points="{Ps[0]:.1f},{Ps[1]:.1f} {Bs[0]:.1f},{Bs[1]:.1f} {Cs[0]:.1f},{Cs[1]:.1f}" fill="rgba(232, 184, 90, 0.18)" stroke="rgba(232, 184, 90, 0.45)" stroke-width="1.4" />
    <polygon points="{Ps[0]:.1f},{Ps[1]:.1f} {Cs[0]:.1f},{Cs[1]:.1f} {As[0]:.1f},{As[1]:.1f}" fill="rgba(56, 189, 248, 0.16)" stroke="rgba(56, 189, 248, 0.45)" stroke-width="1.4" />
    <polygon points="{Ps[0]:.1f},{Ps[1]:.1f} {As[0]:.1f},{As[1]:.1f} {Bs[0]:.1f},{Bs[1]:.1f}" fill="rgba(94, 194, 126, 0.16)" stroke="rgba(94, 194, 126, 0.45)" stroke-width="1.4" />

    <polygon points="{As[0]:.1f},{As[1]:.1f} {Bs[0]:.1f},{Bs[1]:.1f} {Cs[0]:.1f},{Cs[1]:.1f}" fill="none" stroke="#f8f6f0" stroke-width="2.4" />

    <line x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{Pa[0]:.1f}" y2="{Pa[1]:.1f}" stroke="#e8b85a" stroke-width="3.4" />
    <line x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{Pb[0]:.1f}" y2="{Pb[1]:.1f}" stroke="#38bdf8" stroke-width="3.4" />
    <line x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{Pc[0]:.1f}" y2="{Pc[1]:.1f}" stroke="#5ec27e" stroke-width="3.4" />

    <circle cx="{Ps[0]:.1f}" cy="{Ps[1]:.1f}" r="7.5" fill="{accent}" stroke="#ffffff" stroke-width="2.2" />

    <text x="{As[0] - 16:.1f}" y="{As[1] + 18:.1f}" fill="#f8f6f0" font-family="Georgia, serif" font-size="18" font-weight="bold">A</text>
    <text x="{Bs[0] + 6:.1f}" y="{Bs[1] + 18:.1f}" fill="#f8f6f0" font-family="Georgia, serif" font-size="18" font-weight="bold">B</text>
    <text x="{Cs[0] - 6:.1f}" y="{Cs[1] - 10:.1f}" fill="#f8f6f0" font-family="Georgia, serif" font-size="18" font-weight="bold">C</text>

    <rect x="{x_off + 16:.1f}" y="435" width="258" height="118" rx="10" fill="rgba(20, 26, 38, 0.95)" stroke="rgba(232, 184, 90, 0.35)" />
    <text x="{x_off + 145:.1f}" y="466" text-anchor="middle" fill="#94a3b8" font-family="JetBrains Mono, monospace" font-size="14" font-weight="bold">TRILINEAR DISTANCES</text>
    <text x="{x_off + 145:.1f}" y="500" text-anchor="middle" fill="#e8b85a" font-family="JetBrains Mono, monospace" font-size="16" font-weight="bold">{html.escape(tri_lbl)}</text>
    <text x="{x_off + 145:.1f}" y="532" text-anchor="middle" fill="#cbd5e1" font-family="JetBrains Mono, monospace" font-size="14">{html.escape(tri_sub)}</text>

    <rect x="{x_off + 16:.1f}" y="572" width="258" height="132" rx="10" fill="rgba(20, 26, 38, 0.95)" stroke="rgba(56, 189, 248, 0.35)" />
    <text x="{x_off + 145:.1f}" y="603" text-anchor="middle" fill="#94a3b8" font-family="JetBrains Mono, monospace" font-size="14" font-weight="bold">BARYCENTRIC AREAS</text>
    <text x="{x_off + 145:.1f}" y="638" text-anchor="middle" fill="#38bdf8" font-family="JetBrains Mono, monospace" font-size="16" font-weight="bold">{html.escape(bary_lbl)}</text>
    <text x="{x_off + 145:.1f}" y="672" text-anchor="middle" fill="#cbd5e1" font-family="JetBrains Mono, monospace" font-size="14">{html.escape(bary_sub)}</text>
  </g>""")

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 760" width="100%" height="100%">
  {''.join(panels)}
</svg>"""


def generate_symbolic_four_triangles_svg(num: int = 1) -> str:
    """Generate an interactive 1000x760 2x2 SVG showing ``X_num`` across the 4 Canonical Exact Symbolic Reference Triangles."""
    quad_specs = [
        (
            "heronian",
            "Heronian (15, 13, 14)",
            "Δ = 84 • ℚ",
            token_hex(REFERENCE_TRIANGLE_COLORS["heronian"]),
            35.0,
            22.0,
        ),
        (
            "right",
            "Right (3, 4, 5)",
            "Δ = 6 • ℚ",
            token_hex(REFERENCE_TRIANGLE_COLORS["right"]),
            515.0,
            22.0,
        ),
        (
            "kepler",
            "Kepler (1, √φ, φ)",
            "Δ = √φ/2 • ℚ(√φ)",
            token_hex(REFERENCE_TRIANGLE_COLORS["kepler"]),
            35.0,
            390.0,
        ),
        (
            "kimberling",
            "Kimberling (6, 9, 13)",
            "Δ = 3√35 • ℚ(√35)",
            token_hex(REFERENCE_TRIANGLE_COLORS["kimberling"]),
            515.0,
            390.0,
        ),
    ]

    catalog: dict[str, Any] = {}
    panels: list[str] = []

    for key, label, field_badge, accent, x_off, y_off in quad_specs:
        tri = CANONICAL_TRIANGLES[key]
        sym_reg = CenterSymbolicRegistry(tri)
        rec = sym_reg.get(num)
        if rec is None:
            continue

        kp = rec.is_kepler
        A_ex, B_ex, C_ex = tri.A_xy, tri.B_xy, tri.C_xy
        P_ex = rec.xy
        Pa_ex = _exact_pedal_foot(P_ex, B_ex, C_ex, tri)
        Pb_ex = _exact_pedal_foot(P_ex, C_ex, A_ex, tri)
        Pc_ex = _exact_pedal_foot(P_ex, A_ex, B_ex, tri)

        A = (float(A_ex[0].evalf(20)), float(A_ex[1].evalf(20)))
        B = (float(B_ex[0].evalf(20)), float(B_ex[1].evalf(20)))
        C = (float(C_ex[0].evalf(20)), float(C_ex[1].evalf(20)))
        P = (float(P_ex[0].evalf(20)), float(P_ex[1].evalf(20)))
        Pa = (float(Pa_ex[0].evalf(20)), float(Pa_ex[1].evalf(20)))
        Pb = (float(Pb_ex[0].evalf(20)), float(Pb_ex[1].evalf(20)))
        Pc = (float(Pc_ex[0].evalf(20)), float(Pc_ex[1].evalf(20)))

        sc, ox, oy = _fit_points_to_box(
            [A, B, C, P, Pa, Pb, Pc],
            x_off + 52.0,
            y_off + 58.0,
            346.0,
            234.0,
        )

        As = _to_screen(A, sc, ox, oy)
        Bs = _to_screen(B, sc, ox, oy)
        Cs = _to_screen(C, sc, ox, oy)
        Ps = _to_screen(P, sc, ox, oy)
        Pas = _to_screen(Pa, sc, ox, oy)
        Pbs = _to_screen(Pb, sc, ox, oy)
        Pcs = _to_screen(Pc, sc, ox, oy)

        panel_id = f"panel-{key}"
        pt_x_id = f"{key}-X_{num}"
        sub_a_id = f"{key}-sub-a"
        sub_b_id = f"{key}-sub-b"
        sub_c_id = f"{key}-sub-c"
        st_a_id = f"{key}-strut-a"
        st_b_id = f"{key}-strut-b"
        st_c_id = f"{key}-strut-c"

        q_r = tri.simplify(tri.r * tri.r)
        sides_ltx = f"\\left({format_symbolic_latex(tri.a, kepler_phi=kp)},\\; {format_symbolic_latex(tri.b, kepler_phi=kp)},\\; {format_symbolic_latex(tri.c, kepler_phi=kp)}\\right)"
        sides_prt = f"({format_symbolic_pretty(tri.a, kepler_phi=kp)}, {format_symbolic_pretty(tri.b, kepler_phi=kp)}, {format_symbolic_pretty(tri.c, kepler_phi=kp)})"
        xy_ltx = rec.xy_latex()
        xy_prt = rec.xy_pretty()

        panel_rows = [
            {"label": "sides", "latex": sides_ltx, "pretty": sides_prt},
            {"label": f"X_{{{num}}}", "latex": xy_ltx, "pretty": xy_prt},
            {
                "label": "bary",
                "latex": rec.bary_latex(),
                "pretty": rec.bary_pretty(),
            },
            {
                "label": "Δ, r",
                "latex": f"\\Delta = {format_symbolic_latex(tri.area, kepler_phi=kp)},\\; r = {format_symbolic_latex(tri.r, kepler_phi=kp)}",
                "pretty": f"Δ = {format_symbolic_pretty(tri.area, kepler_phi=kp)}, r = {format_symbolic_pretty(tri.r, kepler_phi=kp)}",
            },
        ]
        catalog[panel_id] = {
            "ID": panel_id,
            "type": "triangle",
            "color": accent,
            "name": label,
            "symbolic_rows": panel_rows,
            "approx": f"X_{num} ≈ ({P[0]:.6f}, {P[1]:.6f})",
        }
        catalog[pt_x_id] = _pt_meta_entry(
            pt_x_id,
            f"X_{num} on {label}",
            "#ffd700",
            P_ex,
            rec.bary_latex(),
            rec.bary_pretty(),
            rec.trilinear_latex(),
            rec.trilinear_pretty(),
            kepler_phi=kp,
        )
        catalog[f"{key}-A"] = _pt_meta_entry(f"{key}-A", f"Vertex A ({label})", "#66ff66", A_ex, kepler_phi=kp)
        catalog[f"{key}-B"] = _pt_meta_entry(f"{key}-B", f"Vertex B ({label})", "#66ff66", B_ex, kepler_phi=kp)
        catalog[f"{key}-C"] = _pt_meta_entry(f"{key}-C", f"Vertex C ({label})", "#f8f6f0", C_ex, kepler_phi=kp)

        for sid, p1_e, p2_e, p3_e, scol, sv in [
            (sub_a_id, P_ex, B_ex, C_ex, "#e8b85a", "BC"),
            (sub_b_id, P_ex, C_ex, A_ex, "#38bdf8", "CA"),
            (sub_c_id, P_ex, A_ex, B_ex, "#5ec27e", "AB"),
        ]:
            sa_val = _exact_sub_area(p1_e, p2_e, p3_e, tri)
            catalog[sid] = {
                "ID": sid,
                "type": "polygon",
                "color": scol,
                "name": f"Sub-Triangle △X_{num}{sv} ({label})",
                "symbolic_rows": [
                    {
                        "label": "Δ",
                        "latex": format_symbolic_latex(sa_val, kepler_phi=kp),
                        "pretty": format_symbolic_pretty(sa_val, kepler_phi=kp),
                    },
                    {
                        "label": "bary",
                        "latex": rec.bary_latex(),
                        "pretty": rec.bary_pretty(),
                    },
                ],
                "approx": f"≈ {float(sa_val.evalf(20)):.6f}",
            }

        for st_id, f_ex, scol, ssym, snm in [
            (st_a_id, Pa_ex, "#e8b85a", "\\alpha", "BC"),
            (st_b_id, Pb_ex, "#38bdf8", "\\beta", "CA"),
            (st_c_id, Pc_ex, "#5ec27e", "\\gamma", "AB"),
        ]:
            q_st = tri.simplify((f_ex[0] - P_ex[0]) ** 2 + (f_ex[1] - P_ex[1]) ** 2)
            l_st = tri.simplify(sp.sqrt(q_st))
            catalog[st_id] = {
                "ID": st_id,
                "type": "segment",
                "color": scol,
                "name": f"Strut ⊥ {snm} ({label})",
                "symbolic_rows": [
                    {
                        "label": "d",
                        "latex": f"{ssym}_0 = {format_symbolic_latex(l_st, kepler_phi=kp)}",
                        "pretty": format_symbolic_pretty(l_st, kepler_phi=kp),
                    },
                    {
                        "label": "Q",
                        "latex": format_symbolic_latex(q_st, kepler_phi=kp),
                        "pretty": format_symbolic_pretty(q_st, kepler_phi=kp),
                    },
                ],
                "approx": f"≈ {float(l_st.evalf(20)):.6f}",
            }

        incircle_panel_svg = ""
        if num == 1:
            r_scr = float(tri.r.evalf(20)) * sc
            inc_id = f"{key}-incircle"
            catalog[inc_id] = {
                "ID": inc_id,
                "type": "circle",
                "color": "#f472b6",
                "name": f"Incircle on {label}",
                "symbolic_rows": [
                    {
                        "label": "r",
                        "latex": format_symbolic_latex(tri.r, kepler_phi=kp),
                        "pretty": format_symbolic_pretty(tri.r, kepler_phi=kp),
                    },
                    {
                        "label": "Q_r",
                        "latex": format_symbolic_latex(q_r, kepler_phi=kp),
                        "pretty": format_symbolic_pretty(q_r, kepler_phi=kp),
                    },
                ],
                "approx": f"r ≈ {float(tri.r.evalf(20)):.6f}",
            }
            incircle_panel_svg = (
                f'    <circle id="{inc_id}" data-id="{inc_id}" data-ref="{inc_id}" class="etc-plate-circle" '
                f'cx="{Ps[0]:.1f}" cy="{Ps[1]:.1f}" r="{r_scr:.1f}" '
                f'fill="none" stroke="rgba(244, 114, 182, 0.55)" stroke-width="1.8" stroke-dasharray="5,4" />\n'
            )

        coord_footer = f"X_{num} = {xy_prt}"
        if len(coord_footer) > 42:
            coord_footer = coord_footer[:39] + "..."

        panels.append(f"""
  <g id="{panel_id}" data-id="{panel_id}" data-ref="{panel_id}" class="etc-plate-panel">
    <rect class="etc-panel-border" x="{x_off:.1f}" y="{y_off:.1f}" width="450" height="346" rx="16" fill="rgba(13, 17, 26, 0.92)" stroke="{accent}" stroke-width="1.8" />
    <text x="{x_off + 22:.1f}" y="{y_off + 34:.1f}" fill="{accent}" font-family="JetBrains Mono, monospace" font-size="17" font-weight="bold" pointer-events="none">{html.escape(label)}</text>
    <text x="{x_off + 428:.1f}" y="{y_off + 34:.1f}" text-anchor="end" fill="#94a3b8" font-family="JetBrains Mono, monospace" font-size="13.5" pointer-events="none">{html.escape(field_badge)}</text>

    <polygon id="{sub_a_id}" data-id="{sub_a_id}" data-ref="{sub_a_id}" class="etc-plate-poly" points="{Ps[0]:.1f},{Ps[1]:.1f} {Bs[0]:.1f},{Bs[1]:.1f} {Cs[0]:.1f},{Cs[1]:.1f}" fill="#e8b85a" fill-opacity="0.14" stroke="none" />
    <polygon id="{sub_b_id}" data-id="{sub_b_id}" data-ref="{sub_b_id}" class="etc-plate-poly" points="{Ps[0]:.1f},{Ps[1]:.1f} {Cs[0]:.1f},{Cs[1]:.1f} {As[0]:.1f},{As[1]:.1f}" fill="#38bdf8" fill-opacity="0.14" stroke="none" />
    <polygon id="{sub_c_id}" data-id="{sub_c_id}" data-ref="{sub_c_id}" class="etc-plate-poly" points="{Ps[0]:.1f},{Ps[1]:.1f} {As[0]:.1f},{As[1]:.1f} {Bs[0]:.1f},{Bs[1]:.1f}" fill="#5ec27e" fill-opacity="0.14" stroke="none" />

{incircle_panel_svg}    <polygon points="{As[0]:.1f},{As[1]:.1f} {Bs[0]:.1f},{Bs[1]:.1f} {Cs[0]:.1f},{Cs[1]:.1f}" fill="none" stroke="#cbd5e1" stroke-width="2.3" stroke-dasharray="2, 4.5" stroke-linecap="round" pointer-events="none" />
    <line id="{st_a_id}" data-id="{st_a_id}" data-ref="{st_a_id}" class="etc-plate-strut" x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{Pas[0]:.1f}" y2="{Pas[1]:.1f}" stroke="#e8b85a" stroke-width="2.9" />
    <line id="{st_b_id}" data-id="{st_b_id}" data-ref="{st_b_id}" class="etc-plate-strut" x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{Pbs[0]:.1f}" y2="{Pbs[1]:.1f}" stroke="#38bdf8" stroke-width="2.9" />
    <line id="{st_c_id}" data-id="{st_c_id}" data-ref="{st_c_id}" class="etc-plate-strut" x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{Pcs[0]:.1f}" y2="{Pcs[1]:.1f}" stroke="#5ec27e" stroke-width="2.9" />

    <circle id="{key}-A" data-id="{key}-A" data-ref="{key}-A" class="etc-plate-pt" cx="{As[0]:.1f}" cy="{As[1]:.1f}" r="4.6" fill="#66ff66" />
    <circle id="{key}-B" data-id="{key}-B" data-ref="{key}-B" class="etc-plate-pt" cx="{Bs[0]:.1f}" cy="{Bs[1]:.1f}" r="4.6" fill="#66ff66" />
    <circle id="{key}-C" data-id="{key}-C" data-ref="{key}-C" class="etc-plate-pt" cx="{Cs[0]:.1f}" cy="{Cs[1]:.1f}" r="4.6" fill="#f8f6f0" />
    <circle id="{pt_x_id}" data-id="{pt_x_id}" data-ref="{pt_x_id}" class="etc-plate-pt" cx="{Ps[0]:.1f}" cy="{Ps[1]:.1f}" r="7.5" fill="#ffd700" stroke="#00ffff" stroke-width="2.2" />

    <g pointer-events="none">
      <text x="{As[0] - 18:.1f}" y="{As[1] + 18:.1f}" fill="#88ff88" font-family="Georgia, serif" font-size="18" font-weight="bold">A</text>
      <text x="{Bs[0] + 8:.1f}" y="{Bs[1] + 18:.1f}" fill="#88ff88" font-family="Georgia, serif" font-size="18" font-weight="bold">B</text>
      <text x="{Cs[0] - 6:.1f}" y="{Cs[1] - 10:.1f}" fill="#f8f6f0" font-family="Georgia, serif" font-size="18" font-weight="bold">C</text>
      <text x="{Ps[0] + 12:.1f}" y="{Ps[1] - 10:.1f}" fill="#ffd700" font-family="JetBrains Mono, monospace" font-size="17" font-weight="bold">{_svg_x(num)}</text>
      <text x="{x_off + 225:.1f}" y="{y_off + 332:.1f}" text-anchor="middle" fill="#cbd5e1" font-family="JetBrains Mono, monospace" font-size="12.5">{html.escape(coord_footer)}</text>
    </g>
  </g>""")

    meta_json = _safe_meta_json(catalog)
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg class="geometor-etc-drawing" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 760" data-initial-viewbox="0 0 1000 760" width="100%" height="100%" preserveAspectRatio="xMidYMid meet">
  <style>{EXPLORER_SVG_CSS}</style>
  {''.join(panels)}
  <script type="application/json" class="etc-elements-meta">{meta_json}</script>
  <script>//<![CDATA[
{INTERACTIVE_SVG_JS}
//]]></script>
</svg>"""


def generate_four_triangles_svg(
    num: int,
    regs_by_preset: dict[str, tuple[str, TriangleContext, CenterRegistry]] | None = None,
) -> str:
    """Generate a 1000x760 2x2 SVG showing ``X_n`` across the 4 Canonical Reference Triangles."""
    if (
        regs_by_preset is None
        or CenterSymbolicRegistry(CANONICAL_TRIANGLES["heronian"]).get(num) is not None
    ):
        return generate_symbolic_four_triangles_svg(num=num)

    quad_specs = [
        ("acute", "Acute", token_hex(REFERENCE_TRIANGLE_COLORS["acute"]), 35.0, 22.0),
        ("right", "Right", token_hex(REFERENCE_TRIANGLE_COLORS["right"]), 515.0, 22.0),
        ("kepler", "Kepler", token_hex(REFERENCE_TRIANGLE_COLORS["kepler"]), 35.0, 390.0),
        ("kimberling", "Kimberling", token_hex(REFERENCE_TRIANGLE_COLORS["kimberling"]), 515.0, 390.0),
    ]
    panels = []
    for key, label, accent, x_off, y_off in quad_specs:
        if key not in regs_by_preset:
            continue
        _, ctx, reg = regs_by_preset[key]
        A, B, C = ctx.A_xy, ctx.B_xy, ctx.C_xy
        P = reg.xy_cache.get(num, (0.5, 0.25))
        Pa = _foot_on_line(P, B, C)
        Pb = _foot_on_line(P, C, A)
        Pc = _foot_on_line(P, A, B)
        sc, ox, oy = _fit_points_to_box([A, B, C, P, Pa, Pb, Pc], x_off + 55.0, y_off + 62.0, 340.0, 250.0)
        As = _to_screen(A, sc, ox, oy)
        Bs = _to_screen(B, sc, ox, oy)
        Cs = _to_screen(C, sc, ox, oy)
        Ps = _to_screen(P, sc, ox, oy)
        Pas = _to_screen(Pa, sc, ox, oy)
        Pbs = _to_screen(Pb, sc, ox, oy)
        Pcs = _to_screen(Pc, sc, ox, oy)
        panels.append(f"""
  <g>
    <rect x="{x_off:.1f}" y="{y_off:.1f}" width="450" height="346" rx="16" fill="rgba(13, 17, 26, 0.92)" stroke="{accent}" stroke-width="1.8" />
    <text x="{x_off + 24:.1f}" y="{y_off + 36:.1f}" fill="{accent}" font-family="JetBrains Mono, monospace" font-size="18" font-weight="bold">{html.escape(label)}</text>
    <polygon points="{As[0]:.1f},{As[1]:.1f} {Bs[0]:.1f},{Bs[1]:.1f} {Cs[0]:.1f},{Cs[1]:.1f}" fill="none" stroke="#cbd5e1" stroke-width="2.3" stroke-dasharray="2, 4.5" />
    <line x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{Pas[0]:.1f}" y2="{Pas[1]:.1f}" stroke="#e8b85a" stroke-width="2.8" />
    <line x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{Pbs[0]:.1f}" y2="{Pbs[1]:.1f}" stroke="#38bdf8" stroke-width="2.8" />
    <line x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{Pcs[0]:.1f}" y2="{Pcs[1]:.1f}" stroke="#5ec27e" stroke-width="2.8" />
    <circle cx="{Ps[0]:.1f}" cy="{Ps[1]:.1f}" r="7.5" fill="#ffd700" stroke="#00ffff" stroke-width="2.2" />
  </g>""")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 760" width="100%" height="100%">
  {''.join(panels)}
</svg>"""


def generate_construction_picture_svg(
    num: int,
    title: str,
    enunciation: str,
    ctx: TriangleContext,
    reg: CenterRegistry,
    mode: str = "identity",
) -> str:
    """Generate a 1000x760 SVG in screen coordinates showing the geometric construction of X_n."""
    A, B, C = ctx.A_xy, ctx.B_xy, ctx.C_xy
    P = reg.xy_cache.get(num, (0.5, 0.25))
    bary = reg.bary_cache.get(num, (ctx.raw_a, ctx.raw_b, ctx.raw_c))

    scale = 610.0
    ox = 195.0
    oy = 505.0

    As = _to_screen(A, scale, ox, oy)
    Bs = _to_screen(B, scale, ox, oy)
    Cs = _to_screen(C, scale, ox, oy)
    Ps = _to_screen(P, scale, ox, oy)

    u, v, w = bary
    ap_xy = (
        (v * B[0] + w * C[0]) / (v + w) if abs(v + w) > 1e-9 else 0.5 * (B[0] + C[0]),
        (v * B[1] + w * C[1]) / (v + w) if abs(v + w) > 1e-9 else 0.5 * (B[1] + C[1]),
    )
    bp_xy = (
        (w * C[0] + u * A[0]) / (w + u) if abs(w + u) > 1e-9 else 0.5 * (C[0] + A[0]),
        (w * C[1] + u * A[1]) / (w + u) if abs(w + u) > 1e-9 else 0.5 * (C[1] + A[1]),
    )
    cp_xy = (
        (u * A[0] + v * B[0]) / (u + v) if abs(u + v) > 1e-9 else 0.5 * (A[0] + B[0]),
        (u * A[1] + v * B[1]) / (u + v) if abs(u + v) > 1e-9 else 0.5 * (A[1] + B[1]),
    )
    Aps = _to_screen(ap_xy, scale, ox, oy)
    Bps = _to_screen(bp_xy, scale, ox, oy)
    Cps = _to_screen(cp_xy, scale, ox, oy)

    Tas = _to_screen(_foot_on_line(P, B, C), scale, ox, oy)
    Tbs = _to_screen(_foot_on_line(P, C, A), scale, ox, oy)
    Tcs = _to_screen(_foot_on_line(P, A, B), scale, ox, oy)

    circle_svg = ""
    derived_tri_svg = ""
    if num == 1:
        r_scr = math.hypot(Ps[0] - Tcs[0], Ps[1] - Tcs[1])
        circle_svg = (
            f'<circle cx="{Ps[0]:.1f}" cy="{Ps[1]:.1f}" r="{r_scr:.1f}" '
            f'fill="rgba(224, 64, 251, 0.07)" stroke="#e040fb" stroke-width="3.2" />'
        )
        derived_tri_svg = (
            f'<polygon points="{Tas[0]:.1f},{Tas[1]:.1f} {Tbs[0]:.1f},{Tbs[1]:.1f} {Tcs[0]:.1f},{Tcs[1]:.1f}" '
            f'fill="rgba(56, 189, 248, 0.12)" stroke="#38bdf8" stroke-width="2.4" stroke-dasharray="6,4" />'
            f'<circle cx="{Tas[0]:.1f}" cy="{Tas[1]:.1f}" r="5" fill="#38bdf8" />'
            f'<circle cx="{Tbs[0]:.1f}" cy="{Tbs[1]:.1f}" r="5" fill="#38bdf8" />'
            f'<circle cx="{Tcs[0]:.1f}" cy="{Tcs[1]:.1f}" r="5" fill="#38bdf8" />'
            f'<text x="{Tas[0] + 12:.1f}" y="{Tas[1] - 8:.1f}" fill="#38bdf8" font-family="Georgia, serif" font-size="19" font-weight="bold">T<tspan dy="0.28em" font-size="74%">a</tspan></text>'
            f'<text x="{Tbs[0] - 36:.1f}" y="{Tbs[1] - 10:.1f}" fill="#38bdf8" font-family="Georgia, serif" font-size="19" font-weight="bold">T<tspan dy="0.28em" font-size="74%">b</tspan></text>'
            f'<text x="{Tcs[0] + 10:.1f}" y="{Tcs[1] + 26:.1f}" fill="#38bdf8" font-family="Georgia, serif" font-size="19" font-weight="bold">T<tspan dy="0.28em" font-size="74%">c</tspan></text>'
        )
    else:
        derived_tri_svg = (
            f'<polygon points="{Aps[0]:.1f},{Aps[1]:.1f} {Bps[0]:.1f},{Bps[1]:.1f} {Cps[0]:.1f},{Cps[1]:.1f}" '
            f'fill="rgba(56, 189, 248, 0.10)" stroke="#38bdf8" stroke-width="2.2" stroke-dasharray="6,4" />'
        )

    cev_stroke = "#e8b85a" if mode == "construction" else "#94a3b8"
    cev_w = "3.6" if mode == "construction" else "2.4"

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 760" width="100%" height="100%">
  <defs>
    <filter id="glow-construct" filterUnits="userSpaceOnUse" x="-100" y="-100" width="1200" height="960">
      <feGaussianBlur stdDeviation="5" result="blur" />
      <feMerge><feMergeNode in="blur" /><feMergeNode in="SourceGraphic" /></feMerge>
    </filter>
  </defs>

  <polygon points="{As[0]:.1f},{As[1]:.1f} {Bs[0]:.1f},{Bs[1]:.1f} {Cs[0]:.1f},{Cs[1]:.1f}"
           fill="rgba(214, 207, 197, 0.05)" stroke="#d6cfc5" stroke-width="3.4" stroke-linejoin="round" />

  {derived_tri_svg}
  {circle_svg}

  <line x1="{As[0]:.1f}" y1="{As[1]:.1f}" x2="{Aps[0]:.1f}" y2="{Aps[1]:.1f}"
        stroke="{cev_stroke}" stroke-width="{cev_w}" stroke-dasharray="12,5,2.5,5" stroke-linecap="round" />
  <line x1="{Bs[0]:.1f}" y1="{Bs[1]:.1f}" x2="{Bps[0]:.1f}" y2="{Bps[1]:.1f}"
        stroke="{cev_stroke}" stroke-width="{cev_w}" stroke-dasharray="12,5,2.5,5" stroke-linecap="round" />
  <line x1="{Cs[0]:.1f}" y1="{Cs[1]:.1f}" x2="{Cps[0]:.1f}" y2="{Cps[1]:.1f}"
        stroke="{cev_stroke}" stroke-width="{cev_w}" stroke-dasharray="12,5,2.5,5" stroke-linecap="round" />

  <circle cx="{Aps[0]:.1f}" cy="{Aps[1]:.1f}" r="5.5" fill="#e8b85a" stroke="#0d111a" stroke-width="2" />
  <circle cx="{Bps[0]:.1f}" cy="{Bps[1]:.1f}" r="5.5" fill="#e8b85a" stroke="#0d111a" stroke-width="2" />
  <circle cx="{Cps[0]:.1f}" cy="{Cps[1]:.1f}" r="5.5" fill="#e8b85a" stroke="#0d111a" stroke-width="2" />

  <text x="{Aps[0] + 12:.1f}" y="{Aps[1] + 6:.1f}" fill="#e8b85a" font-family="Georgia, serif" font-size="19" font-weight="bold">I<tspan dy="0.28em" font-size="74%">a</tspan></text>
  <text x="{Bps[0] - 34:.1f}" y="{Bps[1] + 12:.1f}" fill="#e8b85a" font-family="Georgia, serif" font-size="19" font-weight="bold">I<tspan dy="0.28em" font-size="74%">b</tspan></text>
  <text x="{Cps[0] - 28:.1f}" y="{Cps[1] + 26:.1f}" fill="#e8b85a" font-family="Georgia, serif" font-size="19" font-weight="bold">I<tspan dy="0.28em" font-size="74%">c</tspan></text>

  <circle cx="{As[0]:.1f}" cy="{As[1]:.1f}" r="6.5" fill="#f8f6f0" stroke="#0d111a" stroke-width="2.2" />
  <circle cx="{Bs[0]:.1f}" cy="{Bs[1]:.1f}" r="6.5" fill="#f8f6f0" stroke="#0d111a" stroke-width="2.2" />
  <circle cx="{Cs[0]:.1f}" cy="{Cs[1]:.1f}" r="6.5" fill="#f8f6f0" stroke="#0d111a" stroke-width="2.2" />

  <text x="{As[0] - 28:.1f}" y="{As[1] + 24:.1f}" fill="#f8f6f0" font-family="Georgia, serif" font-size="26" font-weight="bold">A</text>
  <text x="{Bs[0] + 16:.1f}" y="{Bs[1] + 24:.1f}" fill="#f8f6f0" font-family="Georgia, serif" font-size="26" font-weight="bold">B</text>
  <text x="{Cs[0] - 8:.1f}" y="{Cs[1] - 18:.1f}" fill="#f8f6f0" font-family="Georgia, serif" font-size="26" font-weight="bold">C</text>

  <circle cx="{Ps[0]:.1f}" cy="{Ps[1]:.1f}" r="10.5" fill="#e8b85a" stroke="#ffffff" stroke-width="3" filter="url(#glow-construct)" />
  <rect x="{Ps[0] - 36:.1f}" y="{Ps[1] - 46:.1f}" width="72" height="30" rx="6" fill="rgba(13, 17, 26, 0.92)" stroke="#e8b85a" stroke-width="1.5" />
  <text x="{Ps[0]:.1f}" y="{Ps[1] - 25:.1f}" text-anchor="middle" fill="#e8b85a" font-family="JetBrains Mono, monospace" font-size="19" font-weight="bold">{_svg_x(num)}</text>
</svg>"""


# ---------------------------------------------------------------------------
# Per-Center Video Profiles for Collection 1 (X_1 through X_19)
# ---------------------------------------------------------------------------

_SPOKEN_NUMS: dict[int, str] = {
    1: "X one",
    2: "X two",
    3: "X three",
    4: "X four",
    5: "X five",
    6: "X six",
    7: "X seven",
    8: "X eight",
    9: "X nine",
    10: "X ten",
    11: "X eleven",
    12: "X twelve",
    13: "X thirteen",
    14: "X fourteen",
    15: "X fifteen",
    16: "X sixteen",
    17: "X seventeen",
    18: "X eighteen",
    19: "X nineteen",
}

_COLLECTION_1_PROFILES: dict[int, dict[str, Any]] = {
    1: {
        "short_title": "INCENTER",
        "enunciation": "The intersection of the three interior angle bisectors and center of the inscribed circle of triangle ABC.",
        "partners": [8, 10, 75],
        "script": """[bell:proposition]
In the Encyclopedia of Triangle Centers, <pause> X one is the Incenter: <pause> the point where the three interior angle bisectors of triangle A B C concur, <pause> and the center of its unique inscribed circle.

[bell:construction]
Because X one is equidistant from sidelines B C, C A, and A B by the inradius r, <pause> its trilinear coordinates are simply one, to one, to one, <pause> while its barycentric sub-triangle areas scale directly with the side lengths, <pause> a, to b, to c. <pause> Toggle the central lines, <pause> and X one anchors the Nagel line through X two, X eight, and X ten, <pause> the Feuerbach line through X five and X eleven, <pause> and the Soddy line through X seven.

[bell:insight]
Under functional relations, <pause> X one is its own isogonal conjugate, <pause> the isotomic conjugate of X seventy-five, <pause> the anticomplement of the Spieker center X ten, <pause> and the complement of the Nagel point X eight. <pause> Across acute, right, Kepler, and Kimberling reference triangles, <pause> X one remains the invariant center of the incircle.
""",
        "s1": (
            "X_1 = Incenter • [A I_a] ∩ [B I_b] ∩ [C I_c]",
            '<span class="clause-line"><span class="g-tok">X_1</span> is the <b>Incenter</b> of reference triangle <span class="g-tok">ABC</span> — the concurrence of the interior angle bisectors <span class="g-tok">AI_a</span>, <span class="g-tok">BI_b</span>, <span class="g-tok">CI_c</span> and center of the <b>incircle</b> tangent at <span class="coincide-tok">T_a T_b T_c</span>.</span>',
            "EUCLID IV.4 • CONCURRENCE",
            "Cevian triangle: Incentral triangle I_a I_b I_c • Pedal triangle: Intouch triangle T_a T_b T_c.",
        ),
        "s2": (
            "Trilinears 1 : 1 : 1 • Barycentrics a : b : c",
            '<span class="clause-line"><b>Coordinates of X_1:</b> Equal perpendicular distances <span class="eq-tok">α : β : γ = 1 : 1 : 1</span> (each equal to inradius <span class="eq-tok">r</span>), partitioning <span class="g-tok">△ABC</span> into sub-triangle areas <span class="coincide-tok">u : v : w = a : b : c</span>.</span>',
            "HOMOGENEOUS COORDINATES",
            "On Heronian triangle (15, 13, 14), orthogonal struts have length r = 4 (Q_r = 16, ratio 1 : 1 : 1) and sub-areas are 30 : 26 : 28 = 15 : 13 : 14.",
        ),
        "s3": (
            "Nagel Line {1, 2, 8, 10} • Feuerbach Line {1, 5, 11}",
            '<span class="clause-line"><b>Incident Central Lines:</b> <span class="g-tok">X_1</span> anchors the <b>Nagel line</b> <span class="coincide-tok">{1, 2, 8, 10}</span>, the <b>Feuerbach line</b> <span class="eq-tok">{1, 5, 11}</span>, the <b>OI line</b> <span class="g-tok">{1, 3, 40}</span>, and the <b>Soddy line</b> <span class="coincide-tok">{1, 7, 20}</span>.</span>',
            "CENTRAL LINE INCIDENCES",
            "On the Nagel line, X_10 (Spieker center) is the exact midpoint of X_1 (Incenter) and X_8 (Nagel point).",
        ),
        "s4": (
            "Self-Isogonal (X_1) • Anticomplement of X_10 • Complement of X_8",
            '<span class="clause-line"><b>Functional Relations:</b> <span class="g-tok">X_1</span> is self-isogonal, the isotomic conjugate of <span class="coincide-tok">X_75</span>, the anticomplement of <span class="g-tok">X_10</span>, and the complement of <span class="eq-tok">X_8</span>.</span>',
            "CONJUGATES & HOMOTHETY",
            "Circumcircle inverse: X_36 • Midpoint of X_1 and X_8: X_10 (Spieker center).",
        ),
    },
    2: {
        "short_title": "CENTROID",
        "enunciation": "The intersection of the three medians and center of mass of triangle ABC.",
        "partners": [3, 4, 5, 6],
        "script": """[bell:proposition]
X two is the Centroid of triangle A B C: <pause> the intersection of the three medians joining vertices A, B, and C to the opposite side midpoints M sub a, M sub b, and M sub c.

[bell:construction]
As the planar center of mass, <pause> X two partitions triangle A B C into three sub-triangles of equal area, <pause> giving barycentric coordinates one, to one, to one, <pause> and trilinear distances inversely proportional to the side lengths, <pause> one over a, to one over b, to one over c. <pause> On the central lines layer, <pause> X two anchors both the Euler line through X three, X four, and X five, <pause> and the Nagel line through X one, X eight, and X ten.

[bell:insight]
Under functional relations, <pause> X two is the isogonal conjugate of the Symmedian point X six, <pause> its own isotomic conjugate, <pause> and the fixed center of the complement and anticomplement dilations. <pause> Across all four reference triangles, <pause> X two divides the segment from Circumcenter X three to Orthocenter X four in the exact ratio one to two.
""",
        "s1": (
            "X_2 = Centroid • [A M_a] ∩ [B M_b] ∩ [C M_c]",
            '<span class="clause-line"><span class="g-tok">X_2</span> is the <b>Centroid</b> of <span class="g-tok">△ABC</span> — the concurrence of the three medians <span class="g-tok">AM_a</span>, <span class="g-tok">BM_b</span>, <span class="g-tok">CM_c</span> and perspector of the <b>medial triangle</b> <span class="coincide-tok">M_a M_b M_c</span>.</span>',
            "ARCHIMEDES • CENTER OF MASS",
            "Divides each median in a 2 : 1 ratio from vertex to midpoint; Shinagawa Euler coefficients (1, 0).",
        ),
        "s2": (
            "Trilinears 1/a : 1/b : 1/c • Barycentrics 1 : 1 : 1",
            '<span class="clause-line"><b>Coordinates of X_2:</b> Equal sub-triangle areas <span class="eq-tok">u : v : w = 1 : 1 : 1</span> (each exactly <span class="eq-tok">⅓ Area(ABC)</span>), with perpendicular distances <span class="g-tok">α : β : γ = 1/a : 1/b : 1/c</span>.</span>',
            "EQUAL AREA PARTITION",
            "On acute triangle (5, 6, 7), perpendicular struts are 42 : 35 : 30 and sub-areas are 33.3% : 33.3% : 33.3%.",
        ),
        "s3": (
            "Euler Line {2, 3, 4, 5} • Nagel Line {1, 2, 8, 10}",
            '<span class="clause-line"><b>Incident Central Lines:</b> <span class="g-tok">X_2</span> is the intersection of the <b>Euler line</b> <span class="g-tok">{2, 3, 4, 5}</span>, the <b>Nagel line</b> <span class="coincide-tok">{1, 2, 8, 10}</span>, and the <b>Centroid–Gergonne line</b> <span class="eq-tok">{2, 7, 9}</span>.</span>',
            "EULER & NAGEL INTERSECTION",
            "On the Euler line, X_2 trisects segment X_3–X_4; on the Nagel line, X_2 trisects segment X_1–X_8.",
        ),
        "s4": (
            "Isogonal Conjugate X_6 • Self-Isotomic (X_2)",
            '<span class="clause-line"><b>Functional Relations:</b> <span class="g-tok">X_2</span> is the isogonal conjugate of <span class="coincide-tok">X_6</span> (Symmedian point), self-isotomic, and the cyclocevian conjugate of <span class="eq-tok">X_4</span>.</span>',
            "HOMOTHETIC FIXED CENTER",
            "X_2 is the dilation center (scale -1/2 and -2) mapping every center to its complement and anticomplement.",
        ),
    },
    3: {
        "short_title": "CIRCUMCENTER",
        "enunciation": "The intersection of the three perpendicular bisectors of the sides and center of the circumscribed circle of triangle ABC.",
        "partners": [2, 4, 5, 6],
        "script": """[bell:proposition]
X three is the Circumcenter of triangle A B C: <pause> the intersection of the perpendicular bisectors of the three sidelines, <pause> equidistant from vertices A, B, and C by the circumradius R.

[bell:construction]
Its trilinear coordinates are cosine A, to cosine B, to cosine C, <pause> and its barycentric coordinates are sine two A, to sine two B, to sine two C. <pause> On the central lines layer, <pause> X three anchors the Euler line with X two, X four, and X five, <pause> the Brocard axis with X six, X fifteen, and X sixteen, <pause> and the O I line with X one and X forty.

[bell:insight]
X three is the isogonal conjugate and complement of the Orthocenter X four, <pause> and the anticomplement of the Nine-Point Center X five. <pause> Notice across the four reference triangles how X three lies inside an acute triangle, <pause> lands on the hypotenuse midpoint of the three-four-five right triangle, <pause> and moves outside the obtuse Kimberling triangle.
""",
        "s1": (
            "X_3 = Circumcenter • Center of Circumcircle (A B C)",
            '<span class="clause-line"><span class="g-tok">X_3</span> is the <b>Circumcenter</b> of <span class="g-tok">△ABC</span> — the concurrence of the perpendicular bisectors at side midpoints <span class="coincide-tok">M_a, M_b, M_c</span> and center of the <b>circumcircle</b>.</span>',
            "EUCLID IV.5 • CIRCUMCIRCLE",
            "Equidistant from vertices A, B, C with radius R = abc / (4·Area); orthocenter of medial triangle M_a M_b M_c.",
        ),
        "s2": (
            "Trilinears cos A : cos B : cos C • Barycentrics sin 2A : sin 2B : sin 2C",
            '<span class="clause-line"><b>Coordinates of X_3:</b> Perpendicular distances <span class="g-tok">α : β : γ = cos A : cos B : cos C</span> (actual lengths <span class="eq-tok">R cos A, R cos B, R cos C</span>) and sub-areas <span class="coincide-tok">sin 2A : sin 2B : sin 2C</span>.</span>',
            "TRIGONOMETRIC COORDINATES",
            "Algebraic barycentrics: a²(b² + c² - a²) : b²(c² + a² - b²) : c²(a² + b² - c²).",
        ),
        "s3": (
            "Euler Line {2, 3, 4, 5} • Brocard Axis {3, 6, 15, 16}",
            '<span class="clause-line"><b>Incident Central Lines:</b> <span class="g-tok">X_3</span> anchors the <b>Euler line</b> <span class="g-tok">{2, 3, 4, 5}</span>, the <b>Brocard axis</b> <span class="coincide-tok">{3, 6, 15, 16}</span>, and the <b>OI line</b> <span class="eq-tok">{1, 3, 40}</span>.</span>',
            "EULER & BROCARD ANCHOR",
            "Midpoint of X_1 (Incenter) and X_40 (Bevan point); midpoint of X_4 (Orthocenter) and X_20 (de Longchamps).",
        ),
        "s4": (
            "Isogonal Conjugate X_4 • Complement X_5 • Anticomplement X_4",
            '<span class="clause-line"><b>Functional Relations:</b> <span class="g-tok">X_3</span> is both the isogonal conjugate and complement of <span class="coincide-tok">X_4</span> (Orthocenter), and its complement is <span class="eq-tok">X_5</span> (Nine-Point Center).</span>',
            "CIRCUMCENTER–ORTHOCENTER DUALITY",
            "Isotomic conjugate: X_264 • Orthocentroidal-circle inverse: X_5.",
        ),
    },
    4: {
        "short_title": "ORTHOCENTER",
        "enunciation": "The intersection of the three altitudes dropped from vertices A, B, C perpendicular to the opposite sidelines.",
        "partners": [2, 3, 5, 69],
        "script": """[bell:proposition]
X four is the Orthocenter of triangle A B C: <pause> the point of concurrence of the three altitudes A H sub a, B H sub b, and C H sub c, <pause> and the perspector of the orthic triangle H sub a, H sub b, H sub c.

[bell:construction]
Its trilinear coordinates are secant A, to secant B, to secant C, <pause> and its barycentric coordinates are tangent A, to tangent B, to tangent C. <pause> On the central lines layer, <pause> X four lies on the Euler line through X two, X three, and X five, <pause> the Orthocenter–Spieker line through X nine and X ten, <pause> and the Fuhrmann line through X eight.

[bell:insight]
X four is the isogonal conjugate and anticomplement of the Circumcenter X three, <pause> and the isotomic conjugate of the symmedian point of the anticomplementary triangle, X sixty-nine. <pause> On the right three-four-five triangle, <pause> all three altitudes concur directly at the right-angled vertex C.
""",
        "s1": (
            "X_4 = Orthocenter • [A H_a] ∩ [B H_b] ∩ [C H_c]",
            '<span class="clause-line"><span class="g-tok">X_4</span> is the <b>Orthocenter</b> of <span class="g-tok">△ABC</span> — the concurrence of the three altitudes <span class="g-tok">AH_a</span>, <span class="g-tok">BH_b</span>, <span class="g-tok">CH_c</span> and perspector of the <b>orthic triangle</b> <span class="coincide-tok">H_a H_b H_c</span>.</span>',
            "ALTITUDE CONCURRENCE",
            "For acute △ABC, X_4 is also the incenter of its pedal (orthic) triangle △H_a H_b H_c.",
        ),
        "s2": (
            "Trilinears sec A : sec B : sec C • Barycentrics tan A : tan B : tan C",
            '<span class="clause-line"><b>Coordinates of X_4:</b> Trilinear distances <span class="g-tok">α : β : γ = sec A : sec B : sec C</span> and barycentric sub-areas <span class="coincide-tok">u : v : w = tan A : tan B : tan C = 1/S_A : 1/S_B : 1/S_C</span>.</span>',
            "CONWAY NOTATION • 1/S_A : 1/S_B : 1/S_C",
            "Vertices A, B, C and X_4 form an orthocentric system: each point is the orthocenter of the other three.",
        ),
        "s3": (
            "Euler Line {2, 3, 4, 5} • Orthocenter–Spieker Line {4, 9, 10}",
            '<span class="clause-line"><b>Incident Central Lines:</b> <span class="g-tok">X_4</span> lies on the <b>Euler line</b> <span class="g-tok">{2, 3, 4, 5}</span>, the <b>Orthocenter–Spieker line</b> <span class="coincide-tok">{4, 9, 10, 19}</span>, and the <b>Fuhrmann line</b> <span class="eq-tok">{4, 8}</span>.</span>',
            "EULER & ORTHIC AXES",
            "Reflection of X_3 across X_5 on the Euler line; Shinagawa Euler coefficients (0, 1).",
        ),
        "s4": (
            "Isogonal Conjugate X_3 • Complement X_3 • Isotomic X_69",
            '<span class="clause-line"><b>Functional Relations:</b> <span class="g-tok">X_4</span> has isogonal conjugate and complement <span class="coincide-tok">X_3</span> (Circumcenter), isotomic conjugate <span class="eq-tok">X_69</span>, and cyclocevian conjugate <span class="g-tok">X_2</span>.</span>',
            "ISOGONAL & COMPLEMENTARY PAIR",
            "Circumcircle inverse: X_186 • Midpoint of X_3 and X_4: X_5 (Nine-Point Center).",
        ),
    },
    5: {
        "short_title": "NINE-POINT CENTER",
        "enunciation": "The center of the nine-point circle passing through the three side midpoints, three altitude feet, and three Euler midpoints.",
        "partners": [2, 3, 4, 11, 54],
        "script": """[bell:proposition]
X five is the Nine-Point Center: <pause> the center of the remarkable circle of radius R over two that passes through nine classical points of triangle A B C—<pause> the three side midpoints M sub a, M sub b, M sub c, <pause> the three altitude feet H sub a, H sub b, H sub c, <pause> and the three Euler midpoints toward the orthocenter.

[bell:construction]
Its trilinear coordinates are cosine of B minus C, <pause> to cosine of C minus A, <pause> to cosine of A minus B. <pause> On the central lines layer, <pause> X five is the exact midpoint between Circumcenter X three and Orthocenter X four on the Euler line, <pause> and joins Incenter X one on the Feuerbach line through X eleven.

[bell:insight]
Under functional relations, <pause> X five is the complement of the Circumcenter X three, <pause> the isogonal conjugate of the Kosnita point X fifty-four, <pause> and the isotomic conjugate of X ninety-five. <pause> Across all four reference triangles, <pause> the nine-point circle centered at X five remains tangent to the incircle at the Feuerbach point X eleven.
""",
        "s1": (
            "X_5 = Nine-Point Center • Midpoint of X_3 and X_4",
            '<span class="clause-line"><span class="g-tok">X_5</span> is the <b>Nine-Point Center</b> of <span class="g-tok">△ABC</span> — the center of the circle through side midpoints <span class="coincide-tok">M_a, M_b, M_c</span> and altitude feet <span class="eq-tok">H_a, H_b, H_c</span>.</span>',
            "EULER–FEUERBACH NINE-POINT CIRCLE",
            "Circumcenter of both the medial triangle △M_a M_b M_c and the orthic triangle △H_a H_b H_c; radius R / 2.",
        ),
        "s2": (
            "Trilinears cos(B-C) : cos(C-A) : cos(A-B)",
            '<span class="clause-line"><b>Coordinates of X_5:</b> Trilinear distances <span class="g-tok">cos(B - C) : cos(C - A) : cos(A - B)</span> and barycentric areas <span class="coincide-tok">a cos(B - C) : b cos(C - A) : c cos(A - B)</span>.</span>',
            "SHINAGAWA COEFFICIENTS (1, 1)",
            "On the Euler line, X_5 divides X_2–X_4 in ratio 1 : 3 and bisects segment X_3–X_4.",
        ),
        "s3": (
            "Euler Line {2, 3, 4, 5} • Feuerbach Line {1, 5, 11, 12}",
            '<span class="clause-line"><b>Incident Central Lines:</b> <span class="g-tok">X_5</span> lies at the intersection of the <b>Euler line</b> <span class="g-tok">{2, 3, 4, 5}</span>, the <b>Feuerbach line</b> <span class="coincide-tok">{1, 5, 11, 12}</span>, and lines <span class="eq-tok">{5, 13, 18}</span> and <span class="eq-tok">{5, 14, 17}</span>.</span>',
            "EULER & FEUERBACH NEXUS",
            "Distance d(X_1, X_5) = R/2 - r (Feuerbach's theorem: nine-point circle touches the incircle internally).",
        ),
        "s4": (
            "Complement of X_3 • Isogonal Conjugate X_54 (Kosnita)",
            '<span class="clause-line"><b>Functional Relations:</b> <span class="g-tok">X_5</span> is the complement of <span class="coincide-tok">X_3</span>, the midpoint of <span class="g-tok">X_3</span> and <span class="g-tok">X_4</span>, and the isogonal conjugate of <span class="eq-tok">X_54</span> (Kosnita point).</span>',
            "COMPLEMENT & KOSNITA DUALITY",
            "Isotomic conjugate: X_95 • Orthocentroidal-circle inverse of X_3.",
        ),
    },
    6: {
        "short_title": "SYMMEDIAN POINT",
        "enunciation": "The intersection of the three symmedians (reflections of the medians across the angle bisectors) of triangle ABC.",
        "partners": [2, 3, 9, 76],
        "script": """[bell:proposition]
X six is the Symmedian Point—<pause> also known as the Lemoine Point or Grebe Point: <pause> the concurrence of the three symmedians obtained by reflecting each median across its corresponding interior angle bisector, <pause> and the perspector of the tangential triangle.

[bell:construction]
Its trilinear distances are directly proportional to the side lengths, <pause> a, to b, to c, <pause> which makes X six the unique point inside triangle A B C that minimizes the sum of the squares of the perpendicular distances to the three sidelines. <pause> Its barycentric sub-triangle areas are proportional to the squares of the sides, <pause> a squared, to b squared, to c squared. <pause> On the central lines layer, <pause> X six anchors the Brocard axis through X three, X fifteen, and X sixteen.

[bell:insight]
X six is the isogonal conjugate of the Centroid X two, <pause> the isotomic conjugate of the third Brocard point X seventy-six, <pause> and the Gergonne point of the tangential triangle.
""",
        "s1": (
            "X_6 = Symmedian Point • Perspector of Tangential △Tan_a Tan_b Tan_c",
            '<span class="clause-line"><span class="g-tok">X_6</span> is the <b>Symmedian (Lemoine) Point</b> — the concurrence of the three symmedians <span class="g-tok">A–Tan_a</span>, <span class="g-tok">B–Tan_b</span>, <span class="g-tok">C–Tan_c</span> and perspector of the <b>tangential triangle</b>.</span>',
            "LEMOINE–GREBE SYMMEDIAN CONCURRENCE",
            "Reflect each median AM_a across angle bisector AI_a to obtain the symmedian; minimizes α² + β² + γ².",
        ),
        "s2": (
            "Trilinears a : b : c • Barycentrics a² : b² : c²",
            '<span class="clause-line"><b>Coordinates of X_6:</b> Perpendicular distances scale with side lengths <span class="g-tok">α : β : γ = a : b : c</span>, while sub-triangle areas scale with squared sides <span class="coincide-tok">u : v : w = a² : b² : c²</span>.</span>',
            "LEAST SQUARES DISTANCE PROPERTY",
            "On acute triangle (5, 6, 7), perpendicular struts are 5 : 6 : 7 and sub-areas are 25 : 36 : 49 (22.7% : 32.7% : 44.5%).",
        ),
        "s3": (
            "Brocard Axis {3, 6, 15, 16} • Line {1, 6, 9}",
            '<span class="clause-line"><b>Incident Central Lines:</b> <span class="g-tok">X_6</span> anchors the <b>Brocard axis</b> <span class="g-tok">{3, 6, 15, 16}</span>, the <b>Incenter–Symmedian line</b> <span class="coincide-tok">{1, 6, 9}</span>, and lines <span class="eq-tok">{6, 13, 14}</span> and <span class="eq-tok">{6, 17, 18}</span>.</span>',
            "BROCARD AXIS DIAMETER",
            "Segment X_3–X_6 is the diameter of the Brocard (Seven-Point) circle centered at X_182.",
        ),
        "s4": (
            "Isogonal Conjugate X_2 (Centroid) • Isotomic Conjugate X_76",
            '<span class="clause-line"><b>Functional Relations:</b> <span class="g-tok">X_6</span> is the isogonal conjugate of <span class="coincide-tok">X_2</span> (Centroid), the isotomic conjugate of <span class="eq-tok">X_76</span>, and circumcircle inverse of <span class="g-tok">X_187</span>.</span>',
            "CENTROID–SYMMEDIAN ISOGONAL DUALITY",
            "Trilinear inversion maps Centroid (1/a : 1/b : 1/c) directly to Symmedian Point (a : b : c).",
        ),
    },
    7: {
        "short_title": "GERGONNE POINT",
        "enunciation": "The point of concurrence of the three cevians joining vertices A, B, C to the touchpoints of the inscribed circle.",
        "partners": [1, 2, 8, 9, 55],
        "script": """[bell:proposition]
X seven is the Gergonne Point of triangle A B C: <pause> let T sub a, T sub b, and T sub c be the three contact points where the incircle touches sidelines B C, C A, and A B; <pause> the cevians A T sub a, B T sub b, and C T sub c concur at X seven.

[bell:construction]
Its barycentric coordinates are inversely proportional to the semiperimeter excesses, <pause> one over s minus a, <pause> to one over s minus b, <pause> to one over s minus c. <pause> On the central lines layer, <pause> X seven anchors the Soddy line through X one and X twenty, <pause> the Centroid–Gergonne line through X two and X nine, <pause> and the Gergonne–Nagel line through X eight.

[bell:insight]
Under functional relations, <pause> X seven is the isotomic conjugate of the Nagel point X eight, <pause> the anticomplement of the Mittenpunkt X nine, <pause> the isogonal conjugate of the insimilicenter X fifty-five, <pause> and its own cyclocevian conjugate.
""",
        "s1": (
            "X_7 = Gergonne Point • [A T_a] ∩ [B T_b] ∩ [C T_c]",
            '<span class="clause-line"><span class="g-tok">X_7</span> is the <b>Gergonne Point</b> — the concurrence of cevians <span class="g-tok">AT_a</span>, <span class="g-tok">BT_b</span>, <span class="g-tok">CT_c</span> to the incircle touchpoints and perspector of the <b>intouch triangle</b> <span class="coincide-tok">T_a T_b T_c</span>.</span>',
            "CEVA'S THEOREM ON INCIRCLE TANGENTS",
            "Equal tangent lengths from each vertex guarantee (AT_c / T_cB)·(BT_a / T_aC)·(CT_b / T_bA) = 1.",
        ),
        "s2": (
            "Barycentrics 1/(s-a) : 1/(s-b) : 1/(s-c)",
            '<span class="clause-line"><b>Coordinates of X_7:</b> Barycentric sub-areas <span class="coincide-tok">u : v : w = 1/(s - a) : 1/(s - b) : 1/(s - c)</span> and trilinears <span class="g-tok">bc/(s - a) : ca/(s - b) : ab/(s - c)</span>.</span>',
            "SEMIPERIMETER RECIPROCAL COORDINATES",
            "On acute triangle (5, 6, 7) with s = 9, barycentric sub-areas are 1/4 : 1/3 : 1/2 = 3 : 4 : 6.",
        ),
        "s3": (
            "Soddy Line {1, 7, 20} • Line {2, 7, 9} • Line {7, 8}",
            '<span class="clause-line"><b>Incident Central Lines:</b> <span class="g-tok">X_7</span> lies on the <b>Soddy line</b> <span class="g-tok">{1, 7, 20}</span>, the <b>Centroid–Gergonne line</b> <span class="coincide-tok">{2, 7, 9}</span>, and the <b>Gergonne–Nagel line</b> <span class="eq-tok">{7, 8, 65}</span>.</span>',
            "SODDY & MITTENPUNKT COLLINEARITIES",
            "On {2, 7, 9}, Centroid X_2 divides X_7 (Gergonne) and X_9 (Mittenpunkt) in the complement ratio 2 : 1.",
        ),
        "s4": (
            "Isotomic Conjugate X_8 (Nagel) • Complement X_9 (Mittenpunkt)",
            '<span class="clause-line"><b>Functional Relations:</b> <span class="g-tok">X_7</span> is the isotomic conjugate of <span class="coincide-tok">X_8</span> (Nagel point), has complement <span class="eq-tok">X_9</span> (Mittenpunkt), and isogonal conjugate <span class="g-tok">X_55</span>.</span>',
            "GERGONNE–NAGEL ISOTOMIC DUALITY",
            "X_7 is self-cyclocevian conjugate: the Gergonne point of the intouch triangle with respect to ABC.",
        ),
    },
    8: {
        "short_title": "NAGEL POINT",
        "enunciation": "The point of concurrence of the three perimeter-bisecting splitters joining vertices A, B, C to the excircle touchpoints.",
        "partners": [1, 2, 7, 10, 56],
        "script": """[bell:proposition]
X eight is the Nagel Point of triangle A B C: <pause> let N sub a, N sub b, and N sub c be the points where the three excircles touch sidelines B C, C A, and A B; <pause> the perimeter-bisecting cevians A N sub a, B N sub b, and C N sub c concur at X eight.

[bell:construction]
Its barycentric coordinates are directly proportional to the semiperimeter excesses, <pause> s minus a, to s minus b, to s minus c, <pause> and its trilinears are s minus a over a, <pause> to s minus b over b, <pause> to s minus c over c. <pause> On the central lines layer, <pause> X eight anchors the Nagel line with X one, X two, and X ten, <pause> the Fuhrmann line with X four, <pause> and the Gergonne–Nagel line with X seven.

[bell:insight]
X eight is the isotomic conjugate of the Gergonne point X seven, <pause> the anticomplement of the Incenter X one, <pause> and the reflection of X one across the Spieker center X ten.
""",
        "s1": (
            "X_8 = Nagel Point • [A N_a] ∩ [B N_b] ∩ [C N_c]",
            '<span class="clause-line"><span class="g-tok">X_8</span> is the <b>Nagel Point</b> — the concurrence of the perimeter-bisecting splitters <span class="g-tok">AN_a</span>, <span class="g-tok">BN_b</span>, <span class="g-tok">CN_c</span> and perspector of the <b>extouch triangle</b> <span class="coincide-tok">N_a N_b N_c</span>.</span>',
            "PERIMETER SPLITTER CONCURRENCE",
            "Each cevian AN_a bisects the triangle's perimeter into two equal paths of length s = (a + b + c)/2.",
        ),
        "s2": (
            "Trilinears (s-a)/a : (s-b)/b : (s-c)/c • Barycentrics s-a : s-b : s-c",
            '<span class="clause-line"><b>Coordinates of X_8:</b> Barycentric sub-areas <span class="coincide-tok">u : v : w = (s - a) : (s - b) : (s - c)</span> and trilinear distances <span class="g-tok">(s - a)/a : (s - b)/b : (s - c)/c</span>.</span>',
            "SEMIPERIMETER EXCESS COORDINATES",
            "On acute triangle (5, 6, 7) with s = 9, barycentric sub-areas are 4 : 3 : 2 (44.4% : 33.3% : 22.2%).",
        ),
        "s3": (
            "Nagel Line {1, 2, 8, 10} • Fuhrmann Line {4, 8} • Line {7, 8}",
            '<span class="clause-line"><b>Incident Central Lines:</b> <span class="g-tok">X_8</span> anchors the <b>Nagel line</b> <span class="g-tok">{1, 2, 8, 10}</span>, the <b>Fuhrmann line</b> <span class="coincide-tok">{4, 8, 72}</span>, and the <b>Gergonne–Nagel line</b> <span class="eq-tok">{7, 8, 65}</span>.</span>',
            "NAGEL & FUHRMANN AXES",
            "Segment X_4–X_8 is the diameter of the Fuhrmann circle; on the Nagel line, X_1 X_2 : X_2 X_8 = 1 : 2.",
        ),
        "s4": (
            "Anticomplement of X_1 • Isotomic Conjugate X_7 • Isogonal X_56",
            '<span class="clause-line"><b>Functional Relations:</b> <span class="g-tok">X_8</span> is the anticomplement of <span class="g-tok">X_1</span> (Incenter), the isotomic conjugate of <span class="coincide-tok">X_7</span> (Gergonne point), and isogonal conjugate of <span class="eq-tok">X_56</span>.</span>',
            "ANTICOMPLEMENTARY INCENTER",
            "X_8 is the incenter of the anticomplementary triangle △K_a K_b K_c; midpoint of X_1 and X_8 is X_10.",
        ),
    },
    9: {
        "short_title": "MITTENPUNKT",
        "enunciation": "The symmedian point of the excentral triangle, where lines joining the three excenters to the side midpoints concur.",
        "partners": [1, 2, 6, 7, 57],
        "script": """[bell:proposition]
Introduced by Christian Heinrich von Nagel in eighteen thirty-six, <pause> X nine is the Mittenpunkt—<pause> literally the middle point: <pause> the concurrence of the three lines joining the excenters J sub a, J sub b, and J sub c to the corresponding side midpoints M sub a, M sub b, and M sub c.

[bell:construction]
Geometrically, <pause> X nine is the symmedian point of the excentral triangle. <pause> Its trilinear distances are proportional to the semiperimeter excesses, <pause> s minus a, to s minus b, to s minus c, <pause> and its barycentric areas are a times s minus a, <pause> to b times s minus b, <pause> to c times s minus c. <pause> On the central lines layer, <pause> X nine lies at the intersection of line X one X six, <pause> line X two X seven, <pause> and the Orthocenter–Spieker line X four X ten.

[bell:insight]
Under functional relations, <pause> X nine is the complement of the Gergonne point X seven, <pause> the isogonal conjugate of X fifty-seven, <pause> and the isotomic conjugate of X eighty-five.
""",
        "s1": (
            "X_9 = Mittenpunkt • [J_a M_a] ∩ [J_b M_b] ∩ [J_c M_c]",
            '<span class="clause-line"><span class="g-tok">X_9</span> is the <b>Mittenpunkt</b> — the concurrence of lines joining the excenters <span class="g-tok">J_a, J_b, J_c</span> to the side midpoints <span class="coincide-tok">M_a, M_b, M_c</span>.</span>',
            "SYMMEDIAN OF THE EXCENTRAL TRIANGLE",
            "Perspector of the excentral triangle △J_a J_b J_c and the medial triangle △M_a M_b M_c.",
        ),
        "s2": (
            "Trilinears (s-a) : (s-b) : (s-c) • Barycentrics a(s-a) : b(s-b) : c(s-c)",
            '<span class="clause-line"><b>Coordinates of X_9:</b> Perpendicular distances <span class="g-tok">α : β : γ = (b+c-a) : (c+a-b) : (a+b-c)</span> and barycentric areas <span class="coincide-tok">a(s-a) : b(s-b) : c(s-c)</span>.</span>',
            "TRILINEAR–BARYCENTRIC BRIDGE",
            "Notice that X_9's trilinears (s-a : s-b : s-c) equal X_8's barycentrics! On (5, 6, 7), barycentrics are 10 : 9 : 7.",
        ),
        "s3": (
            "Line {1, 6, 9} • Line {2, 7, 9} • Line {4, 9, 10}",
            '<span class="clause-line"><b>Incident Central Lines:</b> <span class="g-tok">X_9</span> is the triple intersection of the <b>Incenter–Symmedian line</b> <span class="g-tok">{1, 6, 9}</span>, the <b>Centroid–Gergonne line</b> <span class="coincide-tok">{2, 7, 9}</span>, and <span class="eq-tok">{4, 9, 10}</span>.</span>',
            "TRIPLE CLASSICAL INTERSECTION",
            "Constructible directly as the intersection of line X_1–X_6 and line X_2–X_7.",
        ),
        "s4": (
            "Complement of X_7 (Gergonne) • Isogonal X_57 • Isotomic X_85",
            '<span class="clause-line"><b>Functional Relations:</b> <span class="g-tok">X_9</span> is the complement of <span class="coincide-tok">X_7</span> (Gergonne point), the isogonal conjugate of <span class="eq-tok">X_57</span>, and isotomic conjugate of <span class="g-tok">X_85</span>.</span>',
            "MEDIAL GERGONNE POINT",
            "As the complement of X_7, X_9 is the Gergonne point of the medial triangle △M_a M_b M_c.",
        ),
    },
    10: {
        "short_title": "SPIEKER CENTER",
        "enunciation": "The incenter of the medial triangle M_a M_b M_c and center of mass of the uniform perimeter wireframe of triangle ABC.",
        "partners": [1, 2, 8, 4, 9, 58],
        "script": """[bell:proposition]
X ten is the Spieker Center of triangle A B C: <pause> the incenter of the medial triangle M sub a, M sub b, M sub c, <pause> the center of the inscribed Spieker circle, <pause> and the physical center of mass of the triangle's uniform wire perimeter.

[bell:construction]
Its barycentric coordinates are simply b plus c, <pause> to c plus a, <pause> to a plus b, <pause> and its trilinear coordinates are b c times b plus c, <pause> to c a times c plus a, <pause> to a b times a plus b. <pause> On the central lines layer, <pause> X ten lies on the Nagel line as the exact midpoint between Incenter X one and Nagel point X eight, <pause> and on the Orthocenter–Mittenpunkt line through X four and X nine.

[bell:insight]
X ten is the complement of the Incenter X one, <pause> the radical center of the three excircles, <pause> the isogonal conjugate of X fifty-eight, <pause> and the isotomic conjugate of X eighty-six.
""",
        "s1": (
            "X_10 = Spieker Center • Incenter of Medial △M_a M_b M_c",
            '<span class="clause-line"><span class="g-tok">X_10</span> is the <b>Spieker Center</b> — the concurrence of the interior angle bisectors of the <b>medial triangle</b> <span class="coincide-tok">M_a M_b M_c</span> and center of the <b>Spieker circle</b>.</span>',
            "PERIMETER CENTER OF MASS",
            "Center of gravity of the three wire sidelines BC, CA, AB; radical center of the three excircles.",
        ),
        "s2": (
            "Trilinears bc(b+c) : ca(c+a) : ab(a+b) • Barycentrics b+c : c+a : a+b",
            '<span class="clause-line"><b>Coordinates of X_10:</b> Barycentric sub-areas <span class="coincide-tok">u : v : w = (b + c) : (c + a) : (a + b)</span> and trilinear distances <span class="g-tok">bc(b+c) : ca(c+a) : ab(a+b)</span>.</span>',
            "PAIRWISE SIDE-SUM BARYCENTRICS",
            "On acute triangle (5, 6, 7), barycentric sub-areas are 13 : 12 : 11 (36.1% : 33.3% : 30.6%).",
        ),
        "s3": (
            "Nagel Line {1, 2, 8, 10} • Line {4, 9, 10, 19}",
            '<span class="clause-line"><b>Incident Central Lines:</b> <span class="g-tok">X_10</span> lies on the <b>Nagel line</b> <span class="g-tok">{1, 2, 8, 10}</span> as the midpoint of <span class="coincide-tok">X_1–X_8</span>, and on the <b>Orthocenter–Spieker line</b> <span class="eq-tok">{4, 9, 10, 19}</span>.</span>',
            "MIDPOINT OF INCENTER & NAGEL POINT",
            "Four classical centers X_1, X_2, X_10, X_8 lie on the Nagel line in harmonic/homothetic progression.",
        ),
        "s4": (
            "Complement of X_1 (Incenter) • Midpoint of X_1 & X_8 • Isogonal X_58",
            '<span class="clause-line"><b>Functional Relations:</b> <span class="g-tok">X_10</span> is the complement of <span class="g-tok">X_1</span> (Incenter), the midpoint of <span class="coincide-tok">X_1</span> and <span class="coincide-tok">X_8</span>, and isogonal conjugate of <span class="eq-tok">X_58</span>.</span>',
            "MEDIAL HOMOTHETY OF X_1",
            "Spieker circle radius is exactly r / 2 (half the inradius of △ABC); isotomic conjugate: X_86.",
        ),
    },
    11: {
        "short_title": "FEUERBACH POINT",
        "enunciation": "The unique point of internal tangency between the inscribed circle and the nine-point circle of triangle ABC.",
        "partners": [1, 5, 12, 59],
        "script": """[bell:proposition]
Discovered by Karl Wilhelm Feuerbach in eighteen twenty-two, <pause> X eleven is the Feuerbach Point: <pause> the celebrated point where the incircle centered at X one and the nine-point circle centered at X five kiss in internal tangency.

[bell:construction]
Its trilinear coordinates are one minus cosine of B minus C, <pause> to one minus cosine of C minus A, <pause> to one minus cosine of A minus B, <pause> with algebraic barycentrics s minus a times b minus c squared. <pause> Because the point of tangency of two circles always lies on their line of centers, <pause> X eleven lies directly on the Feuerbach line through X one, X five, and X twelve.

[bell:insight]
X eleven is the harmonic conjugate of X twelve with respect to X one and X five, <pause> the isogonal conjugate of X fifty-nine, <pause> and lies on the circumcircle of the intouch triangle and the pedal circle of the Spieker center.
""",
        "s1": (
            "X_11 = Feuerbach Point • Incircle  tangent to Nine-Point Circle",
            '<span class="clause-line"><span class="g-tok">X_11</span> is the <b>Feuerbach Point</b> — the exact point of internal tangency between the <b>incircle</b> (center <span class="g-tok">X_1</span>) and the <b>nine-point circle</b> (center <span class="coincide-tok">X_5</span>).</span>',
            "FEUERBACH'S THEOREM (1822)",
            "The nine-point circle is tangent to the incircle at X_11 and externally tangent to all three excircles.",
        ),
        "s2": (
            "Trilinears 1-cos(B-C) : : • Barycentrics (s-a)(b-c)² : :",
            '<span class="clause-line"><b>Coordinates of X_11:</b> Trilinear distances <span class="g-tok">1 - cos(B - C) : 1 - cos(C - A) : 1 - cos(A - B)</span> and barycentrics <span class="coincide-tok">(s - a)(b - c)² : (s - b)(c - a)² : (s - c)(a - b)²</span>.</span>',
            "TANGENCY COORDINATE SIGNATURE",
            "On acute triangle (5, 6, 7), barycentric sub-areas are 4(1)² : 3(2)² : 2(1)² = 2 : 6 : 1.",
        ),
        "s3": (
            "Feuerbach Line {1, 5, 11, 12} • Line {2, 11, 55} • Line {4, 11, 56}",
            '<span class="clause-line"><b>Incident Central Lines:</b> <span class="g-tok">X_11</span> lies on the <b>Feuerbach line</b> <span class="g-tok">{1, 5, 11, 12}</span>, line <span class="coincide-tok">{2, 11, 55}</span>, and line <span class="eq-tok">{4, 11, 56}</span>.</span>',
            "LINE OF CENTERS X_1–X_5",
            "Collinear with Incenter X_1 and Nine-Point Center X_5 since d(X_1, X_5) = R/2 - r.",
        ),
        "s4": (
            "{X_1, X_5}-Harmonic Conjugate X_12 • Isogonal X_59 • Complement X_100",
            '<span class="clause-line"><b>Functional Relations:</b> <span class="g-tok">X_11</span> and <span class="coincide-tok">X_12</span> divide <span class="g-tok">X_1–X_5</span> harmonically; <span class="g-tok">X_11</span> has isogonal conjugate <span class="eq-tok">X_59</span> and complement <span class="coincide-tok">X_100</span>.</span>',
            "HARMONIC DIVISION ON FEUERBACH LINE",
            "X_100 (anticomplement of X_11) lies on the circumcircle of △ABC.",
        ),
    },
    12: {
        "short_title": "{X_1, X_5}-HARMONIC CONJUGATE OF X_11",
        "enunciation": "The perspector of triangle ABC and the Feuerbach triangle formed by the three excircle touchpoints on the nine-point circle.",
        "partners": [1, 5, 11, 55, 56],
        "script": """[bell:proposition]
X twelve is the X one, X five harmonic conjugate of the Feuerbach point X eleven: <pause> while the nine-point circle touches the incircle at X eleven, <pause> it also touches the three excircles at three outer Feuerbach points, <pause> and the lines from A, B, and C to those three touchpoints concur at X twelve.

[bell:construction]
Its trilinear coordinates flip the minus sign of X eleven to a plus: <pause> one plus cosine of B minus C, <pause> to one plus cosine of C minus A, <pause> to one plus cosine of A minus B, <pause> with barycentrics b plus c squared over s minus a. <pause> On the central lines layer, <pause> X twelve lies on the Feuerbach line through X one, X five, and X eleven, <pause> and on lines X two X fifty-six and X four X fifty-five.

[bell:insight]
Together, <pause> X one, X five, X eleven, and X twelve form a fundamental harmonic range on the Feuerbach line, <pause> linking the incircle, nine-point circle, and three excircles.
""",
        "s1": (
            "X_12 = Perspector of Feuerbach Excircle-Touch Triangle",
            '<span class="clause-line"><span class="g-tok">X_12</span> is the <b>{X_1, X_5}-Harmonic Conjugate of X_11</b> — the perspector of <span class="g-tok">△ABC</span> and the triangle of touchpoints where the <b>nine-point circle</b> meets the three excircles.</span>',
            "FEUERBACH EXCIRCLE TANGENCY",
            "Internal center of similitude of the incircle (center X_1, radius r) and nine-point circle (center X_5, radius R/2).",
        ),
        "s2": (
            "Trilinears 1+cos(B-C) : : • Barycentrics (b+c)²/(s-a) : :",
            '<span class="clause-line"><b>Coordinates of X_12:</b> Trilinear distances <span class="g-tok">1 + cos(B - C) : 1 + cos(C - A) : 1 + cos(A - B)</span> and barycentrics <span class="coincide-tok">(b + c)²/(s - a) : (c + a)²/(s - b) : (a + b)²/(s - c)</span>.</span>',
            "PLUS-COSINE FEUERBACH PAIR",
            "On acute triangle (5, 6, 7), barycentric sub-areas are 169/4 : 144/3 : 121/2 = 507 : 576 : 726.",
        ),
        "s3": (
            "Feuerbach Line {1, 5, 11, 12} • Line {2, 12, 56} • Line {4, 12, 55}",
            '<span class="clause-line"><b>Incident Central Lines:</b> <span class="g-tok">X_12</span> lies on the <b>Feuerbach line</b> <span class="g-tok">{1, 5, 11, 12}</span>, line <span class="coincide-tok">{2, 12, 56}</span>, and line <span class="eq-tok">{4, 12, 55}</span>.</span>',
            "SIMILICENTER INCIDENCE",
            "Notice the symmetric swap with X_11: X_11 lies on {2, 55} and {4, 56}, while X_12 lies on {2, 56} and {4, 55}.",
        ),
        "s4": (
            "Harmonic Quadruple (X_1, X_5; X_11, X_12)",
            '<span class="clause-line"><b>Functional Relations:</b> <span class="g-tok">X_11</span> (external similicenter) and <span class="g-tok">X_12</span> (internal similicenter) divide <span class="coincide-tok">X_1</span> and <span class="eq-tok">X_5</span> in ratio <span class="eq-tok">2r : R</span>.</span>',
            "HARMONIC RANGE ON LINE {1, 5}",
            "Isotomic conjugate of the isogonal conjugate of X_181 (Apollonius point).",
        ),
    },
    13: {
        "short_title": "1st ISOGONIC CENTER (FERMAT POINT)",
        "enunciation": "The perspector of the outward equilateral triangles erected on sides BC, CA, AB, minimizing PA + PB + PC when all angles < 120°.",
        "partners": [15, 14, 2, 6, 17],
        "script": """[bell:proposition]
Posed by Pierre de Fermat to Evangelista Torricelli, <pause> X thirteen is the First Isogonic Center, <pause> or Fermat Point: <pause> erect outward equilateral triangles on sides B C, C A, and A B, <pause> join their outer apexes to the opposite vertices A, B, and C, <pause> and those three segments of equal length concur at X thirteen.

[bell:construction]
At X thirteen, <pause> each side of triangle A B C subtends an equal angle of one hundred twenty degrees, <pause> minimizing the sum of distances P A plus P B plus P C whenever every angle of A B C is less than one hundred twenty degrees. <pause> Its trilinear coordinates are cosecant of A plus pi over three, <pause> to cosecant of B plus pi over three, <pause> to cosecant of C plus pi over three.

[bell:insight]
X thirteen is the isogonal conjugate of the First Isodynamic Point X fifteen, <pause> the orthocentroidal-circle inverse of the Second Isogonic Center X fourteen, <pause> and collinear with X three and the First Napoleon Point X seventeen.
""",
        "s1": (
            "X_13 = 1st Isogonic (Fermat) Center • [A A'] ∩ [B B'] ∩ [C C']",
            '<span class="clause-line"><span class="g-tok">X_13</span> is the <b>1st Isogonic (Fermat–Torricelli) Center</b> — the concurrence of lines joining <span class="g-tok">A, B, C</span> to the apexes of <b>outward equilateral triangles</b> on <span class="coincide-tok">BC, CA, AB</span>.</span>',
            "FERMAT–TORRICELLI MINIMUM STEINER TREE",
            "Segments AA', BB', CC' have equal length and meet at 60° angles; ∠BX_13C = ∠CX_13A = ∠AX_13B = 120°.",
        ),
        "s2": (
            "Trilinears csc(A + π/3) : csc(B + π/3) : csc(C + π/3)",
            '<span class="clause-line"><b>Coordinates of X_13:</b> Trilinear distances <span class="g-tok">csc(A + π/3) : csc(B + π/3) : csc(C + π/3)</span> and barycentrics <span class="coincide-tok">a csc(A + π/3) : b csc(B + π/3) : c csc(C + π/3)</span>.</span>',
            "60° PHASE-SHIFTED COSECANT LAW",
            "Equivalently in Conway notation: barycentrics 1/(S_A + √3·Area) : 1/(S_B + √3·Area) : 1/(S_C + √3·Area).",
        ),
        "s3": (
            "Lines {2, 13, 16} • {3, 13, 17} • {5, 13, 18} • {6, 13, 14}",
            '<span class="clause-line"><b>Incident Central Lines:</b> <span class="g-tok">X_13</span> lies on <span class="g-tok">{6, 13, 14}</span> with the Symmedian point, <span class="coincide-tok">{3, 13, 17}</span> with the 1st Napoleon point, and <span class="eq-tok">{2, 13, 16}</span>.</span>',
            "KIEPERT HYPERBOLA VERTEX",
            "X_13 and X_14 are the +/-60° points on the Kiepert hyperbola through A, B, C, X_2, X_4.",
        ),
        "s4": (
            "Isogonal Conjugate X_15 (1st Isodynamic) • Inverse X_14",
            '<span class="clause-line"><b>Functional Relations:</b> <span class="g-tok">X_13</span> is the isogonal conjugate of <span class="coincide-tok">X_15</span> (1st Isodynamic point) and the orthocentroidal-circle inverse of <span class="eq-tok">X_14</span>.</span>',
            "ISOGONIC–ISODYNAMIC DUALITY",
            "Reflection of X_14 across X_115 (center of the Kiepert hyperbola); isotomic conjugate: X_298.",
        ),
    },
    14: {
        "short_title": "2nd ISOGONIC CENTER",
        "enunciation": "The perspector of the inward equilateral triangles erected on sides BC, CA, AB of triangle ABC.",
        "partners": [16, 13, 2, 6, 18],
        "script": """[bell:proposition]
X fourteen is the Second Isogonic Center of triangle A B C: <pause> erect equilateral triangles inward across sides B C, C A, and A B, <pause> join their apexes to the opposite vertices A, B, and C, <pause> and those three lines concur at X fourteen.

[bell:construction]
Its trilinear coordinates replace plus pi over three with minus pi over three: <pause> cosecant of A minus pi over three, <pause> to cosecant of B minus pi over three, <pause> to cosecant of C minus pi over three. <pause> On the central lines layer, <pause> X fourteen joins X thirteen and the Symmedian point X six on line six, thirteen, fourteen, <pause> and joins X two and X fifteen, <pause> as well as X three and X eighteen.

[bell:insight]
Under functional relations, <pause> X fourteen is the isogonal conjugate of the Second Isodynamic Point X sixteen, <pause> the orthocentroidal-circle inverse of X thirteen, <pause> and the reflection of X thirteen across the Kiepert center X one hundred fifteen.
""",
        "s1": (
            "X_14 = 2nd Isogonic Center • Inward Equilateral Perspector",
            '<span class="clause-line"><span class="g-tok">X_14</span> is the <b>2nd Isogonic Center</b> — the concurrence of lines joining <span class="g-tok">A, B, C</span> to the apexes of <b>inward equilateral triangles</b> on <span class="coincide-tok">BC, CA, AB</span>.</span>',
            "INWARD EQUILATERAL PERSPECTIVITY",
            "Companion to Fermat point X_13; lies outside △ABC unless an angle of △ABC equals 60°.",
        ),
        "s2": (
            "Trilinears csc(A - π/3) : csc(B - π/3) : csc(C - π/3)",
            '<span class="clause-line"><b>Coordinates of X_14:</b> Trilinear distances <span class="g-tok">csc(A - π/3) : csc(B - π/3) : csc(C - π/3)</span> and barycentrics <span class="coincide-tok">1/(S_A - √3·Area) : 1/(S_B - √3·Area) : 1/(S_C - √3·Area)</span>.</span>',
            "-60° KIEPERT SIGNATURE",
            "Because A < 60° on the (5, 6, 7) acute triangle, sin(A - π/3) < 0 and X_14 lies across sideline BC.",
        ),
        "s3": (
            "Lines {6, 13, 14} • {2, 14, 15} • {3, 14, 18} • {5, 14, 17}",
            '<span class="clause-line"><b>Incident Central Lines:</b> <span class="g-tok">X_14</span> lies on <span class="g-tok">{6, 13, 14}</span>, <span class="coincide-tok">{2, 14, 15}</span>, <span class="eq-tok">{3, 14, 18}</span>, and <span class="eq-tok">{5, 14, 17}</span>.</span>',
            "DUAL ISOGONIC INCIDENCES",
            "Every incidence of X_14 mirrors X_13 under the swap (13 ↔ 14, 15 ↔ 16, 17 ↔ 18).",
        ),
        "s4": (
            "Isogonal Conjugate X_16 (2nd Isodynamic) • Inverse X_13",
            '<span class="clause-line"><b>Functional Relations:</b> <span class="g-tok">X_14</span> is the isogonal conjugate of <span class="coincide-tok">X_16</span> (2nd Isodynamic point) and the reflection of <span class="eq-tok">X_13</span> in <span class="g-tok">X_115</span>.</span>',
            "KIEPERT DIAMETER ENDPOINT",
            "Segment X_13–X_14 is a diameter of the Lester circle; isotomic conjugate: X_299.",
        ),
    },
    15: {
        "short_title": "1st ISODYNAMIC POINT",
        "enunciation": "The internal common intersection of the three Apollonian circles of triangle ABC, whose pedal triangle is equilateral.",
        "partners": [13, 16, 3, 6, 2],
        "script": """[bell:proposition]
X fifteen is the First Isodynamic Point of triangle A B C: <pause> construct the three Apollonian circles passing through each vertex and the interior and exterior angle bisector feet on the opposite side, <pause> and all three circles intersect inside the circumcircle at X fifteen.

[bell:construction]
Its trilinear coordinates are sine of A plus pi over three, <pause> to sine of B plus pi over three, <pause> to sine of C plus pi over three—<pause> the exact reciprocals of the Fermat point X thirteen. <pause> Remarkably, <pause> the pedal triangle of X fifteen is always equilateral! <pause> On the central lines layer, <pause> X fifteen lies on the Brocard axis through X three, X six, and X sixteen.

[bell:insight]
X fifteen is the isogonal conjugate of the Fermat point X thirteen, <pause> and the circumcircle inverse of the Second Isodynamic Point X sixteen.
""",
        "s1": (
            "X_15 = 1st Isodynamic Point • Intersection of Apollonian Circles",
            '<span class="clause-line"><span class="g-tok">X_15</span> is the <b>1st Isodynamic Point</b> — the internal common intersection of the three <b>Apollonian circles</b> of <span class="g-tok">△ABC</span> on the <b>Brocard axis</b>.</span>',
            "EQUILATERAL PEDAL TRIANGLE",
            "Distances from X_15 to vertices A, B, C are inversely proportional to opposite sides: a·X_15A = b·X_15B = c·X_15C.",
        ),
        "s2": (
            "Trilinears sin(A + π/3) : : • Barycentrics a sin(A + π/3) : :",
            '<span class="clause-line"><b>Coordinates of X_15:</b> Trilinear distances <span class="g-tok">sin(A + π/3) : sin(B + π/3) : sin(C + π/3)</span> and barycentric areas <span class="coincide-tok">a sin(A + π/3) : b sin(B + π/3) : c sin(C + π/3)</span>.</span>',
            "RECIPROCAL FERMAT TRILINEARS",
            "Conway barycentrics: a²(S_A + √3·Area) : b²(S_B + √3·Area) : c²(S_C + √3·Area).",
        ),
        "s3": (
            "Brocard Axis {3, 6, 15, 16} • Line {2, 14, 15} • Line {4, 15, 17}",
            '<span class="clause-line"><b>Incident Central Lines:</b> <span class="g-tok">X_15</span> lies on the <b>Brocard axis</b> <span class="g-tok">{3, 6, 15, 16}</span>, line <span class="coincide-tok">{2, 14, 15}</span>, and line <span class="eq-tok">{4, 15, 17}</span>.</span>',
            "BROCARD AXIS & APOLLONIAN CHORD",
            "The Brocard axis {3, 6} is the common radical axis (line of centers' perpendicular) of the Apollonian circles.",
        ),
        "s4": (
            "Isogonal Conjugate X_13 (Fermat) • Circumcircle Inverse X_16",
            '<span class="clause-line"><b>Functional Relations:</b> <span class="g-tok">X_15</span> is the isogonal conjugate of <span class="coincide-tok">X_13</span> (Fermat point) and the circumcircle inverse of <span class="eq-tok">X_16</span> (2nd Isodynamic point).</span>',
            "CIRCUMCIRCLE INVERSION PAIR",
            "X_3, X_15, X_6, X_16 form a harmonic range on the Brocard axis; isotomic conjugate: X_300.",
        ),
    },
    16: {
        "short_title": "2nd ISODYNAMIC POINT",
        "enunciation": "The external common intersection of the three Apollonian circles of triangle ABC and isogonal conjugate of X_14.",
        "partners": [14, 15, 3, 6, 2],
        "script": """[bell:proposition]
X sixteen is the Second Isodynamic Point of triangle A B C: <pause> the second common intersection of the three Apollonian circles, <pause> lying outside the circumcircle on the Brocard axis.

[bell:construction]
Its trilinear coordinates are sine of A minus pi over three, <pause> to sine of B minus pi over three, <pause> to sine of C minus pi over three, <pause> and like X fifteen, <pause> its pedal triangle with respect to A B C is strictly equilateral. <pause> On the central lines layer, <pause> X sixteen lies on the Brocard axis through X three, X six, and X fifteen, <pause> and on lines X two X thirteen and X four X eighteen.

[bell:insight]
X sixteen is the isogonal conjugate of the Second Isogonic Center X fourteen, <pause> and the inverse of the First Isodynamic Point X fifteen in the circumcircle of triangle A B C.
""",
        "s1": (
            "X_16 = 2nd Isodynamic Point • External Apollonian Intersection",
            '<span class="clause-line"><span class="g-tok">X_16</span> is the <b>2nd Isodynamic Point</b> — the external intersection of the three <b>Apollonian circles</b> and circumcircle inverse of <span class="coincide-tok">X_15</span> on the <b>Brocard axis</b>.</span>',
            "SECOND EQUILATERAL PEDAL LOCUS",
            "X_15 and X_16 are the only two points in the plane whose pedal triangles with respect to △ABC are equilateral.",
        ),
        "s2": (
            "Trilinears sin(A - π/3) : : • Barycentrics a sin(A - π/3) : :",
            '<span class="clause-line"><b>Coordinates of X_16:</b> Trilinear distances <span class="g-tok">sin(A - π/3) : sin(B - π/3) : sin(C - π/3)</span> and barycentrics <span class="coincide-tok">a sin(A - π/3) : b sin(B - π/3) : c sin(C - π/3)</span>.</span>',
            "-60° ISODYNAMIC COORDINATES",
            "Conway barycentrics: a²(S_A - √3·Area) : b²(S_B - √3·Area) : c²(S_C - √3·Area).",
        ),
        "s3": (
            "Brocard Axis {3, 6, 15, 16} • Line {2, 13, 16} • Line {4, 16, 18}",
            '<span class="clause-line"><b>Incident Central Lines:</b> <span class="g-tok">X_16</span> lies on the <b>Brocard axis</b> <span class="g-tok">{3, 6, 15, 16}</span>, line <span class="coincide-tok">{2, 13, 16}</span>, and line <span class="eq-tok">{4, 16, 18}</span>.</span>',
            "BROCARD HARMONIC QUADRUPLE",
            "On the Brocard axis, (X_3, X_6; X_15, X_16) is a harmonic range and X_3·X_15 · X_3·X_16 = R².",
        ),
        "s4": (
            "Isogonal Conjugate X_14 • Circumcircle Inverse X_15",
            '<span class="clause-line"><b>Functional Relations:</b> <span class="g-tok">X_16</span> is the isogonal conjugate of <span class="coincide-tok">X_14</span> (2nd Isogonic center) and the circumcircle inverse of <span class="eq-tok">X_15</span>.</span>',
            "INVERSION IN THE CIRCUMCIRCLE",
            "Midpoint of X_15 and X_16 is X_187 (circumcircle inverse of X_6); isotomic conjugate: X_301.",
        ),
    },
    17: {
        "short_title": "1st NAPOLEON POINT",
        "enunciation": "The perspector of triangle ABC and the outer Napoleon equilateral triangle formed by the centers of outward side equilateral triangles.",
        "partners": [13, 18, 3, 4, 15, 61],
        "script": """[bell:proposition]
X seventeen is the First Napoleon Point of triangle A B C: <pause> by Napoleon's theorem, <pause> the centroids Nap sub a, Nap sub b, and Nap sub c of the three outward equilateral triangles erected on sides B C, C A, and A B always form an equilateral triangle, <pause> and the lines joining A, B, and C to those three centers concur at X seventeen.

[bell:construction]
Its trilinear coordinates shift the phase to pi over six: <pause> cosecant of A plus pi over six, <pause> to cosecant of B plus pi over six, <pause> to cosecant of C plus pi over six. <pause> On the central lines layer, <pause> X seventeen lies on line X three X thirteen, <pause> line X four X fifteen, <pause> line X five X fourteen, <pause> and line X six X eighteen.

[bell:insight]
X seventeen lies on the Kiepert hyperbola at angle plus thirty degrees, <pause> is the isogonal conjugate of X sixty-one, <pause> and pairs with the Second Napoleon Point X eighteen.
""",
        "s1": (
            "X_17 = 1st Napoleon Point • [A Nap_a] ∩ [B Nap_b] ∩ [C Nap_c]",
            '<span class="clause-line"><span class="g-tok">X_17</span> is the <b>1st Napoleon Point</b> — the perspector of <span class="g-tok">△ABC</span> and the equilateral <b>outer Napoleon triangle</b> <span class="coincide-tok">Nap_a Nap_b Nap_c</span>.</span>',
            "NAPOLEON'S THEOREM • OUTER TRIANGLE",
            "Nap_a, Nap_b, Nap_c are the centroids (30° base angles) of outward equilateral triangles on BC, CA, AB.",
        ),
        "s2": (
            "Trilinears csc(A + π/6) : : • Barycentrics a csc(A + π/6) : :",
            '<span class="clause-line"><b>Coordinates of X_17:</b> Trilinear distances <span class="g-tok">csc(A + π/6) : csc(B + π/6) : csc(C + π/6)</span> and barycentrics <span class="coincide-tok">1/(√3·S_A + Area) : 1/(√3·S_B + Area) : 1/(√3·S_C + Area)</span>.</span>',
            "+30° KIEPERT PERSPECTOR",
            "Point on the Kiepert hyperbola corresponding to base angle θ = +π/6 (30°).",
        ),
        "s3": (
            "Lines {3, 13, 17} • {4, 15, 17} • {5, 14, 17} • {6, 17, 18}",
            '<span class="clause-line"><b>Incident Central Lines:</b> <span class="g-tok">X_17</span> lies at the intersection of <span class="g-tok">{3, 13, 17}</span>, <span class="coincide-tok">{4, 15, 17}</span>, <span class="eq-tok">{5, 14, 17}</span>, and <span class="eq-tok">{6, 17, 18}</span>.</span>',
            "FERMAT–NAPOLEON–ISODYNAMIC GRID",
            "Notice how X_17 connects Circumcenter X_3 to Fermat point X_13 and Orthocenter X_4 to 1st Isodynamic X_15.",
        ),
        "s4": (
            "Isogonal Conjugate X_61 • Isotomic Conjugate X_302",
            '<span class="clause-line"><b>Functional Relations:</b> <span class="g-tok">X_17</span> is the isogonal conjugate of <span class="coincide-tok">X_61</span>, the isotomic conjugate of <span class="eq-tok">X_302</span>, and pairs with <span class="g-tok">X_18</span> on <span class="g-tok">{6, 17, 18}</span>.</span>',
            "NAPOLEON–ISOGONAL PAIR",
            "Complement: X_627 • Anticomplement: X_629.",
        ),
    },
    18: {
        "short_title": "2nd NAPOLEON POINT",
        "enunciation": "The perspector of triangle ABC and the inner Napoleon equilateral triangle formed by the centers of inward side equilateral triangles.",
        "partners": [14, 17, 3, 5, 13, 62],
        "script": """[bell:proposition]
X eighteen is the Second Napoleon Point of triangle A B C: <pause> erect equilateral triangles inward on sides B C, C A, and A B, <pause> take their centroids Nap prime sub a, Nap prime sub b, and Nap prime sub c to form the inner Napoleon equilateral triangle, <pause> and the lines from A, B, and C to those three centers concur at X eighteen.

[bell:construction]
Its trilinear coordinates are cosecant of A minus pi over six, <pause> to cosecant of B minus pi over six, <pause> to cosecant of C minus pi over six. <pause> Remarkably, <pause> the difference in area between the outer Napoleon triangle of X seventeen and the inner Napoleon triangle of X eighteen equals the exact area of triangle A B C!

[bell:insight]
X eighteen lies on lines X three X fourteen, <pause> X five X thirteen, <pause> X four X sixteen, <pause> and X six X seventeen, <pause> and is the isogonal conjugate of X sixty-two.
""",
        "s1": (
            "X_18 = 2nd Napoleon Point • [A Nap'_a] ∩ [B Nap'_b] ∩ [C Nap'_c]",
            '<span class="clause-line"><span class="g-tok">X_18</span> is the <b>2nd Napoleon Point</b> — the perspector of <span class="g-tok">△ABC</span> and the equilateral <b>inner Napoleon triangle</b> <span class="coincide-tok">Nap\'_a Nap\'_b Nap\'_c</span>.</span>',
            "NAPOLEON'S THEOREM • INNER TRIANGLE",
            "Area(Outer Napoleon △) - Area(Inner Napoleon △) = Area(△ABC).",
        ),
        "s2": (
            "Trilinears csc(A - π/6) : : • Barycentrics a csc(A - π/6) : :",
            '<span class="clause-line"><b>Coordinates of X_18:</b> Trilinear distances <span class="g-tok">csc(A - π/6) : csc(B - π/6) : csc(C - π/6)</span> and barycentrics <span class="coincide-tok">1/(√3·S_A - Area) : 1/(√3·S_B - Area) : 1/(√3·S_C - Area)</span>.</span>',
            "-30° KIEPERT PERSPECTOR",
            "Point on the Kiepert hyperbola corresponding to base angle θ = -π/6 (-30°).",
        ),
        "s3": (
            "Lines {3, 14, 18} • {5, 13, 18} • {4, 16, 18} • {6, 17, 18}",
            '<span class="clause-line"><b>Incident Central Lines:</b> <span class="g-tok">X_18</span> lies at the intersection of <span class="g-tok">{3, 14, 18}</span>, <span class="coincide-tok">{5, 13, 18}</span>, <span class="eq-tok">{4, 16, 18}</span>, and <span class="eq-tok">{6, 17, 18}</span>.</span>',
            "SYMMETRIC NAPOLEON INCIDENCES",
            "Pairs with 1st Napoleon Point X_17 on line {6, 17, 18} through Symmedian Point X_6.",
        ),
        "s4": (
            "Isogonal Conjugate X_62 • Isotomic Conjugate X_303",
            '<span class="clause-line"><b>Functional Relations:</b> <span class="g-tok">X_18</span> is the isogonal conjugate of <span class="coincide-tok">X_62</span>, the isotomic conjugate of <span class="eq-tok">X_303</span>, and collinear with <span class="g-tok">X_5, X_13</span>.</span>',
            "KIEPERT CONJUGATE SYMMETRY",
            "Complement: X_628 • Anticomplement: X_630.",
        ),
    },
    19: {
        "short_title": "CLAWSON POINT",
        "enunciation": "The homothetic center (perspector) of the orthic triangle H_a H_b H_c and the extangents ( or extouch) triangle.",
        "partners": [4, 9, 10, 6, 63],
        "script": """[bell:proposition]
Completing the first classical collection of the Encyclopedia of Triangle Centers, <pause> X nineteen is the Clawson Point, <pause> discovered by John Wentworth Clawson in nineteen twenty-five: <pause> the homothetic center and perspector of the orthic triangle H sub a, H sub b, H sub c and the extangents triangle, <pause> as well as the perspector of the orthic and extouch triangles.

[bell:construction]
Its trilinear coordinates are simply tangent A, to tangent B, to tangent C—<pause> matching the barycentric coordinates of the Orthocenter X four! <pause> Consequently, <pause> its barycentric coordinates are a tangent A, <pause> to b tangent B, <pause> to c tangent C. <pause> On the central lines layer, <pause> X nineteen lies on the Orthocenter–Mittenpunkt–Spieker line through X four, X nine, and X ten.

[bell:insight]
Under functional relations, <pause> X nineteen is the isogonal conjugate of X sixty-three, <pause> the isotomic conjugate of X three hundred four, <pause> and concludes the nineteen foundational centers of the ETC.
""",
        "s1": (
            "X_19 = Clawson Point • Orthic & Extouch Perspector",
            '<span class="clause-line"><span class="g-tok">X_19</span> is the <b>Clawson Point</b> — the homothetic center of the <b>orthic triangle</b> <span class="g-tok">H_a H_b H_c</span> and the extangents triangle, and perspector with <span class="coincide-tok">N_a N_b N_c</span>.</span>',
            "CLAWSON'S THEOREM (1925)",
            "Lines joining altitude feet H_a, H_b, H_c to corresponding vertices of the extangents/extouch triangles concur at X_19.",
        ),
        "s2": (
            "Trilinears tan A : tan B : tan C • Barycentrics a/S_A : b/S_B : c/S_C",
            '<span class="clause-line"><b>Coordinates of X_19:</b> Trilinear distances <span class="g-tok">α : β : γ = tan A : tan B : tan C</span> and barycentric areas <span class="coincide-tok">u : v : w = a tan A : b tan B : c tan C</span>.</span>',
            "TRILINEAR TANGENT CENTER",
            "Notice the duality with Orthocenter X_4: X_4 has barycentrics tan A : tan B : tan C, while X_19 has trilinears tan A : tan B : tan C.",
        ),
        "s3": (
            "Orthocenter–Spieker Line {4, 9, 10, 19} • Line {1, 19, 28}",
            '<span class="clause-line"><b>Incident Central Lines:</b> <span class="g-tok">X_19</span> lies on the <b>Orthocenter–Spieker line</b> <span class="g-tok">{4, 9, 10, 19}</span>, line <span class="coincide-tok">{1, 19, 28}</span>, and line <span class="eq-tok">{6, 19, 34}</span>.</span>',
            "FOUR-CENTER COLLINEARITY {4, 9, 10, 19}",
            "Orthocenter X_4, Mittenpunkt X_9, Spieker Center X_10, and Clawson Point X_19 are collinear.",
        ),
        "s4": (
            "Isogonal Conjugate X_63 • Isotomic Conjugate X_304",
            '<span class="clause-line"><b>Functional Relations:</b> <span class="g-tok">X_19</span> is the isogonal conjugate of <span class="coincide-tok">X_63</span> (whose trilinears are cot A : cot B : cot C) and isotomic conjugate of <span class="eq-tok">X_304</span>.</span>',
            "TANGENT–COTANGENT ISOGONAL PAIR",
            "Complement: X_4329 • Anticomplement: X_18589.",
        ),
    },
}


def _parse_primary_svg_elements(primary_svg_path: Path, num: int, s1_clause: str = "") -> tuple[list[str], list[str], list[str]]:
    """Return `(construction_ids, secondary_poly_ids, circle_ids)` from `01_primary.svg`."""
    if not primary_svg_path.is_file():
        return [f"X_{num}"], [], []
    raw = primary_svg_path.read_text(encoding="utf-8")
    construction_ids: list[str] = [f"X_{num}"]
    secondary_poly_ids: list[str] = []
    circle_ids: list[str] = []

    for m in re.finditer(r'<line\b([^>]+)>', raw):
        attrs = m.group(1)
        cls_m = re.search(r'class="([^"]*)"', attrs)
        id_m = re.search(r'data-id="([^"]*)"', attrs)
        if not id_m:
            continue
        cls_str = cls_m.group(1) if cls_m else ""
        el_id = html.unescape(id_m.group(1))
        if (
            "sideline" in cls_str
            or "central_line" in cls_str
            or "incident" in cls_str
            or ("euler" in cls_str and "Euler line" not in s1_clause)
        ):
            continue
        construction_ids.append(el_id)
        for pt_attr in ("data-pt1", "data-pt2"):
            pm = re.search(rf'{pt_attr}="([^"]*)"', attrs)
            if pm:
                pt_id = html.unescape(pm.group(1))
                if pt_id not in ("A", "B", "C") and pt_id not in construction_ids:
                    construction_ids.append(pt_id)

    for m in re.finditer(r'<polygon\b([^>]+)>', raw):
        attrs = m.group(1)
        cls_m = re.search(r'class="([^"]*)"', attrs)
        id_m = re.search(r'data-id="([^"]*)"', attrs)
        if not id_m:
            continue
        cls_str = cls_m.group(1) if cls_m else ""
        el_id = html.unescape(id_m.group(1))
        if "secondary" in cls_str:
            secondary_poly_ids.append(el_id)
            pts = el_id.strip("<> ").split()
            for p in pts:
                if p not in ("A", "B", "C") and p not in secondary_poly_ids:
                    secondary_poly_ids.append(p)

    all_circles: list[tuple[str, str]] = []
    guide_pt_ids: list[str] = []
    for m in re.finditer(r'<circle\b([^>]+)>', raw):
        attrs = m.group(1)
        cls_m = re.search(r'class="([^"]*)"', attrs)
        id_m = re.search(r'data-id="([^"]*)"', attrs)
        if not id_m:
            continue
        cls_str = cls_m.group(1) if cls_m else ""
        cls_tokens = cls_str.split()
        el_id = html.unescape(id_m.group(1))
        if "point" in cls_tokens:
            if (
                "given" not in cls_tokens
                and "incident" not in cls_tokens
                and el_id not in ("A", "B", "C", f"X_{num}")
                and not el_id.startswith("E_")
            ):
                guide_pt_ids.append(el_id)
            continue
        all_circles.append((el_id, cls_str))

    if len(construction_ids) == 1 and guide_pt_ids:
        for pid in guide_pt_ids:
            if pid not in construction_ids:
                construction_ids.append(pid)

    non_guide_circles = [cid for cid, ccls in all_circles if "guide" not in ccls.split()]
    circle_ids = non_guide_circles if non_guide_circles else [cid for cid, _ in all_circles]
    return construction_ids, secondary_poly_ids, circle_ids


def ensure_center_incident_lines_in_model(model: Model, num: int, reg: CenterRegistry) -> None:
    """Ensure every `{a, b, ...}` central line referenced in `X_num`'s `s3` clause is present as an `.incident` line in `model`."""
    import sympy.geometry as spg

    prof = _COLLECTION_1_PROFILES.get(num)
    if not prof:
        return
    s3_clause = prof["s3"][1]
    brace_sets = [
        [int(x) for x in re.findall(r"\d+", m.group(1))]
        for m in re.finditer(r"\{([\d,\s]+)\}", s3_clause)
    ]
    if not brace_sets:
        return

    pts_by_id: dict[str, spg.Point] = {}
    existing_line_pairs: list[set[int]] = []
    for el, data in model.items():
        if isinstance(el, spg.Point) and getattr(data, "ID", None):
            pts_by_id[data.ID] = el
        elif isinstance(el, spg.Line) and getattr(data, "ID", None):
            lid = str(data.ID)
            if lid.startswith("{") and lid.endswith("}"):
                lnums = {int(x) for x in re.findall(r"\d+", lid)}
                if len(lnums) >= 2:
                    existing_line_pairs.append(lnums)

    def ensure_inc_pt(k: int, force: bool = False) -> spg.Point | None:
        pid = f"X_{k}"
        if pid in pts_by_id:
            return pts_by_id[pid]
        xy = reg.xy_cache.get(k)
        if xy is None:
            return None
        if not force and not (-0.65 <= xy[0] <= 1.65 and -0.65 <= xy[1] <= 1.25):
            return None
        pt = _add_point(model, xy[0], xy[1], ID=pid, classes=["center", "incident"])
        pts_by_id[pid] = pt
        return pt

    for bset in brace_sets:
        valid_nums = [k for k in bset if k in reg.xy_cache]
        if len(valid_nums) < 2:
            continue
        for k in valid_nums:
            if k != num:
                ensure_inc_pt(k, force=False)
        bset_set = set(valid_nums)
        if any(lp <= bset_set for lp in existing_line_pairs):
            continue
        other_nums = [k for k in valid_nums if k != num]
        if len(other_nums) >= 2:
            c1, c2 = other_nums[0], other_nums[1]
        else:
            c1, c2 = valid_nums[0], valid_nums[1]
        p1 = ensure_inc_pt(c1, force=True)
        p2 = ensure_inc_pt(c2, force=True)
        if p1 is not None and p2 is not None:
            i_min, i_max = min(c1, c2), max(c1, c2)
            _add_line(model, p1, p2, ID=f"{{ {i_min}, {i_max} }}", classes=["central_line", "incident"])
            existing_line_pairs.append({i_min, i_max})

    target_pt = pts_by_id.get(f"X_{num}")
    if target_pt is not None and target_pt in model:
        promote_point_to_top(model, target_pt)


def _mute_other_spans(clause_html: str, keep_classes: set[str]) -> str:
    """Replace token spans not in `keep_classes` with a subtle muted inline style so text colors match active graphic colors."""
    def repl(m: re.Match) -> str:
        cls = m.group(1)
        inner = m.group(2)
        if cls in keep_classes:
            return m.group(0)
        return f'<span style="color:#94a3b8;font-family:\'JetBrains Mono\',monospace;font-weight:600;">{inner}</span>'

    return re.sub(r'<span class="(g-tok|coincide-tok|eq-tok)">(.*?)</span>', repl, clause_html)


def _tag_circle_terms_in_clause(clause_html: str, tok_cls: str = "eq-tok") -> str:
    """Wrap bold circle names like `<b>incircle</b>` or `<b>circumcircle</b>` in `<span class="eq-tok">` so circle color matches text."""
    circle_pat = re.compile(
        r"<b>((?:nine-point|Spieker|Apollonian|Fuhrmann|in|circum|ex)[\w\s-]*circles?)</b>",
        re.IGNORECASE,
    )
    return circle_pat.sub(rf'<span class="{tok_cls}">\1</span>', clause_html)


_COLLECTION_1_COORDS: dict[int, tuple[tuple[str, str, str], tuple[str, str, str]]] = {
    1: (("1", "1", "1"), ("a", "b", "c")),
    2: (("1/a", "1/b", "1/c"), ("1", "1", "1")),
    3: (("cos A", "cos B", "cos C"), ("sin 2A", "sin 2B", "sin 2C")),
    4: (("sec A", "sec B", "sec C"), ("tan A", "tan B", "tan C")),
    5: (("cos(B − C)", "cos(C − A)", "cos(A − B)"), ("a cos(B − C)", "b cos(C − A)", "c cos(A − B)")),
    6: (("a", "b", "c"), ("a²", "b²", "c²")),
    7: (("bc/(s − a)", "ca/(s − b)", "ab/(s − c)"), ("1/(s − a)", "1/(s − b)", "1/(s − c)")),
    8: (("(s − a)/a", "(s − b)/b", "(s − c)/c"), ("s − a", "s − b", "s − c")),
    9: (("s − a", "s − b", "s − c"), ("a(s − a)", "b(s − b)", "c(s − c)")),
    10: (("bc(b + c)", "ca(c + a)", "ab(a + b)"), ("b + c", "c + a", "a + b")),
    11: (("1 − cos(B − C)", "1 − cos(C − A)", "1 − cos(A − B)"), ("(s − a)(b − c)²", "(s − b)(c − a)²", "(s − c)(a − b)²")),
    12: (("1 + cos(B − C)", "1 + cos(C − A)", "1 + cos(A − B)"), ("(b + c)²/(s − a)", "(c + a)²/(s − b)", "(a + b)²/(s − c)")),
    13: (("csc(A + π/3)", "csc(B + π/3)", "csc(C + π/3)"), ("a csc(A + π/3)", "b csc(B + π/3)", "c csc(C + π/3)")),
    14: (("csc(A − π/3)", "csc(B − π/3)", "csc(C − π/3)"), ("a csc(A − π/3)", "b csc(B − π/3)", "c csc(C − π/3)")),
    15: (("sin(A + π/3)", "sin(B + π/3)", "sin(C + π/3)"), ("a sin(A + π/3)", "b sin(B + π/3)", "c sin(C + π/3)")),
    16: (("sin(A − π/3)", "sin(B − π/3)", "sin(C − π/3)"), ("a sin(A − π/3)", "b sin(B − π/3)", "c sin(C − π/3)")),
    17: (("csc(A + π/6)", "csc(B + π/6)", "csc(C + π/6)"), ("a csc(A + π/6)", "b csc(B + π/6)", "c csc(C + π/6)")),
    18: (("csc(A − π/6)", "csc(B − π/6)", "csc(C − π/6)"), ("a csc(A − π/6)", "b csc(B − π/6)", "c csc(C − π/6)")),
    19: (("cos B cos C / sin A", "cos C cos A / sin B", "cos A cos B / sin C"), ("tan B tan C", "tan C tan A", "tan A tan B")),
}

_COLLECTION_1_LINES_TABLE: dict[int, list[tuple[str, str]]] = {
    1: [
        ("Nagel Line", "{1, 2, 8, 10}"),
        ("Feuerbach Line", "{1, 5, 11}"),
        ("OI Line", "{1, 3, 40}"),
        ("Soddy Line", "{1, 7, 20}"),
    ],
    2: [
        ("Euler Line", "{2, 3, 4, 5}"),
        ("Nagel Line", "{1, 2, 8, 10}"),
        ("Gergonne–Mittenpunkt", "{2, 7, 9}"),
    ],
    3: [
        ("Euler Line", "{2, 3, 4, 5}"),
        ("Brocard Axis", "{3, 6, 15, 16}"),
        ("OI Line", "{1, 3, 40}"),
    ],
    4: [
        ("Euler Line", "{2, 3, 4, 5}"),
        ("Orthocenter–Spieker", "{4, 9, 10, 19}"),
        ("Fuhrmann Line", "{4, 8}"),
    ],
    5: [
        ("Euler Line", "{2, 3, 4, 5}"),
        ("Feuerbach Line", "{1, 5, 11, 12}"),
        ("Fermat–Napoleon Axis", "{5, 13, 18}"),
        ("Isogonic–Napoleon Axis", "{5, 14, 17}"),
    ],
    6: [
        ("Brocard Axis", "{3, 6, 15, 16}"),
        ("Incenter–Mittenpunkt", "{1, 6, 9}"),
        ("Isogonic Axis", "{6, 13, 14}"),
        ("Napoleon Axis", "{6, 17, 18}"),
    ],
    7: [
        ("Soddy Line", "{1, 7, 20}"),
        ("Centroid–Mittenpunkt", "{2, 7, 9}"),
        ("Gergonne–Nagel Line", "{7, 8, 65}"),
    ],
    8: [
        ("Nagel Line", "{1, 2, 8, 10}"),
        ("Fuhrmann Line", "{4, 8, 72}"),
        ("Gergonne–Nagel Line", "{7, 8, 65}"),
    ],
    9: [
        ("Incenter–Symmedian", "{1, 6, 9}"),
        ("Centroid–Gergonne", "{2, 7, 9}"),
        ("Orthocenter–Spieker", "{4, 9, 10}"),
    ],
    10: [
        ("Nagel Line", "{1, 2, 8, 10}"),
        ("Orthocenter–Mittenpunkt", "{4, 9, 10, 19}"),
    ],
    11: [
        ("Feuerbach Line", "{1, 5, 11, 12}"),
        ("Centroid–Insimilicenter", "{2, 11, 55}"),
        ("Orthocenter–Exsimilicenter", "{4, 11, 56}"),
    ],
    12: [
        ("Feuerbach Line", "{1, 5, 11, 12}"),
        ("Centroid–Exsimilicenter", "{2, 12, 56}"),
        ("Orthocenter–Insimilicenter", "{4, 12, 55}"),
    ],
    13: [
        ("Symmedian–Isogonic", "{6, 13, 14}"),
        ("Circumcenter–1st Napoleon", "{3, 13, 17}"),
        ("Centroid–2nd Isodynamic", "{2, 13, 16}"),
    ],
    14: [
        ("Symmedian–Isogonic", "{6, 13, 14}"),
        ("Circumcenter–2nd Napoleon", "{3, 14, 18}"),
        ("Centroid–1st Isodynamic", "{2, 14, 15}"),
    ],
    15: [
        ("Brocard Axis", "{3, 6, 15, 16}"),
        ("Centroid–2nd Isogonic", "{2, 14, 15}"),
        ("Orthocenter–1st Napoleon", "{4, 15, 17}"),
    ],
    16: [
        ("Brocard Axis", "{3, 6, 15, 16}"),
        ("Centroid–1st Isogonic", "{2, 13, 16}"),
        ("Orthocenter–2nd Napoleon", "{4, 16, 18}"),
    ],
    17: [
        ("Circumcenter–1st Isogonic", "{3, 13, 17}"),
        ("Orthocenter–1st Isodynamic", "{4, 15, 17}"),
        ("Symmedian–Napoleon", "{6, 17, 18}"),
    ],
    18: [
        ("Circumcenter–2nd Isogonic", "{3, 14, 18}"),
        ("Orthocenter–2nd Isodynamic", "{4, 16, 18}"),
        ("Symmedian–Napoleon", "{6, 17, 18}"),
    ],
    19: [
        ("Orthocenter–Spieker", "{4, 9, 10, 19}"),
        ("Symmedian–Clawson", "{6, 19, 25}"),
        ("Incenter–Clawson", "{1, 19, 28}"),
    ],
}

_COLLECTION_1_RELATIONS_TABLE: dict[int, list[tuple[str, int, str]]] = {
    1: [
        ("Isogonal Conjugate", 1, "X_1 (self)"),
        ("Isotomic Conjugate", 75, "X_75"),
        ("Anticomplement of", 10, "X_10 (Spieker)"),
        ("Complement of", 8, "X_8 (Nagel)"),
    ],
    2: [
        ("Isogonal Conjugate", 6, "X_6"),
        ("Isotomic Conjugate", 2, "X_2 (self)"),
        ("Cyclocevian Conjugate", 4, "X_4"),
        ("Homothetic Center", 3, "X_3 ↔ X_5"),
    ],
    3: [
        ("Isogonal Conjugate", 4, "X_4"),
        ("Complement", 5, "X_5"),
        ("Anticomplement", 4, "X_4"),
    ],
    4: [
        ("Isogonal Conjugate", 3, "X_3"),
        ("Complement", 3, "X_3"),
        ("Isotomic Conjugate", 69, "X_69"),
        ("Cyclocevian Conjugate", 2, "X_2"),
    ],
    5: [
        ("Anticomplement", 3, "X_3"),
        ("Euler Segment Midpoint", 4, "X_3, X_4"),
        ("Isogonal Conjugate", 54, "X_54"),
    ],
    6: [
        ("Isogonal Conjugate", 2, "X_2"),
        ("Isotomic Conjugate", 76, "X_76"),
        ("Brocard Diameter Partner", 3, "X_3"),
    ],
    7: [
        ("Isotomic Conjugate", 8, "X_8"),
        ("Complement", 9, "X_9"),
        ("Isogonal Conjugate", 55, "X_55"),
    ],
    8: [
        ("Anticomplement", 1, "X_1"),
        ("Isotomic Conjugate", 7, "X_7"),
        ("Isogonal Conjugate", 56, "X_56"),
    ],
    9: [
        ("Anticomplement", 7, "X_7"),
        ("Isogonal Conjugate", 57, "X_57"),
        ("Excentral Symmedian", 1, "X_1, X_6"),
    ],
    10: [
        ("Anticomplement", 1, "X_1"),
        ("Midpoint on Nagel Line", 8, "X_1, X_8"),
        ("Isogonal Conjugate", 58, "X_58"),
    ],
    11: [
        ("Harmonic Conjugate", 12, "X_12"),
        ("Tangency Centers", 5, "X_1, X_5"),
        ("Isogonal Conjugate", 59, "X_59"),
    ],
    12: [
        ("Harmonic Conjugate", 11, "X_11"),
        ("Internal Similicenter", 5, "X_1, X_5"),
        ("Excircle Similicenter", 55, "X_55"),
    ],
    13: [
        ("Isogonal Conjugate", 15, "X_15"),
        ("Orthocentroidal Inverse", 14, "X_14"),
        ("Napoleon Collinear", 17, "X_17"),
    ],
    14: [
        ("Isogonal Conjugate", 16, "X_16"),
        ("Orthocentroidal Inverse", 13, "X_13"),
        ("Napoleon Collinear", 18, "X_18"),
    ],
    15: [
        ("Isogonal Conjugate", 13, "X_13"),
        ("Circumcircle Inverse", 16, "X_16"),
        ("Brocard Axis Anchor", 3, "X_3, X_6"),
    ],
    16: [
        ("Isogonal Conjugate", 14, "X_14"),
        ("Circumcircle Inverse", 15, "X_15"),
        ("Brocard Axis Anchor", 3, "X_3, X_6"),
    ],
    17: [
        ("Napoleon Companion", 18, "X_18"),
        ("1st Isogonic Partner", 13, "X_13"),
        ("1st Isodynamic Partner", 15, "X_15"),
    ],
    18: [
        ("Napoleon Companion", 17, "X_17"),
        ("2nd Isogonic Partner", 14, "X_14"),
        ("2nd Isodynamic Partner", 16, "X_16"),
    ],
    19: [
        ("Orthic Perspector Partner", 4, "X_4"),
        ("Symmedian Partner", 6, "X_6"),
        ("Spieker Collinear", 10, "X_10"),
    ],
}


def _format_component_colored_coordinates_clause(num: int, target_center: dict[str, Any]) -> str:
    """Format Step 3 (`02_coordinates.svg`) as a clean tabular layout with headings 'Trilinear Distances' and 'Barycentric Sub-Areas'."""
    if num in _COLLECTION_1_COORDS:
        (ta, tb, tc), (ba, bb, bc) = _COLLECTION_1_COORDS[num]
    else:
        tri_raw = _clean_formula((target_center.get("trilinears") or ["1 : 1 : 1"])[0])
        bary_raw = _clean_formula((target_center.get("barycentrics") or ["a : b : c"])[0])
        tri_parts = [p.strip() for p in tri_raw.split(":") if p.strip()]
        bary_parts = [p.strip() for p in bary_raw.split(":") if p.strip()]

        if len(tri_parts) >= 3:
            ta, tb, tc = tri_parts[0][:18], tri_parts[1][:18], tri_parts[2][:18]
        else:
            ta = tb = tc = (tri_parts[0] if tri_parts else "1")[:18]

        if len(bary_parts) >= 3:
            ba, bb, bc = bary_parts[0][:18], bary_parts[1][:18], bary_parts[2][:18]
        else:
            ba, bb, bc = f"a·({ta})", f"b·({tb})", f"c·({tc})"

    tri_stack = " stack" if max(len(ta), len(tb), len(tc)) > 11 else ""
    bary_stack = " stack" if max(len(ba), len(bb), len(bc)) > 11 else ""

    return (
        '<div class="etc-table-block">'
        '<div class="etc-section">'
        '<div class="etc-sec-head">Trilinear Distances</div>'
        f'<div class="etc-coord-grid{tri_stack}">'
        f'<span class="g-tok">α = {html.escape(ta)}</span>'
        f'<span class="coincide-tok">β = {html.escape(tb)}</span>'
        f'<span class="eq-tok">γ = {html.escape(tc)}</span>'
        "</div>"
        "</div>"
        '<div class="etc-section">'
        '<div class="etc-sec-head">Barycentric Sub-Areas</div>'
        f'<div class="etc-coord-grid{bary_stack}">'
        f'<span class="g-tok">u = {html.escape(ba)}</span>'
        f'<span class="coincide-tok">v = {html.escape(bb)}</span>'
        f'<span class="eq-tok">w = {html.escape(bc)}</span>'
        "</div>"
        "</div>"
        "</div>"
    )


def _extract_lines_rows_from_clause(s3_clause: str) -> list[tuple[str, str]]:
    """Extract `(line_label, '{a, b, ...}')` pairs from an `s3_clause` string."""
    rows: list[tuple[str, str]] = []
    # Find all {...} spans and the preceding text chunk
    pos = 0
    for m in re.finditer(r'<span class="(?:g-tok|coincide-tok|eq-tok)">(\{[\d,\s]+\})</span>', s3_clause):
        brace_str = m.group(1).strip()
        prefix_raw = s3_clause[pos : m.start()]
        pos = m.end()
        # Look for <b>...</b> in prefix_raw first
        bold_matches = re.findall(r"<b>([^<]+)</b>", prefix_raw)
        if bold_matches and "incident central lines" not in bold_matches[-1].lower():
            lbl = bold_matches[-1].strip().rstrip(":").title()
        else:
            clean_p = re.sub(r"<[^>]+>", "", prefix_raw)
            clean_p = re.sub(r"^.*?:", "", clean_p)
            clean_p = re.sub(r"\b(anchors|lies on|is the intersection of|the|and|with|joins|pair)\b", " ", clean_p, flags=re.IGNORECASE)
            clean_p = re.sub(r"\bX_\d+\b", " ", clean_p)
            clean_p = re.sub(r"[,;.]", " ", clean_p)
            clean_p = " ".join(clean_p.split()).strip()
            lbl = clean_p.title() if clean_p and len(clean_p) > 2 else f"Central Line {brace_str}"
        rows.append((lbl, brace_str))
    return rows


_COLLECTION_1_PRIMARY_ROWS: dict[int, list[tuple[str, str, str]]] = {
    1: [
        ("Target Center", "X_1 (Incenter)", "gold"),
        ("Interior Bisectors", "AI_a, BI_b, CI_c", "gold"),
        ("Inscribed Circle", "Incircle (r)", "pink"),
        ("Bisector Feet", "I_a, I_b, I_c", "blue"),
    ],
    2: [
        ("Target Center", "X_2 (Centroid)", "gold"),
        ("Medians", "AM_a, BM_b, CM_c", "gold"),
        ("Medial Triangle", "△M_a M_b M_c", "blue"),
    ],
    3: [
        ("Target Center", "X_3 (Circumcenter)", "gold"),
        ("Perpendicular Bisectors", "at M_a, M_b, M_c", "gold"),
        ("Circumscribed Circle", "Circumcircle (R)", get_circle_color_token("circumcircle")),
    ],
    4: [
        ("Target Center", "X_4 (Orthocenter)", "gold"),
        ("Altitudes", "AH_a, BH_b, CH_c", "gold"),
        ("Orthic Triangle", "△H_a H_b H_c", "blue"),
    ],
    5: [
        ("Target Center", "X_5 (Nine-Point)", "gold"),
        ("Nine-Point Circle", "Radius R / 2", get_circle_color_token("nine_point_circle")),
        ("Midpoints & Feet", "M_a..c, H_a..c", "blue"),
    ],
    6: [
        ("Target Center", "X_6 (Symmedian)", "gold"),
        ("Symmedians", "A–Tan_a, B–Tan_b, C–Tan_c", "gold"),
        ("Tangential Triangle", "△Tan_a Tan_b Tan_c", "blue"),
    ],
    7: [
        ("Target Center", "X_7 (Gergonne)", "gold"),
        ("Contact Cevians", "AT_a, BT_b, CT_c", "gold"),
        ("Inscribed Circle", "Incircle (r)", get_circle_color_token("incircle")),
        ("Intouch Triangle", "△T_a T_b T_c", "blue"),
    ],
    8: [
        ("Target Center", "X_8 (Nagel)", "gold"),
        ("Perimeter Splitters", "AN_a, BN_b, CN_c", "gold"),
        ("Extouch Triangle", "△N_a N_b N_c", "blue"),
    ],
    9: [
        ("Target Center", "X_9 (Mittenpunkt)", "gold"),
        ("Excenter–Midpoint Lines", "J_a M_a, J_b M_b, J_c M_c", "gold"),
        ("Medial Triangle", "△M_a M_b M_c", "blue"),
    ],
    10: [
        ("Target Center", "X_10 (Spieker)", "gold"),
        ("Medial Bisectors", "of △M_a M_b M_c", "gold"),
        ("Spieker Circle", "Radius r / 2", get_circle_color_token("spieker_circle")),
        ("Medial Triangle", "△M_a M_b M_c", "blue"),
    ],
    11: [
        ("Target Center", "X_11 (Feuerbach)", "gold"),
        ("Inscribed Circle", "Incircle (X_1)", get_circle_color_token("incircle")),
        ("Nine-Point Circle", "Nine-Point (X_5)", get_circle_color_token("nine_point_circle")),
    ],
    12: [
        ("Target Center", "X_12 (Harmonic)", "gold"),
        ("Feuerbach Cevians", "on △ABC", "gold"),
        ("Incircle & Nine-Point", "X_1, X_5", get_circle_color_token("nine_point_circle")),
    ],
}


def _format_primary_construction_steps(
    num: int,
    short_title: str,
    construction_ids: list[str],
    secondary_poly_ids: list[str],
    circle_ids: list[str],
) -> tuple[str, str, list[str], list[str]]:
    """Return `(s1a_clause, s1b_clause, step1_active, step2_active)` with structured `.etc-data-list` rows and canonical colors."""
    line_ids = [cid for cid in construction_ids if cid.startswith("[")]
    pt_ids = [
        cid
        for cid in construction_ids
        if not cid.startswith("[") and cid != f"X_{num}"
    ]

    if num in _COLLECTION_1_PRIMARY_ROWS:
        spec_rows = _COLLECTION_1_PRIMARY_ROWS[num]
    else:
        spec_rows = [("Target Center", f"X_{num} ({short_title.title()})", "gold")]
        if line_ids:
            spec_rows.append(("Concurrence Lines", ", ".join(line_ids[:3]), "gold"))
        for cid in circle_ids[:2]:
            c_tok = get_circle_color_token(cid)
            spec_rows.append(("Circle", cid.replace("_", " ").title(), c_tok))
        if secondary_poly_ids:
            spec_rows.append(("Derived Triangle", secondary_poly_ids[0], "blue"))

    has_non_gold = any(col != "gold" for _, _, col in spec_rows)
    s1_rows_html: list[str] = []
    s2_rows_html: list[str] = []
    for idx, (lbl, val, col) in enumerate(spec_rows):
        lbl_e = html.escape(lbl)
        val_e = html.escape(val)
        if col == "gold" or not has_non_gold:
            s1_rows_html.append(
                f'<div class="etc-data-row"><span class="etc-row-label">{lbl_e}</span>'
                f'<span class="tok-{col}">{val_e}</span></div>'
            )
        else:
            s1_rows_html.append(
                f'<div class="etc-data-row muted-row"><span class="etc-row-label">{lbl_e}</span>'
                f'<span class="muted-tok">{val_e}</span></div>'
            )

        # In Step 2 (GOAL), if there are secondary circles/polygons, mute the construction lines row so lines return to dotted
        if idx > 0 and col == "gold" and has_non_gold:
            s2_rows_html.append(
                f'<div class="etc-data-row muted-row"><span class="etc-row-label">{lbl_e}</span>'
                f'<span class="muted-tok">{val_e}</span></div>'
            )
        else:
            s2_rows_html.append(
                f'<div class="etc-data-row"><span class="etc-row-label">{lbl_e}</span>'
                f'<span class="tok-{col}">{val_e}</span></div>'
            )

    s1a_clause = (
        '<div class="etc-table-block">'
        '<div class="etc-sec-head">Primary Construction</div>'
        f'<div class="etc-data-list">{"".join(s1_rows_html)}</div>'
        "</div>"
    )
    s1b_clause = (
        '<div class="etc-table-block">'
        '<div class="etc-sec-head">Primary Construction</div>'
        f'<div class="etc-data-list">{"".join(s2_rows_html)}</div>'
        "</div>"
    )

    step1_active: list[str] = [f"X_{num}:gold"] + [f"{lid}:gold" for lid in line_ids]
    if not line_ids and circle_ids:
        first_c = circle_ids[0]
        step1_active.append(f"{first_c}:{get_circle_color_token(first_c)}")

    step2_active: list[str] = [f"X_{num}:gold"]
    for cid in circle_ids:
        step2_active.append(f"{cid}:{get_circle_color_token(cid)}")
    for sid in secondary_poly_ids:
        step2_active.append(f"{sid}:blue")
    if not secondary_poly_ids and pt_ids:
        for pid in pt_ids:
            step2_active.append(f"{pid}:blue")
    if len(step2_active) == 1:
        step2_active = list(step1_active)

    return s1a_clause, s1b_clause, step1_active, step2_active


def _format_reference_triangles_clause() -> str:
    """Format Step 7 (`05_four_triangles.svg`) as a clean structured table with tabular a, b, c columns and no parens/commas."""
    rows = [
        ("Heronian Triangle", ("15", "13", "14"), REFERENCE_TRIANGLE_COLORS["heronian"]),
        ("Right Triangle", ("3", "4", "5"), REFERENCE_TRIANGLE_COLORS["right"]),
        ("Kepler Triangle", ("1", "√φ", "φ"), REFERENCE_TRIANGLE_COLORS["kepler"]),
        ("Kimberling Triangle", ("6", "9", "13"), REFERENCE_TRIANGLE_COLORS["kimberling"]),
    ]
    rows_html = "".join(
        f'<div class="etc-data-row"><span class="etc-row-label">{html.escape(lbl)}</span>'
        f'<div class="etc-row-cells">'
        + "".join(f'<span class="tok-{col}">{html.escape(v)}</span>' for v in vals)
        + "</div></div>"
        for lbl, vals, col in rows
    )
    return (
        '<div class="etc-table-block">'
        '<div class="etc-sec-head-row"><span class="etc-sec-head">Reference Triangles</span>'
        '<div class="etc-head-cols"><span>a</span><span>b</span><span>c</span></div></div>'
        f'<div class="etc-data-list">{rows_html}</div>'
        "</div>"
    )


def _sequence_central_lines_clause(
    s3_clause: str,
    num: int,
    is_topic: bool = False,
) -> tuple[str, str, list[str], list[str], list[str]]:
    """Render structured `.etc-data-list` rows for Steps 4 & 5 using each central line's canonical color from `palette.py`."""
    if not is_topic and num in _COLLECTION_1_LINES_TABLE:
        rows = _COLLECTION_1_LINES_TABLE[num]
    else:
        rows = _extract_lines_rows_from_clause(s3_clause)

    used_tokens: set[str] = set()
    line_colors: list[str] = []
    for label, brace_str in rows:
        c_tok = get_central_line_color_token(brace_str, label, used_tokens=used_tokens)
        used_tokens.add(c_tok)
        line_colors.append(c_tok)

    step4_rows_html: list[str] = []
    step5_rows_html: list[str] = []
    for idx, ((label, brace_str), c_tok) in enumerate(zip(rows, line_colors)):
        tok_cls = f"tok-{c_tok}"
        lbl_esc = html.escape(label)
        b_esc = html.escape(brace_str)
        if idx == 0:
            step4_rows_html.append(
                f'<div class="etc-data-row"><span class="etc-row-label">{lbl_esc}</span>'
                f'<span class="{tok_cls}">{b_esc}</span></div>'
            )
        else:
            step4_rows_html.append(
                f'<div class="etc-data-row muted-row"><span class="etc-row-label">{lbl_esc}</span>'
                f'<span class="muted-tok">{b_esc}</span></div>'
            )
        step5_rows_html.append(
            f'<div class="etc-data-row"><span class="etc-row-label">{lbl_esc}</span>'
            f'<span class="{tok_cls}">{b_esc}</span></div>'
        )

    head_title = "Central Line Incidences" if is_topic else "Incident Central Lines"
    step4_clause = (
        '<div class="etc-table-block">'
        f'<div class="etc-sec-head">{head_title}</div>'
        f'<div class="etc-data-list">{"".join(step4_rows_html)}</div>'
        "</div>"
    )
    step5_clause = (
        '<div class="etc-table-block">'
        f'<div class="etc-sec-head">{head_title}</div>'
        f'<div class="etc-data-list">{"".join(step5_rows_html)}</div>'
        "</div>"
    )

    step4_active = [f"X_{num}:gold"] + (
        [f"{rows[0][1]}:{line_colors[0]}"] if rows else []
    )
    step5_active = [f"X_{num}:gold"] + [
        f"{brace_str}:{c_tok}" for (_, brace_str), c_tok in zip(rows, line_colors)
    ]
    return step4_clause, step5_clause, step4_active, step5_active, []


def _normalize_relations_clause(
    s4_clause: str,
    num: int,
    reg: CenterRegistry | None = None,
    is_topic: bool = False,
) -> tuple[str, list[str], list[str], list[str]]:
    """Assign each partner center `X_k` (`k != num`) a distinct color from `PARTNER_COLOR_RING` while keeping connecting lines dotted."""
    active_ids: list[str] = [f"X_{num}:gold"]
    coincide_ids: list[str] = []
    equal_ids: list[str] = []

    table_rows = _COLLECTION_1_RELATIONS_TABLE.get(num) if not is_topic else None

    partner_order: list[int] = []
    if table_rows:
        for _, k, _ in table_rows:
            if k != num and k not in partner_order:
                partner_order.append(k)
    else:
        for m in re.finditer(r'<span class="(?:g-tok|coincide-tok|eq-tok|tok-[a-z]+)">\s*X_(\d+)\b.*?</span>', s4_clause):
            k = int(m.group(1))
            if k != num and k not in partner_order:
                partner_order.append(k)

    partner_color_map: dict[int, str] = {}
    for idx, k in enumerate(partner_order):
        c_tok = PARTNER_COLOR_RING[idx % len(PARTNER_COLOR_RING)]
        partner_color_map[k] = c_tok
        active_ids.append(f"X_{k}:{c_tok}")

    if table_rows:
        rows_html: list[str] = []
        for rel_label, k, pill_text in table_rows:
            c_tok = "gold" if k == num else partner_color_map.get(k, "blue")
            rows_html.append(
                f'<div class="etc-data-row"><span class="etc-row-label">{html.escape(rel_label)}</span>'
                f'<span class="tok-{c_tok}">{html.escape(pill_text)}</span></div>'
            )
        norm_clause = (
            '<div class="etc-table-block">'
            '<div class="etc-sec-head">Functional Relations</div>'
            f'<div class="etc-data-list">{"".join(rows_html)}</div>'
            "</div>"
        )
        return norm_clause, active_ids, coincide_ids, equal_ids

    def repl_tok(m: re.Match) -> str:
        inner = m.group(2).strip()
        xm = re.match(r"^X_(\d+)\b", inner)
        if xm:
            k = int(xm.group(1))
            if k == num:
                return f'<span class="tok-gold">{inner}</span>'
            c_tok = partner_color_map.get(k, "blue")
            return f'<span class="tok-{c_tok}">{inner}</span>'
        return m.group(0)

    norm_clause = re.sub(r'<span class="(g-tok|coincide-tok|eq-tok|tok-[a-z]+)">(.*?)</span>', repl_tok, s4_clause)
    return norm_clause, active_ids, coincide_ids, equal_ids


def _split_id_list(val: str) -> list[str]:
    """Split comma-separated SVG element IDs while keeping commas inside `[...]` and `{...}` intact."""
    items: list[str] = []
    cur: list[str] = []
    depth = 0
    for ch in val:
        if ch in "[{":
            depth += 1
            cur.append(ch)
        elif ch in "]}":
            depth = max(0, depth - 1)
            cur.append(ch)
        elif ch == "," and depth == 0:
            tok = "".join(cur).strip()
            if tok:
                items.append(tok)
            cur = []
        else:
            cur.append(ch)
    tok = "".join(cur).strip()
    if tok:
        items.append(tok)
    return items


_CLS_TO_COLOR_TAG = {
    "g-tok": "gold",
    "coincide-tok": "blue",
    "eq-tok": "green",
    "muted-tok": "muted",
    "tok-gold": "gold",
    "tok-orange": "orange",
    "tok-teal": "teal",
    "tok-blue": "blue",
    "tok-purple": "purple",
    "tok-orchid": "orchid",
    "tok-pink": "pink",
    "tok-green": "green",
    "tok-lime": "lime",
    "tok-muted": "muted",
}

_COLOR_TAG_TO_CLS = {
    "gold": "tok-gold",
    "orange": "tok-orange",
    "teal": "tok-teal",
    "blue": "tok-blue",
    "purple": "tok-purple",
    "orchid": "tok-orchid",
    "pink": "tok-pink",
    "green": "tok-green",
    "lime": "tok-lime",
    "muted": "muted-tok",
}


def _html_clause_to_script_lines(clause_html: str) -> list[str]:
    """Convert internal `clause_html` into human-readable `section:`, `head:`, `row:`, or `text:` script lines."""
    if "etc-coord-grid" in clause_html:
        lines: list[str] = []
        for sec_m in re.finditer(
            r'<div class="etc-section">\s*<div class="etc-sec-head">(.*?)</div>\s*<div class="etc-coord-grid[^"]*">(.*?)</div>\s*</div>',
            clause_html,
            flags=re.DOTALL,
        ):
            sec_title = html.unescape(sec_m.group(1).strip())
            grid_body = sec_m.group(2)
            cells: list[str] = []
            for sp_m in re.finditer(r'<span class="([^"]+)">(.*?)</span>', grid_body, flags=re.DOTALL):
                c_tag = _CLS_TO_COLOR_TAG.get(sp_m.group(1).strip(), "gold")
                val_txt = html.unescape(sp_m.group(2).strip())
                cells.append(f"{val_txt}:{c_tag}")
            lines.append(f"section: {sec_title} | " + " | ".join(cells))
        if lines:
            return lines

    if "etc-data-list" in clause_html:
        lines = []
        head_m = re.search(r'<span class="etc-sec-head">(.*?)</span>\s*<div class="etc-head-cols">(.*?)</div>', clause_html, flags=re.DOTALL)
        if head_m:
            h_title = html.unescape(head_m.group(1).strip())
            cols = [html.unescape(cm.group(1).strip()) for cm in re.finditer(r"<span>(.*?)</span>", head_m.group(2), flags=re.DOTALL)]
            lines.append(f"head: {h_title} | " + " | ".join(cols))
        else:
            head_m2 = re.search(r'<div class="etc-sec-head">(.*?)</div>', clause_html, flags=re.DOTALL)
            if head_m2:
                lines.append(f"head: {html.unescape(head_m2.group(1).strip())}")

        for row_m in re.finditer(
            r'<div class="etc-data-row[^"]*">\s*<span class="etc-row-label">(.*?)</span>\s*(.*?)\s*</div>(?=\s*(?:<div class="etc-data-row|</div>))',
            clause_html,
            flags=re.DOTALL,
        ):
            lbl = html.unescape(row_m.group(1).strip())
            rhs_html = row_m.group(2).strip()
            spans = list(re.finditer(r'<span class="([^"]+)">(.*?)</span>', rhs_html, flags=re.DOTALL))
            if len(spans) == 1:
                c_tag = _CLS_TO_COLOR_TAG.get(spans[0].group(1).strip(), "gold")
                val = html.unescape(spans[0].group(2).strip())
                lines.append(f"row: {lbl} | {val}:{c_tag}")
            elif len(spans) > 1:
                c_tags = [_CLS_TO_COLOR_TAG.get(sp.group(1).strip(), "gold") for sp in spans]
                vals = [html.unescape(sp.group(2).strip()) for sp in spans]
                if len(set(c_tags)) == 1:
                    lines.append(f"row: {lbl} | " + " | ".join(vals[:-1] + [f"{vals[-1]}:{c_tags[-1]}"]) )
                else:
                    lines.append(f"row: {lbl} | " + " | ".join(f"{v}:{c}" for v, c in zip(vals, c_tags)))
        if lines:
            return lines

    inner = re.sub(r'^<span class="clause-line">(.*)</span>$', r"\1", clause_html.strip(), flags=re.DOTALL)
    inner = re.sub(r"<b>(.*?)</b>", r"**\1**", inner, flags=re.DOTALL)

    def _span_repl(m: re.Match) -> str:
        c_tag = _CLS_TO_COLOR_TAG.get(m.group(1).strip(), "gold")
        txt = html.unescape(m.group(2).strip())
        return f"{{{txt}:{c_tag}}}"

    inner = re.sub(r'<span class="([^"]+)">(.*?)</span>', _span_repl, inner, flags=re.DOTALL)
    inner = html.unescape(inner)
    return [f"text: {inner}"]


def _script_lines_to_clause_html(
    sections: list[str],
    head_str: str,
    rows: list[str],
    text_lines: list[str],
    raw_clause: str,
) -> str:
    """Compile `section:`, `head:`/`row:`, or `text:` lines from `script.txt` into `clause_html`."""
    if raw_clause:
        return raw_clause
    if sections:
        sec_blocks: list[str] = []
        for sec in sections:
            parts = [p.strip() for p in sec.split("|") if p.strip()]
            if not parts:
                continue
            sec_title = html.escape(parts[0])
            cell_vals: list[tuple[str, str]] = []
            for p in parts[1:]:
                if ":" in p:
                    val_part, c_tag = p.rsplit(":", 1)
                    cls_name = _COLOR_TAG_TO_CLS.get(c_tag.strip(), "tok-gold")
                    cell_vals.append((cls_name, val_part.strip()))
                else:
                    cell_vals.append(("tok-gold", p))
            max_len = max((len(v.split("=", 1)[-1].strip()) for _, v in cell_vals), default=0)
            stack_cls = " stack" if max_len > 11 else ""
            spans_html = "".join(f'<span class="{c}">{html.escape(v)}</span>' for c, v in cell_vals)
            sec_blocks.append(
                f'<div class="etc-section"><div class="etc-sec-head">{sec_title}</div>'
                f'<div class="etc-coord-grid{stack_cls}">{spans_html}</div></div>'
            )
        return f'<div class="etc-table-block">{"".join(sec_blocks)}</div>'

    if rows:
        row_blocks: list[str] = []
        for r in rows:
            parts = [p.strip() for p in r.split("|")]
            if len(parts) < 2:
                continue
            lbl = parts[0]
            cells_raw = parts[1:]
            if len(cells_raw) == 1:
                rhs = cells_raw[0]
                if ":" in rhs:
                    val_part, c_tag = rhs.rsplit(":", 1)
                    c_tag = c_tag.strip()
                    val_part = val_part.strip()
                else:
                    val_part, c_tag = rhs, "gold"
                cls_name = _COLOR_TAG_TO_CLS.get(c_tag, "tok-gold")
                row_cls = "etc-data-row muted-row" if c_tag == "muted" else "etc-data-row"
                row_blocks.append(
                    f'<div class="{row_cls}"><span class="etc-row-label">{html.escape(lbl)}</span>'
                    f'<span class="{cls_name}">{html.escape(val_part)}</span></div>'
                )
            else:
                default_c_tag = "gold"
                if ":" in cells_raw[-1]:
                    _, maybe_c = cells_raw[-1].rsplit(":", 1)
                    if maybe_c.strip() in _COLOR_TAG_TO_CLS:
                        default_c_tag = maybe_c.strip()
                cell_spans: list[str] = []
                all_muted = True
                for cell_str in cells_raw:
                    c_tag = default_c_tag
                    val_part = cell_str
                    if ":" in cell_str:
                        vp, ct = cell_str.rsplit(":", 1)
                        if ct.strip() in _COLOR_TAG_TO_CLS:
                            val_part = vp.strip()
                            c_tag = ct.strip()
                    if c_tag != "muted":
                        all_muted = False
                    cls_name = _COLOR_TAG_TO_CLS.get(c_tag, "tok-gold")
                    cell_spans.append(f'<span class="{cls_name}">{html.escape(val_part)}</span>')
                row_cls = "etc-data-row muted-row" if all_muted else "etc-data-row"
                row_blocks.append(
                    f'<div class="{row_cls}"><span class="etc-row-label">{html.escape(lbl)}</span>'
                    f'<div class="etc-row-cells">{"".join(cell_spans)}</div></div>'
                )

        if "|" in (head_str or ""):
            h_parts = [p.strip() for p in head_str.split("|") if p.strip()]
            h_title = html.escape(h_parts[0])
            col_spans = "".join(f"<span>{html.escape(cp)}</span>" for cp in h_parts[1:])
            head_html = f'<div class="etc-sec-head-row"><span class="etc-sec-head">{h_title}</span><div class="etc-head-cols">{col_spans}</div></div>'
        else:
            head_html = f'<div class="etc-sec-head">{html.escape(head_str or "Incident Central Lines")}</div>'
        return f'<div class="etc-table-block">{head_html}<div class="etc-data-list">{"".join(row_blocks)}</div></div>'

    combined = " ".join(text_lines).strip()
    combined = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", combined)

    def _tok_repl(m: re.Match) -> str:
        tok_txt = m.group(1)
        c_tag = m.group(2).strip()
        cls_name = _COLOR_TAG_TO_CLS.get(c_tag, "tok-gold")
        return f'<span class="{cls_name}">{tok_txt}</span>'

    combined = re.sub(
        r"\{([^{}]+?):(gold|orange|teal|blue|purple|orchid|pink|green|lime|muted)\}",
        _tok_repl,
        combined,
    )
    return f'<span class="clause-line">{combined}</span>'


def _split_act_text_for_subslides(act_idx: int, act_text: str, count: int) -> list[str]:
    """Split a single `[bell:...]` act paragraph cleanly across `count` subslides so joined `say:` lines equal `act_text`."""
    text = " ".join(act_text.strip().split())
    if count <= 1 or not text:
        return [text]

    if count == 2:
        if act_idx == 0:
            # Split before the final <pause> clause (which introduces the circle/secondary feature)
            idx = text.rfind("<pause>")
            if idx > 0:
                return [text[:idx].strip(), text[idx:].strip()]
        else:
            # Act 3: split before "<pause> Across" or "<pause> Notice across" or last sentence
            for marker in ("<pause> Across ", "<pause> Notice across ", "<pause> On the right "):
                idx = text.find(marker)
                if idx > 0:
                    return [text[:idx].strip(), text[idx:].strip()]
            idx = text.rfind("<pause>")
            if idx > 0:
                return [text[:idx].strip(), text[idx:].strip()]

    if count == 3:
        # Act 2: coordinates sentence(s) -> primary central line -> remaining central lines
        line_start = -1
        for marker in (
            "<pause> Toggle the central lines,",
            "<pause> On the central lines layer,",
            "<pause> Because the point of tangency",
        ):
            pos = text.find(marker)
            if pos > 0:
                line_start = pos
                break
        if line_start < 0:
            # Fallback: split at first ". <pause>"
            pos = text.find(". <pause>")
            if pos > 0:
                line_start = pos + 2
        if line_start > 0:
            part1 = text[:line_start].strip()
            rest = text[line_start:].strip()
            # Split `rest` after the first central line clause (second `<pause>` inside `rest` after initial `<pause>`)
            p_positions = [m.start() for m in re.finditer(r"<pause>", rest)]
            if len(p_positions) >= 3:
                split2 = p_positions[2]
                return [part1, rest[:split2].strip(), rest[split2:].strip()]
            elif len(p_positions) >= 2:
                split2 = p_positions[1]
                return [part1, rest[:split2].strip(), rest[split2:].strip()]
            return [part1, rest, ""]

    # Fallback proportional split on `<pause>` boundaries
    parts = [p.strip() for p in re.split(r"(?=<pause>)", text) if p.strip()]
    if len(parts) >= count:
        out: list[str] = []
        chunk = max(1, len(parts) // count)
        for i in range(count - 1):
            out.append(" ".join(parts[i * chunk : (i + 1) * chunk]))
        out.append(" ".join(parts[(count - 1) * chunk :]))
        return out
    return [text] + [""] * (count - 1)


def format_unified_script(scenes: list[dict[str, Any]], raw_script_text: str) -> str:
    """Format a complete unified `script.txt` with top-level metadata, `[bell:...]` acts, `[screen:...]` directives, `zoom:` specs, and `say:` narration."""
    first_sub = scenes[0]["subslides"][0]
    short_code = first_sub.get("short_code") or "X_1"
    title = first_sub.get("g_id") or ""
    folio = first_sub.get("folio") or "Kimberling ETC • Collection 1 (X_1–X_19)"
    enunciation = first_sub.get("enunciation") or ""

    out: list[str] = [
        f"center: {short_code}",
        f"title: {title}",
        f"folio: {folio}",
        f"enunciation: {enunciation}",
        "",
    ]

    # Extract `[bell:...]` blocks from raw_script_text
    bell_blocks: list[tuple[str, str]] = []
    cur_bell = "proposition"
    cur_lines: list[str] = []
    for line in raw_script_text.splitlines():
        s = line.strip()
        if not s:
            continue
        m = re.match(r"^\[bell:([^\]]+)\]$", s, flags=re.IGNORECASE)
        if m:
            if cur_lines:
                bell_blocks.append((cur_bell, " ".join(cur_lines)))
                cur_lines = []
            cur_bell = m.group(1).strip()
        else:
            cur_lines.append(s)
    if cur_lines:
        bell_blocks.append((cur_bell, " ".join(cur_lines)))

    for act_idx, sc in enumerate(scenes):
        bell_name = bell_blocks[act_idx][0] if act_idx < len(bell_blocks) else "proposition"
        act_spoken = bell_blocks[act_idx][1] if act_idx < len(bell_blocks) else ""
        subslides = sc.get("subslides") or []
        say_parts = _split_act_text_for_subslides(act_idx, act_spoken, len(subslides))

        out.append(f"[bell:{bell_name}]")
        out.append("")

        for sub_idx, sub in enumerate(subslides):
            kind = sub.get("step_kind") or "CONSTRUCT"
            svg_name = Path(sub.get("svg_path") or "01_primary.svg").name
            weight = sub.get("weight", 1.0)
            header_parts = [f"screen: {kind}", f"svg: {svg_name}", f"weight: {weight:g}"]
            if sub.get("is_punchline"):
                header_parts.append("punchline: true")
            out.append("[" + " | ".join(header_parts) + "]")

            if sub.get("symbolic"):
                out.append(f"symbolic: {sub['symbolic']}")
            if sub.get("zoom"):
                out.append("zoom: " + ", ".join(sub["zoom"]))
            if sub.get("thumb_zoom"):
                out.append("thumb_zoom: " + ", ".join(sub["thumb_zoom"]))
            if sub.get("active_ids"):
                out.append("active: " + ", ".join(sub["active_ids"]))
            if sub.get("coincide_ids"):
                out.append("coincide: " + ", ".join(sub["coincide_ids"]))
            if sub.get("equal_ids"):
                out.append("equal: " + ", ".join(sub["equal_ids"]))

            out.extend(_html_clause_to_script_lines(sub.get("clause_html") or ""))

            j_tag = sub.get("just_tag") or ""
            j_id = sub.get("just_id") or ""
            j_title = sub.get("just_title") or ""
            if j_tag or j_id or j_title:
                out.append(f"just: {j_tag} | {j_id} | {j_title}")

            say_txt = say_parts[sub_idx] if sub_idx < len(say_parts) else ""
            if say_txt:
                out.append(f"say: {say_txt}")
            out.append("")

    return "\n".join(out).rstrip() + "\n"


def compile_scenes_from_script(script_text: str, svgs_dir: Path) -> list[dict[str, Any]]:
    """Compile a unified `script.txt` (containing `[bell:...]`, `[screen:...]`, `zoom:`, `active:`, `section:`, `row:`, `text:`, `just:`, `say:`) into `scenes.json` structure."""
    meta: dict[str, str] = {
        "center": "X_1",
        "title": "INCENTER",
        "folio": "Kimberling ETC • Collection 1 (X_1–X_19)",
        "enunciation": "",
    }

    acts: list[dict[str, Any]] = []
    cur_act: dict[str, Any] | None = None
    cur_screen: dict[str, Any] | None = None

    def _flush_screen() -> None:
        nonlocal cur_screen, cur_act
        if not cur_screen:
            return
        if cur_act is None:
            cur_act = {"bell": "proposition", "screens": []}
            acts.append(cur_act)
        cur_act["screens"].append(cur_screen)
        cur_screen = None

    for raw_line in script_text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("===") or re.match(r"^\[style:[^\]]+\]$", line, flags=re.IGNORECASE):
            _flush_screen()
            continue

        bell_m = re.match(r"^\[bell:([^\]]+)\]$", line, flags=re.IGNORECASE)
        if bell_m:
            _flush_screen()
            cur_act = {"bell": bell_m.group(1).strip(), "screens": []}
            acts.append(cur_act)
            continue

        screen_m = re.match(r"^\[screen:\s*(.+)\]$", line, flags=re.IGNORECASE)
        if screen_m:
            _flush_screen()
            parts = [p.strip() for p in screen_m.group(1).split("|") if p.strip()]
            step_kind = parts[0] if parts else "CONSTRUCT"
            attrs: dict[str, str] = {}
            for p in parts[1:]:
                if ":" in p:
                    k, v = p.split(":", 1)
                    attrs[k.strip().lower()] = v.strip()
            cur_screen = {
                "step_kind": step_kind,
                "svg": attrs.get("svg", "01_primary.svg"),
                "weight": float(attrs["weight"]) if "weight" in attrs and attrs["weight"] != "auto" else None,
                "is_punchline": attrs.get("punchline", "").lower() in ("true", "1", "yes"),
                "symbolic": "",
                "zoom": [],
                "thumb_zoom": [],
                "active_ids": [],
                "coincide_ids": [],
                "equal_ids": [],
                "sections": [],
                "head": "",
                "rows": [],
                "text_lines": [],
                "raw_clause": "",
                "just_tag": "",
                "just_id": "",
                "just_title": "",
                "say_lines": [],
            }
            continue

        if cur_screen is None:
            # Top-level metadata header
            for key in ("center", "title", "folio", "enunciation"):
                if line.lower().startswith(f"{key}:"):
                    meta[key] = line.split(":", 1)[1].strip()
                    break
            continue

        # Inside a `[screen:...]` block
        if ":" in line:
            key, val = line.split(":", 1)
            k_low = key.strip().lower()
            val = val.strip()
            if k_low == "symbolic":
                cur_screen["symbolic"] = val
            elif k_low == "zoom":
                cur_screen["zoom"] = _split_id_list(val)
            elif k_low == "thumb_zoom":
                cur_screen["thumb_zoom"] = _split_id_list(val)
            elif k_low == "active":
                cur_screen["active_ids"] = _split_id_list(val)
            elif k_low == "coincide":
                cur_screen["coincide_ids"] = _split_id_list(val)
            elif k_low == "equal":
                cur_screen["equal_ids"] = _split_id_list(val)
            elif k_low == "section":
                cur_screen["sections"].append(val)
            elif k_low == "head":
                cur_screen["head"] = val
            elif k_low == "row":
                cur_screen["rows"].append(val)
            elif k_low == "text":
                cur_screen["text_lines"].append(val)
            elif k_low == "clause":
                cur_screen["raw_clause"] = val
            elif k_low == "just":
                j_parts = [p.strip() for p in val.split("|")]
                cur_screen["just_tag"] = j_parts[0] if len(j_parts) > 0 else ""
                cur_screen["just_id"] = j_parts[1] if len(j_parts) > 1 else ""
                cur_screen["just_title"] = j_parts[2] if len(j_parts) > 2 else ""
            elif k_low == "say":
                cur_screen["say_lines"].append(val)

    _flush_screen()

    total_steps = sum(len(a["screens"]) for a in acts)
    short_code = meta["center"]
    short_title = meta["title"]
    prop_id = f"ETC • {short_code}" if short_code.startswith("X_") else f"ETC.{short_code}"
    common = {
        "prop_id": prop_id,
        "short_code": short_code,
        "g_id": short_title,
        "folio": meta["folio"],
        "enunciation": meta["enunciation"],
        "step_total": total_steps,
        "visible_ids": ["*"],
    }

    scenes: list[dict[str, Any]] = []
    step_counter = 0
    for act_idx, act in enumerate(acts, start=1):
        subslides: list[dict[str, Any]] = []
        for scr in act["screens"]:
            step_counter += 1
            say_joined = " ".join(scr["say_lines"]).strip()
            auto_w = max(0.35, len(re.sub(r"<pause>", "", say_joined).split()) / 18.0) if say_joined else 1.0
            weight = scr["weight"] if scr["weight"] is not None else round(auto_w, 2)
            clause_html = _script_lines_to_clause_html(
                scr["sections"],
                scr["head"],
                scr["rows"],
                scr["text_lines"],
                scr["raw_clause"],
            )
            has_highlights = bool(scr["active_ids"] or scr["coincide_ids"] or scr["equal_ids"])
            sub_dict: dict[str, Any] = {
                **common,
                "type": "euclid_step",
                "weight": weight,
                "step_num": step_counter,
                "step_kind": scr["step_kind"],
                "svg_path": str(svgs_dir / scr["svg"]),
                "symbolic": scr["symbolic"],
                "clause_html": clause_html,
                "just_tag": scr["just_tag"],
                "just_id": scr["just_id"],
                "just_title": scr["just_title"],
            }
            if scr["is_punchline"]:
                sub_dict["is_punchline"] = True
            if has_highlights:
                sub_dict["strict_step_ids"] = True
                sub_dict["active_ids"] = scr["active_ids"]
                sub_dict["coincide_ids"] = scr["coincide_ids"]
                sub_dict["equal_ids"] = scr["equal_ids"]
            if scr["zoom"]:
                sub_dict["zoom"] = scr["zoom"]
            if scr["thumb_zoom"]:
                sub_dict["thumb_zoom"] = scr["thumb_zoom"]
            subslides.append(sub_dict)

        scenes.append(
            {
                "id": f"act_{act_idx}_{act['bell']}",
                "title": f"{short_code} {short_title} — Act {act_idx}",
                "subslides": subslides,
            }
        )

    return scenes


def _plotted_points_in_svg(svg_path: Path) -> set[str]:
    """Return the set of `<circle class="point ...">` IDs present in `#points` of `svg_path`."""
    if not svg_path.exists():
        return set()
    svg_txt = svg_path.read_text()
    pts_idx = svg_txt.find('id="points"')
    sub = svg_txt[pts_idx:] if pts_idx >= 0 else svg_txt
    return set(re.findall(r'<circle[^>]*\bid="([^"]+)"', sub))


def _expand_brace_points(
    id_list: list[str],
    plotted_pts: set[str],
    reg: CenterRegistry | None = None,
) -> list[str]:
    """Expand `{1, 2, 8, 10}:orange` and `X_k:blue` items into ordered `X_k` point IDs in `plotted_pts`, filtering extreme exterior outliers when a tight cluster exists."""
    raw_out: list[str] = []
    for item in id_list:
        s = re.sub(r":(gold|orange|teal|blue|purple|orchid|pink|green|lime|muted)$", "", item.strip(), flags=re.IGNORECASE).strip()
        if s.startswith("{") and s.endswith("}"):
            for k_str in s[1:-1].split(","):
                k_str = k_str.strip()
                if k_str.isdigit():
                    pt_id = f"X_{k_str}"
                    if (not plotted_pts or pt_id in plotted_pts) and pt_id not in raw_out:
                        raw_out.append(pt_id)
        elif (
            s.startswith("X_")
            and (not plotted_pts or s in plotted_pts)
            and s not in raw_out
        ):
            raw_out.append(s)

    if reg and len(raw_out) > 4:
        near_out: list[str] = []
        for pid in raw_out:
            k = int(pid.split("_")[1])
            xy = reg.xy_cache.get(k)
            if xy and -0.15 <= xy[0] <= 1.15 and -0.15 <= xy[1] <= 0.72:
                near_out.append(pid)
        if len(near_out) >= 4:
            return near_out
    return raw_out


def build_center_video_package(
    num: int,
    target_center: dict[str, Any],
    svgs_dir: Path,
    acute_reg: CenterRegistry,
    kimberling_reg: CenterRegistry,
) -> tuple[str, list[dict[str, Any]], list[int]]:
    """Build `(script_text, scenes_list, partner_nums)` for center `X_num` using the unified script format with `[screen:...]` and `zoom:` specs."""
    prof = _COLLECTION_1_PROFILES.get(num)
    raw_title = target_center.get("title") or f"X_{num}"
    short_title = prof["short_title"] if prof else raw_title.split("(")[0].strip()
    enunciation = prof["enunciation"] if prof else (target_center.get("notes") or [raw_title])[0]
    partner_nums = prof["partners"] if prof else [1, 2, 3, 4, 6]

    # Compute Kimberling (6, 9, 13) search value (actual shortest directed trilinear distance on (6,9,13))
    k_bary = kimberling_reg.bary_cache.get(num, (1.0, 1.0, 1.0))
    k_ctx = kimberling_reg.ctx
    denom = k_bary[0] + k_bary[1] + k_bary[2]
    if abs(denom) > 1e-12:
        k_search = 2.0 * k_ctx.area * (k_bary[0] / k_ctx.raw_a) / denom
    else:
        k_search = 0.0
    search_str = target_center.get("search_value") or f"{k_search:.12f}"

    if prof:
        raw_script_text = prof["script"]
        s1_sym, s1_clause, s1_jid, s1_jtitle = prof["s1"]
        s2_sym, _, s2_jid, s2_jtitle = prof["s2"]
        s3_sym, s3_clause, s3_jid, s3_jtitle = prof["s3"]
        s4_sym, s4_clause, s4_jid, s4_jtitle = prof["s4"]
    else:
        spoken = _SPOKEN_NUMS.get(num, f"X {num}")
        tri_f = _clean_formula((target_center.get("trilinears") or ["1 : 1 : 1"])[0])
        bary_f = _clean_formula((target_center.get("barycentrics") or ["a : b : c"])[0])
        raw_script_text = f"""[bell:proposition]
In the Encyclopedia of Triangle Centers, <pause> {spoken} is {short_title}.

[bell:construction]
Its homogeneous coordinates determine both its perpendicular trilinear distances to sidelines B C, C A, and A B, <pause> and its barycentric sub-triangle areas. <pause> On the central lines layer, <pause> {spoken} lies at the intersection of classical central lines of triangle A B C.

[bell:insight]
Across acute, right, Kepler, and Kimberling reference triangles, <pause> {spoken} preserves its exact projective and conjugate relations.
"""
        s1_sym = f"X_{num} = {short_title}"
        s1_clause = f'<span class="clause-line"><span class="g-tok">X_{num}</span> is <b>{html.escape(short_title)}</b> on reference triangle <span class="g-tok">ABC</span>.</span>'
        s1_jid = f"ETC • X_{num}"
        s1_jtitle = enunciation[:110]
        s2_sym = f"α:β:γ = {tri_f[:24]} • u:v:w = {bary_f[:24]}"
        s2_jid = "HOMOGENEOUS COORDINATES"
        s2_jtitle = "Bridge identity: u : v : w = a·α : b·β : c·γ."
        s3_sym = f"Incident Central Lines through X_{num}"
        s3_clause = f'<span class="clause-line"><b>Incident Central Lines:</b> <span class="g-tok">X_{num}</span> lies at the concurrence of classical central lines of <span class="g-tok">△ABC</span>.</span>'
        s3_jid = "COLLINEARITIES"
        s3_jtitle = "Central lines toggled via .show-lines on the primary construction."
        s4_sym = f"Functional Relations of X_{num}"
        s4_clause = f'<span class="clause-line"><b>Functional Relations:</b> Conjugates and homothetic partners of <span class="g-tok">X_{num}</span> on <span class="g-tok">△ABC</span>.</span>'
        s4_jid = "CONJUGATE TRANSFORMATIONS"
        s4_jtitle = "Isogonal, isotomic, and complementary partners."

    # Coordinate text & graphic colors across all 7 sequenced steps
    primary_svg_path = svgs_dir / "01_primary.svg"
    plotted_pts = _plotted_points_in_svg(primary_svg_path)
    construction_ids, secondary_poly_ids, circle_ids = _parse_primary_svg_elements(primary_svg_path, num, s1_clause)

    s1a_clause, s1b_clause, step1_active, step2_active = _format_primary_construction_steps(
        num, short_title, construction_ids, secondary_poly_ids, circle_ids
    )
    s2_coord_clause = _format_component_colored_coordinates_clause(num, target_center)
    s3a_clause, s3b_clause, step4_active, step5_active, _ = _sequence_central_lines_clause(s3_clause, num)
    s4_norm_clause, rel_active, rel_coincide, rel_equal = _normalize_relations_clause(s4_clause, num, acute_reg)
    s5_triangles_clause = _format_reference_triangles_clause()

    # Compute default zoom specs per step
    step1_zoom = ["A", "B", "C"]
    if num == 1:
        step2_zoom = ["incircle", "I_a", "I_b", "I_c"]
    else:
        step2_zoom = [f"X_{num}"] + circle_ids + [
            p for p in (secondary_poly_ids + construction_ids)
            if not p.startswith("[") and not p.startswith("poly-")
        ]
        if len(step2_zoom) <= 1:
            step2_zoom = ["A", "B", "C"]

    step4_zoom = _expand_brace_points(step4_active, plotted_pts, acute_reg) or [f"X_{num}"]
    step5_zoom = _expand_brace_points(step5_active, plotted_pts, acute_reg) or step4_zoom

    rel_pts: list[str] = []
    for item in rel_active + rel_coincide + rel_equal + ["X_3"]:
        clean_it = item.split(":", 1)[0].strip()
        if clean_it.startswith("X_") and clean_it not in rel_pts:
            rel_pts.append(clean_it)
    step6_zoom = rel_pts or [f"X_{num}", "X_3"]

    common = {
        "prop_id": f"ETC • X_{num}",
        "short_code": f"X_{num}",
        "g_id": short_title,
        "folio": "Kimberling ETC • Collection 1 (X_1–X_19)",
        "enunciation": enunciation,
        "step_total": 7,
        "visible_ids": ["*"],
    }

    seed_scenes = [
        {
            "id": "act_1_primary",
            "title": f"X_{num} {short_title} — Primary Construction",
            "subslides": [
                {
                    **common,
                    "type": "euclid_step",
                    "weight": 1.0,
                    "step_num": 1,
                    "step_kind": "CONSTRUCT",
                    "svg_path": str(svgs_dir / "01_primary.svg"),
                    "symbolic": s1_sym,
                    "clause_html": s1a_clause,
                    "just_tag": "∵ CONCURRENCE",
                    "just_id": s1_jid,
                    "just_title": s1_jtitle,
                    "strict_step_ids": True,
                    "active_ids": step1_active,
                    "coincide_ids": [],
                    "equal_ids": [],
                    "zoom": step1_zoom,
                },
                {
                    **common,
                    "type": "euclid_step",
                    "is_punchline": True,
                    "weight": 1.0,
                    "step_num": 2,
                    "step_kind": "GOAL",
                    "svg_path": str(svgs_dir / "01_primary.svg"),
                    "symbolic": s1_sym,
                    "clause_html": s1b_clause,
                    "just_tag": "∵ DEFINITION",
                    "just_id": s1_jid,
                    "just_title": s1_jtitle,
                    "strict_step_ids": True,
                    "active_ids": step2_active,
                    "coincide_ids": [],
                    "equal_ids": [],
                    "zoom": step2_zoom,
                    "thumb_zoom": ["A", "B", "C"],
                },
            ],
        },
        {
            "id": "act_2_coordinates_and_lines",
            "title": f"X_{num} Coordinates & Central Lines",
            "subslides": [
                {
                    **common,
                    "type": "euclid_step",
                    "weight": 1.15,
                    "step_num": 3,
                    "step_kind": "ASSERT",
                    "svg_path": str(svgs_dir / "02_coordinates.svg"),
                    "symbolic": s2_sym,
                    "clause_html": s2_coord_clause,
                    "just_tag": "∵ COORDINATES",
                    "just_id": s2_jid,
                    "just_title": s2_jtitle,
                },
                {
                    **common,
                    "type": "euclid_step",
                    "weight": 0.50,
                    "step_num": 4,
                    "step_kind": "INTERSECT",
                    "svg_path": str(svgs_dir / "03_central_lines.svg"),
                    "symbolic": s3_sym,
                    "clause_html": s3a_clause,
                    "just_tag": "∵ PRIMARY AXIS",
                    "just_id": s3_jid,
                    "just_title": s3_jtitle,
                    "strict_step_ids": True,
                    "active_ids": step4_active,
                    "coincide_ids": [],
                    "equal_ids": [],
                    "zoom": step4_zoom,
                },
                {
                    **common,
                    "type": "euclid_step",
                    "weight": 0.55,
                    "step_num": 5,
                    "step_kind": "INTERSECT",
                    "svg_path": str(svgs_dir / "03_central_lines.svg"),
                    "symbolic": s3_sym,
                    "clause_html": s3b_clause,
                    "just_tag": "∵ COLLINEARITIES",
                    "just_id": s3_jid,
                    "just_title": s3_jtitle,
                    "strict_step_ids": True,
                    "active_ids": step5_active,
                    "coincide_ids": [],
                    "equal_ids": [],
                    "zoom": step5_zoom,
                },
            ],
        },
        {
            "id": "act_3_relations_and_triangles",
            "title": f"X_{num} Functional Relations & Four Reference Triangles",
            "subslides": [
                {
                    **common,
                    "type": "euclid_step",
                    "weight": 1.05,
                    "step_num": 6,
                    "step_kind": "PROVE",
                    "svg_path": str(svgs_dir / "04_relations.svg"),
                    "symbolic": s4_sym,
                    "clause_html": s4_norm_clause,
                    "just_tag": "∵ RELATIONS",
                    "just_id": s4_jid,
                    "just_title": s4_jtitle,
                    "strict_step_ids": True,
                    "active_ids": rel_active,
                    "coincide_ids": rel_coincide,
                    "equal_ids": rel_equal,
                    "zoom": step6_zoom,
                },
                {
                    **common,
                    "type": "euclid_step",
                    "weight": 0.95,
                    "step_num": 7,
                    "step_kind": "∴",
                    "svg_path": str(svgs_dir / "05_four_triangles.svg"),
                    "symbolic": f"Kimberling (6, 9, 13) Search = {search_str}",
                    "clause_html": s5_triangles_clause,
                    "just_tag": "∵ INVARIANCE",
                    "just_id": f"KIMBERLING SEARCH VALUE • X_{num}",
                    "just_title": f"Shortest directed trilinear distance on reference triangle (6, 9, 13): {search_str}.",
                },
            ],
        },
    ]

    unified_script = format_unified_script(seed_scenes, raw_script_text)
    compiled_scenes = compile_scenes_from_script(unified_script, svgs_dir)
    return unified_script, compiled_scenes, partner_nums


