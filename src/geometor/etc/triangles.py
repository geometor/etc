"""Exact symbolic reference triangles for the Encyclopedia of Triangle Centers.

Defines the four canonical exact symbolic reference triangles over closed-form
algebraic number fields in SymPy:

1. ``heronian`` — Acute Heronian :math:`(15, 13, 14)` over :math:`\\mathbb{Q}`
2. ``right`` — Pythagorean Right :math:`(3, 4, 5)` over :math:`\\mathbb{Q}`
3. ``kepler`` — Kepler Golden Right :math:`(1, \\sqrt{\\phi}, \\phi)` over :math:`\\mathbb{Q}(\\sqrt{\\phi})`
4. ``kimberling`` — Kimberling Search :math:`(6, 9, 13)` over :math:`\\mathbb{Q}(\\sqrt{35})`
"""

from __future__ import annotations

from collections.abc import Callable, Iterable
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
SQRT_3: sp.Expr = sp.sqrt(3)
SQRT_35: sp.Expr = sp.sqrt(35)
SQRT_105: sp.Expr = sp.sqrt(105)
_U3 = sp.Dummy("u3")


def _extract_u3(expr: sp.Expr) -> tuple[sp.Expr, bool]:
    """Replace factor-of-3 square-root atoms with polynomial dummy ``_U3``."""
    repl: dict[sp.Basic, sp.Expr] = {}
    for p in expr.atoms(sp.Pow):
        if not (isinstance(p.exp, sp.Rational) and p.exp.q == 2):
            continue
        k = int(p.exp.p)
        base = p.base
        if base.is_Integer:
            b_int = int(base)
            if b_int > 0 and b_int % 3 == 0 and (b_int // 3) % 3 != 0:
                q_pow = sp.Pow(sp.Integer(b_int // 3), sp.Rational(k, 2))
                repl[p] = (_U3**k) * q_pow
        elif not base.is_Rational and not base.free_symbols:
            content, _ = base.as_content_primitive()
            if isinstance(content, sp.Rational) and content.p % 3 == 0 and (content.p // 3) % 3 != 0:
                q_base = sp.expand_mul(base / sp.Integer(3))
                q_pow = sp.Pow(q_base, sp.Rational(k, 2))
                repl[p] = (_U3**k) * q_pow
    if not repl:
        return expr, False
    return expr.xreplace(repl), True


def _poly_mod_u3(poly_expr: sp.Expr) -> tuple[sp.Expr, sp.Expr]:
    """Reduce ``poly_expr`` in ``_U3`` modulo ``_U3**2 - 3`` to ``(c0, c1)``."""
    if _U3 not in poly_expr.free_symbols:
        return poly_expr, sp.Integer(0)
    poly = sp.Poly(sp.expand_mul(poly_expr), _U3)
    c0: sp.Expr = sp.Integer(0)
    c1: sp.Expr = sp.Integer(0)
    for (deg,), coeff in poly.terms():
        scale = sp.Integer(3) ** (deg // 2)
        if deg % 2 == 0:
            c0 += scale * coeff
        else:
            c1 += scale * coeff
    return c0, c1


def _reduce_sqrt3_extension(
    expr: sp.Expr,
    base_simplify: Callable[[sp.Expr], sp.Expr],
    *,
    expand_radicals: bool = True,
) -> sp.Expr | None:
    """Rationalize ``expr`` in ``K(sqrt(3))`` given canonical reducer ``base_simplify`` on ``K``."""
    u_expr, found = _extract_u3(expr)
    if not found:
        return None
    try:
        num, den = sp.fraction(sp.together(u_expr))
        p0_raw, p1_raw = _poly_mod_u3(num)
        q0_raw, q1_raw = _poly_mod_u3(den)
        p0 = base_simplify(p0_raw)
        p1 = base_simplify(p1_raw)
        q0 = base_simplify(q0_raw)
        q1 = base_simplify(q1_raw)
        if zero_test(q1):
            if zero_test(q0):
                return None
            a0 = base_simplify(p0 / q0)
            a1 = base_simplify(p1 / q0)
        else:
            norm_d = base_simplify(q0**2 - sp.Integer(3) * q1**2)
            if zero_test(norm_d):
                return None
            a0 = base_simplify((p0 * q0 - sp.Integer(3) * p1 * q1) / norm_d)
            a1 = base_simplify((p1 * q0 - p0 * q1) / norm_d)
        if zero_test(a1):
            return a0
        if expand_radicals:
            return a0 + sp.expand_mul(a1 * SQRT_3)
        return a0 + a1 * SQRT_3
    except ( sp.PolynomialError, ZeroDivisionError, ValueError ):
        return None


def _simplify_rational(expr: sp.Expr) -> sp.Expr:
    """Canonicalize an expression in Q."""
    s = sp.cancel(expr)
    return s if s.is_Rational else clean_expr(s)


def _simplify_rational_or_general(expr: sp.Expr) -> sp.Expr:
    """Simplify a rational or Q(sqrt(3)) / general algebraic SymPy expression without floats."""
    s = sp.sympify(expr)
    if s.is_Rational:
        return s
    if not s.atoms(sp.Pow):
        c = sp.cancel(s)
        if c.is_Rational:
            return c
    rad_atoms = {
        p
        for p in s.atoms(sp.Pow)
        if isinstance(p.exp, sp.Rational) and p.exp.q == 2
    }
    if rad_atoms and rad_atoms <= {SQRT_3, sp.Integer(1) / SQRT_3}:
        res = _reduce_sqrt3_extension(s, _simplify_rational, expand_radicals=True)
        if res is not None:
            return res
    cleaned = clean_expr(s)
    if cleaned.is_Rational:
        return cleaned
    return sp.radsimp(cleaned, symbolic=False) if len(cleaned.atoms(sp.Pow)) <= 3 else cleaned


def _base_kimberling(expr: sp.Expr) -> sp.Expr:
    s = sp.sympify(expr)
    if s.is_Rational:
        return s
    return reduce_in_field(s, SQRT_35)


def _simplify_kimberling(expr: sp.Expr) -> sp.Expr:
    """Reduce an expression over Q(sqrt(35)) or biquadratic Q(sqrt(3), sqrt(35))."""
    s = sp.sympify(expr)
    if s.is_Rational:
        return s
    rad_atoms = {
        p
        for p in s.atoms(sp.Pow)
        if isinstance(p.exp, sp.Rational) and p.exp.q == 2
    }
    if rad_atoms <= {SQRT_35, sp.Integer(1) / SQRT_35}:
        return reduce_in_field(s, SQRT_35)
    if rad_atoms <= {
        SQRT_3,
        sp.Integer(1) / SQRT_3,
        SQRT_35,
        sp.Integer(1) / SQRT_35,
        SQRT_105,
        sp.Integer(1) / SQRT_105,
    }:
        res = _reduce_sqrt3_extension(s, _base_kimberling, expand_radicals=True)
        if res is not None:
            return res
    cleaned = clean_expr(s)
    return sp.radsimp(cleaned, symbolic=False) if len(cleaned.atoms(sp.Pow)) <= 4 else cleaned


def _simplify_kepler(expr: sp.Expr) -> sp.Expr:
    """Reduce an expression in Q(sqrt(phi)) or octic Q(sqrt(phi), sqrt(3))."""
    s = sp.sympify(expr)
    if s.is_Rational:
        return s
    res = _reduce_sqrt3_extension(s, canonicalize_kepler, expand_radicals=False)
    if res is not None:
        return res
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

    def has_sqrt3_extension(self, exprs: Iterable[sp.Expr]) -> bool:
        """Return whether ``exprs`` adjoin :math:`\\sqrt{3}` over this triangle's base field."""
        for e in exprs:
            _, found = _extract_u3(sp.sympify(e))
            if found:
                return True
        return False

    def coordinate_field_latex(self, exprs: Iterable[sp.Expr] = ()) -> str:
        """Return exact LaTeX notation for the minimal number field of ``exprs`` on this triangle."""
        ext3 = self.has_sqrt3_extension(exprs)
        base_key = self.key.replace("_unit", "")
        if base_key in {"heronian", "right"}:
            return r"\mathbb{Q}(\sqrt{3})" if ext3 else r"\mathbb{Q}"
        if base_key == "kepler":
            return r"\mathbb{Q}(\sqrt{\phi}, \sqrt{3})" if ext3 else r"\mathbb{Q}(\sqrt{\phi})"
        if base_key == "kimberling":
            return r"\mathbb{Q}(\sqrt{3}, \sqrt{35})" if ext3 else r"\mathbb{Q}(\sqrt{35})"
        return self.field_latex

    def coordinate_field_pretty(self, exprs: Iterable[sp.Expr] = ()) -> str:
        """Return compact Unicode notation for the minimal number field of ``exprs`` on this triangle."""
        ext3 = self.has_sqrt3_extension(exprs)
        base_key = self.key.replace("_unit", "")
        if base_key in {"heronian", "right"}:
            return "ℚ(√3)" if ext3 else "ℚ"
        if base_key == "kepler":
            return "ℚ(√φ, √3)" if ext3 else "ℚ(√φ)"
        if base_key == "kimberling":
            return "ℚ(√3, √35)" if ext3 else "ℚ(√35)"
        return "ℚ" if self.area.is_Rational else "ℚ̄"


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
