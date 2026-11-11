"""Exact symbolic geometric construction operators for `geometor.etc` using `geometor.model`.

Every operator accepts ``(model, A, B, C, ...)`` or ``(model, P, Q, ...)`` where
points are exact :class:`sympy.geometry.Point` instances registered in ``model``
over :math:`\\mathbb{Q}`, :math:`\\mathbb{Q}(\\sqrt{d})`, or :math:`\\mathbb{Q}(\\sqrt{\\phi})`.

Canonical *Principles of Geometry* ``snake_case`` constructors (:func:`incenter`,
:func:`centroid`, :func:`circumcenter`, :func:`orthocenter`, :func:`nine_point_center`,
:func:`symmedian_point`, :func:`gergonne_point`, :func:`nagel_point`, :func:`mittenpunkt`,
:func:`spieker_center`, :func:`feuerbach_point`, :func:`fermat_point`, etc.) are
provided alongside legacy ``*_of`` aliases and Kimberling ``X_n`` concordance metadata.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import sympy as sp
import sympy.geometry as spg
from geometor.model import (
    Model,
    clean_expr,
    exact_sign,
    intersect_2d,
    quadrance,
    zero_test,
)
from geometor.model.element import Element

from .triangles import (
    SymbolicTriangle,
    build_symbolic_triangle_from_sides,
    get_canonical_triangle,
)


@dataclass(frozen=True)
class CenterConcordance:
    """Concordance entry linking canonical function names, Kimberling IDs, and classical citations."""

    num: int
    function_name: str
    etc_id: str
    title: str
    classical_ref: str

    @property
    def signature(self) -> str:
        """Return canonical functional signature string."""
        return f"{self.function_name}(A, B, C) -> {self.etc_id}"


CANONICAL_CENTER_CONCORDANCE: dict[int, CenterConcordance] = {
    1: CenterConcordance(1, "incenter", "X_1", "INCENTER", "Euclid IV.4"),
    2: CenterConcordance(2, "centroid", "X_2", "CENTROID", "Archimedes Equilibriums I.14"),
    3: CenterConcordance(3, "circumcenter", "X_3", "CIRCUMCENTER", "Euclid IV.5"),
    4: CenterConcordance(4, "orthocenter", "X_4", "ORTHOCENTER", "Archimedes Lemmas 5 • Pappus VII"),
    5: CenterConcordance(5, "nine_point_center", "X_5", "NINE-POINT CENTER", "Poncelet–Brianchon–Feuerbach (1822)"),
    6: CenterConcordance(6, "symmedian_point", "X_6", "SYMMEDIAN POINT", "Grebe (1847) • Lemoine (1873)"),
    7: CenterConcordance(7, "gergonne_point", "X_7", "GERGONNE POINT", "Gergonne (1818)"),
    8: CenterConcordance(8, "nagel_point", "X_8", "NAGEL POINT", "Nagel (1836)"),
    9: CenterConcordance(9, "mittenpunkt", "X_9", "MITTENPUNKT", "Nagel (1836)"),
    10: CenterConcordance(10, "spieker_center", "X_10", "SPIEKER CENTER", "Spieker (1888)"),
    11: CenterConcordance(11, "feuerbach_point", "X_11", "FEUERBACH POINT", "Feuerbach (1822)"),
    12: CenterConcordance(12, "harmonic_feuerbach_point", "X_12", "{X_1,X_5}-HARMONIC CONJUGATE OF X_11", "Kimberling ETC"),
    13: CenterConcordance(13, "fermat_point", "X_13", "1st ISOGONIC CENTER (FERMAT POINT)", "Fermat • Torricelli (c. 1640)"),
    14: CenterConcordance(14, "second_isogonic_center", "X_14", "2nd ISOGONIC CENTER", "Torricelli • Neuberg"),
    15: CenterConcordance(15, "first_isodynamic_point", "X_15", "1st ISODYNAMIC POINT", "Neuberg (1885)"),
    16: CenterConcordance(16, "second_isodynamic_point", "X_16", "2nd ISODYNAMIC POINT", "Neuberg (1885)"),
    17: CenterConcordance(17, "first_napoleon_point", "X_17", "1st NAPOLEON POINT", "Kiepert • Napoleon"),
    18: CenterConcordance(18, "second_napoleon_point", "X_18", "2nd NAPOLEON POINT", "Kiepert • Napoleon"),
    19: CenterConcordance(19, "clawson_point", "X_19", "CLAWSON POINT", "Clawson (1925)"),
    20: CenterConcordance(20, "de_longchamps_point", "X_20", "DE LONGCHAMPS POINT", "de Longchamps (1886)"),
    36: CenterConcordance(36, "circumcircle_inverse_of_incenter", "X_36", "INVERSE-IN-CIRCUMCIRCLE OF INCENTER", "Kimberling ETC"),
    40: CenterConcordance(40, "bevan_point", "X_40", "BEVAN POINT", "Bevan (1806)"),
    75: CenterConcordance(75, "isotomic_conjugate_of_incenter", "X_75", "ISOTOMIC CONJUGATE OF INCENTER", "Kimberling ETC"),
}


def get_center_concordance(num: int) -> CenterConcordance | None:
    """Return the :class:`CenterConcordance` for center ``X_num``, if registered."""
    return CANONICAL_CENTER_CONCORDANCE.get(num)


# ---------------------------------------------------------------------------
# Exact Coordinate Coercion & Simplification Helpers
# ---------------------------------------------------------------------------


def _to_exact_expr(val: sp.Expr | float, model: Model | None = None) -> sp.Expr:
    """Coerce numeric or symbolic input into a 100% ``sp.Float``-free SymPy expression."""
    if isinstance(val, int):
        expr: sp.Expr = sp.Integer(val)
    elif isinstance(val, sp.Rational):
        expr = val
    elif isinstance(val, float):
        expr = sp.nsimplify(val, rational=True)
    else:
        expr = sp.sympify(val)
        if expr.atoms(sp.Float):
            expr = sp.nsimplify(expr, rational=True)

    simplifier = getattr(model, "_simplifier", None) if model is not None else None
    if simplifier is not None:
        return simplifier(expr)
    return clean_expr(expr)


def _model_simplify(model: Model | None, expr: sp.Expr | int) -> sp.Expr:
    simplifier = getattr(model, "_simplifier", None) if model is not None else None
    if simplifier is not None:
        return simplifier(sp.sympify(expr))
    return clean_expr(expr)


# ---------------------------------------------------------------------------
# Public `geometor.model.Model` Element Registration (Zero Bypasses)
# ---------------------------------------------------------------------------


def create_model(name: str = "ETC Construction") -> Model:
    """Create a silent exact :class:`geometor.model.Model` with ``auto_intersect=False``."""
    return Model(name, auto_intersect=False, enable_logging=False)


def add_point(
    model: Model,
    x: sp.Expr | float,
    y: sp.Expr | float,
    ID: str,
    classes: list[str] | None = None,
    parents: list[Any] | None = None,
    guide: bool = False,
) -> spg.Point:
    """Register or update an exact :class:`sympy.geometry.Point` in ``model``."""
    existing = model.get_element_by_ID(ID)
    if existing is not None and isinstance(existing, spg.Point):
        if classes:
            for c in classes:
                model[existing].classes[c] = ""
        if not guide:
            model[existing].guide = False
        return existing

    sx = _to_exact_expr(x, model)
    sy = _to_exact_expr(y, model)
    return model.set_point(
        sx,
        sy,
        parents=parents or [],
        classes=list(classes) if classes else [],
        ID=ID,
        guide=guide,
    )


def add_line(
    model: Model,
    pt1: spg.Point,
    pt2: spg.Point,
    ID: str = "",
    classes: list[str] | None = None,
    guide: bool = False,
) -> spg.Line | None:
    """Construct an exact :class:`sympy.geometry.Line` through ``pt1`` and ``pt2``."""
    if pt1 == pt2:
        return None
    if zero_test(pt1.x - pt2.x) and zero_test(pt1.y - pt2.y):
        return None
    return model.construct_line(
        pt1,
        pt2,
        classes=list(classes) if classes else [],
        ID=ID,
        guide=guide,
        intersect=False,
    )


def add_circle(
    model: Model,
    pt_center: spg.Point,
    pt_radius: spg.Point | sp.Expr | float,
    ID: str = "",
    classes: list[str] | None = None,
    guide: bool = False,
) -> spg.Circle | None:
    """Construct an exact :class:`sympy.geometry.Circle` centered at ``pt_center``."""
    if isinstance(pt_radius, spg.Point):
        if zero_test(pt_center.x - pt_radius.x) and zero_test(pt_center.y - pt_radius.y):
            return None
        if pt_radius in model:
            return model.construct_circle(
                pt_center,
                pt_radius,
                classes=list(classes) if classes else [],
                ID=ID,
                guide=guide,
                intersect=False,
            )
        r_expr = _model_simplify(model, sp.sqrt(quadrance(pt_center, pt_radius)))
    else:
        r_expr = _to_exact_expr(pt_radius, model)
        if zero_test(r_expr):
            return None

    if not ID:
        c_id = model[pt_center].ID if pt_center in model else "O"
        ID = f"( {c_id} {r_expr} )"
    circ = spg.Circle(pt_center, r_expr)
    el = Element(
        circ,
        parents=[pt_center],
        classes=list(classes) if classes else [],
        ID=ID,
        guide=guide,
    )
    model[circ] = el
    return circ


def add_polygon(
    model: Model,
    pts: list[spg.Point],
    ID: str = "",
    classes: list[str] | None = None,
) -> spg.Polygon:
    """Construct and register an exact :class:`sympy.geometry.Polygon` in ``model``."""
    return model.construct_polygon(
        pts,
        classes=list(classes) if classes else [],
        ID=ID,
        guide=False,
    )


def add_segment(
    model: Model,
    pt1: spg.Point,
    pt2: spg.Point,
    ID: str = "",
    classes: list[str] | None = None,
) -> spg.Segment | None:
    """Construct and register an exact :class:`sympy.geometry.Segment` in ``model``."""
    if pt1 == pt2 or (zero_test(pt1.x - pt2.x) and zero_test(pt1.y - pt2.y)):
        return None
    return model.construct_segment(
        pt1,
        pt2,
        classes=list(classes) if classes else ["segment"],
        ID=ID,
        guide=False,
    )


def promote_point_to_top(model: Model, pt: spg.Point) -> spg.Point:
    """Move ``pt`` to the end of ``model`` insertion order so it renders topmost."""
    if pt in model:
        el_data = model.pop(pt)
        model[pt] = el_data
    return pt


# ---------------------------------------------------------------------------
# Exact Reference Triangle Construction
# ---------------------------------------------------------------------------


def construct_reference_triangle(
    model: Model,
    preset: str | SymbolicTriangle = "heronian",
    *,
    unit_baseline: bool = False,
    show_guides: bool = False,
) -> tuple[spg.Point, spg.Point, spg.Point]:
    """Construct one of the 4 canonical exact symbolic reference triangles in ``model``.

    Parameters
    ----------
    model :
        Target :class:`geometor.model.Model`.
    preset :
        Canonical preset key (``"heronian"``, ``"right"``, ``"kepler"``,
        ``"kimberling"``) or a :class:`SymbolicTriangle`.
    unit_baseline :
        When ``True``, normalizes side :math:`AB = 1`. Defaults to ``False`` so
        Heronian :math:`(15, 13, 14)` and Right :math:`(3, 4, 5)` preserve exact
        integer vertex and center coordinates.
    show_guides :
        When ``True``, includes Euclid I.22 compass guide circles centered at
        :math:`A` and :math:`B`.
    """
    tri = (
        preset.unit_baseline()
        if isinstance(preset, SymbolicTriangle) and unit_baseline
        else preset
        if isinstance(preset, SymbolicTriangle)
        else get_canonical_triangle(preset, unit_baseline=unit_baseline)
    )
    model.set_simplifier(tri.simplify)
    model._etc_triangle = tri

    A = add_point(model, tri.A_xy[0], tri.A_xy[1], ID="A", classes=["given", "vertex"])
    B = add_point(model, tri.B_xy[0], tri.B_xy[1], ID="B", classes=["given", "vertex"])
    add_line(model, A, B, ID="[ A B ]", classes=["given", "sideline"])

    if show_guides:
        R_b = add_point(model, tri.b, sp.Integer(0), ID="R_b", classes=["guide"], guide=True)
        R_a = add_point(
            model,
            tri.simplify(tri.c - tri.a),
            sp.Integer(0),
            ID="R_a",
            classes=["guide"],
            guide=True,
        )
        cA = add_circle(model, A, R_b, ID="( A R_b )", classes=["guide"], guide=True)
        cB = add_circle(model, B, R_a, ID="( B R_a )", classes=["guide"], guide=True)
        C = add_point(
            model,
            tri.C_xy[0],
            tri.C_xy[1],
            ID="C",
            classes=["vertex"],
            parents=[p for p in (cA, cB) if p is not None],
        )
    else:
        C = add_point(model, tri.C_xy[0], tri.C_xy[1], ID="C", classes=["vertex"])

    add_line(model, B, C, ID="[ B C ]", classes=["sideline"])
    add_line(model, C, A, ID="[ C A ]", classes=["sideline"])
    add_polygon(model, [A, B, C], ID="< A B C >", classes=["reference"])
    return A, B, C


def construct_baseline_triangle(
    model: Model,
    a: sp.Expr | float = 15,
    b: sp.Expr | float = 13,
    c: sp.Expr | float = 14,
    show_guides: bool = False,
    *,
    unit_baseline: bool = True,
) -> tuple[spg.Point, spg.Point, spg.Point]:
    """Construct an exact symbolic triangle with side ratios ``(a, b, c)``.

    Preserves backward compatibility for scripts calling
    ``construct_baseline_triangle(model, 5, 6, 7)`` while computing exact algebraic
    coordinates without floating-point approximations.
    """
    tri = build_symbolic_triangle_from_sides(
        a, b, c, unit_baseline=unit_baseline
    )
    return construct_reference_triangle(
        model, tri, unit_baseline=False, show_guides=show_guides
    )


# ---------------------------------------------------------------------------
# Exact Euclidean & Coordinate Helpers on (A, B, C)
# ---------------------------------------------------------------------------


def triangle_side_quadrances(
    A: spg.Point, B: spg.Point, C: spg.Point, model: Model | None = None
) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    """Return exact side quadrances ``(Q_a, Q_b, Q_c) = (|BC|^2, |CA|^2, |AB|^2)``."""
    return (
        _model_simplify(model, quadrance(B, C)),
        _model_simplify(model, quadrance(C, A)),
        _model_simplify(model, quadrance(A, B)),
    )


def triangle_side_lengths(
    A: spg.Point, B: spg.Point, C: spg.Point, model: Model | None = None
) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    """Return exact symbolic side lengths ``(a, b, c) = (|BC|, |CA|, |AB|)``."""
    tri = getattr(model, "_etc_triangle", None) if model is not None else None
    if (
        isinstance(tri, SymbolicTriangle)
        and zero_test(A.x - tri.A_xy[0])
        and zero_test(A.y - tri.A_xy[1])
        and zero_test(B.x - tri.B_xy[0])
        and zero_test(B.y - tri.B_xy[1])
        and zero_test(C.x - tri.C_xy[0])
        and zero_test(C.y - tri.C_xy[1])
    ):
        return (tri.a, tri.b, tri.c)

    qa, qb, qc = triangle_side_quadrances(A, B, C, model=model)
    return (
        _model_simplify(model, sp.sqrt(qa)),
        _model_simplify(model, sp.sqrt(qb)),
        _model_simplify(model, sp.sqrt(qc)),
    )


def triangle_signed_area(
    A: spg.Point, B: spg.Point, C: spg.Point, model: Model | None = None
) -> sp.Expr:
    """Return exact signed area :math:`\\Delta` of triangle ``ABC``."""
    raw = ((B.x - A.x) * (C.y - A.y) - (C.x - A.x) * (B.y - A.y)) / sp.Integer(2)
    return _model_simplify(model, raw)


def barycentrics_of(
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    P: spg.Point,
    model: Model | None = None,
) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    """Compute exact normalized barycentric coordinates ``(u, v, w)`` of ``P``."""
    det = _model_simplify(
        model, (B.y - C.y) * (A.x - C.x) + (C.x - B.x) * (A.y - C.y)
    )
    if zero_test(det):
        third = sp.Rational(1, 3)
        return (third, third, third)
    u = _model_simplify(
        model, ((B.y - C.y) * (P.x - C.x) + (C.x - B.x) * (P.y - C.y)) / det
    )
    v = _model_simplify(
        model, ((C.y - A.y) * (P.x - C.x) + (A.x - C.x) * (P.y - C.y)) / det
    )
    w = _model_simplify(model, sp.Integer(1) - u - v)
    return (u, v, w)


def point_from_barycentrics(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    u: sp.Expr | float,
    v: sp.Expr | float,
    w: sp.Expr | float,
    ID: str = "P",
    classes: list[str] | None = None,
    guide: bool = False,
) -> spg.Point:
    """Construct an exact point in ``model`` from homogeneous barycentrics ``(u : v : w)``."""
    su = _to_exact_expr(u, model)
    sv = _to_exact_expr(v, model)
    sw = _to_exact_expr(w, model)
    s_sum = _model_simplify(model, su + sv + sw)
    if zero_test(s_sum):
        # Ideal point on the line at infinity: exact rational offset from centroid
        gx = _model_simplify(model, (A.x + B.x + C.x) / sp.Integer(3))
        gy = _model_simplify(model, (A.y + B.y + C.y) / sp.Integer(3))
        dx = _model_simplify(model, su * A.x + sv * B.x + sw * C.x)
        dy = _model_simplify(model, su * A.y + sv * B.y + sw * C.y)
        return add_point(
            model,
            _model_simplify(model, gx + dx),
            _model_simplify(model, gy + dy),
            ID=ID,
            classes=classes,
            parents=[A, B, C],
            guide=guide,
        )

    x = _model_simplify(model, (su * A.x + sv * B.x + sw * C.x) / s_sum)
    y = _model_simplify(model, (su * A.y + sv * B.y + sw * C.y) / s_sum)
    return add_point(
        model, x, y, ID=ID, classes=classes, parents=[A, B, C], guide=guide
    )


def point_from_trilinears(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    alpha: sp.Expr | float,
    beta: sp.Expr | float,
    gamma: sp.Expr | float,
    ID: str = "P",
    classes: list[str] | None = None,
    guide: bool = False,
) -> spg.Point:
    """Construct an exact point in ``model`` from homogeneous trilinears ``(alpha : beta : gamma)``."""
    a, b, c = triangle_side_lengths(A, B, C, model=model)
    sa = _to_exact_expr(alpha, model)
    sb = _to_exact_expr(beta, model)
    sc = _to_exact_expr(gamma, model)
    return point_from_barycentrics(
        model,
        A,
        B,
        C,
        a * sa,
        b * sb,
        c * sc,
        ID=ID,
        classes=classes,
        guide=guide,
    )


def _eval_cyclic_symbolic_on_triangle(
    model: Model | None, A: spg.Point, B: spg.Point, C: spg.Point, expr_str: str
) -> tuple[sp.Expr, sp.Expr, sp.Expr] | None:
    """Evaluate a cyclic coordinate expression ``f(a, b, c, A, B, C)`` symbolically."""
    a, b, c = triangle_side_lengths(A, B, C, model=model)
    qa, qb, qc = triangle_side_quadrances(A, B, C, model=model)
    area = abs(triangle_signed_area(A, B, C, model=model))
    two_area = _model_simplify(model, sp.Integer(2) * area)
    s_semi = _model_simplify(model, (a + b + c) / sp.Integer(2))
    R = _model_simplify(model, (a * b * c) / (sp.Integer(4) * area))
    r = _model_simplify(model, area / s_semi)
    SA = _model_simplify(model, (qb + qc - qa) / sp.Integer(2))
    SB = _model_simplify(model, (qc + qa - qb) / sp.Integer(2))
    SC = _model_simplify(model, (qa + qb - qc) / sp.Integer(2))
    SW = _model_simplify(model, (qa + qb + qc) / sp.Integer(2))
    Ra = _model_simplify(model, area / (s_semi - a))
    Rb = _model_simplify(model, area / (s_semi - b))
    Rc = _model_simplify(model, area / (s_semi - c))

    a_s, b_s, c_s = sp.symbols("a b c", positive=True)
    A_s, B_s, C_s, om_s = sp.symbols("A B C omega", real=True)
    SA_s, SB_s, SC_s, S_s, SW_s = sp.symbols("SA SB SC S SW", real=True)
    Ra_s, Rb_s, Rc_s = sp.symbols("Ra Rb Rc", positive=True)
    r_s, R_s, s_s, area_s = sp.symbols("r R s area", positive=True)

    local_ns: dict[str, Any] = {
        "a": a_s,
        "b": b_s,
        "c": c_s,
        "A": A_s,
        "B": B_s,
        "C": C_s,
        "omega": om_s,
        "SA": SA_s,
        "SB": SB_s,
        "SC": SC_s,
        "S": S_s,
        "SW": SW_s,
        "Ra": Ra_s,
        "Rb": Rb_s,
        "Rc": Rc_s,
        "r": r_s,
        "R": R_s,
        "s": s_s,
        "area": area_s,
        "sin": sp.sin,
        "cos": sp.cos,
        "tan": sp.tan,
        "cot": sp.cot,
        "sec": sp.sec,
        "csc": sp.csc,
        "sqrt": sp.sqrt,
        "pi": sp.pi,
    }
    try:
        parsed = sp.sympify(expr_str, locals=local_ns)
        expanded = sp.expand_trig(parsed)
        trig_subs = {
            sp.sin(A_s): S_s / (b_s * c_s),
            sp.sin(B_s): S_s / (c_s * a_s),
            sp.sin(C_s): S_s / (a_s * b_s),
            sp.cos(A_s): SA_s / (b_s * c_s),
            sp.cos(B_s): SB_s / (c_s * a_s),
            sp.cos(C_s): SC_s / (a_s * b_s),
            sp.tan(A_s): S_s / SA_s,
            sp.tan(B_s): S_s / SB_s,
            sp.tan(C_s): S_s / SC_s,
            sp.cot(A_s): SA_s / S_s,
            sp.cot(B_s): SB_s / S_s,
            sp.cot(C_s): SC_s / S_s,
            sp.sec(A_s): (b_s * c_s) / SA_s,
            sp.sec(B_s): (c_s * a_s) / SB_s,
            sp.sec(C_s): (a_s * b_s) / SC_s,
            sp.csc(A_s): (b_s * c_s) / S_s,
            sp.csc(B_s): (c_s * a_s) / S_s,
            sp.csc(C_s): (a_s * b_s) / S_s,
            sp.cot(om_s): SW_s / S_s,
            sp.tan(om_s): S_s / SW_s,
        }
        alg = expanded.subs(trig_subs)
        perms = [
            (a, b, c, SA, SB, SC, Ra, Rb, Rc),
            (b, c, a, SB, SC, SA, Rb, Rc, Ra),
            (c, a, b, SC, SA, SB, Rc, Ra, Rb),
        ]
        vals: list[sp.Expr] = []
        for pa, pb, pc, pSA, pSB, pSC, pRa, pRb, pRc in perms:
            val = alg.subs(
                {
                    a_s: pa,
                    b_s: pb,
                    c_s: pc,
                    SA_s: pSA,
                    SB_s: pSB,
                    SC_s: pSC,
                    Ra_s: pRa,
                    Rb_s: pRb,
                    Rc_s: pRc,
                    S_s: two_area,
                    SW_s: SW,
                    r_s: r,
                    R_s: R,
                    s_s: s_semi,
                    area_s: area,
                }
            )
            if val.atoms(sp.zoo, sp.nan, sp.oo):
                return None
            vals.append(_model_simplify(model, val))
        if all(zero_test(v) for v in vals):
            return None
        return (vals[0], vals[1], vals[2])
    except (sp.SympifyError, ArithmeticError, TypeError, ValueError):
        return None


def eval_barycentric_point(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    expr_str: str,
    ID: str = "P",
    classes: list[str] | None = None,
    guide: bool = False,
) -> spg.Point:
    """Construct an exact point by evaluating a cyclic barycentric coordinate expression."""
    res = _eval_cyclic_symbolic_on_triangle(model, A, B, C, expr_str)
    if res is None:
        return point_from_barycentrics(
            model, A, B, C, 1, 1, 1, ID=ID, classes=classes, guide=guide
        )
    return point_from_barycentrics(
        model, A, B, C, res[0], res[1], res[2], ID=ID, classes=classes, guide=guide
    )


def eval_trilinear_point(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    expr_str: str,
    ID: str = "P",
    classes: list[str] | None = None,
    guide: bool = False,
) -> spg.Point:
    """Construct an exact point by evaluating a cyclic trilinear coordinate expression."""
    res = _eval_cyclic_symbolic_on_triangle(model, A, B, C, expr_str)
    if res is None:
        return point_from_trilinears(
            model, A, B, C, 1, 1, 1, ID=ID, classes=classes, guide=guide
        )
    return point_from_trilinears(
        model, A, B, C, res[0], res[1], res[2], ID=ID, classes=classes, guide=guide
    )


def midpoint(
    model: Model,
    P: spg.Point,
    Q: spg.Point,
    ID: str = "",
    classes: list[str] | None = None,
    guide: bool = True,
) -> spg.Point:
    """Construct the exact midpoint of segment ``PQ`` (Euclid I.10)."""
    if not ID:
        ID = f"M_{{{model[P].ID}{model[Q].ID}}}"
    return add_point(
        model,
        _model_simplify(model, (P.x + Q.x) / sp.Integer(2)),
        _model_simplify(model, (P.y + Q.y) / sp.Integer(2)),
        ID=ID,
        classes=classes or ["midpoint"],
        parents=[P, Q],
        guide=guide,
    )


def perpendicular_foot(
    model: Model,
    P: spg.Point,
    L1: spg.Point,
    L2: spg.Point,
    ID: str = "",
    classes: list[str] | None = None,
    guide: bool = True,
) -> spg.Point:
    """Construct the exact orthogonal projection (Euclid I.12) of ``P`` onto line ``L1-L2``."""
    dx = _model_simplify(model, L2.x - L1.x)
    dy = _model_simplify(model, L2.y - L1.y)
    len_sq = _model_simplify(model, dx * dx + dy * dy)
    t = (
        _model_simplify(model, ((P.x - L1.x) * dx + (P.y - L1.y) * dy) / len_sq)
        if not zero_test(len_sq)
        else sp.Integer(0)
    )
    if not ID:
        ID = f"H_{{{model[P].ID}}}"
    return add_point(
        model,
        _model_simplify(model, L1.x + t * dx),
        _model_simplify(model, L1.y + t * dy),
        ID=ID,
        classes=classes or ["foot"],
        parents=[P, L1, L2],
        guide=guide,
    )


def equilateral_apex(
    model: Model,
    P1: spg.Point,
    P2: spg.Point,
    opp: spg.Point,
    outward: bool = True,
    ID: str = "",
    classes: list[str] | None = None,
    guide: bool = True,
) -> spg.Point:
    """Construct the exact apex of an equilateral triangle erected on ``P1-P2`` (Euclid I.1)."""
    mx = _model_simplify(model, (P1.x + P2.x) / sp.Integer(2))
    my = _model_simplify(model, (P1.y + P2.y) / sp.Integer(2))
    dx = _model_simplify(model, P2.x - P1.x)
    dy = _model_simplify(model, P2.y - P1.y)
    nx, ny = -dy, dx
    dot_opp = _model_simplify(model, nx * (opp.x - mx) + ny * (opp.y - my))
    if exact_sign(dot_opp) > 0:
        nx, ny = -nx, -ny
    sign = sp.Integer(1) if outward else sp.Integer(-1)
    h = sign * sp.sqrt(3) / sp.Integer(2)
    if not ID:
        ID = f"E_{{{model[opp].ID}}}"
    return add_point(
        model,
        _model_simplify(model, mx + h * nx),
        _model_simplify(model, my + h * ny),
        ID=ID,
        classes=classes or ["apex"],
        parents=[P1, P2],
        guide=guide,
    )


def intersect_lines(
    model: Model,
    P1: spg.Point,
    P2: spg.Point,
    Q1: spg.Point,
    Q2: spg.Point,
    ID: str = "X",
    classes: list[str] | None = None,
    guide: bool = False,
) -> spg.Point | None:
    """Intersect line ``P1-P2`` with line ``Q1-Q2`` using exact closed-form 2D algebra."""
    l1 = spg.Line(P1, P2)
    l2 = spg.Line(Q1, Q2)
    pts = intersect_2d(l1, l2)
    if not pts:
        return None
    pt = pts[0]
    return add_point(
        model,
        pt.x,
        pt.y,
        ID=ID,
        classes=classes,
        parents=[P1, P2, Q1, Q2],
        guide=guide,
    )


def reflection_in_point(
    model: Model,
    P: spg.Point,
    center: spg.Point,
    ID: str = "",
    classes: list[str] | None = None,
    guide: bool = False,
) -> spg.Point:
    """Reflect point ``P`` across ``center`` (``2*center - P``)."""
    if not ID:
        ID = f"R({model[P].ID},{model[center].ID})"
    return add_point(
        model,
        _model_simplify(model, sp.Integer(2) * center.x - P.x),
        _model_simplify(model, sp.Integer(2) * center.y - P.y),
        ID=ID,
        classes=classes,
        parents=[P, center],
        guide=guide,
    )


# ---------------------------------------------------------------------------
# Derived Triangles on (A, B, C)
# ---------------------------------------------------------------------------


def medial_triangle(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    draw_polygon: bool = True,
) -> tuple[spg.Point, spg.Point, spg.Point]:
    """Construct the medial triangle ``M_a M_b M_c`` (side midpoints of ``ABC``)."""
    Ma = midpoint(model, B, C, ID="M_a", guide=True)
    Mb = midpoint(model, C, A, ID="M_b", guide=True)
    Mc = midpoint(model, A, B, ID="M_c", guide=True)
    if draw_polygon:
        add_polygon(model, [Ma, Mb, Mc], ID="< M_a M_b M_c >", classes=["secondary"])
    return Ma, Mb, Mc


def anticomplementary_triangle(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    draw_polygon: bool = True,
) -> tuple[spg.Point, spg.Point, spg.Point]:
    """Construct the anticomplementary triangle ``K_a K_b K_c``."""
    Aa = point_from_barycentrics(model, A, B, C, -1, 1, 1, ID="K_a", guide=True)
    Ba = point_from_barycentrics(model, A, B, C, 1, -1, 1, ID="K_b", guide=True)
    Ca = point_from_barycentrics(model, A, B, C, 1, 1, -1, ID="K_c", guide=True)
    if draw_polygon:
        add_polygon(model, [Aa, Ba, Ca], ID="< K_a K_b K_c >", classes=["secondary"])
    return Aa, Ba, Ca


def orthic_triangle(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    draw_polygon: bool = True,
) -> tuple[spg.Point, spg.Point, spg.Point]:
    """Construct the orthic triangle ``H_a H_b H_c`` (altitude feet on ``BC, CA, AB``)."""
    Ha = perpendicular_foot(model, A, B, C, ID="H_a", guide=True)
    Hb = perpendicular_foot(model, B, C, A, ID="H_b", guide=True)
    Hc = perpendicular_foot(model, C, A, B, ID="H_c", guide=True)
    if draw_polygon:
        add_polygon(model, [Ha, Hb, Hc], ID="< H_a H_b H_c >", classes=["secondary"])
    return Ha, Hb, Hc


def incentral_triangle(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    draw_polygon: bool = False,
) -> tuple[spg.Point, spg.Point, spg.Point]:
    """Construct the incentral triangle ``I_a I_b I_c`` (internal angle bisector feet)."""
    a, b, c = triangle_side_lengths(A, B, C, model=model)
    Ia = point_from_barycentrics(model, A, B, C, 0, b, c, ID="I_a", classes=["guide"], guide=True)
    Ib = point_from_barycentrics(model, A, B, C, a, 0, c, ID="I_b", classes=["guide"], guide=True)
    Ic = point_from_barycentrics(model, A, B, C, a, b, 0, ID="I_c", classes=["guide"], guide=True)
    if draw_polygon:
        add_polygon(model, [Ia, Ib, Ic], ID="< I_a I_b I_c >", classes=["secondary"])
    return Ia, Ib, Ic


def intouch_triangle(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    draw_polygon: bool = True,
    draw_incircle: bool = True,
) -> tuple[spg.Point, spg.Point, spg.Point]:
    """Construct the intouch (contact) triangle ``T_a T_b T_c`` of the incircle."""
    a, b, c = triangle_side_lengths(A, B, C, model=model)
    X1 = point_from_barycentrics(model, A, B, C, a, b, c, ID="X_1", classes=["center"])
    Ta = perpendicular_foot(model, X1, B, C, ID="T_a", guide=True)
    Tb = perpendicular_foot(model, X1, C, A, ID="T_b", guide=True)
    Tc = perpendicular_foot(model, X1, A, B, ID="T_c", guide=True)
    if draw_incircle:
        add_circle(model, X1, Tc, ID="incircle", classes=["incircle"])
    if draw_polygon:
        add_polygon(model, [Ta, Tb, Tc], ID="< T_a T_b T_c >", classes=["secondary"])
    return Ta, Tb, Tc


def extouch_triangle(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    draw_polygon: bool = True,
) -> tuple[spg.Point, spg.Point, spg.Point]:
    """Construct the extouch triangle ``N_a N_b N_c`` (excircle tangency points)."""
    a, b, c = triangle_side_lengths(A, B, C, model=model)
    s_semi = _model_simplify(model, (a + b + c) / sp.Integer(2))
    Na = point_from_barycentrics(model, A, B, C, 0, s_semi - c, s_semi - b, ID="N_a", guide=True)
    Nb = point_from_barycentrics(model, A, B, C, s_semi - c, 0, s_semi - a, ID="N_b", guide=True)
    Nc = point_from_barycentrics(model, A, B, C, s_semi - b, s_semi - a, 0, ID="N_c", guide=True)
    if draw_polygon:
        add_polygon(model, [Na, Nb, Nc], ID="< N_a N_b N_c >", classes=["secondary"])
    return Na, Nb, Nc


def excentral_triangle(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    draw_polygon: bool = True,
) -> tuple[spg.Point, spg.Point, spg.Point]:
    """Construct the excentral triangle ``J_a J_b J_c`` (excenters of ``ABC``)."""
    a, b, c = triangle_side_lengths(A, B, C, model=model)
    Ja = point_from_barycentrics(model, A, B, C, -a, b, c, ID="J_a", guide=True)
    Jb = point_from_barycentrics(model, A, B, C, a, -b, c, ID="J_b", guide=True)
    Jc = point_from_barycentrics(model, A, B, C, a, b, -c, ID="J_c", guide=True)
    if draw_polygon:
        add_polygon(model, [Ja, Jb, Jc], ID="< J_a J_b J_c >", classes=["secondary"])
    return Ja, Jb, Jc


def tangential_triangle(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    draw_polygon: bool = True,
    draw_circumcircle: bool = True,
) -> tuple[spg.Point, spg.Point, spg.Point]:
    """Construct the tangential triangle ``Tan_a Tan_b Tan_c``."""
    qa, qb, qc = triangle_side_quadrances(A, B, C, model=model)
    if draw_circumcircle:
        circumcircle(model, A, B, C)
    Ta = point_from_barycentrics(model, A, B, C, -qa, qb, qc, ID="Tan_a", guide=True)
    Tb = point_from_barycentrics(model, A, B, C, qa, -qb, qc, ID="Tan_b", guide=True)
    Tc = point_from_barycentrics(model, A, B, C, qa, qb, -qc, ID="Tan_c", guide=True)
    if draw_polygon:
        add_polygon(model, [Ta, Tb, Tc], ID="< Tan_a Tan_b Tan_c >", classes=["secondary"])
    return Ta, Tb, Tc


def outer_equilateral_triangles(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    draw_polygons: bool = True,
) -> tuple[spg.Point, spg.Point, spg.Point]:
    """Erect outward equilateral triangles on ``BC, CA, AB`` (Euclid I.1)."""
    Ea = equilateral_apex(model, B, C, A, outward=True, ID="A'", guide=True)
    Eb = equilateral_apex(model, C, A, B, outward=True, ID="B'", guide=True)
    Ec = equilateral_apex(model, A, B, C, outward=True, ID="C'", guide=True)
    if draw_polygons:
        add_polygon(model, [B, C, Ea], ID="< B C A' >", classes=["secondary"])
        add_polygon(model, [C, A, Eb], ID="< C A B' >", classes=["secondary"])
        add_polygon(model, [A, B, Ec], ID="< A B C' >", classes=["secondary"])
    return Ea, Eb, Ec


def inner_equilateral_triangles(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    draw_polygons: bool = True,
) -> tuple[spg.Point, spg.Point, spg.Point]:
    """Erect inward equilateral triangles on ``BC, CA, AB`` (Euclid I.1)."""
    Ea = equilateral_apex(model, B, C, A, outward=False, ID="A''", guide=True)
    Eb = equilateral_apex(model, C, A, B, outward=False, ID="B''", guide=True)
    Ec = equilateral_apex(model, A, B, C, outward=False, ID="C''", guide=True)
    if draw_polygons:
        add_polygon(model, [B, C, Ea], ID="< B C A'' >", classes=["secondary"])
        add_polygon(model, [C, A, Eb], ID="< C A B'' >", classes=["secondary"])
        add_polygon(model, [A, B, Ec], ID="< A B C'' >", classes=["secondary"])
    return Ea, Eb, Ec


def outer_napoleon_triangle(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    draw_polygon: bool = True,
) -> tuple[spg.Point, spg.Point, spg.Point]:
    """Construct the outer Napoleon triangle ``Nap_a Nap_b Nap_c``."""
    Ea, Eb, Ec = outer_equilateral_triangles(model, A, B, C, draw_polygons=True)
    Na = point_from_barycentrics(model, B, C, Ea, 1, 1, 1, ID="Nap_a", guide=True)
    Nb = point_from_barycentrics(model, C, A, Eb, 1, 1, 1, ID="Nap_b", guide=True)
    Nc = point_from_barycentrics(model, A, B, Ec, 1, 1, 1, ID="Nap_c", guide=True)
    if draw_polygon:
        add_polygon(model, [Na, Nb, Nc], ID="< Nap_a Nap_b Nap_c >", classes=["secondary"])
    return Na, Nb, Nc


def inner_napoleon_triangle(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    draw_polygon: bool = True,
) -> tuple[spg.Point, spg.Point, spg.Point]:
    """Construct the inner Napoleon triangle ``Nap'_a Nap'_b Nap'_c``."""
    Ea, Eb, Ec = inner_equilateral_triangles(model, A, B, C, draw_polygons=True)
    Na = point_from_barycentrics(model, B, C, Ea, 1, 1, 1, ID="Nap'_a", guide=True)
    Nb = point_from_barycentrics(model, C, A, Eb, 1, 1, 1, ID="Nap'_b", guide=True)
    Nc = point_from_barycentrics(model, A, B, Ec, 1, 1, 1, ID="Nap'_c", guide=True)
    if draw_polygon:
        add_polygon(model, [Na, Nb, Nc], ID="< Nap'_a Nap'_b Nap'_c >", classes=["secondary"])
    return Na, Nb, Nc


def pedal_triangle(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    P: spg.Point,
    prefix: str = "P",
    draw_polygon: bool = True,
) -> tuple[spg.Point, spg.Point, spg.Point]:
    """Construct the pedal triangle of ``P`` with respect to ``ABC``."""
    Pa = perpendicular_foot(model, P, B, C, ID=f"{prefix}_a", guide=True)
    Pb = perpendicular_foot(model, P, C, A, ID=f"{prefix}_b", guide=True)
    Pc = perpendicular_foot(model, P, A, B, ID=f"{prefix}_c", guide=True)
    if draw_polygon:
        add_polygon(
            model, [Pa, Pb, Pc], ID=f"< {prefix}_a {prefix}_b {prefix}_c >", classes=["secondary"]
        )
    return Pa, Pb, Pc


def cevian_triangle(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    P: spg.Point,
    prefix: str = "C",
    draw_polygon: bool = True,
) -> tuple[spg.Point, spg.Point, spg.Point]:
    """Construct the cevian triangle of ``P`` with respect to ``ABC``."""
    u, v, w = barycentrics_of(A, B, C, P, model=model)
    Ca = point_from_barycentrics(model, A, B, C, 0, v, w, ID=f"{prefix}_a", guide=True)
    Cb = point_from_barycentrics(model, A, B, C, u, 0, w, ID=f"{prefix}_b", guide=True)
    Cc = point_from_barycentrics(model, A, B, C, u, v, 0, ID=f"{prefix}_c", guide=True)
    if draw_polygon:
        add_polygon(
            model, [Ca, Cb, Cc], ID=f"< {prefix}_a {prefix}_b {prefix}_c >", classes=["secondary"]
        )
    return Ca, Cb, Cc


# ---------------------------------------------------------------------------
# Canonical *Principles of Geometry* Standard Library Constructors (X_1 - X_20+)
# ---------------------------------------------------------------------------


def perspector(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    A2: spg.Point,
    B2: spg.Point,
    C2: spg.Point,
    ID: str = "X",
    classes: list[str] | None = None,
    draw_cevians: bool = True,
) -> spg.Point | None:
    """Construct the perspector of ``ABC`` and ``A2 B2 C2`` by intersecting ``AA2, BB2, CC2``."""
    if draw_cevians:
        add_line(model, A, A2, classes=["bisector"])
        add_line(model, B, B2, classes=["bisector"])
        add_line(model, C, C2, classes=["bisector"])
    return intersect_lines(
        model, A, A2, B, B2, ID=ID, classes=classes or ["selected", "target"]
    )


def incenter(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X_1",
    classes: list[str] | None = None,
    draw_bisectors: bool = False,
    draw_incircle: bool = False,
    draw_touchpoints: bool = False,
) -> spg.Point:
    """Construct the incenter ``X_1`` of triangle ``ABC`` (Euclid IV.4).

    Parameters
    ----------
    model :
        Target :class:`geometor.model.Model`.
    A, B, C :
        Vertices of reference triangle ``ABC``.
    ID :
        Element identifier (defaults to ``"X_1"``).
    classes :
        Optional CSS/model classes.
    draw_bisectors :
        When ``True``, constructs exact internal angle bisector feet ``I_a, I_b, I_c``
        and concurring bisector lines ``[ A I_a ]``, ``[ B I_b ]``, ``[ C I_c ]``.
    draw_incircle :
        When ``True``, constructs the inscribed circle ``incircle`` centered at
        ``X_1`` through exact tangency foot ``T_c``.
    draw_touchpoints :
        When ``True``, constructs all three right-spread touchpoints ``T_a, T_b, T_c``.
    """
    a, b, c = triangle_side_lengths(A, B, C, model=model)
    X1 = point_from_barycentrics(
        model, A, B, C, a, b, c, ID=ID, classes=classes or ["center"]
    )
    if draw_bisectors:
        Ia, Ib, Ic = incentral_triangle(model, A, B, C, draw_polygon=False)
        add_line(model, A, Ia, ID="[ A I_a ]", classes=["bisector"])
        add_line(model, B, Ib, ID="[ B I_b ]", classes=["bisector"])
        add_line(model, C, Ic, ID="[ C I_c ]", classes=["bisector"])
    if draw_touchpoints:
        perpendicular_foot(model, X1, B, C, ID="T_a", classes=["foot", "guide"], guide=True)
        perpendicular_foot(model, X1, C, A, ID="T_b", classes=["foot", "guide"], guide=True)
        Tc = perpendicular_foot(model, X1, A, B, ID="T_c", classes=["foot", "guide"], guide=True)
    else:
        Tc = model.get_element_by_ID("T_c")
    if draw_incircle:
        if not isinstance(Tc, spg.Point):
            Tc = perpendicular_foot(
                model, X1, A, B, ID="T_c", classes=["foot", "guide"], guide=True
            )
        add_circle(model, X1, Tc, ID="incircle", classes=["incircle"])
    return X1


def centroid(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X_2",
    classes: list[str] | None = None,
    draw_medians: bool = False,
) -> spg.Point:
    """Construct the centroid ``X_2`` of triangle ``ABC``."""
    if draw_medians:
        Ma, Mb, Mc = medial_triangle(model, A, B, C, draw_polygon=True)
        add_line(model, A, Ma, ID="[ A M_a ]", classes=["bisector"])
        add_line(model, B, Mb, ID="[ B M_b ]", classes=["bisector"])
        add_line(model, C, Mc, ID="[ C M_c ]", classes=["bisector"])
    return point_from_barycentrics(
        model, A, B, C, 1, 1, 1, ID=ID, classes=classes or ["center"]
    )


def circumcenter(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X_3",
    classes: list[str] | None = None,
    draw_bisectors: bool = False,
    draw_circumcircle: bool = False,
) -> spg.Point:
    """Construct the circumcenter ``X_3`` of triangle ``ABC`` (Euclid IV.5)."""
    qa, qb, qc = triangle_side_quadrances(A, B, C, model=model)
    sa = _model_simplify(model, qb + qc - qa)
    sb = _model_simplify(model, qc + qa - qb)
    sc = _model_simplify(model, qa + qb - qc)
    X3 = point_from_barycentrics(
        model, A, B, C, qa * sa, qb * sb, qc * sc, ID=ID, classes=classes or ["center"]
    )
    if draw_bisectors:
        Ma = midpoint(model, B, C, ID="M_a", guide=True)
        Mb = midpoint(model, C, A, ID="M_b", guide=True)
        Mc = midpoint(model, A, B, ID="M_c", guide=True)
        add_line(model, X3, Ma, ID=f"[ {ID} M_a ]", classes=["bisector"])
        add_line(model, X3, Mb, ID=f"[ {ID} M_b ]", classes=["bisector"])
        add_line(model, X3, Mc, ID=f"[ {ID} M_c ]", classes=["bisector"])
    if draw_circumcircle:
        add_circle(model, X3, A, ID="circumcircle", classes=["circumcircle"])
    return X3


def orthocenter(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X_4",
    classes: list[str] | None = None,
    draw_altitudes: bool = False,
) -> spg.Point:
    """Construct the orthocenter ``X_4`` of triangle ``ABC``."""
    qa, qb, qc = triangle_side_quadrances(A, B, C, model=model)
    sa = _model_simplify(model, qb + qc - qa)
    sb = _model_simplify(model, qc + qa - qb)
    sc = _model_simplify(model, qa + qb - qc)
    if draw_altitudes:
        Ha, Hb, Hc = orthic_triangle(model, A, B, C, draw_polygon=True)
        add_line(model, A, Ha, ID="[ A H_a ]", classes=["bisector"])
        add_line(model, B, Hb, ID="[ B H_b ]", classes=["bisector"])
        add_line(model, C, Hc, ID="[ C H_c ]", classes=["bisector"])
    return point_from_barycentrics(
        model, A, B, C, sb * sc, sc * sa, sa * sb, ID=ID, classes=classes or ["center"]
    )


def nine_point_center(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X_5",
    classes: list[str] | None = None,
    draw_circle: bool = False,
) -> spg.Point:
    """Construct the nine-point center ``X_5`` of triangle ``ABC``."""
    qa, qb, qc = triangle_side_quadrances(A, B, C, model=model)
    u = _model_simplify(model, qa * (qb + qc) - (qb - qc) ** 2)
    v = _model_simplify(model, qb * (qc + qa) - (qc - qa) ** 2)
    w = _model_simplify(model, qc * (qa + qb) - (qa - qb) ** 2)
    X5 = point_from_barycentrics(
        model, A, B, C, u, v, w, ID=ID, classes=classes or ["center"]
    )
    if draw_circle:
        Mc = model.get_element_by_ID("M_c")
        if not isinstance(Mc, spg.Point):
            Mc = midpoint(model, A, B, ID="M_c", guide=True)
        add_circle(model, X5, Mc, ID="nine_point_circle", classes=["nine_point_circle"])
    return X5


def symmedian_point(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X_6",
    classes: list[str] | None = None,
    draw_symmedians: bool = False,
) -> spg.Point:
    """Construct the symmedian (Lemoine) point ``X_6`` of triangle ``ABC``."""
    qa, qb, qc = triangle_side_quadrances(A, B, C, model=model)
    if draw_symmedians:
        Ta, Tb, Tc = tangential_triangle(
            model, A, B, C, draw_polygon=True, draw_circumcircle=True
        )
        add_line(model, A, Ta, ID="[ A Tan_a ]", classes=["bisector"])
        add_line(model, B, Tb, ID="[ B Tan_b ]", classes=["bisector"])
        add_line(model, C, Tc, ID="[ C Tan_c ]", classes=["bisector"])
    return point_from_barycentrics(
        model, A, B, C, qa, qb, qc, ID=ID, classes=classes or ["center"]
    )


def gergonne_point(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X_7",
    classes: list[str] | None = None,
    draw_cevians: bool = False,
    draw_intouch: bool = False,
) -> spg.Point:
    """Construct the Gergonne point ``X_7`` of triangle ``ABC``."""
    if draw_cevians or draw_intouch:
        Ta, Tb, Tc = intouch_triangle(
            model, A, B, C, draw_polygon=True, draw_incircle=True
        )
        if draw_cevians:
            add_line(model, A, Ta, ID="[ A T_a ]", classes=["bisector"])
            add_line(model, B, Tb, ID="[ B T_b ]", classes=["bisector"])
            add_line(model, C, Tc, ID="[ C T_c ]", classes=["bisector"])
    a, b, c = triangle_side_lengths(A, B, C, model=model)
    return point_from_barycentrics(
        model,
        A,
        B,
        C,
        (a + b - c) * (c + a - b),
        (b + c - a) * (a + b - c),
        (c + a - b) * (b + c - a),
        ID=ID,
        classes=classes or ["center"],
    )


def nagel_point(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X_8",
    classes: list[str] | None = None,
    draw_cevians: bool = False,
    draw_extouch: bool = False,
) -> spg.Point:
    """Construct the Nagel point ``X_8`` of triangle ``ABC``."""
    if draw_cevians or draw_extouch:
        Na, Nb, Nc = extouch_triangle(model, A, B, C, draw_polygon=True)
        if draw_cevians:
            add_line(model, A, Na, ID="[ A N_a ]", classes=["bisector"])
            add_line(model, B, Nb, ID="[ B N_b ]", classes=["bisector"])
            add_line(model, C, Nc, ID="[ C N_c ]", classes=["bisector"])
    a, b, c = triangle_side_lengths(A, B, C, model=model)
    return point_from_barycentrics(
        model,
        A,
        B,
        C,
        b + c - a,
        c + a - b,
        a + b - c,
        ID=ID,
        classes=classes or ["center"],
    )


def mittenpunkt(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X_9",
    classes: list[str] | None = None,
) -> spg.Point:
    """Construct the Mittenpunkt ``X_9`` of triangle ``ABC``."""
    a, b, c = triangle_side_lengths(A, B, C, model=model)
    return point_from_barycentrics(
        model,
        A,
        B,
        C,
        a * (b + c - a),
        b * (c + a - b),
        c * (a + b - c),
        ID=ID,
        classes=classes or ["center"],
    )


def spieker_center(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X_10",
    classes: list[str] | None = None,
    draw_circle: bool = False,
    draw_bisectors: bool = False,
    draw_medial: bool = False,
) -> spg.Point:
    """Construct the Spieker center ``X_10`` of triangle ``ABC``."""
    a, b, c = triangle_side_lengths(A, B, C, model=model)
    X10 = point_from_barycentrics(
        model, A, B, C, b + c, c + a, a + b, ID=ID, classes=classes or ["center"]
    )
    if draw_medial or draw_bisectors or draw_circle:
        Ma, Mb, Mc = medial_triangle(model, A, B, C, draw_polygon=True)
        if draw_bisectors:
            add_line(model, Ma, X10, ID=f"[ M_a {ID} ]", classes=["bisector"])
            add_line(model, Mb, X10, ID=f"[ M_b {ID} ]", classes=["bisector"])
            add_line(model, Mc, X10, ID=f"[ M_c {ID} ]", classes=["bisector"])
        if draw_circle:
            sp_foot = perpendicular_foot(
                model, X10, Ma, Mb, ID="T_sp", classes=["foot", "guide"], guide=True
            )
            add_circle(model, X10, sp_foot, ID="spieker_circle", classes=["incircle"])
    return X10


def feuerbach_point(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X_11",
    classes: list[str] | None = None,
    draw_circles: bool = False,
) -> spg.Point:
    """Construct the Feuerbach point ``X_11`` of triangle ``ABC``."""
    if draw_circles:
        incircle(model, A, B, C)
        nine_point_circle(model, A, B, C)
    a, b, c = triangle_side_lengths(A, B, C, model=model)
    return point_from_barycentrics(
        model,
        A,
        B,
        C,
        (b + c - a) * (b - c) ** 2,
        (c + a - b) * (c - a) ** 2,
        (a + b - c) * (a - b) ** 2,
        ID=ID,
        classes=classes or ["center"],
    )


def harmonic_feuerbach_point(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X_12",
    classes: list[str] | None = None,
) -> spg.Point:
    """Construct ``X_12`` (the ``{X_1, X_5}``-harmonic conjugate of ``X_11``)."""
    a, b, c = triangle_side_lengths(A, B, C, model=model)
    return point_from_barycentrics(
        model,
        A,
        B,
        C,
        (b + c) ** 2 * (a + b - c) * (c + a - b),
        (c + a) ** 2 * (b + c - a) * (a + b - c),
        (a + b) ** 2 * (c + a - b) * (b + c - a),
        ID=ID,
        classes=classes or ["center"],
    )


def fermat_point(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X_13",
    classes: list[str] | None = None,
    draw_equilaterals: bool = False,
) -> spg.Point:
    """Construct the 1st isogonic center (Fermat point) ``X_13``."""
    if draw_equilaterals:
        Ea, Eb, Ec = outer_equilateral_triangles(model, A, B, C, draw_polygons=True)
        add_line(model, A, Ea, ID="[ A A' ]", classes=["bisector"])
        add_line(model, B, Eb, ID="[ B B' ]", classes=["bisector"])
        add_line(model, C, Ec, ID="[ C C' ]", classes=["bisector"])
    qa, qb, qc = triangle_side_quadrances(A, B, C, model=model)
    SA = _model_simplify(model, (qb + qc - qa) / sp.Integer(2))
    SB = _model_simplify(model, (qc + qa - qb) / sp.Integer(2))
    SC = _model_simplify(model, (qa + qb - qc) / sp.Integer(2))
    S = _model_simplify(model, sp.Integer(2) * abs(triangle_signed_area(A, B, C, model=model)))
    s3 = sp.sqrt(3)
    return point_from_barycentrics(
        model,
        A,
        B,
        C,
        (S + s3 * SB) * (S + s3 * SC),
        (S + s3 * SC) * (S + s3 * SA),
        (S + s3 * SA) * (S + s3 * SB),
        ID=ID,
        classes=classes or ["center"],
    )


def second_isogonic_center(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X_14",
    classes: list[str] | None = None,
) -> spg.Point:
    """Construct the 2nd isogonic center ``X_14``."""
    qa, qb, qc = triangle_side_quadrances(A, B, C, model=model)
    SA = _model_simplify(model, (qb + qc - qa) / sp.Integer(2))
    SB = _model_simplify(model, (qc + qa - qb) / sp.Integer(2))
    SC = _model_simplify(model, (qa + qb - qc) / sp.Integer(2))
    S = _model_simplify(model, sp.Integer(2) * abs(triangle_signed_area(A, B, C, model=model)))
    s3 = sp.sqrt(3)
    return point_from_barycentrics(
        model,
        A,
        B,
        C,
        (S - s3 * SB) * (S - s3 * SC),
        (S - s3 * SC) * (S - s3 * SA),
        (S - s3 * SA) * (S - s3 * SB),
        ID=ID,
        classes=classes or ["center"],
    )


def first_isodynamic_point(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X_15",
    classes: list[str] | None = None,
) -> spg.Point:
    """Construct the 1st isodynamic point ``X_15``."""
    qa, qb, qc = triangle_side_quadrances(A, B, C, model=model)
    SA = _model_simplify(model, (qb + qc - qa) / sp.Integer(2))
    SB = _model_simplify(model, (qc + qa - qb) / sp.Integer(2))
    SC = _model_simplify(model, (qa + qb - qc) / sp.Integer(2))
    S = _model_simplify(model, sp.Integer(2) * abs(triangle_signed_area(A, B, C, model=model)))
    s3 = sp.sqrt(3)
    return point_from_barycentrics(
        model,
        A,
        B,
        C,
        qa * (S + s3 * SA),
        qb * (S + s3 * SB),
        qc * (S + s3 * SC),
        ID=ID,
        classes=classes or ["center"],
    )


def second_isodynamic_point(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X_16",
    classes: list[str] | None = None,
) -> spg.Point:
    """Construct the 2nd isodynamic point ``X_16``."""
    qa, qb, qc = triangle_side_quadrances(A, B, C, model=model)
    SA = _model_simplify(model, (qb + qc - qa) / sp.Integer(2))
    SB = _model_simplify(model, (qc + qa - qb) / sp.Integer(2))
    SC = _model_simplify(model, (qa + qb - qc) / sp.Integer(2))
    S = _model_simplify(model, sp.Integer(2) * abs(triangle_signed_area(A, B, C, model=model)))
    s3 = sp.sqrt(3)
    return point_from_barycentrics(
        model,
        A,
        B,
        C,
        qa * (S - s3 * SA),
        qb * (S - s3 * SB),
        qc * (S - s3 * SC),
        ID=ID,
        classes=classes or ["center"],
    )


def first_napoleon_point(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X_17",
    classes: list[str] | None = None,
) -> spg.Point:
    """Construct the 1st Napoleon point ``X_17``."""
    qa, qb, qc = triangle_side_quadrances(A, B, C, model=model)
    SA = _model_simplify(model, (qb + qc - qa) / sp.Integer(2))
    SB = _model_simplify(model, (qc + qa - qb) / sp.Integer(2))
    SC = _model_simplify(model, (qa + qb - qc) / sp.Integer(2))
    S = _model_simplify(model, sp.Integer(2) * abs(triangle_signed_area(A, B, C, model=model)))
    s3 = sp.sqrt(3)
    return point_from_barycentrics(
        model,
        A,
        B,
        C,
        (SB + s3 * S) * (SC + s3 * S),
        (SC + s3 * S) * (SA + s3 * S),
        (SA + s3 * S) * (SB + s3 * S),
        ID=ID,
        classes=classes or ["center"],
    )


def second_napoleon_point(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X_18",
    classes: list[str] | None = None,
) -> spg.Point:
    """Construct the 2nd Napoleon point ``X_18``."""
    qa, qb, qc = triangle_side_quadrances(A, B, C, model=model)
    SA = _model_simplify(model, (qb + qc - qa) / sp.Integer(2))
    SB = _model_simplify(model, (qc + qa - qb) / sp.Integer(2))
    SC = _model_simplify(model, (qa + qb - qc) / sp.Integer(2))
    S = _model_simplify(model, sp.Integer(2) * abs(triangle_signed_area(A, B, C, model=model)))
    s3 = sp.sqrt(3)
    return point_from_barycentrics(
        model,
        A,
        B,
        C,
        (SB - s3 * S) * (SC - s3 * S),
        (SC - s3 * S) * (SA - s3 * S),
        (SA - s3 * S) * (SB - s3 * S),
        ID=ID,
        classes=classes or ["center"],
    )


def clawson_point(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X_19",
    classes: list[str] | None = None,
) -> spg.Point:
    """Construct the Clawson point ``X_19``."""
    a, b, c = triangle_side_lengths(A, B, C, model=model)
    qa, qb, qc = triangle_side_quadrances(A, B, C, model=model)
    sa = _model_simplify(model, qb + qc - qa)
    sb = _model_simplify(model, qc + qa - qb)
    sc = _model_simplify(model, qa + qb - qc)
    return point_from_barycentrics(
        model,
        A,
        B,
        C,
        a * sb * sc,
        b * sc * sa,
        c * sa * sb,
        ID=ID,
        classes=classes or ["center"],
    )


def de_longchamps_point(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X_20",
    classes: list[str] | None = None,
) -> spg.Point:
    """Construct the de Longchamps point ``X_20`` (reflection of ``X_4`` in ``X_3``)."""
    qa, qb, qc = triangle_side_quadrances(A, B, C, model=model)
    u = _model_simplify(
        model, -sp.Integer(3) * qa**2 + sp.Integer(2) * qa * (qb + qc) + (qb - qc) ** 2
    )
    v = _model_simplify(
        model, -sp.Integer(3) * qb**2 + sp.Integer(2) * qb * (qc + qa) + (qc - qa) ** 2
    )
    w = _model_simplify(
        model, -sp.Integer(3) * qc**2 + sp.Integer(2) * qc * (qa + qb) + (qa - qb) ** 2
    )
    return point_from_barycentrics(
        model, A, B, C, u, v, w, ID=ID, classes=classes or ["center"]
    )


def circumcircle_inverse_of_incenter(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X_36",
    classes: list[str] | None = None,
) -> spg.Point:
    """Construct ``X_36``, the circumcircle inverse of ``X_1``."""
    a, b, c = triangle_side_lengths(A, B, C, model=model)
    qa, qb, qc = triangle_side_quadrances(A, B, C, model=model)
    return point_from_barycentrics(
        model,
        A,
        B,
        C,
        qa * (qb + qc - qa - b * c),
        qb * (qc + qa - qb - c * a),
        qc * (qa + qb - qc - a * b),
        ID=ID,
        classes=classes or ["center"],
    )


def bevan_point(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X_40",
    classes: list[str] | None = None,
) -> spg.Point:
    """Construct the Bevan point ``X_40`` (reflection of ``X_1`` across ``X_3``)."""
    a, b, c = triangle_side_lengths(A, B, C, model=model)
    u = a * (a**3 + a**2 * (b + c) - a * (b + c) ** 2 - (b + c) * (b - c) ** 2)
    v = b * (b**3 + b**2 * (c + a) - b * (c + a) ** 2 - (c + a) * (c - a) ** 2)
    w = c * (c**3 + c**2 * (a + b) - c * (a + b) ** 2 - (a + b) * (a - b) ** 2)
    return point_from_barycentrics(
        model, A, B, C, u, v, w, ID=ID, classes=classes or ["center"]
    )


def isotomic_conjugate_of_incenter(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X_75",
    classes: list[str] | None = None,
) -> spg.Point:
    """Construct ``X_75``, the isotomic conjugate of ``X_1``."""
    a, b, c = triangle_side_lengths(A, B, C, model=model)
    return point_from_barycentrics(
        model, A, B, C, b * c, c * a, a * b, ID=ID, classes=classes or ["center"]
    )


# Backward-compatible `*_of` aliases for existing center construction scripts
incenter_of = incenter
centroid_of = centroid
circumcenter_of = circumcenter
orthocenter_of = orthocenter
nine_point_center_of = nine_point_center
symmedian_point_of = symmedian_point
gergonne_point_of = gergonne_point
nagel_point_of = nagel_point
mittenpunkt_of = mittenpunkt
spieker_center_of = spieker_center
feuerbach_point_of = feuerbach_point
fermat_point_of = fermat_point
clawson_point_of = clawson_point
de_longchamps_point_of = de_longchamps_point
bevan_point_of = bevan_point


# ---------------------------------------------------------------------------
# Fundamental Triangle Circles
# ---------------------------------------------------------------------------


def circumcircle(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Circle | None:
    """Construct the exact circumcircle of triangle ``ABC`` centered at ``X_3``."""
    X3 = circumcenter(model, A, B, C, ID="X_3")
    return add_circle(model, X3, A, ID="circumcircle", classes=["circumcircle"])


def incircle(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Circle | None:
    """Construct the exact incircle of triangle ``ABC`` centered at ``X_1``."""
    X1 = incenter(model, A, B, C, ID="X_1")
    Tc = model.get_element_by_ID("T_c")
    if not isinstance(Tc, spg.Point):
        Tc = perpendicular_foot(
            model, X1, A, B, ID="T_c", classes=["foot", "guide"], guide=True
        )
    return add_circle(model, X1, Tc, ID="incircle", classes=["incircle"])


def nine_point_circle(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Circle | None:
    """Construct the exact nine-point circle of triangle ``ABC`` centered at ``X_5``."""
    X5 = nine_point_center(model, A, B, C, ID="X_5")
    Mc = model.get_element_by_ID("M_c")
    if not isinstance(Mc, spg.Point):
        Mc = midpoint(model, A, B, ID="M_c", guide=True)
    return add_circle(model, X5, Mc, ID="nine_point_circle", classes=["nine_point_circle"])


def spieker_circle(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Circle | None:
    """Construct the exact Spieker circle (incircle of medial triangle) centered at ``X_10``."""
    Ma, Mb, _ = medial_triangle(model, A, B, C, draw_polygon=True)
    X10 = spieker_center(model, A, B, C, ID="X_10")
    Tsp = perpendicular_foot(
        model, X10, Ma, Mb, ID="T_sp", classes=["foot", "guide"], guide=True
    )
    return add_circle(model, X10, Tsp, ID="spieker_circle", classes=["incircle"])


# ---------------------------------------------------------------------------
# Exact Point Conjugates & Algebraic Triangle Operators on (A, B, C, P, ...)
# ---------------------------------------------------------------------------


def isogonal_conjugate(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    P: spg.Point,
    ID: str = "",
    classes: list[str] | None = None,
) -> spg.Point:
    """Construct the exact isogonal conjugate of point ``P`` with respect to ``ABC``."""
    qa, qb, qc = triangle_side_quadrances(A, B, C, model=model)
    u, v, w = barycentrics_of(A, B, C, P, model=model)
    if not ID:
        ID = f"isogonal({model[P].ID})"
    return point_from_barycentrics(
        model,
        A,
        B,
        C,
        qa * v * w,
        qb * w * u,
        qc * u * v,
        ID=ID,
        classes=classes,
    )


def isotomic_conjugate(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    P: spg.Point,
    ID: str = "",
    classes: list[str] | None = None,
) -> spg.Point:
    """Construct the exact isotomic conjugate of point ``P`` with respect to ``ABC``."""
    u, v, w = barycentrics_of(A, B, C, P, model=model)
    if not ID:
        ID = f"isotomic({model[P].ID})"
    return point_from_barycentrics(
        model, A, B, C, v * w, w * u, u * v, ID=ID, classes=classes
    )


def complement(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    P: spg.Point,
    ID: str = "",
    classes: list[str] | None = None,
) -> spg.Point:
    """Construct the exact complement of ``P`` (homothety at ``X_2`` by ``-1/2``)."""
    u, v, w = barycentrics_of(A, B, C, P, model=model)
    if not ID:
        ID = f"complement({model[P].ID})"
    return point_from_barycentrics(
        model, A, B, C, v + w, w + u, u + v, ID=ID, classes=classes
    )


def anticomplement(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    P: spg.Point,
    ID: str = "",
    classes: list[str] | None = None,
) -> spg.Point:
    """Construct the exact anticomplement of ``P`` (homothety at ``X_2`` by ``-2``)."""
    u, v, w = barycentrics_of(A, B, C, P, model=model)
    if not ID:
        ID = f"anticomplement({model[P].ID})"
    return point_from_barycentrics(
        model, A, B, C, -u + v + w, u - v + w, u + v - w, ID=ID, classes=classes
    )


def ceva_conjugate(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    P: spg.Point,
    Q: spg.Point,
    ID: str = "",
    classes: list[str] | None = None,
) -> spg.Point:
    """Construct the exact ``P``-Ceva conjugate of ``Q`` with respect to ``ABC``."""
    p, q, r_v = barycentrics_of(A, B, C, P, model=model)
    u, v, w = barycentrics_of(A, B, C, Q, model=model)
    if not ID:
        ID = f"ceva({model[P].ID},{model[Q].ID})"
    return point_from_barycentrics(
        model,
        A,
        B,
        C,
        u * (-u * q * r_v + v * r_v * p + w * p * q),
        v * (u * q * r_v - v * r_v * p + w * p * q),
        w * (u * q * r_v + v * r_v * p - w * p * q),
        ID=ID,
        classes=classes,
    )


def crosspoint(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    P: spg.Point,
    Q: spg.Point,
    ID: str = "",
    classes: list[str] | None = None,
) -> spg.Point:
    """Construct the exact crosspoint of ``P`` and ``Q`` with respect to ``ABC``."""
    p, q, r_v = barycentrics_of(A, B, C, P, model=model)
    u, v, w = barycentrics_of(A, B, C, Q, model=model)
    if not ID:
        ID = f"cross({model[P].ID},{model[Q].ID})"
    return point_from_barycentrics(
        model,
        A,
        B,
        C,
        p * u * (q * w + r_v * v),
        q * v * (r_v * u + p * w),
        r_v * w * (p * v + q * u),
        ID=ID,
        classes=classes,
    )


def cevapoint(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    P: spg.Point,
    Q: spg.Point,
    ID: str = "",
    classes: list[str] | None = None,
) -> spg.Point:
    """Construct the exact cevapoint of ``P`` and ``Q`` with respect to ``ABC``."""
    p, q, r_v = barycentrics_of(A, B, C, P, model=model)
    u, v, w = barycentrics_of(A, B, C, Q, model=model)
    if not ID:
        ID = f"cevapoint({model[P].ID},{model[Q].ID})"
    return point_from_barycentrics(
        model,
        A,
        B,
        C,
        (p * v + q * u) * (p * w + r_v * u),
        (q * w + r_v * v) * (q * u + p * v),
        (r_v * u + p * w) * (r_v * v + q * w),
        ID=ID,
        classes=classes,
    )


def central_line(
    model: Model,
    P: spg.Point,
    Q: spg.Point,
    i_num: int,
    j_num: int,
    incident: bool = False,
) -> spg.Line | None:
    """Add the exact central line ``{i, j}`` passing through ``X_i`` and ``X_j``."""
    cls = (
        ["golden", "euler"]
        if {i_num, j_num} <= {2, 3, 4, 5, 20, 30}
        else ["central_line"]
    )
    if incident:
        cls.append("incident")
    return add_line(model, P, Q, ID=f"{{ {i_num}, {j_num} }}", classes=cls)
