"""Exact symbolic reference triangles for the Encyclopedia of Triangle Centers.

Defines the four canonical exact symbolic reference triangles over closed-form
algebraic number fields in SymPy:

1. ``heronian`` — Acute Heronian :math:`(15, 13, 14)` over :math:`\\mathbb{Q}`
2. ``right`` — Pythagorean Right :math:`(3, 4, 5)` over :math:`\\mathbb{Q}`
3. ``kepler`` — Kepler Golden Right :math:`(1, \\sqrt{\\phi}, \\phi)` over :math:`\\mathbb{Q}(\\sqrt{\\phi})`
4. ``kimberling`` — Kimberling Search :math:`(6, 9, 13)` over :math:`\\mathbb{Q}(\\sqrt{35})`
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

import sympy as sp
from geometor.model import (
    canonicalize_kepler,
    clean_expr,
    reduce_in_field,
    zero_test,
)

PHI: sp.Expr = (sp.Integer(1) + sp.sqrt(5)) / sp.Integer(2)
SQRT_PHI: sp.Expr = sp.sqrt(PHI)
SQRT_35: sp.Expr = sp.sqrt(35)


def _simplify_rational_or_general(expr: sp.Expr) -> sp.Expr:
    """Simplify a rational or general algebraic SymPy expression without floats."""
    s = sp.sympify(expr)
    if s.is_Rational:
        return s
    cleaned = clean_expr(s)
    if cleaned.is_Rational:
        return cleaned
    return sp.radsimp(cleaned) if len(cleaned.atoms(sp.Pow)) <= 3 else cleaned


def _simplify_kimberling(expr: sp.Expr) -> sp.Expr:
    """Reduce an expression over Q(sqrt(35)) (or Q(sqrt(35), sqrt(3)))."""
    s = sp.sympify(expr)
    if s.is_Rational:
        return s
    rad_atoms = {
        p
        for p in s.atoms(sp.Pow)
        if isinstance(p.exp, sp.Rational) and p.exp.q == 2
    }
    if rad_atoms <= {SQRT_35}:
        return reduce_in_field(s, SQRT_35)
    return clean_expr(s)


def _simplify_kepler(expr: sp.Expr) -> sp.Expr:
    """Reduce an expression in the Kepler biquadratic tower Q(sqrt(phi))."""
    s = sp.sympify(expr)
    if s.is_Rational:
        return s
    return canonicalize_kepler(s)


@dataclass(frozen=True)
class SymbolicTriangle:
    """Exact symbolic reference triangle with side lengths, vertices, and invariants.

    Parameters
    ----------
    key :
        Preset identifier (``"heronian"``, ``"right"``, ``"kepler"``, ``"kimberling"``,
        or ``"acute"``).
    label :
        Short human-readable title (e.g. ``"Heronian (15, 13, 14)"``).
    field_latex :
        LaTeX string naming the ambient algebraic field (e.g. ``r"\\mathbb{Q}"``).
    a, b, c :
        Exact side lengths :math:`a = |BC|`, :math:`b = |CA|`, :math:`c = |AB|`.
    A_xy, B_xy, C_xy :
        Exact Cartesian coordinates of vertices :math:`A`, :math:`B`, :math:`C`.
    area :
        Exact area :math:`\\Delta = \\operatorname{Area}(\\triangle ABC)`.
    simplify_fn :
        Field-aware exact simplification callable.
    """

    key: str
    label: str
    field_latex: str
    a: sp.Expr
    b: sp.Expr
    c: sp.Expr
    A_xy: tuple[sp.Expr, sp.Expr]
    B_xy: tuple[sp.Expr, sp.Expr]
    C_xy: tuple[sp.Expr, sp.Expr]
    area: sp.Expr
    simplify_fn: Callable[[sp.Expr], sp.Expr] = _simplify_rational_or_general

    def simplify(self, expr: sp.Expr | int) -> sp.Expr:
        """Simplify ``expr`` in this triangle's algebraic field."""
        return self.simplify_fn(sp.sympify(expr))

    @property
    def Q_a(self) -> sp.Expr:
        """Exact quadrance :math:`Q_a = a^2` of side :math:`BC`."""
        return self.simplify(self.a**2)

    @property
    def Q_b(self) -> sp.Expr:
        """Exact quadrance :math:`Q_b = b^2` of side :math:`CA`."""
        return self.simplify(self.b**2)

    @property
    def Q_c(self) -> sp.Expr:
        """Exact quadrance :math:`Q_c = c^2` of side :math:`AB`."""
        return self.simplify(self.c**2)

    @property
    def s(self) -> sp.Expr:
        """Exact semiperimeter :math:`s = (a + b + c)/2`."""
        return self.simplify((self.a + self.b + self.c) / sp.Integer(2))

    @property
    def two_area(self) -> sp.Expr:
        """Conway doubled area :math:`S = 2\\Delta`."""
        return self.simplify(sp.Integer(2) * self.area)

    @property
    def r(self) -> sp.Expr:
        """Exact inradius :math:`r = \\Delta / s`."""
        return self.simplify(self.area / self.s)

    @property
    def Q_r(self) -> sp.Expr:
        """Exact incircle quadrance :math:`Q_r = r^2`."""
        return self.simplify(self.r**2)

    @property
    def R(self) -> sp.Expr:
        """Exact circumradius :math:`R = abc / (4\\Delta)`."""
        return self.simplify((self.a * self.b * self.c) / (sp.Integer(4) * self.area))

    @property
    def Q_R(self) -> sp.Expr:
        """Exact circumcircle quadrance :math:`Q_R = R^2`."""
        return self.simplify(self.R**2)

    @property
    def S_A(self) -> sp.Expr:
        """Conway symbol :math:`S_A = (b^2 + c^2 - a^2)/2`."""
        return self.simplify((self.Q_b + self.Q_c - self.Q_a) / sp.Integer(2))

    @property
    def S_B(self) -> sp.Expr:
        """Conway symbol :math:`S_B = (c^2 + a^2 - b^2)/2`."""
        return self.simplify((self.Q_c + self.Q_a - self.Q_b) / sp.Integer(2))

    @property
    def S_C(self) -> sp.Expr:
        """Conway symbol :math:`S_C = (a^2 + b^2 - c^2)/2`."""
        return self.simplify((self.Q_a + self.Q_b - self.Q_c) / sp.Integer(2))

    def unit_baseline(self) -> SymbolicTriangle:
        """Return a homothetic copy scaled by :math:`1/c` so :math:`A=(0,0), B=(1,0)`."""
        inv_c = self.simplify(sp.Integer(1) / self.c)
        inv_c2 = self.simplify(inv_c**2)
        return SymbolicTriangle(
            key=f"{self.key}_unit",
            label=f"{self.label} | AB = 1",
            field_latex=self.field_latex,
            a=self.simplify(self.a * inv_c),
            b=self.simplify(self.b * inv_c),
            c=sp.Integer(1),
            A_xy=(sp.Integer(0), sp.Integer(0)),
            B_xy=(sp.Integer(1), sp.Integer(0)),
            C_xy=(
                self.simplify(self.C_xy[0] * inv_c),
                self.simplify(self.C_xy[1] * inv_c),
            ),
            area=self.simplify(self.area * inv_c2),
            simplify_fn=self.simplify_fn,
        )

    def trilinear_to_bary(
        self, alpha: sp.Expr, beta: sp.Expr, gamma: sp.Expr
    ) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
        """Convert homogeneous trilinears :math:`(\\alpha : \\beta : \\gamma)` to barycentrics."""
        return (
            self.simplify(self.a * alpha),
            self.simplify(self.b * beta),
            self.simplify(self.c * gamma),
        )

    def bary_to_trilinear(
        self, u: sp.Expr, v: sp.Expr, w: sp.Expr
    ) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
        """Convert homogeneous barycentrics :math:`(u : v : w)` to trilinears."""
        return (
            self.simplify(u / self.a),
            self.simplify(v / self.b),
            self.simplify(w / self.c),
        )

    def normalize_bary(
        self, u: sp.Expr, v: sp.Expr, w: sp.Expr
    ) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
        """Normalize homogeneous barycentrics so :math:`u + v + w = 1`."""
        denom = self.simplify(u + v + w)
        if zero_test(denom):
            raise ZeroDivisionError("Point lies on the line at infinity (u + v + w = 0).")
        return (
            self.simplify(u / denom),
            self.simplify(v / denom),
            self.simplify(w / denom),
        )

    def bary_to_cartesian(
        self, u: sp.Expr, v: sp.Expr, w: sp.Expr
    ) -> tuple[sp.Expr, sp.Expr]:
        """Map homogeneous barycentrics :math:`(u : v : w)` to exact Cartesian :math:`(x, y)`."""
        nu, nv, nw = self.normalize_bary(u, v, w)
        x = self.simplify(
            nu * self.A_xy[0] + nv * self.B_xy[0] + nw * self.C_xy[0]
        )
        y = self.simplify(
            nu * self.A_xy[1] + nv * self.B_xy[1] + nw * self.C_xy[1]
        )
        return (x, y)

    def cartesian_to_sub_areas(
        self, x: sp.Expr, y: sp.Expr
    ) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
        """Return exact signed sub-triangle areas :math:`(\\Delta_a, \\Delta_b, \\Delta_c)`."""
        ax, ay = self.A_xy
        bx, by = self.B_xy
        cx, cy = self.C_xy
        da = self.simplify(
            ((bx - x) * (cy - y) - (cx - x) * (by - y)) / sp.Integer(2)
        )
        db = self.simplify(
            ((cx - x) * (ay - y) - (ax - x) * (cy - y)) / sp.Integer(2)
        )
        dc = self.simplify(
            ((ax - x) * (by - y) - (bx - x) * (ay - y)) / sp.Integer(2)
        )
        return (da, db, dc)

    def kimberling_search_value(
        self, u: sp.Expr, v: sp.Expr, w: sp.Expr
    ) -> sp.Expr:
        """Return exact directed distance :math:`h_a = 2\\Delta u / (a(u + v + w))` to :math:`BC`."""
        denom = self.simplify(self.a * (u + v + w))
        if zero_test(denom):
            return sp.oo
        return self.simplify((sp.Integer(2) * self.area * u) / denom)


def build_symbolic_triangle_from_sides(
    a: sp.Expr | float,
    b: sp.Expr | float,
    c: sp.Expr | float,
    *,
    key: str = "custom",
    label: str | None = None,
    unit_baseline: bool = False,
) -> SymbolicTriangle:
    """Construct an exact :class:`SymbolicTriangle` from three side lengths.

    Any Python ``float`` inputs representing exact rationals (such as ``5.0``) are
    coerced via :func:`sympy.nsimplify` so zero ``sp.Float`` atoms enter symbolic
    computations.
    """

    def _to_exact(val: sp.Expr | float) -> sp.Expr:
        if isinstance(val, float):
            return sp.nsimplify(val, rational=True)
        s = sp.sympify(val)
        if s.atoms(sp.Float):
            return sp.nsimplify(s, rational=True)
        return s

    sa, sb, sc = _to_exact(a), _to_exact(b), _to_exact(c)
    s_semi = (sa + sb + sc) / sp.Integer(2)
    area_sq = clean_expr(s_semi * (s_semi - sa) * (s_semi - sb) * (s_semi - sc))
    area = clean_expr(sp.sqrt(area_sq))
    cx = clean_expr((sb**2 + sc**2 - sa**2) / (sp.Integer(2) * sc))
    cy = clean_expr((sp.Integer(2) * area) / sc)
    tri = SymbolicTriangle(
        key=key,
        label=label or f"({sa}, {sb}, {sc})",
        field_latex=r"\mathbb{Q}" if area.is_Rational else r"\overline{\mathbb{Q}}",
        a=sa,
        b=sb,
        c=sc,
        A_xy=(sp.Integer(0), sp.Integer(0)),
        B_xy=(sc, sp.Integer(0)),
        C_xy=(cx, cy),
        area=area,
        simplify_fn=_simplify_rational_or_general,
    )
    return tri.unit_baseline() if unit_baseline else tri


HERONIAN_TRIANGLE = SymbolicTriangle(
    key="heronian",
    label="Heronian (15, 13, 14)",
    field_latex=r"\mathbb{Q}",
    a=sp.Integer(15),
    b=sp.Integer(13),
    c=sp.Integer(14),
    A_xy=(sp.Integer(0), sp.Integer(0)),
    B_xy=(sp.Integer(14), sp.Integer(0)),
    C_xy=(sp.Integer(5), sp.Integer(12)),
    area=sp.Integer(84),
    simplify_fn=_simplify_rational_or_general,
)

RIGHT_TRIANGLE = SymbolicTriangle(
    key="right",
    label="Right (3, 4, 5)",
    field_latex=r"\mathbb{Q}",
    a=sp.Integer(3),
    b=sp.Integer(4),
    c=sp.Integer(5),
    A_xy=(sp.Integer(0), sp.Integer(0)),
    B_xy=(sp.Integer(5), sp.Integer(0)),
    C_xy=(sp.Rational(16, 5), sp.Rational(12, 5)),
    area=sp.Integer(6),
    simplify_fn=_simplify_rational_or_general,
)

KEPLER_TRIANGLE = SymbolicTriangle(
    key="kepler",
    label="Kepler (1, √φ, φ)",
    field_latex=r"\mathbb{Q}(\sqrt{\phi})",
    a=sp.Integer(1),
    b=SQRT_PHI,
    c=PHI,
    A_xy=(sp.Integer(0), sp.Integer(0)),
    B_xy=(PHI, sp.Integer(0)),
    C_xy=(sp.Integer(1), _simplify_kepler(SQRT_PHI * (PHI - sp.Integer(1)))),
    area=_simplify_kepler(SQRT_PHI / sp.Integer(2)),
    simplify_fn=_simplify_kepler,
)

KIMBERLING_TRIANGLE = SymbolicTriangle(
    key="kimberling",
    label="Kimberling (6, 9, 13)",
    field_latex=r"\mathbb{Q}(\sqrt{35})",
    a=sp.Integer(6),
    b=sp.Integer(9),
    c=sp.Integer(13),
    A_xy=(sp.Integer(0), sp.Integer(0)),
    B_xy=(sp.Integer(13), sp.Integer(0)),
    C_xy=(
        sp.Rational(107, 13),
        sp.Rational(8, 13) * SQRT_35,
    ),
    area=sp.Integer(4) * SQRT_35,
    simplify_fn=_simplify_kimberling,
)

LEGACY_ACUTE_TRIANGLE = build_symbolic_triangle_from_sides(
    5, 6, 7, key="acute", label="Acute (5, 6, 7)", unit_baseline=True
)

CANONICAL_TRIANGLES: dict[str, SymbolicTriangle] = {
    "heronian": HERONIAN_TRIANGLE,
    "right": RIGHT_TRIANGLE,
    "kepler": KEPLER_TRIANGLE,
    "kimberling": KIMBERLING_TRIANGLE,
}


def get_canonical_triangle(
    preset: str = "heronian", *, unit_baseline: bool = False
) -> SymbolicTriangle:
    """Return a canonical :class:`SymbolicTriangle` by preset key.

    Parameters
    ----------
    preset :
        One of ``"heronian"``, ``"right"``, ``"kepler"``, ``"kimberling"``
        (or legacy ``"acute"``).
    unit_baseline :
        When ``True``, scales the triangle by :math:`1/c` so :math:`AB = 1`.
    """
    key = preset.strip().lower()
    if key in CANONICAL_TRIANGLES:
        tri = CANONICAL_TRIANGLES[key]
        return tri.unit_baseline() if unit_baseline else tri
    if key == "acute":
        tri = build_symbolic_triangle_from_sides(
            5, 6, 7, key="acute", label="Acute (5, 6, 7)", unit_baseline=unit_baseline
        )
        return tri
    raise KeyError(
        f"Unknown canonical triangle preset {preset!r}; expected one of "
        f"{sorted(CANONICAL_TRIANGLES)}"
    )
