"""Composable geometric construction operators for `geometor.etc` using `geometor.model`.

Every operator accepts `(model, A, B, C, ...)` or `(model, P, Q, ...)` where points are
`sympy.geometry.Point` instances registered in `model`, enabling both classical Euclidean
compass-and-straightedge constructions and higher-order triangle-center compositions.
"""

from __future__ import annotations

import logging
import math
from typing import Any

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model
from geometor.model.element import CircleElement, Element

_SILENT_LOGGER = logging.getLogger("geometor.etc.silent")
_SILENT_LOGGER.addHandler(logging.NullHandler())
_SILENT_LOGGER.propagate = False


# ---------------------------------------------------------------------------
# Low-level `geometor.model.Model` Element Registration
# ---------------------------------------------------------------------------


def create_model(name: str = "ETC Construction") -> Model:
    """Create a silent `geometor.model.Model` instance for fast batch or standalone execution."""
    return Model(name, logger=_SILENT_LOGGER)


def add_point(
    model: Model,
    x: float,
    y: float,
    ID: str,
    classes: list[str] | None = None,
    parents: list[Any] | None = None,
    guide: bool = False,
) -> spg.Point:
    """Add or update a `Point` element in `model`."""
    existing = model.get_element_by_ID(ID)
    if existing is not None and isinstance(existing, spg.Point):
        if classes:
            for c in classes:
                model[existing].classes[c] = ""
        if not guide:
            model[existing].guide = False
        return existing

    pt = spg.Point(sp.Float(round(float(x), 8)), sp.Float(round(float(y), 8)), evaluate=False)
    el = Element(
        pt,
        parents=parents or [],
        classes=classes or [],
        ID=ID,
        guide=guide,
    )
    super(Model, model).__setitem__(pt, el)
    return pt


def add_line(
    model: Model,
    pt1: spg.Point,
    pt2: spg.Point,
    ID: str = "",
    classes: list[str] | None = None,
    guide: bool = False,
) -> spg.Line | None:
    """Add a `Line` element through `pt1` and `pt2` in `model`."""
    if pt1 == pt2:
        return None
    if not ID:
        ID = f"[ {model[pt1].ID} {model[pt2].ID} ]"
    ln = spg.Line(pt1, pt2, evaluate=False)
    el = Element(
        ln,
        parents=[pt1, pt2],
        classes=classes or [],
        ID=ID,
        guide=guide,
    )
    super(Model, model).__setitem__(ln, el)
    return ln


def add_circle(
    model: Model,
    pt_center: spg.Point,
    pt_radius: spg.Point,
    ID: str = "",
    classes: list[str] | None = None,
    guide: bool = False,
) -> spg.Circle | None:
    """Add a `CircleElement` centered at `pt_center` passing through `pt_radius`."""
    r_val = math.hypot(
        float(pt_center.x) - float(pt_radius.x),
        float(pt_center.y) - float(pt_radius.y),
    )
    if r_val < 1e-7:
        return None
    if not ID:
        ID = f"( {model[pt_center].ID} {model[pt_radius].ID} )"
    circ = spg.Circle(pt_center, sp.Float(round(r_val, 8)), evaluate=False)
    el = CircleElement(
        circ,
        pt_radius=pt_radius,
        parents=[pt_center, pt_radius],
        classes=classes or [],
        ID=ID,
        guide=guide,
    )
    super(Model, model).__setitem__(circ, el)
    return circ


def add_polygon(
    model: Model,
    pts: list[spg.Point],
    ID: str = "",
    classes: list[str] | None = None,
) -> spg.Polygon:
    """Add a `Polygon` (or `Triangle`) element to `model`."""
    if not ID:
        ids_str = " ".join(model[p].ID for p in pts)
        ID = f"< {ids_str} >"
    if len(pts) == 3:
        poly = sp.Basic.__new__(spg.Triangle, *pts)
    else:
        poly = sp.Basic.__new__(spg.Polygon, *pts)
    el = Element(
        poly,
        parents=pts,
        classes=classes or [],
        ID=ID,
        guide=False,
    )
    super(Model, model).__setitem__(poly, el)
    return poly


def add_segment(
    model: Model,
    pt1: spg.Point,
    pt2: spg.Point,
    ID: str = "",
    classes: list[str] | None = None,
) -> spg.Segment | None:
    """Add a `Segment` element between `pt1` and `pt2` in `model`."""
    if pt1 == pt2:
        return None
    if not ID:
        ID = f"/ {model[pt1].ID} {model[pt2].ID} /"
    seg = spg.Segment(pt1, pt2, evaluate=False)
    el = Element(
        seg,
        parents=[pt1, pt2],
        classes=classes or ["segment"],
        ID=ID,
        guide=False,
    )
    super(Model, model).__setitem__(seg, el)
    return seg


def promote_point_to_top(model: Model, pt: spg.Point) -> spg.Point:
    """Move `pt` to the end of `model` insertion order so it renders topmost in SVG."""
    if pt in model:
        el_data = model.pop(pt)
        super(Model, model).__setitem__(pt, el_data)
    return pt


# ---------------------------------------------------------------------------
# Baseline Reference Triangle Construction (Euclid I.22 on Unit Segment AB)
# ---------------------------------------------------------------------------


def construct_baseline_triangle(
    model: Model,
    a: float = 5.0,
    b: float = 6.0,
    c: float = 7.0,
    show_guides: bool = False,
) -> tuple[spg.Point, spg.Point, spg.Point]:
    """Construct reference triangle ABC on unit baseline AB = 1 with side ratios (a : b : c).

    Uses Euclid I.22 circle intersection centered at A=(0, 0) and B=(1, 0) with normalized
    radii b/c and a/c to determine vertex C in the upper half-plane.
    """
    scale = 1.0 / float(c)
    a_n = float(a) * scale
    b_n = float(b) * scale

    A = add_point(model, 0.0, 0.0, ID="A", classes=["given", "vertex"])
    B = add_point(model, 1.0, 0.0, ID="B", classes=["given", "vertex"])
    add_line(model, A, B, ID="[ A B ]", classes=["given", "sideline"])

    x_c = (1.0 + b_n**2 - a_n**2) / 2.0
    y_c = math.sqrt(max(0.0, b_n**2 - x_c**2))

    if show_guides:
        R_b = add_point(model, b_n, 0.0, ID="R_b", classes=["guide"], guide=True)
        R_a = add_point(model, 1.0 - a_n, 0.0, ID="R_a", classes=["guide"], guide=True)
        cA = add_circle(model, A, R_b, ID="( A R_b )", classes=["guide"], guide=True)
        cB = add_circle(model, B, R_a, ID="( B R_a )", classes=["guide"], guide=True)
        C = add_point(model, x_c, y_c, ID="C", classes=["vertex"], parents=[cA, cB])
    else:
        C = add_point(model, x_c, y_c, ID="C", classes=["vertex"])

    add_line(model, B, C, ID="[ B C ]", classes=["sideline"])
    add_line(model, C, A, ID="[ C A ]", classes=["sideline"])
    add_polygon(model, [A, B, C], ID="< A B C >", classes=["reference"])
    return A, B, C


# ---------------------------------------------------------------------------
# Euclidean & Coordinate Helpers on (A, B, C)
# ---------------------------------------------------------------------------


def _xy(pt: spg.Point) -> tuple[float, float]:
    return (float(pt.x), float(pt.y))


def triangle_side_lengths(
    A: spg.Point, B: spg.Point, C: spg.Point
) -> tuple[float, float, float]:
    """Return side lengths ``(a, b, c) = (|BC|, |CA|, |AB|)`` of triangle ABC."""
    ax, ay = _xy(A)
    bx, by = _xy(B)
    cx, cy = _xy(C)
    a = math.hypot(cx - bx, cy - by)
    b = math.hypot(ax - cx, ay - cy)
    c = math.hypot(bx - ax, by - ay)
    return (a, b, c)


def barycentrics_of(
    A: spg.Point, B: spg.Point, C: spg.Point, P: spg.Point
) -> tuple[float, float, float]:
    """Compute normalized barycentric coordinates (u, v, w) of point P with respect to ABC."""
    ax, ay = _xy(A)
    bx, by = _xy(B)
    cx, cy = _xy(C)
    px, py = _xy(P)
    det = (by - cy) * (ax - cx) + (cx - bx) * (ay - cy)
    if abs(det) < 1e-14:
        return (1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0)
    u = ((by - cy) * (px - cx) + (cx - bx) * (py - cy)) / det
    v = ((cy - ay) * (px - cx) + (ax - cx) * (py - cy)) / det
    w = 1.0 - u - v
    return (u, v, w)


def point_from_barycentrics(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    u: float,
    v: float,
    w: float,
    ID: str = "P",
    classes: list[str] | None = None,
    guide: bool = False,
) -> spg.Point:
    """Construct a point in `model` from homogeneous barycentric coordinates (u : v : w)."""
    ax, ay = _xy(A)
    bx, by = _xy(B)
    cx, cy = _xy(C)
    s = u + v + w
    if abs(s) < 1e-9:
        # Ideal point at infinity: project from centroid along direction vector
        gx, gy = (ax + bx + cx) / 3.0, (ay + by + cy) / 3.0
        dx = u * ax + v * bx + w * cx
        dy = u * ay + v * by + w * cy
        norm = math.hypot(dx, dy) or 1.0
        a_s, b_s, c_s = triangle_side_lengths(A, B, C)
        semi = 0.5 * (a_s + b_s + c_s)
        area = math.sqrt(max(1e-12, semi * (semi - a_s) * (semi - b_s) * (semi - c_s)))
        r_proj = 1.15 * (a_s * b_s * c_s) / (4.0 * area)
        return add_point(
            model,
            gx + r_proj * (dx / norm),
            gy + r_proj * (dy / norm),
            ID=ID,
            classes=classes,
            guide=guide,
        )
    x = (u * ax + v * bx + w * cx) / s
    y = (u * ay + v * by + w * cy) / s
    return add_point(model, x, y, ID=ID, classes=classes, guide=guide)


def point_from_trilinears(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    alpha: float,
    beta: float,
    gamma: float,
    ID: str = "P",
    classes: list[str] | None = None,
    guide: bool = False,
) -> spg.Point:
    """Construct a point in `model` from homogeneous trilinear coordinates (alpha : beta : gamma)."""
    a, b, c = triangle_side_lengths(A, B, C)
    return point_from_barycentrics(
        model, A, B, C, a * alpha, b * beta, c * gamma, ID=ID, classes=classes, guide=guide
    )


def _eval_cyclic_on_triangle(
    A: spg.Point, B: spg.Point, C: spg.Point, expr_str: str
) -> tuple[float, float, float] | None:
    """Evaluate a cyclic coordinate expression f(a, b, c, A, B, C) for all three cyclic permutations."""
    a, b, c = triangle_side_lengths(A, B, C)
    s = 0.5 * (a + b + c)
    area = math.sqrt(max(1e-16, s * (s - a) * (s - b) * (s - c)))
    R = (a * b * c) / (4.0 * area)
    r = area / s

    cos_A = max(-1.0, min(1.0, (b**2 + c**2 - a**2) / (2.0 * b * c)))
    cos_B = max(-1.0, min(1.0, (c**2 + a**2 - b**2) / (2.0 * c * a)))
    cos_C = max(-1.0, min(1.0, (a**2 + b**2 - c**2) / (2.0 * a * b)))
    ang_A = math.acos(cos_A)
    ang_B = math.acos(cos_B)
    ang_C = math.acos(cos_C)

    cot_A = cos_A / math.sin(ang_A)
    cot_B = cos_B / math.sin(ang_B)
    cot_C = cos_C / math.sin(ang_C)
    omega = math.atan(1.0 / (cot_A + cot_B + cot_C))

    Ra = area / (s - a)
    Rb = area / (s - b)
    Rc = area / (s - c)
    SA = 0.5 * (b**2 + c**2 - a**2)
    SB = 0.5 * (c**2 + a**2 - b**2)
    SC = 0.5 * (a**2 + b**2 - c**2)
    SW = 0.5 * (a**2 + b**2 + c**2)

    safe_funcs = {
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "cot": lambda x: math.cos(x) / math.sin(x),
        "sec": lambda x: 1.0 / math.cos(x),
        "csc": lambda x: 1.0 / math.sin(x),
        "sqrt": math.sqrt,
        "pi": math.pi,
        "omega": omega,
        "area": area,
        "R": R,
        "r": r,
        "s": s,
        "S": 2.0 * area,
        "SW": SW,
    }
    perms = [
        {"a": a, "b": b, "c": c, "A": ang_A, "B": ang_B, "C": ang_C, "Ra": Ra, "Rb": Rb, "Rc": Rc, "SA": SA, "SB": SB, "SC": SC},
        {"a": b, "b": c, "c": a, "A": ang_B, "B": ang_C, "C": ang_A, "Ra": Rb, "Rb": Rc, "Rc": Ra, "SA": SB, "SB": SC, "SC": SA},
        {"a": c, "b": a, "c": b, "A": ang_C, "B": ang_A, "C": ang_B, "Ra": Rc, "Rb": Ra, "Rc": Rb, "SA": SC, "SB": SA, "SC": SB},
    ]
    vals: list[float] = []
    try:
        code = compile(expr_str, "<coord>", "eval")
        for p in perms:
            val = float(eval(code, {"__builtins__": {}}, {**safe_funcs, **p}))
            if not math.isfinite(val):
                return None
            vals.append(val)
    except Exception:
        return None
    if all(abs(v) < 1e-14 for v in vals):
        return None
    return (vals[0], vals[1], vals[2])


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
    """Construct a point in `model` by evaluating a cyclic barycentric coordinate expression on ABC."""
    res = _eval_cyclic_on_triangle(A, B, C, expr_str)
    if res is None:
        return point_from_barycentrics(model, A, B, C, 1.0, 1.0, 1.0, ID=ID, classes=classes, guide=guide)
    return point_from_barycentrics(model, A, B, C, res[0], res[1], res[2], ID=ID, classes=classes, guide=guide)


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
    """Construct a point in `model` by evaluating a cyclic trilinear coordinate expression on ABC."""
    res = _eval_cyclic_on_triangle(A, B, C, expr_str)
    if res is None:
        return point_from_trilinears(model, A, B, C, 1.0, 1.0, 1.0, ID=ID, classes=classes, guide=guide)
    return point_from_trilinears(model, A, B, C, res[0], res[1], res[2], ID=ID, classes=classes, guide=guide)


def midpoint(
    model: Model,
    P: spg.Point,
    Q: spg.Point,
    ID: str = "",
    classes: list[str] | None = None,
    guide: bool = True,
) -> spg.Point:
    """Construct the midpoint of segment PQ (Euclid I.10)."""
    px, py = _xy(P)
    qx, qy = _xy(Q)
    if not ID:
        ID = f"M_{{{model[P].ID}{model[Q].ID}}}"
    return add_point(
        model,
        0.5 * (px + qx),
        0.5 * (py + qy),
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
    """Construct the orthogonal projection (foot of perpendicular, Euclid I.12) of P onto line L1-L2."""
    px, py = _xy(P)
    x1, y1 = _xy(L1)
    x2, y2 = _xy(L2)
    dx, dy = x2 - x1, y2 - y1
    len_sq = dx * dx + dy * dy
    t = ((px - x1) * dx + (py - y1) * dy) / len_sq if len_sq > 1e-14 else 0.0
    if not ID:
        ID = f"H_{{{model[P].ID}}}"
    return add_point(
        model,
        x1 + t * dx,
        y1 + t * dy,
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
    """Construct the apex of an equilateral triangle erected on segment P1-P2 (Euclid I.1)."""
    x1, y1 = _xy(P1)
    x2, y2 = _xy(P2)
    ox, oy = _xy(opp)
    mx, my = 0.5 * (x1 + x2), 0.5 * (y1 + y2)
    dx, dy = x2 - x1, y2 - y1
    nx, ny = -dy, dx
    if nx * (ox - mx) + ny * (oy - my) > 0:
        nx, ny = -nx, -ny
    sign = 1.0 if outward else -1.0
    h = sign * (math.sqrt(3.0) / 2.0)
    if not ID:
        ID = f"E_{{{model[opp].ID}}}"
    return add_point(
        model,
        mx + h * nx,
        my + h * ny,
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
    """Intersect line P1-P2 with line Q1-Q2 and register the intersection point in `model`."""
    x1, y1 = _xy(P1)
    x2, y2 = _xy(P2)
    x3, y3 = _xy(Q1)
    x4, y4 = _xy(Q2)
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(denom) < 1e-13:
        return None
    det1 = x1 * y2 - y1 * x2
    det2 = x3 * y4 - y3 * x4
    px = (det1 * (x3 - x4) - (x1 - x2) * det2) / denom
    py = (det1 * (y3 - y4) - (y1 - y2) * det2) / denom
    return add_point(model, px, py, ID=ID, classes=classes, parents=[P1, P2, Q1, Q2], guide=guide)


def reflection_in_point(
    model: Model,
    P: spg.Point,
    center: spg.Point,
    ID: str = "",
    classes: list[str] | None = None,
    guide: bool = False,
) -> spg.Point:
    """Reflect point P across `center` (2*center - P)."""
    px, py = _xy(P)
    cx, cy = _xy(center)
    if not ID:
        ID = f"R({model[P].ID},{model[center].ID})"
    return add_point(
        model,
        2.0 * cx - px,
        2.0 * cy - py,
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
    """Construct the medial triangle M_a M_b M_c (side midpoints of ABC)."""
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
    """Construct the anticomplementary triangle A_a B_a C_a (parallels to opposite sides through A, B, C)."""
    Aa = point_from_barycentrics(model, A, B, C, -1.0, 1.0, 1.0, ID="K_a", guide=True)
    Ba = point_from_barycentrics(model, A, B, C, 1.0, -1.0, 1.0, ID="K_b", guide=True)
    Ca = point_from_barycentrics(model, A, B, C, 1.0, 1.0, -1.0, ID="K_c", guide=True)
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
    """Construct the orthic triangle H_a H_b H_c (altitude feet on BC, CA, AB)."""
    Ha = perpendicular_foot(model, A, B, C, ID="H_a", guide=True)
    Hb = perpendicular_foot(model, B, C, A, ID="H_b", guide=True)
    Hc = perpendicular_foot(model, C, A, B, ID="H_c", guide=True)
    if draw_polygon:
        add_polygon(model, [Ha, Hb, Hc], ID="< H_a H_b H_c >", classes=["secondary"])
    return Ha, Hb, Hc


def intouch_triangle(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    draw_polygon: bool = True,
    draw_incircle: bool = True,
) -> tuple[spg.Point, spg.Point, spg.Point]:
    """Construct the intouch (contact) triangle T_a T_b T_c of the incircle on BC, CA, AB."""
    a, b, c = triangle_side_lengths(A, B, C)
    X1 = point_from_barycentrics(model, A, B, C, a, b, c, ID="X(1)", classes=["center"])
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
    """Construct the extouch triangle N_a N_b N_c (excircle tangency points on BC, CA, AB)."""
    a, b, c = triangle_side_lengths(A, B, C)
    s = 0.5 * (a + b + c)
    Na = point_from_barycentrics(model, A, B, C, 0.0, s - c, s - b, ID="N_a", guide=True)
    Nb = point_from_barycentrics(model, A, B, C, s - c, 0.0, s - a, ID="N_b", guide=True)
    Nc = point_from_barycentrics(model, A, B, C, s - b, s - a, 0.0, ID="N_c", guide=True)
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
    """Construct the excentral triangle J_a J_b J_c (excenters of ABC)."""
    a, b, c = triangle_side_lengths(A, B, C)
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
    """Construct the tangential triangle Tan_a Tan_b Tan_c bounded by circumcircle tangents at A, B, C."""
    a, b, c = triangle_side_lengths(A, B, C)
    if draw_circumcircle:
        circumcircle(model, A, B, C)
    Ta = point_from_barycentrics(model, A, B, C, -(a**2), b**2, c**2, ID="Tan_a", guide=True)
    Tb = point_from_barycentrics(model, A, B, C, a**2, -(b**2), c**2, ID="Tan_b", guide=True)
    Tc = point_from_barycentrics(model, A, B, C, a**2, b**2, -(c**2), ID="Tan_c", guide=True)
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
    """Erect outward equilateral triangles on BC, CA, AB (Euclid I.1) and return their apexes (A', B', C')."""
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
    """Erect inward equilateral triangles on BC, CA, AB (Euclid I.1) and return their apexes (A'', B'', C'')."""
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
    """Construct the outer Napoleon triangle (centroids of outward equilateral triangles on BC, CA, AB)."""
    Ea, Eb, Ec = outer_equilateral_triangles(model, A, B, C, draw_polygons=True)
    Na = point_from_barycentrics(model, B, C, Ea, 1.0, 1.0, 1.0, ID="Nap_a", guide=True)
    Nb = point_from_barycentrics(model, C, A, Eb, 1.0, 1.0, 1.0, ID="Nap_b", guide=True)
    Nc = point_from_barycentrics(model, A, B, Ec, 1.0, 1.0, 1.0, ID="Nap_c", guide=True)
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
    """Construct the inner Napoleon triangle (centroids of inward equilateral triangles on BC, CA, AB)."""
    Ea, Eb, Ec = inner_equilateral_triangles(model, A, B, C, draw_polygons=True)
    Na = point_from_barycentrics(model, B, C, Ea, 1.0, 1.0, 1.0, ID="Nap'_a", guide=True)
    Nb = point_from_barycentrics(model, C, A, Eb, 1.0, 1.0, 1.0, ID="Nap'_b", guide=True)
    Nc = point_from_barycentrics(model, A, B, Ec, 1.0, 1.0, 1.0, ID="Nap'_c", guide=True)
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
    """Construct the pedal triangle of P with respect to ABC (orthogonal projections onto BC, CA, AB)."""
    Pa = perpendicular_foot(model, P, B, C, ID=f"{prefix}_a", guide=True)
    Pb = perpendicular_foot(model, P, C, A, ID=f"{prefix}_b", guide=True)
    Pc = perpendicular_foot(model, P, A, B, ID=f"{prefix}_c", guide=True)
    if draw_polygon:
        add_polygon(model, [Pa, Pb, Pc], ID=f"< {prefix}_a {prefix}_b {prefix}_c >", classes=["secondary"])
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
    """Construct the cevian triangle of P with respect to ABC (intersections of AP, BP, CP with BC, CA, AB)."""
    u, v, w = barycentrics_of(A, B, C, P)
    Ca = point_from_barycentrics(model, A, B, C, 0.0, v, w, ID=f"{prefix}_a", guide=True)
    Cb = point_from_barycentrics(model, A, B, C, u, 0.0, w, ID=f"{prefix}_b", guide=True)
    Cc = point_from_barycentrics(model, A, B, C, u, v, 0.0, ID=f"{prefix}_c", guide=True)
    if draw_polygon:
        add_polygon(model, [Ca, Cb, Cc], ID=f"< {prefix}_a {prefix}_b {prefix}_c >", classes=["secondary"])
    return Ca, Cb, Cc


# ---------------------------------------------------------------------------
# Fundamental Triangle Circles & Concurrency Operators
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
    """Construct the perspector of triangle ABC and triangle A2 B2 C2 by intersecting AA2, BB2, CC2."""
    if draw_cevians:
        add_line(model, A, A2, classes=["bisector"])
        add_line(model, B, B2, classes=["bisector"])
        add_line(model, C, C2, classes=["bisector"])
    return intersect_lines(
        model, A, A2, B, B2, ID=ID, classes=classes or ["selected", "target"]
    )


def incenter_of(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X(1)",
    classes: list[str] | None = None,
    draw_bisectors: bool = False,
    draw_incircle: bool = False,
) -> spg.Point:
    """Construct the incenter X(1) of triangle ABC (concurrency of internal angle bisectors, Euclid IV.4)."""
    a, b, c = triangle_side_lengths(A, B, C)
    X1 = point_from_barycentrics(
        model, A, B, C, a, b, c, ID=ID, classes=classes or ["center"]
    )
    if draw_incircle:
        Tc = perpendicular_foot(model, X1, A, B, ID="T_c", guide=True)
        add_circle(model, X1, Tc, ID="incircle", classes=["incircle"])
    if draw_bisectors:
        add_line(model, A, X1, ID=f"[ {model[A].ID} {ID} ]", classes=["bisector"])
        add_line(model, B, X1, ID=f"[ {model[B].ID} {ID} ]", classes=["bisector"])
        add_line(model, C, X1, ID=f"[ {model[C].ID} {ID} ]", classes=["bisector"])
    return X1


def centroid_of(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X(2)",
    classes: list[str] | None = None,
    draw_medians: bool = False,
) -> spg.Point:
    """Construct the centroid X(2) of triangle ABC (perspector of the medial triangle)."""
    if draw_medians:
        Ma, Mb, Mc = medial_triangle(model, A, B, C, draw_polygon=True)
        add_line(model, A, Ma, ID="[ A M_a ]", classes=["bisector"])
        add_line(model, B, Mb, ID="[ B M_b ]", classes=["bisector"])
        add_line(model, C, Mc, ID="[ C M_c ]", classes=["bisector"])
    return point_from_barycentrics(
        model, A, B, C, 1.0, 1.0, 1.0, ID=ID, classes=classes or ["center"]
    )


def circumcenter_of(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X(3)",
    classes: list[str] | None = None,
    draw_bisectors: bool = False,
    draw_circumcircle: bool = False,
) -> spg.Point:
    """Construct the circumcenter X(3) of triangle ABC (concurrency of perpendicular bisectors, Euclid IV.5)."""
    a, b, c = triangle_side_lengths(A, B, C)
    sa = b**2 + c**2 - a**2
    sb = c**2 + a**2 - b**2
    sc = a**2 + b**2 - c**2
    X3 = point_from_barycentrics(
        model, A, B, C, a**2 * sa, b**2 * sb, c**2 * sc, ID=ID, classes=classes or ["center"]
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


def orthocenter_of(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X(4)",
    classes: list[str] | None = None,
    draw_altitudes: bool = False,
) -> spg.Point:
    """Construct the orthocenter X(4) of triangle ABC (concurrency of altitudes / perspector of orthic triangle)."""
    a, b, c = triangle_side_lengths(A, B, C)
    sa = b**2 + c**2 - a**2
    sb = c**2 + a**2 - b**2
    sc = a**2 + b**2 - c**2
    if draw_altitudes:
        Ha, Hb, Hc = orthic_triangle(model, A, B, C, draw_polygon=True)
        add_line(model, A, Ha, ID="[ A H_a ]", classes=["bisector"])
        add_line(model, B, Hb, ID="[ B H_b ]", classes=["bisector"])
        add_line(model, C, Hc, ID="[ C H_c ]", classes=["bisector"])
    return point_from_barycentrics(
        model, A, B, C, sb * sc, sc * sa, sa * sb, ID=ID, classes=classes or ["center"]
    )


def nine_point_center_of(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X(5)",
    classes: list[str] | None = None,
    draw_circle: bool = False,
) -> spg.Point:
    """Construct the nine-point center X(5) of triangle ABC (midpoint of X(3) and X(4))."""
    X3 = circumcenter_of(model, A, B, C, ID="X(3)")
    X4 = orthocenter_of(model, A, B, C, ID="X(4)")
    X5 = midpoint(model, X3, X4, ID=ID, classes=classes or ["center"], guide=False)
    if draw_circle:
        Mc = midpoint(model, A, B, ID="M_c", guide=True)
        add_circle(model, X5, Mc, ID="nine_point_circle", classes=["nine_point_circle"])
    return X5


def symmedian_point_of(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X(6)",
    classes: list[str] | None = None,
    draw_symmedians: bool = False,
) -> spg.Point:
    """Construct the symmedian (Lemoine) point X(6) of triangle ABC (isogonal conjugate of X(2))."""
    a, b, c = triangle_side_lengths(A, B, C)
    if draw_symmedians:
        Ta, Tb, Tc = tangential_triangle(model, A, B, C, draw_polygon=True, draw_circumcircle=True)
        add_line(model, A, Ta, ID="[ A Tan_a ]", classes=["bisector"])
        add_line(model, B, Tb, ID="[ B Tan_b ]", classes=["bisector"])
        add_line(model, C, Tc, ID="[ C Tan_c ]", classes=["bisector"])
    return point_from_barycentrics(
        model, A, B, C, a**2, b**2, c**2, ID=ID, classes=classes or ["center"]
    )


def gergonne_point_of(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X(7)",
    classes: list[str] | None = None,
    draw_cevians: bool = False,
) -> spg.Point:
    """Construct the Gergonne point X(7) of triangle ABC (perspector of the intouch triangle)."""
    Ta, Tb, Tc = intouch_triangle(model, A, B, C, draw_polygon=True, draw_incircle=True)
    if draw_cevians:
        add_line(model, A, Ta, ID="[ A T_a ]", classes=["bisector"])
        add_line(model, B, Tb, ID="[ B T_b ]", classes=["bisector"])
        add_line(model, C, Tc, ID="[ C T_c ]", classes=["bisector"])
    a, b, c = triangle_side_lengths(A, B, C)
    s = 0.5 * (a + b + c)
    return point_from_barycentrics(
        model,
        A,
        B,
        C,
        1.0 / (s - a),
        1.0 / (s - b),
        1.0 / (s - c),
        ID=ID,
        classes=classes or ["center"],
    )


def nagel_point_of(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X(8)",
    classes: list[str] | None = None,
    draw_cevians: bool = False,
) -> spg.Point:
    """Construct the Nagel point X(8) of triangle ABC (perspector of the extouch triangle)."""
    Na, Nb, Nc = extouch_triangle(model, A, B, C, draw_polygon=True)
    if draw_cevians:
        add_line(model, A, Na, ID="[ A N_a ]", classes=["bisector"])
        add_line(model, B, Nb, ID="[ B N_b ]", classes=["bisector"])
        add_line(model, C, Nc, ID="[ C N_c ]", classes=["bisector"])
    a, b, c = triangle_side_lengths(A, B, C)
    s = 0.5 * (a + b + c)
    return point_from_barycentrics(
        model, A, B, C, s - a, s - b, s - c, ID=ID, classes=classes or ["center"]
    )


def mittenpunkt_of(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X(9)",
    classes: list[str] | None = None,
) -> spg.Point:
    """Construct the Mittenpunkt X(9) of triangle ABC (symmedian point of the excentral triangle)."""
    a, b, c = triangle_side_lengths(A, B, C)
    s = 0.5 * (a + b + c)
    return point_from_barycentrics(
        model,
        A,
        B,
        C,
        a * (s - a),
        b * (s - b),
        c * (s - c),
        ID=ID,
        classes=classes or ["center"],
    )


def spieker_center_of(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X(10)",
    classes: list[str] | None = None,
    draw_circle: bool = False,
) -> spg.Point:
    """Construct the Spieker center X(10) of triangle ABC (incenter of the medial triangle)."""
    Ma, Mb, Mc = medial_triangle(model, A, B, C, draw_polygon=True)
    a, b, c = triangle_side_lengths(A, B, C)
    X10 = point_from_barycentrics(
        model, A, B, C, b + c, c + a, a + b, ID=ID, classes=classes or ["center"]
    )
    if draw_circle:
        Sc = perpendicular_foot(model, X10, Ma, Mb, ID="S_c", guide=True)
        add_circle(model, X10, Sc, ID="spieker_circle", classes=["incircle"])
    return X10


def feuerbach_point_of(
    model: Model,
    A: spg.Point,
    B: spg.Point,
    C: spg.Point,
    ID: str = "X(11)",
    classes: list[str] | None = None,
    draw_circles: bool = False,
) -> spg.Point:
    """Construct the Feuerbach point X(11) of triangle ABC (tangency point of incircle and nine-point circle)."""
    if draw_circles:
        incircle(model, A, B, C)
        nine_point_circle(model, A, B, C)
    a, b, c = triangle_side_lengths(A, B, C)
    s = 0.5 * (a + b + c)
    return point_from_barycentrics(
        model,
        A,
        B,
        C,
        (s - a) * (b - c) ** 2,
        (s - b) * (c - a) ** 2,
        (s - c) * (a - b) ** 2,
        ID=ID,
        classes=classes or ["center"],
    )


def circumcircle(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Circle:
    """Construct the circumcircle of triangle ABC centered at X(3)."""
    X3 = circumcenter_of(model, A, B, C, ID="X(3)")
    return add_circle(model, X3, A, ID="circumcircle", classes=["circumcircle"])


def incircle(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Circle:
    """Construct the incircle of triangle ABC centered at X(1)."""
    X1 = incenter_of(model, A, B, C, ID="X(1)")
    Tc = perpendicular_foot(model, X1, A, B, ID="T_c", guide=True)
    return add_circle(model, X1, Tc, ID="incircle", classes=["incircle"])


def nine_point_circle(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Circle:
    """Construct the nine-point circle of triangle ABC centered at X(5)."""
    X5 = nine_point_center_of(model, A, B, C, ID="X(5)")
    Mc = midpoint(model, A, B, ID="M_c", guide=True)
    return add_circle(model, X5, Mc, ID="nine_point_circle", classes=["nine_point_circle"])


def spieker_circle(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Circle:
    """Construct the Spieker circle (incircle of the medial triangle) centered at X(10)."""
    Ma, Mb, _ = medial_triangle(model, A, B, C, draw_polygon=True)
    X10 = spieker_center_of(model, A, B, C, ID="X(10)")
    Sc = perpendicular_foot(model, X10, Ma, Mb, ID="S_c", guide=True)
    return add_circle(model, X10, Sc, ID="spieker_circle", classes=["incircle"])


# ---------------------------------------------------------------------------
# Point Conjugates & Algebraic Triangle Operators on (A, B, C, P, ...)
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
    """Construct the isogonal conjugate of point P with respect to triangle ABC."""
    a, b, c = triangle_side_lengths(A, B, C)
    u, v, w = barycentrics_of(A, B, C, P)
    if not ID:
        ID = f"isogonal({model[P].ID})"
    return point_from_barycentrics(
        model, A, B, C, a**2 / u, b**2 / v, c**2 / w, ID=ID, classes=classes
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
    """Construct the isotomic conjugate of point P with respect to triangle ABC."""
    u, v, w = barycentrics_of(A, B, C, P)
    if not ID:
        ID = f"isotomic({model[P].ID})"
    return point_from_barycentrics(
        model, A, B, C, 1.0 / u, 1.0 / v, 1.0 / w, ID=ID, classes=classes
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
    """Construct the complement of point P with respect to triangle ABC (homothety at X(2) by -1/2)."""
    u, v, w = barycentrics_of(A, B, C, P)
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
    """Construct the anticomplement of point P with respect to triangle ABC (homothety at X(2) by -2)."""
    u, v, w = barycentrics_of(A, B, C, P)
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
    """Construct the P-Ceva conjugate of Q with respect to triangle ABC."""
    p, q, r_v = barycentrics_of(A, B, C, P)
    u, v, w = barycentrics_of(A, B, C, Q)
    if not ID:
        ID = f"ceva({model[P].ID},{model[Q].ID})"
    return point_from_barycentrics(
        model,
        A,
        B,
        C,
        u * (-u / p + v / q + w / r_v),
        v * (u / p - v / q + w / r_v),
        w * (u / p + v / q - w / r_v),
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
    """Construct the crosspoint of P and Q with respect to triangle ABC."""
    p, q, r_v = barycentrics_of(A, B, C, P)
    u, v, w = barycentrics_of(A, B, C, Q)
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
    """Construct the cevapoint of P and Q with respect to triangle ABC."""
    p, q, r_v = barycentrics_of(A, B, C, P)
    u, v, w = barycentrics_of(A, B, C, Q)
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
) -> spg.Line:
    """Add the central line {i, j} passing through X(i) and X(j), styled as Euler line if applicable."""
    cls = ["golden", "euler"] if {i_num, j_num} <= {2, 3, 4, 5, 20, 30} else ["central_line"]
    return add_line(model, P, Q, ID=f"{{ {i_num}, {j_num} }}", classes=cls)
