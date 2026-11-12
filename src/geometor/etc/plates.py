"""Generalized exact symbolic 5-Act documentation plate generators for GEOMETOR ETC.

Generates interactive SVG plates for any triangle center ``X_n`` in ``CenterSymbolicRegistry``
with zero center-specific hardcoding and zero floating-point contamination in symbolic math:

- ``02_coordinates.svg`` — Homogeneous trilinear struts and signed barycentric sub-triangles
- ``03_central_lines.svg`` — Primary symbolic model with ``.show-lines`` active
- ``04_relations.svg`` — Algebraic conjugate, homothetic, and inversion partners
- ``05_four_triangles.svg`` — 2x2 invariance grid across Heronian, Right, Kepler, and Kimberling
"""

from __future__ import annotations

import functools
import html
import json
import math
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

import sympy as sp
from geometor.model import Model, exact_sign, zero_test

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
from .palette import REFERENCE_TRIANGLE_COLORS, token_hex
from .render import (
    EXPLORER_SVG_CSS,
    INTERACTIVE_SVG_JS,
    _load_center_names,
    model_to_elements_list,
    render_model_svg,
)
from .symbolic_cache import (
    EXACT_CYCLIC_BARYCENTRICS,
    CenterSymbolicRegistry,
    SymbolicCenterRecord,
    format_symbolic_latex,
    format_symbolic_pretty,
    reduce_homogeneous_triple,
)
from .triangles import CANONICAL_TRIANGLES, SymbolicTriangle


@dataclass(frozen=True)
class CircleCenterSpec:
    """Metadata for centers that are the center of a canonical named triangle circle."""

    circle_id: str
    circle_label: str
    stroke_hex: str
    stroke_rgba: str
    r_sym: str
    q_sym: str
    table_header: str
    radius_fn: Callable[[SymbolicTriangle], sp.Expr]


CIRCLE_CENTER_SPECS: dict[int, CircleCenterSpec] = {
    1: CircleCenterSpec(
        circle_id="incircle",
        circle_label="Incircle",
        stroke_hex="#f472b6",
        stroke_rgba="rgba(244, 114, 182, 0.54)",
        r_sym="r",
        q_sym="Q_r",
        table_header=r"Inradius & Quadrance :math:`(r,\, Q_r)`",
        radius_fn=lambda tri: tri.r,
    ),
    3: CircleCenterSpec(
        circle_id="circumcircle",
        circle_label="Circumcircle",
        stroke_hex="#a78bfa",
        stroke_rgba="rgba(167, 139, 250, 0.52)",
        r_sym="R",
        q_sym="Q_R",
        table_header=r"Circumradius & Quadrance :math:`(R,\, Q_R)`",
        radius_fn=lambda tri: tri.R,
    ),
    5: CircleCenterSpec(
        circle_id="nine_point_circle",
        circle_label="Nine-Point Circle",
        stroke_hex="#fb923c",
        stroke_rgba="rgba(251, 146, 60, 0.54)",
        r_sym="R_9",
        q_sym="Q_9",
        table_header=r"Nine-Point Radius :math:`(R_9,\, Q_9)`",
        radius_fn=lambda tri: tri.simplify(tri.R / sp.Integer(2)),
    ),
    10: CircleCenterSpec(
        circle_id="spieker_circle",
        circle_label="Spieker Circle",
        stroke_hex="#f472b6",
        stroke_rgba="rgba(244, 114, 182, 0.54)",
        r_sym="r_S",
        q_sym="Q_S",
        table_header=r"Spieker Radius :math:`(r_S,\, Q_S)`",
        radius_fn=lambda tri: tri.simplify(tri.r / sp.Integer(2)),
    ),
}


@dataclass(frozen=True)
class AlgebraicPartnerInfo:
    """Exact symbolic result of applying a triangle-center operator to ``X_n``."""

    operator: str
    partner_num: int | None
    partner_title: str
    xy: tuple[sp.Expr, sp.Expr] | None
    bary: tuple[sp.Expr, sp.Expr, sp.Expr] | None
    is_self: bool = False
    is_ideal: bool = False
    is_center_of_inversion: bool = False
    inversion_quadrance: sp.Expr | None = None
    inversion_scale: sp.Expr | None = None


@dataclass
class CenterRelationsBundle:
    """Exact algebraic operator results and rendered SVG catalog IDs for Act 4."""

    num: int
    preset: str
    isogonal: AlgebraicPartnerInfo
    isotomic: AlgebraicPartnerInfo
    complement: AlgebraicPartnerInfo
    anticomplement: AlgebraicPartnerInfo
    circumcircle_inverse: AlgebraicPartnerInfo
    galois_conjugate: AlgebraicPartnerInfo | None = None
    harmonic_feuerbach_partner: int | None = None
    plotted_partners: list[int] = field(default_factory=list)
    svg_ids: set[str] = field(default_factory=set)


def _svg_x(num: int | str, suffix: str = "") -> str:
    """Return SVG ``<tspan>`` subscript markup for ``X_n`` followed by optional ``suffix``."""
    if suffix:
        return (
            f'X<tspan dy="0.28em" font-size="74%">{num}</tspan>'
            f'<tspan dy="-0.28em">{html.escape(suffix)}</tspan>'
        )
    return f'X<tspan dy="0.28em" font-size="74%">{num}</tspan>'


def _to_screen(
    pt: tuple[float, float], scale: float, ox: float, oy: float
) -> tuple[float, float]:
    return (ox + pt[0] * scale, oy - pt[1] * scale)


def _fit_points_to_box(
    pts: list[tuple[float, float]],
    box_x: float,
    box_y: float,
    box_w: float,
    box_h: float,
) -> tuple[float, float, float]:
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


def _right_angle_path(
    foot_s: tuple[float, float],
    p_s: tuple[float, float],
    q_s: tuple[float, float],
    size: float = 13.0,
) -> str:
    vx = p_s[0] - foot_s[0]
    vy = p_s[1] - foot_s[1]
    v_len = math.hypot(vx, vy)
    ux = q_s[0] - foot_s[0]
    uy = q_s[1] - foot_s[1]
    u_len = math.hypot(ux, uy)
    if v_len < 18.0 or u_len < 1e-6:
        return ""
    eff_size = min(size, 0.38 * v_len)
    vx, vy = (vx / v_len) * eff_size, (vy / v_len) * eff_size
    ux, uy = (ux / u_len) * eff_size, (uy / u_len) * eff_size
    p1 = (foot_s[0] + ux, foot_s[1] + uy)
    p2 = (foot_s[0] + ux + vx, foot_s[1] + uy + vy)
    p3 = (foot_s[0] + vx, foot_s[1] + vy)
    return f"M {p1[0]:.1f},{p1[1]:.1f} L {p2[0]:.1f},{p2[1]:.1f} L {p3[0]:.1f},{p3[1]:.1f}"


def _safe_meta_json(catalog: dict[str, Any]) -> str:
    return (
        json.dumps(catalog, ensure_ascii=True, separators=(",", ":"))
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("&", "\\u0026")
    )


def exact_pedal_foot_and_param(
    p_xy: tuple[sp.Expr, sp.Expr],
    q1_xy: tuple[sp.Expr, sp.Expr],
    q2_xy: tuple[sp.Expr, sp.Expr],
    tri: SymbolicTriangle,
) -> tuple[tuple[sp.Expr, sp.Expr], sp.Expr]:
    """Return ``(foot_xy, t_param)`` for the exact orthogonal projection of ``p_xy`` onto ``q1_xy -> q2_xy``."""
    dx = tri.simplify(q2_xy[0] - q1_xy[0])
    dy = tri.simplify(q2_xy[1] - q1_xy[1])
    denom = tri.simplify(dx * dx + dy * dy)
    if zero_test(denom):
        return q1_xy, sp.Integer(0)
    t = tri.simplify(((p_xy[0] - q1_xy[0]) * dx + (p_xy[1] - q1_xy[1]) * dy) / denom)
    foot = (
        tri.simplify(q1_xy[0] + t * dx),
        tri.simplify(q1_xy[1] + t * dy),
    )
    return foot, t


def _exact_line_eq_pair(
    q1: tuple[sp.Expr, sp.Expr],
    q2: tuple[sp.Expr, sp.Expr],
    tri: SymbolicTriangle,
) -> tuple[str, str]:
    x_sym, y_sym = sp.Symbol("x"), sp.Symbol("y")
    a_c = tri.simplify(q1[1] - q2[1])
    b_c = tri.simplify(q2[0] - q1[0])
    c_c = tri.simplify(q1[0] * q2[1] - q2[0] * q1[1])
    for coeff in (a_c, b_c, c_c):
        if not zero_test(coeff):
            if exact_sign(coeff) < 0:
                a_c, b_c, c_c = tri.simplify(-a_c), tri.simplify(-b_c), tri.simplify(-c_c)
            break
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
    kp = tri.key == "kepler"
    return (
        f"{format_symbolic_latex(lhs, kepler_phi=kp)} = 0",
        f"{format_symbolic_pretty(lhs, kepler_phi=kp)} = 0",
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


def _sideline_extension_svg(
    q1_s: tuple[float, float],
    q2_s: tuple[float, float],
    foot_s: tuple[float, float],
    t_f: float,
    indent: str = "  ",
    stroke_w: float = 1.8,
) -> str:
    """Emit a dashed sideline extension only when the pedal foot lies strictly outside segment ``q1-q2``."""
    if t_f < -0.01:
        return (
            f'{indent}<line x1="{q1_s[0]:.1f}" y1="{q1_s[1]:.1f}" '
            f'x2="{foot_s[0]:.1f}" y2="{foot_s[1]:.1f}" '
            f'stroke="#64748b" stroke-width="{stroke_w}" stroke-dasharray="5,5" pointer-events="none" />\n'
        )
    if t_f > 1.01:
        return (
            f'{indent}<line x1="{q2_s[0]:.1f}" y1="{q2_s[1]:.1f}" '
            f'x2="{foot_s[0]:.1f}" y2="{foot_s[1]:.1f}" '
            f'stroke="#64748b" stroke-width="{stroke_w}" stroke-dasharray="5,5" pointer-events="none" />\n'
        )
    return ""


def generate_doc_coordinates_svg(
    num: int,
    title: str = "",
    preset: str = "heronian",
) -> str:
    """Generate Act 2 ``02_coordinates.svg`` for any center ``X_num`` in ``CenterSymbolicRegistry``."""
    tri = CANONICAL_TRIANGLES.get(preset, CANONICAL_TRIANGLES["heronian"])
    sym_reg = CenterSymbolicRegistry(tri)
    rec = sym_reg.get(num)
    center_names = _load_center_names()
    eff_title = title or center_names.get(str(num), f"Center X_{num}")
    kp = rec.is_kepler

    A_ex, B_ex, C_ex = tri.A_xy, tri.B_xy, tri.C_xy
    P_ex = rec.xy
    Pa_ex, ta_ex = exact_pedal_foot_and_param(P_ex, B_ex, C_ex, tri)
    Pb_ex, tb_ex = exact_pedal_foot_and_param(P_ex, C_ex, A_ex, tri)
    Pc_ex, tc_ex = exact_pedal_foot_and_param(P_ex, A_ex, B_ex, tri)

    A = (float(A_ex[0].evalf(20)), float(A_ex[1].evalf(20)))
    B = (float(B_ex[0].evalf(20)), float(B_ex[1].evalf(20)))
    C = (float(C_ex[0].evalf(20)), float(C_ex[1].evalf(20)))
    P = (float(P_ex[0].evalf(20)), float(P_ex[1].evalf(20)))
    Pa = (float(Pa_ex[0].evalf(20)), float(Pa_ex[1].evalf(20)))
    Pb = (float(Pb_ex[0].evalf(20)), float(Pb_ex[1].evalf(20)))
    Pc = (float(Pc_ex[0].evalf(20)), float(Pc_ex[1].evalf(20)))
    ta_f = float(ta_ex.evalf(15))
    tb_f = float(tb_ex.evalf(15))
    tc_f = float(tc_ex.evalf(15))

    fit_pts = [A, B, C, P, Pa, Pb, Pc]
    c_spec = CIRCLE_CENTER_SPECS.get(num)
    r_ex: sp.Expr | None = None
    if c_spec is not None:
        r_ex = c_spec.radius_fn(tri)
        r_f = float(r_ex.evalf(20))
        fit_pts.extend(
            [
                (P[0] - r_f, P[1]),
                (P[0] + r_f, P[1]),
                (P[0], P[1] - r_f),
                (P[0], P[1] + r_f),
            ]
        )

    scale, ox, oy = _fit_points_to_box(fit_pts, 110.0, 52.0, 780.0, 638.0)
    As = _to_screen(A, scale, ox, oy)
    Bs = _to_screen(B, scale, ox, oy)
    Cs = _to_screen(C, scale, ox, oy)
    Ps = _to_screen(P, scale, ox, oy)
    Pas = _to_screen(Pa, scale, ox, oy)
    Pbs = _to_screen(Pb, scale, ox, oy)
    Pcs = _to_screen(Pc, scale, ox, oy)

    ra_a = _right_angle_path(Pas, Ps, Cs if ta_f < 0.5 else Bs, size=14.0)
    ra_b = _right_angle_path(Pbs, Ps, As if tb_f < 0.5 else Cs, size=14.0)
    ra_c = _right_angle_path(Pcs, Ps, Bs if tc_f < 0.5 else As, size=14.0)

    ma = ((Ps[0] + Pas[0]) * 0.5 + 18.0, (Ps[1] + Pas[1]) * 0.5 - 6.0)
    mb = ((Ps[0] + Pbs[0]) * 0.5 - 26.0, (Ps[1] + Pbs[1]) * 0.5 - 6.0)
    mc = ((Ps[0] + Pcs[0]) * 0.5 + 20.0, (Ps[1] + Pcs[1]) * 0.5 + 6.0)

    fa_id, fb_id, fc_id = ("T_a", "T_b", "T_c")
    sa_id = f"/ X_{num} {fa_id} /"
    sb_id = f"/ X_{num} {fb_id} /"
    sc_id = f"/ X_{num} {fc_id} /"
    sub_a_id = f"< X_{num} B C >"
    sub_b_id = f"< X_{num} C A >"
    sub_c_id = f"< X_{num} A B >"
    sub_a_esc = html.escape(sub_a_id, quote=True)
    sub_b_esc = html.escape(sub_b_id, quote=True)
    sub_c_esc = html.escape(sub_c_id, quote=True)

    area_a, area_b, area_c = rec.sub_areas
    abs_a = tri.simplify(-area_a) if exact_sign(area_a) < 0 else area_a
    abs_b = tri.simplify(-area_b) if exact_sign(area_b) < 0 else area_b
    abs_c = tri.simplify(-area_c) if exact_sign(area_c) < 0 else area_c
    la_s = tri.simplify(sp.Integer(2) * abs_a / tri.a)
    lb_s = tri.simplify(sp.Integer(2) * abs_b / tri.b)
    lc_s = tri.simplify(sp.Integer(2) * abs_c / tri.c)
    qa_s = tri.simplify(la_s * la_s)
    qb_s = tri.simplify(lb_s * lb_s)
    qc_s = tri.simplify(lc_s * lc_s)

    catalog: dict[str, Any] = {
        "A": _pt_meta_entry("A", "Vertex A", "#66ff66", A_ex, "1 : 0 : 0", "1 : 0 : 0", kepler_phi=kp),
        "B": _pt_meta_entry("B", "Vertex B", "#66ff66", B_ex, "0 : 1 : 0", "0 : 1 : 0", kepler_phi=kp),
        "C": _pt_meta_entry("C", "Vertex C", "#f8f6f0", C_ex, "0 : 0 : 1", "0 : 0 : 1", kepler_phi=kp),
        f"X_{num}": _pt_meta_entry(
            f"X_{num}",
            eff_title,
            "#ffd700",
            P_ex,
            rec.bary_latex(),
            rec.bary_pretty(),
            rec.trilinear_latex(),
            rec.trilinear_pretty(),
            kepler_phi=kp,
        ),
        fa_id: _pt_meta_entry(fa_id, f"Right-Spread Pedal Foot {fa_id} on BC", "#e8b85a", Pa_ex, kepler_phi=kp),
        fb_id: _pt_meta_entry(fb_id, f"Right-Spread Pedal Foot {fb_id} on CA", "#38bdf8", Pb_ex, kepler_phi=kp),
        fc_id: _pt_meta_entry(fc_id, f"Right-Spread Pedal Foot {fc_id} on AB", "#5ec27e", Pc_ex, kepler_phi=kp),
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
                    "latex": format_symbolic_latex(s_len, kepler_phi=kp),
                    "pretty": format_symbolic_pretty(s_len, kepler_phi=kp),
                },
                {
                    "label": "Q",
                    "latex": format_symbolic_latex(q_side, kepler_phi=kp),
                    "pretty": format_symbolic_pretty(q_side, kepler_phi=kp),
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
                    "latex": f"{st_sym}_0 = {format_symbolic_latex(st_len, kepler_phi=kp)}",
                    "pretty": format_symbolic_pretty(st_len, kepler_phi=kp),
                },
                {
                    "label": "Q",
                    "latex": format_symbolic_latex(st_q, kepler_phi=kp),
                    "pretty": format_symbolic_pretty(st_q, kepler_phi=kp),
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
                    "latex": format_symbolic_latex(l_spk, kepler_phi=kp),
                    "pretty": format_symbolic_pretty(l_spk, kepler_phi=kp),
                },
                {
                    "label": "Q",
                    "latex": format_symbolic_latex(q_spk, kepler_phi=kp),
                    "pretty": format_symbolic_pretty(q_spk, kepler_phi=kp),
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
                    "latex": format_symbolic_latex(sub_area, kepler_phi=kp),
                    "pretty": format_symbolic_pretty(sub_area, kepler_phi=kp),
                },
                {
                    "label": f"{sym_u} / Δ",
                    "latex": format_symbolic_latex(share, kepler_phi=kp),
                    "pretty": format_symbolic_pretty(share, kepler_phi=kp),
                },
                {
                    "label": "bary",
                    "latex": rec.bary_latex(),
                    "pretty": rec.bary_pretty(),
                },
            ],
            "approx": f"≈ {float(sub_area.evalf(20)):.4f} ({pct:.1f}% of Δ)",
        }

    circle_svg = ""
    if c_spec is not None and r_ex is not None:
        r_scr = float(r_ex.evalf(20)) * scale
        q_c = tri.simplify(r_ex * r_ex)
        x_sym, y_sym = sp.Symbol("x"), sp.Symbol("y")
        eq_lhs = (x_sym - P_ex[0]) ** 2 + (y_sym - P_ex[1]) ** 2
        eq_ltx = f"{format_symbolic_latex(eq_lhs, kepler_phi=kp)} = {format_symbolic_latex(q_c, kepler_phi=kp)}"
        eq_prt = f"{format_symbolic_pretty(eq_lhs, kepler_phi=kp)} = {format_symbolic_pretty(q_c, kepler_phi=kp)}"
        catalog[c_spec.circle_id] = {
            "ID": c_spec.circle_id,
            "type": "circle",
            "color": c_spec.stroke_hex,
            "name": c_spec.circle_label,
            "symbolic_rows": [
                {"label": "eq", "latex": eq_ltx, "pretty": eq_prt},
                {
                    "label": c_spec.r_sym,
                    "latex": format_symbolic_latex(r_ex, kepler_phi=kp),
                    "pretty": format_symbolic_pretty(r_ex, kepler_phi=kp),
                },
                {
                    "label": c_spec.q_sym,
                    "latex": format_symbolic_latex(q_c, kepler_phi=kp),
                    "pretty": format_symbolic_pretty(q_c, kepler_phi=kp),
                },
            ],
            "approx": f"{c_spec.r_sym} ≈ {float(r_ex.evalf(20)):.6f}",
        }
        circle_svg = (
            f'  <circle id="{c_spec.circle_id}" data-id="{c_spec.circle_id}" '
            f'data-ref="{c_spec.circle_id}" class="etc-plate-circle" '
            f'cx="{Ps[0]:.1f}" cy="{Ps[1]:.1f}" r="{r_scr:.1f}" '
            f'fill="none" stroke="{c_spec.stroke_rgba}" stroke-width="2.2" stroke-dasharray="6,5" />\n'
        )

    ext_svg = (
        _sideline_extension_svg(Bs, Cs, Pas, ta_f)
        + _sideline_extension_svg(Cs, As, Pbs, tb_f)
        + _sideline_extension_svg(As, Bs, Pcs, tc_f)
    )

    ra_nodes = ""
    for ra_d, ra_col in [(ra_a, "#e8b85a"), (ra_b, "#38bdf8"), (ra_c, "#5ec27e")]:
        if ra_d:
            ra_nodes += (
                f'  <path d="{ra_d}" fill="none" stroke="{ra_col}" '
                f'stroke-width="2.4" opacity="0.9" pointer-events="none" />\n'
            )

    strut_lbl_nodes = ""
    for m_pt, st_end, g_ch, g_col in [
        (ma, Pas, "α", "#e8b85a"),
        (mb, Pbs, "β", "#38bdf8"),
        (mc, Pcs, "γ", "#5ec27e"),
    ]:
        if math.hypot(Ps[0] - st_end[0], Ps[1] - st_end[1]) >= 22.0:
            strut_lbl_nodes += (
                f'    <rect x="{m_pt[0] - 8:.1f}" y="{m_pt[1] - 24:.1f}" width="34" height="30" rx="6" fill="rgba(13, 17, 26, 0.86)" />\n'
                f'    <text x="{m_pt[0]:.1f}" y="{m_pt[1]:.1f}" fill="{g_col}">{g_ch}</text>\n'
            )

    c_lbl_x = Cs[0] - 10.0
    c_lbl_y = Cs[1] - 18.0
    x_badge_dx = 0.0
    if math.hypot(Ps[0] - Cs[0], Ps[1] - Cs[1]) < 56.0:
        c_lbl_x = Cs[0] - 32.0
        c_lbl_y = Cs[1] - 10.0
        x_badge_dx = 26.0

    fld_str = tri.coordinate_field_pretty([*rec.xy, *rec.bary])
    sub_caption = (
        f"{tri.label} • {fld_str} • Δ = {format_symbolic_pretty(tri.area, kepler_phi=kp)}"
    )
    meta_json = _safe_meta_json(catalog)

    return f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg class="geometor-etc-drawing" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 760" data-initial-viewbox="0 0 1000 760" data-triangle="{html.escape(preset)}" data-field="{html.escape(fld_str)}" width="100%" height="100%" preserveAspectRatio="xMidYMid meet">
  <style>{EXPLORER_SVG_CSS}</style>
  <defs>
    <filter id="glow-coord" filterUnits="userSpaceOnUse" x="-100" y="-100" width="1200" height="960">
      <feGaussianBlur stdDeviation="4.5" result="blur" />
      <feMerge><feMergeNode in="blur" /><feMergeNode in="SourceGraphic" /></feMerge>
    </filter>
  </defs>

  <polygon id="{sub_a_esc}" data-id="{sub_a_esc}" data-ref="{sub_a_esc}" class="etc-plate-poly"
           points="{Ps[0]:.1f},{Ps[1]:.1f} {Bs[0]:.1f},{Bs[1]:.1f} {Cs[0]:.1f},{Cs[1]:.1f}"
           fill="#e8b85a" fill-opacity="0.19" stroke="none" />
  <polygon id="{sub_b_esc}" data-id="{sub_b_esc}" data-ref="{sub_b_esc}" class="etc-plate-poly"
           points="{Ps[0]:.1f},{Ps[1]:.1f} {Cs[0]:.1f},{Cs[1]:.1f} {As[0]:.1f},{As[1]:.1f}"
           fill="#38bdf8" fill-opacity="0.17" stroke="none" />
  <polygon id="{sub_c_esc}" data-id="{sub_c_esc}" data-ref="{sub_c_esc}" class="etc-plate-poly"
           points="{Ps[0]:.1f},{Ps[1]:.1f} {As[0]:.1f},{As[1]:.1f} {Bs[0]:.1f},{Bs[1]:.1f}"
           fill="#5ec27e" fill-opacity="0.17" stroke="none" />

{circle_svg}{ext_svg}  <line id="[ B C ]" data-id="[ B C ]" data-ref="[ B C ]" class="etc-plate-line"
        x1="{Bs[0]:.1f}" y1="{Bs[1]:.1f}" x2="{Cs[0]:.1f}" y2="{Cs[1]:.1f}"
        stroke="#cbd5e1" stroke-width="2.8" stroke-dasharray="2, 4.5" stroke-linecap="round" />
  <line id="[ C A ]" data-id="[ C A ]" data-ref="[ C A ]" class="etc-plate-line"
        x1="{Cs[0]:.1f}" y1="{Cs[1]:.1f}" x2="{As[0]:.1f}" y2="{As[1]:.1f}"
        stroke="#cbd5e1" stroke-width="2.8" stroke-dasharray="2, 4.5" stroke-linecap="round" />
  <line id="[ A B ]" data-id="[ A B ]" data-ref="[ A B ]" class="etc-plate-line"
        x1="{As[0]:.1f}" y1="{As[1]:.1f}" x2="{Bs[0]:.1f}" y2="{Bs[1]:.1f}"
        stroke="#cbd5e1" stroke-width="2.8" stroke-dasharray="2, 4.5" stroke-linecap="round" />

  <line id="/ X_{num} A /" data-id="/ X_{num} A /" data-ref="/ X_{num} A /" class="etc-plate-line"
        x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{As[0]:.1f}" y2="{As[1]:.1f}" stroke="#cbd5e1" stroke-width="2.2" stroke-dasharray="10,5,2.5,5" opacity="0.65" />
  <line id="/ X_{num} B /" data-id="/ X_{num} B /" data-ref="/ X_{num} B /" class="etc-plate-line"
        x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{Bs[0]:.1f}" y2="{Bs[1]:.1f}" stroke="#cbd5e1" stroke-width="2.2" stroke-dasharray="10,5,2.5,5" opacity="0.65" />
  <line id="/ X_{num} C /" data-id="/ X_{num} C /" data-ref="/ X_{num} C /" class="etc-plate-line"
        x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{Cs[0]:.1f}" y2="{Cs[1]:.1f}" stroke="#cbd5e1" stroke-width="2.2" stroke-dasharray="10,5,2.5,5" opacity="0.65" />

{ra_nodes}  <line id="{sa_id}" data-id="{sa_id}" data-ref="{sa_id}" class="etc-plate-strut"
        x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{Pas[0]:.1f}" y2="{Pas[1]:.1f}"
        stroke="#e8b85a" stroke-width="5.2" stroke-linecap="round" filter="url(#glow-coord)" />
  <line id="{sb_id}" data-id="{sb_id}" data-ref="{sb_id}" class="etc-plate-strut"
        x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{Pbs[0]:.1f}" y2="{Pbs[1]:.1f}"
        stroke="#38bdf8" stroke-width="5.2" stroke-linecap="round" filter="url(#glow-coord)" />
  <line id="{sc_id}" data-id="{sc_id}" data-ref="{sc_id}" class="etc-plate-strut"
        x1="{Ps[0]:.1f}" y1="{Ps[1]:.1f}" x2="{Pcs[0]:.1f}" y2="{Pcs[1]:.1f}"
        stroke="#5ec27e" stroke-width="5.2" stroke-linecap="round" filter="url(#glow-coord)" />

  <circle id="{fa_id}" data-id="{fa_id}" data-ref="{fa_id}" class="etc-plate-pt"
          cx="{Pas[0]:.1f}" cy="{Pas[1]:.1f}" r="6.2" fill="#e8b85a" stroke="#0d111a" stroke-width="2" />
  <circle id="{fb_id}" data-id="{fb_id}" data-ref="{fb_id}" class="etc-plate-pt"
          cx="{Pbs[0]:.1f}" cy="{Pbs[1]:.1f}" r="6.2" fill="#38bdf8" stroke="#0d111a" stroke-width="2" />
  <circle id="{fc_id}" data-id="{fc_id}" data-ref="{fc_id}" class="etc-plate-pt"
          cx="{Pcs[0]:.1f}" cy="{Pcs[1]:.1f}" r="6.2" fill="#5ec27e" stroke="#0d111a" stroke-width="2" />

  <circle id="A" data-id="A" data-ref="A" class="etc-plate-pt"
          cx="{As[0]:.1f}" cy="{As[1]:.1f}" r="7.2" fill="#66ff66" stroke="#0d111a" stroke-width="2.2" />
  <circle id="B" data-id="B" data-ref="B" class="etc-plate-pt"
          cx="{Bs[0]:.1f}" cy="{Bs[1]:.1f}" r="7.2" fill="#66ff66" stroke="#0d111a" stroke-width="2.2" />
  <circle id="C" data-id="C" data-ref="C" class="etc-plate-pt"
          cx="{Cs[0]:.1f}" cy="{Cs[1]:.1f}" r="7.2" fill="#f8f6f0" stroke="#0d111a" stroke-width="2.2" />

  <g pointer-events="none">
    <text x="{As[0] - 32:.1f}" y="{As[1] + 26:.1f}" fill="#88ff88" font-family="Georgia, serif" font-size="28" font-weight="bold">A</text>
    <text x="{Bs[0] + 16:.1f}" y="{Bs[1] + 26:.1f}" fill="#88ff88" font-family="Georgia, serif" font-size="28" font-weight="bold">B</text>
    <text x="{c_lbl_x:.1f}" y="{c_lbl_y:.1f}" fill="#f8f6f0" font-family="Georgia, serif" font-size="28" font-weight="bold">C</text>
    <text x="{Pas[0] + 12:.1f}" y="{Pas[1] - 8:.1f}" fill="#e8b85a" font-family="Georgia, serif" font-size="19" font-weight="bold">{fa_id[0]}<tspan dy="0.28em" font-size="74%">{fa_id[-1]}</tspan></text>
    <text x="{Pbs[0] - 34:.1f}" y="{Pbs[1] - 8:.1f}" fill="#38bdf8" font-family="Georgia, serif" font-size="19" font-weight="bold">{fb_id[0]}<tspan dy="0.28em" font-size="74%">{fb_id[-1]}</tspan></text>
    <text x="{Pcs[0] + 10:.1f}" y="{Pcs[1] + 26:.1f}" fill="#5ec27e" font-family="Georgia, serif" font-size="19" font-weight="bold">{fc_id[0]}<tspan dy="0.28em" font-size="74%">{fc_id[-1]}</tspan></text>
  </g>

  <g font-family="Georgia, serif" font-size="26" font-weight="bold" pointer-events="none">
{strut_lbl_nodes}  </g>

  <circle id="X_{num}" data-id="X_{num}" data-ref="X_{num}" class="etc-plate-pt"
          cx="{Ps[0]:.1f}" cy="{Ps[1]:.1f}" r="10.5" fill="#ffd700" stroke="#00ffff" stroke-width="3" filter="url(#glow-coord)" />
  <g pointer-events="none">
    <rect x="{Ps[0] + x_badge_dx - 34:.1f}" y="{Ps[1] - 46:.1f}" width="68" height="30" rx="6" fill="rgba(13, 17, 26, 0.92)" stroke="#e8b85a" stroke-width="1.5" />
    <text x="{Ps[0] + x_badge_dx:.1f}" y="{Ps[1] - 25:.1f}" text-anchor="middle" fill="#ffd700" font-family="JetBrains Mono, monospace" font-size="19" font-weight="bold">{_svg_x(num)}</text>
    <text x="976" y="742" text-anchor="end" fill="#94a3b8" font-family="JetBrains Mono, monospace" font-size="14">{html.escape(sub_caption)}</text>
  </g>
  <script type="application/json" class="etc-elements-meta">{meta_json}</script>
  <script>//<![CDATA[
{INTERACTIVE_SVG_JS}
//]]></script>
</svg>"""


def generate_doc_central_lines_svg(model: Model, subtitle: str = "") -> str:
    """Generate Act 3 ``03_central_lines.svg`` with ``.show-lines`` active and incident framing."""
    return render_model_svg(model, subtitle=subtitle, show_lines=True)


def _match_bary_to_center(
    operator: str,
    target_num: int,
    raw_u: sp.Expr,
    raw_v: sp.Expr,
    raw_w: sp.Expr,
    tri: SymbolicTriangle,
    all_records: dict[int, SymbolicCenterRecord],
    center_names: dict[str, str],
) -> AlgebraicPartnerInfo:
    u_s = tri.simplify(raw_u)
    v_s = tri.simplify(raw_v)
    w_s = tri.simplify(raw_w)
    if zero_test(u_s) and zero_test(v_s) and zero_test(w_s):
        return AlgebraicPartnerInfo(
            operator=operator,
            partner_num=None,
            partner_title="Undefined",
            xy=None,
            bary=None,
            is_ideal=True,
        )
    tot = tri.simplify(u_s + v_s + w_s)
    red_bary = reduce_homogeneous_triple(u_s, v_s, w_s, tri)
    if zero_test(tot):
        return AlgebraicPartnerInfo(
            operator=operator,
            partner_num=None,
            partner_title="Point on Line at Infinity",
            xy=None,
            bary=red_bary,
            is_ideal=True,
        )
    nu = tri.simplify(u_s / tot)
    nv = tri.simplify(v_s / tot)
    xy = tri.bary_to_cartesian(u_s, v_s, w_s)
    matched_num: int | None = None
    for k, rec_k in all_records.items():
        if zero_test(nu - rec_k.norm_bary[0]) and zero_test(nv - rec_k.norm_bary[1]):
            matched_num = k
            red_bary = rec_k.bary
            xy = rec_k.xy
            break
    p_title = (
        center_names.get(str(matched_num), f"X_{matched_num}")
        if matched_num is not None
        else "Exact Algebraic Center"
    )
    return AlgebraicPartnerInfo(
        operator=operator,
        partner_num=matched_num,
        partner_title=p_title,
        xy=xy,
        bary=red_bary,
        is_self=(matched_num == target_num),
    )


@functools.lru_cache(maxsize=8)
def _get_preset_records(preset: str) -> dict[int, SymbolicCenterRecord]:
    tri = CANONICAL_TRIANGLES.get(preset, CANONICAL_TRIANGLES["heronian"])
    sym_reg = CenterSymbolicRegistry(tri)
    return {k: sym_reg.get(k) for k in sorted(EXACT_CYCLIC_BARYCENTRICS)}


def build_center_relations_bundle(
    num: int, preset: str = "heronian"
) -> CenterRelationsBundle:
    """Evaluate exact symbolic conjugates, dilations, and circumcircle inverse for ``X_num``."""
    tri = CANONICAL_TRIANGLES.get(preset, CANONICAL_TRIANGLES["heronian"])
    all_records = _get_preset_records(tri.key)
    rec = all_records[num] if num in all_records else CenterSymbolicRegistry(tri).get(num)
    center_names = _load_center_names()

    u, v, w = rec.bary
    qa, qb, qc = tri.Q_a, tri.Q_b, tri.Q_c

    isogonal = _match_bary_to_center(
        "isogonal",
        num,
        qa * v * w,
        qb * w * u,
        qc * u * v,
        tri,
        all_records,
        center_names,
    )
    isotomic = _match_bary_to_center(
        "isotomic",
        num,
        v * w,
        w * u,
        u * v,
        tri,
        all_records,
        center_names,
    )
    complement = _match_bary_to_center(
        "complement",
        num,
        v + w,
        w + u,
        u + v,
        tri,
        all_records,
        center_names,
    )
    anticomplement = _match_bary_to_center(
        "anticomplement",
        num,
        -u + v + w,
        u - v + w,
        u + v - w,
        tri,
        all_records,
        center_names,
    )

    x3_rec = all_records[3]
    dx3 = tri.simplify(rec.xy[0] - x3_rec.xy[0])
    dy3 = tri.simplify(rec.xy[1] - x3_rec.xy[1])
    q_op = tri.simplify(dx3 * dx3 + dy3 * dy3)
    if zero_test(q_op):
        circ_inv = AlgebraicPartnerInfo(
            operator="circumcircle_inverse",
            partner_num=None,
            partner_title="Ideal Line at Infinity",
            xy=None,
            bary=None,
            is_ideal=True,
            is_center_of_inversion=True,
            inversion_quadrance=sp.Integer(0),
        )
    else:
        inv_scale = tri.simplify(tri.Q_R / q_op)
        inv_x = tri.simplify(x3_rec.xy[0] + inv_scale * dx3)
        inv_y = tri.simplify(x3_rec.xy[1] + inv_scale * dy3)
        inv_sub = tri.cartesian_to_sub_areas(inv_x, inv_y)
        matched_inv = _match_bary_to_center(
            "circumcircle_inverse",
            num,
            inv_sub[0],
            inv_sub[1],
            inv_sub[2],
            tri,
            all_records,
            center_names,
        )
        circ_inv = AlgebraicPartnerInfo(
            operator="circumcircle_inverse",
            partner_num=matched_inv.partner_num,
            partner_title=matched_inv.partner_title,
            xy=(inv_x, inv_y),
            bary=matched_inv.bary,
            is_self=matched_inv.is_self,
            inversion_quadrance=q_op,
            inversion_scale=inv_scale,
        )

    galois_conj: AlgebraicPartnerInfo | None = None
    s3 = sp.sqrt(3)
    if tri.has_sqrt3_extension([*rec.bary]):
        conj_u = tri.simplify(u.xreplace({s3: -s3}))
        conj_v = tri.simplify(v.xreplace({s3: -s3}))
        conj_w = tri.simplify(w.xreplace({s3: -s3}))
        gc = _match_bary_to_center(
            "galois_sqrt3",
            num,
            conj_u,
            conj_v,
            conj_w,
            tri,
            all_records,
            center_names,
        )
        if not gc.is_self and gc.partner_num is not None:
            galois_conj = gc

    # Exact cross-ratio check on the Feuerbach line {X_1, X_5}
    harm_fb: int | None = None
    x1_xy = all_records[1].xy
    x5_xy = all_records[5].xy
    collinear_1_5 = zero_test(
        (x5_xy[0] - x1_xy[0]) * (rec.xy[1] - x1_xy[1])
        - (x5_xy[1] - x1_xy[1]) * (rec.xy[0] - x1_xy[0])
    )
    if collinear_1_5 and num not in {1, 5}:
        # Harmonic conjugate of P = alpha*X_1 + (1-alpha)*X_5 wrt {X_1, X_5}
        # In barycentrics along line X_1 X_5: check against known records on {1, 5}
        for cand_k, cand_rec in all_records.items():
            if cand_k in {1, 5, num}:
                continue
            c_xy = cand_rec.xy
            if not zero_test(
                (x5_xy[0] - x1_xy[0]) * (c_xy[1] - x1_xy[1])
                - (x5_xy[1] - x1_xy[1]) * (c_xy[0] - x1_xy[0])
            ):
                continue
            # Check cross-ratio (X_1, X_5; P, Q) == -1 along non-degenerate coordinate axis
            use_y = not zero_test(x5_xy[1] - x1_xy[1])
            z1 = x1_xy[1] if use_y else x1_xy[0]
            z2 = x5_xy[1] if use_y else x5_xy[0]
            zp = rec.xy[1] if use_y else rec.xy[0]
            zq = c_xy[1] if use_y else c_xy[0]
            cr_sum = tri.simplify(
                (z1 - zp) * (z2 - zq) + (z1 - zq) * (z2 - zp)
            )
            if zero_test(cr_sum):
                harm_fb = cand_k
                break

    return CenterRelationsBundle(
        num=num,
        preset=preset,
        isogonal=isogonal,
        isotomic=isotomic,
        complement=complement,
        anticomplement=anticomplement,
        circumcircle_inverse=circ_inv,
        galois_conjugate=galois_conj,
        harmonic_feuerbach_partner=harm_fb,
    )


def generate_doc_relations_svg(
    num: int, preset: str = "heronian"
) -> tuple[str, CenterRelationsBundle]:
    """Generate Act 4 ``04_relations.svg`` and populate ``bundle.svg_ids`` with exact plotted IDs."""
    tri = CANONICAL_TRIANGLES.get(preset, CANONICAL_TRIANGLES["heronian"])
    sym_reg = CenterSymbolicRegistry(tri)
    bundle = build_center_relations_bundle(num, preset=preset)

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
        rec_c = sym_reg.get(c_num)
        cls = (
            ["selected", "target"]
            if is_target
            else (["guide"] if as_guide else ["center"])
        )
        pt = add_point(
            model,
            rec_c.xy[0],
            rec_c.xy[1],
            ID=f"X_{c_num}",
            classes=cls,
            parents=[A, B, C],
            guide=as_guide and not is_target,
        )
        pts_map[c_num] = pt
        return pt

    candidate_partners: list[int] = []
    for p_info in (
        bundle.isogonal,
        bundle.isotomic,
        bundle.complement,
        bundle.anticomplement,
        bundle.circumcircle_inverse,
        bundle.galois_conjugate,
    ):
        if (
            p_info is not None
            and p_info.partner_num is not None
            and p_info.partner_num != num
            and p_info.partner_num not in candidate_partners
        ):
            candidate_partners.append(p_info.partner_num)
    if bundle.harmonic_feuerbach_partner is not None and bundle.harmonic_feuerbach_partner not in candidate_partners:
        candidate_partners.append(bundle.harmonic_feuerbach_partner)

    plotted_partners: list[int] = []
    for k in candidate_partners:
        rec_k = sym_reg.get(k)
        kx, ky = rec_k.approx_xy()
        if abs(kx - cx) <= 2.15 * span and abs(ky - cy) <= 2.15 * span:
            get_exact_pt(k, is_target=False, as_guide=False)
            plotted_partners.append(k)

    has_homothetic_partner = any(
        p_info.partner_num in plotted_partners
        for p_info in (bundle.complement, bundle.anticomplement)
        if p_info.partner_num is not None
    )
    if has_homothetic_partner and num != 2 and 2 not in plotted_partners:
        get_exact_pt(2, is_target=False, as_guide=True)

    active_circle_centers: set[int] = {3}
    for c_num in CIRCLE_CENTER_SPECS:
        if c_num == num or c_num in plotted_partners:
            active_circle_centers.add(c_num)
    if bundle.harmonic_feuerbach_partner is not None:
        active_circle_centers.update({1, 5})
    if num in {7, 8, 9, 10, 11, 12}:
        active_circle_centers.add(1)

    for c_num in (3, 1, 5, 10):
        if c_num not in active_circle_centers:
            continue
        pt_c = get_exact_pt(
            c_num,
            is_target=(num == c_num),
            as_guide=(c_num not in plotted_partners and num != c_num),
        )
        if pt_c is None:
            continue
        c_spec = CIRCLE_CENTER_SPECS[c_num]
        if c_spec.circle_id == "circumcircle":
            add_circle(model, pt_c, A, ID="circumcircle", classes=["circumcircle"])
        elif c_spec.circle_id == "incircle":
            Tc = perpendicular_foot(
                model, pt_c, A, B, ID="T_c", classes=["foot", "guide"], guide=True
            )
            add_circle(model, pt_c, Tc, ID="incircle", classes=["incircle"])
        elif c_spec.circle_id == "nine_point_circle":
            Mc = midpoint(
                model, A, B, ID="M_c", classes=["foot", "guide"], guide=True
            )
            add_circle(
                model, pt_c, Mc, ID="nine_point_circle", classes=["nine_point_circle"]
            )
        elif c_spec.circle_id == "spieker_circle":
            Ma = midpoint(
                model, B, C, ID="M_a", classes=["foot", "guide"], guide=True
            )
            Mb = midpoint(
                model, C, A, ID="M_b", classes=["foot", "guide"], guide=True
            )
            sp_foot = perpendicular_foot(
                model, pt_c, Ma, Mb, ID="T_sp", classes=["foot", "guide"], guide=True
            )
            add_circle(model, pt_c, sp_foot, ID="spieker_circle", classes=["incircle"])

    target_pt = get_exact_pt(num, is_target=True, as_guide=False)
    drawn_pairs: set[tuple[int, int]] = set()
    if target_pt is not None:
        for k in plotted_partners[:5]:
            pk = pts_map.get(k)
            pair = (min(num, k), max(num, k))
            if pk is not None and pair not in drawn_pairs:
                add_line(
                    model,
                    target_pt,
                    pk,
                    ID=f"{{ {pair[0]}, {pair[1]} }}",
                    classes=["central_line"],
                )
                drawn_pairs.add(pair)
        pt_3 = pts_map.get(3)
        if num != 3 and pt_3 is not None:
            pair3 = (min(num, 3), max(num, 3))
            if pair3 not in drawn_pairs:
                add_line(
                    model,
                    target_pt,
                    pt_3,
                    ID=f"{{ {pair3[0]}, {pair3[1]} }}",
                    classes=["central_line"],
                )
                drawn_pairs.add(pair3)
        promote_point_to_top(model, target_pt)

    svg_text = render_model_svg(model, subtitle=f"{tri.label} | Functional Relations")
    bundle.plotted_partners = plotted_partners
    bundle.svg_ids = {el["ID"] for el in model_to_elements_list(model)}
    return svg_text, bundle


def generate_doc_four_triangles_svg(num: int) -> str:
    """Generate Act 5 ``05_four_triangles.svg`` across all 4 Canonical Symbolic Reference Triangles."""
    quad_specs = [
        ("heronian", "Heronian (15, 13, 14)", token_hex(REFERENCE_TRIANGLE_COLORS["heronian"]), 35.0, 22.0),
        ("right", "Right (3, 4, 5)", token_hex(REFERENCE_TRIANGLE_COLORS["right"]), 515.0, 22.0),
        ("kepler", "Kepler (1, √φ, φ)", token_hex(REFERENCE_TRIANGLE_COLORS["kepler"]), 35.0, 390.0),
        ("kimberling", "Kimberling (6, 9, 13)", token_hex(REFERENCE_TRIANGLE_COLORS["kimberling"]), 515.0, 390.0),
    ]

    c_spec = CIRCLE_CENTER_SPECS.get(num)
    catalog: dict[str, Any] = {}
    panels: list[str] = []

    for key, label, accent, x_off, y_off in quad_specs:
        tri = CANONICAL_TRIANGLES[key]
        sym_reg = CenterSymbolicRegistry(tri)
        rec = sym_reg.get(num)
        kp = rec.is_kepler

        A_ex, B_ex, C_ex = tri.A_xy, tri.B_xy, tri.C_xy
        P_ex = rec.xy
        Pa_ex, ta_ex = exact_pedal_foot_and_param(P_ex, B_ex, C_ex, tri)
        Pb_ex, tb_ex = exact_pedal_foot_and_param(P_ex, C_ex, A_ex, tri)
        Pc_ex, tc_ex = exact_pedal_foot_and_param(P_ex, A_ex, B_ex, tri)

        A = (float(A_ex[0].evalf(20)), float(A_ex[1].evalf(20)))
        B = (float(B_ex[0].evalf(20)), float(B_ex[1].evalf(20)))
        C = (float(C_ex[0].evalf(20)), float(C_ex[1].evalf(20)))
        P = (float(P_ex[0].evalf(20)), float(P_ex[1].evalf(20)))
        Pa = (float(Pa_ex[0].evalf(20)), float(Pa_ex[1].evalf(20)))
        Pb = (float(Pb_ex[0].evalf(20)), float(Pb_ex[1].evalf(20)))
        Pc = (float(Pc_ex[0].evalf(20)), float(Pc_ex[1].evalf(20)))
        ta_f = float(ta_ex.evalf(15))
        tb_f = float(tb_ex.evalf(15))
        tc_f = float(tc_ex.evalf(15))

        fit_pts = [A, B, C, P, Pa, Pb, Pc]
        r_ex: sp.Expr | None = None
        if c_spec is not None:
            r_ex = c_spec.radius_fn(tri)
            r_f = float(r_ex.evalf(20))
            fit_pts.extend(
                [
                    (P[0] - r_f, P[1]),
                    (P[0] + r_f, P[1]),
                    (P[0], P[1] - r_f),
                    (P[0], P[1] + r_f),
                ]
            )

        sc, ox, oy = _fit_points_to_box(
            fit_pts,
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

        fld_pretty = tri.coordinate_field_pretty([*rec.xy, *rec.bary])
        field_badge = f"Δ = {format_symbolic_pretty(tri.area, kepler_phi=kp)} • {fld_pretty}"

        sides_ltx = (
            f"\\left({format_symbolic_latex(tri.a, kepler_phi=kp)},\\; "
            f"{format_symbolic_latex(tri.b, kepler_phi=kp)},\\; "
            f"{format_symbolic_latex(tri.c, kepler_phi=kp)}\\right)"
        )
        sides_prt = (
            f"({format_symbolic_pretty(tri.a, kepler_phi=kp)}, "
            f"{format_symbolic_pretty(tri.b, kepler_phi=kp)}, "
            f"{format_symbolic_pretty(tri.c, kepler_phi=kp)})"
        )
        xy_ltx = rec.xy_latex()
        xy_prt = rec.xy_pretty()

        panel_rows = [
            {"label": "sides", "latex": sides_ltx, "pretty": sides_prt},
            {"label": f"X_{{{num}}}", "latex": xy_ltx, "pretty": xy_prt},
            {"label": "bary", "latex": rec.bary_latex(), "pretty": rec.bary_pretty()},
            {
                "label": "Δ, field",
                "latex": f"\\Delta = {format_symbolic_latex(tri.area, kepler_phi=kp)},\\; {tri.coordinate_field_latex([*rec.xy, *rec.bary])}",
                "pretty": field_badge,
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

        for sid, sa_val, scol, sv in [
            (sub_a_id, rec.sub_areas[0], "#e8b85a", "BC"),
            (sub_b_id, rec.sub_areas[1], "#38bdf8", "CA"),
            (sub_c_id, rec.sub_areas[2], "#5ec27e", "AB"),
        ]:
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

        for st_id, sa_val, s_len, scol, ssym, snm in [
            (st_a_id, rec.sub_areas[0], tri.a, "#e8b85a", "\\alpha", "BC"),
            (st_b_id, rec.sub_areas[1], tri.b, "#38bdf8", "\\beta", "CA"),
            (st_c_id, rec.sub_areas[2], tri.c, "#5ec27e", "\\gamma", "AB"),
        ]:
            abs_sa = tri.simplify(-sa_val) if exact_sign(sa_val) < 0 else sa_val
            l_st = tri.simplify(sp.Integer(2) * abs_sa / s_len)
            q_st = tri.simplify(l_st * l_st)
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

        circle_panel_svg = ""
        if c_spec is not None and r_ex is not None:
            r_scr = float(r_ex.evalf(20)) * sc
            q_c = tri.simplify(r_ex * r_ex)
            cid = f"{key}-{c_spec.circle_id}"
            catalog[cid] = {
                "ID": cid,
                "type": "circle",
                "color": c_spec.stroke_hex,
                "name": f"{c_spec.circle_label} on {label}",
                "symbolic_rows": [
                    {
                        "label": c_spec.r_sym,
                        "latex": format_symbolic_latex(r_ex, kepler_phi=kp),
                        "pretty": format_symbolic_pretty(r_ex, kepler_phi=kp),
                    },
                    {
                        "label": c_spec.q_sym,
                        "latex": format_symbolic_latex(q_c, kepler_phi=kp),
                        "pretty": format_symbolic_pretty(q_c, kepler_phi=kp),
                    },
                ],
                "approx": f"{c_spec.r_sym} ≈ {float(r_ex.evalf(20)):.6f}",
            }
            circle_panel_svg = (
                f'    <circle id="{cid}" data-id="{cid}" data-ref="{cid}" class="etc-plate-circle" '
                f'cx="{Ps[0]:.1f}" cy="{Ps[1]:.1f}" r="{r_scr:.1f}" '
                f'fill="none" stroke="{c_spec.stroke_rgba}" stroke-width="1.8" stroke-dasharray="5,4" />\n'
            )

        ext_panel_svg = (
            _sideline_extension_svg(Bs, Cs, Pas, ta_f, indent="    ", stroke_w=1.4)
            + _sideline_extension_svg(Cs, As, Pbs, tb_f, indent="    ", stroke_w=1.4)
            + _sideline_extension_svg(As, Bs, Pcs, tc_f, indent="    ", stroke_w=1.4)
        )

        c_lx = Cs[0] - 6.0
        c_ly = Cs[1] - 10.0
        x_lx = Ps[0] + 12.0
        x_ly = Ps[1] - 10.0
        if math.hypot(Ps[0] - Cs[0], Ps[1] - Cs[1]) < 24.0:
            c_lx = Cs[0] - 20.0
            c_ly = Cs[1] - 8.0
            x_lx = Ps[0] + 12.0
            x_ly = Ps[1] - 8.0

        coord_footer = f"X_{num} = {xy_prt}"
        if len(coord_footer) > 46:
            coord_footer = coord_footer[:43] + "..."

        panels.append(f"""
  <g id="{panel_id}" data-id="{panel_id}" data-ref="{panel_id}" class="etc-plate-panel">
    <rect class="etc-panel-border" x="{x_off:.1f}" y="{y_off:.1f}" width="450" height="346" rx="16" fill="rgba(13, 17, 26, 0.92)" stroke="{accent}" stroke-width="1.8" />
    <text x="{x_off + 22:.1f}" y="{y_off + 34:.1f}" fill="{accent}" font-family="JetBrains Mono, monospace" font-size="16.5" font-weight="bold" pointer-events="none">{html.escape(label)}</text>
    <text x="{x_off + 428:.1f}" y="{y_off + 34:.1f}" text-anchor="end" fill="#94a3b8" font-family="JetBrains Mono, monospace" font-size="13" pointer-events="none">{html.escape(field_badge)}</text>

    <polygon id="{sub_a_id}" data-id="{sub_a_id}" data-ref="{sub_a_id}" class="etc-plate-poly" points="{Ps[0]:.1f},{Ps[1]:.1f} {Bs[0]:.1f},{Bs[1]:.1f} {Cs[0]:.1f},{Cs[1]:.1f}" fill="#e8b85a" fill-opacity="0.14" stroke="none" />
    <polygon id="{sub_b_id}" data-id="{sub_b_id}" data-ref="{sub_b_id}" class="etc-plate-poly" points="{Ps[0]:.1f},{Ps[1]:.1f} {Cs[0]:.1f},{Cs[1]:.1f} {As[0]:.1f},{As[1]:.1f}" fill="#38bdf8" fill-opacity="0.14" stroke="none" />
    <polygon id="{sub_c_id}" data-id="{sub_c_id}" data-ref="{sub_c_id}" class="etc-plate-poly" points="{Ps[0]:.1f},{Ps[1]:.1f} {As[0]:.1f},{As[1]:.1f} {Bs[0]:.1f},{Bs[1]:.1f}" fill="#5ec27e" fill-opacity="0.14" stroke="none" />

{circle_panel_svg}{ext_panel_svg}    <polygon points="{As[0]:.1f},{As[1]:.1f} {Bs[0]:.1f},{Bs[1]:.1f} {Cs[0]:.1f},{Cs[1]:.1f}" fill="none" stroke="#cbd5e1" stroke-width="2.3" stroke-dasharray="2, 4.5" stroke-linecap="round" pointer-events="none" />
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
      <text x="{c_lx:.1f}" y="{c_ly:.1f}" fill="#f8f6f0" font-family="Georgia, serif" font-size="18" font-weight="bold">C</text>
      <text x="{x_lx:.1f}" y="{x_ly:.1f}" fill="#ffd700" font-family="JetBrains Mono, monospace" font-size="17" font-weight="bold">{_svg_x(num)}</text>
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
