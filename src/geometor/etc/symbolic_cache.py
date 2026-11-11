"""Exact symbolic triangle-center registry and disk cache (`CenterSymbolicRegistry`).

Evaluates homogeneous barycentrics, homogeneous trilinears, normalized
barycentrics, exact Cartesian coordinates, signed sub-triangle areas, and
Kimberling search values over the four canonical exact symbolic reference
triangles without floating-point approximations.
"""

from __future__ import annotations

import json
import math
import re
from collections.abc import Callable
from dataclasses import dataclass
from functools import reduce
from pathlib import Path
from typing import Any

import sympy as sp
from geometor.model import clean_expr, exact_sign, zero_test

from .triangles import (
    PHI,
    SQRT_PHI,
    SymbolicTriangle,
    get_canonical_triangle,
)

_REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_SYMBOLIC_CACHE_DIR = _REPO_ROOT / ".cache" / "symbolic_centers"
_CACHE_SCHEMA_VERSION = 1

_PHI_DISPLAY = sp.Symbol(r"\phi", positive=True)


def format_symbolic_latex(expr: sp.Expr, *, kepler_phi: bool = False) -> str:
    """Render an exact SymPy expression as clean LaTeX.

    When ``kepler_phi`` is ``True``, rewrites :math:`(1 + \\sqrt{5})/2` and
    :math:`\\sqrt{(1 + \\sqrt{5})/2}` in terms of :math:`\\phi` and
    :math:`\\sqrt{\\phi}` for compact typographic display.
    """
    s = sp.sympify(expr)
    if kepler_phi and not s.is_Rational:
        s = _rewrite_in_phi_basis(s)
    tex = sp.latex(s)
    tex = tex.replace(r"\phi^{\frac{3}{2}}", r"\phi \sqrt{\phi}")
    return tex


def format_symbolic_pretty(expr: sp.Expr, *, kepler_phi: bool = False) -> str:
    """Render an exact SymPy expression as compact single-line Unicode math."""
    s = sp.sympify(expr)
    if kepler_phi and not s.is_Rational:
        phi_sym = sp.Symbol("φ", positive=True)
        s = _rewrite_in_phi_basis(s, phi_symbol=phi_sym)
    txt = str(s)
    txt = txt.replace("φ**(3/2)", "φ·√φ")
    txt = txt.replace("**2", "²").replace("**3", "³").replace("**4", "⁴")
    txt = re.sub(r"sqrt\(([^()]+)\)", r"√(\1)", txt)
    txt = re.sub(r"√\((\d+|φ)\)", r"√\1", txt)
    txt = txt.replace("*", "·")
    return txt


def _kepler_basis_coeffs(expr: sp.Expr) -> tuple[sp.Rational, sp.Rational, sp.Rational, sp.Rational] | None:
    """Return exact rational coefficients ``(c0, c1, c2, c3)`` for ``c0 + c1*sqrt(phi) + c2*phi + c3*phi*sqrt(phi)``."""
    from geometor.model.algebra import _cached_from_sympy, get_kepler_field

    field = get_kepler_field()
    anp = _cached_from_sympy(expr, field)
    if anp is None:
        return None
    coeffs_desc = [sp.Rational(field.dom.to_sympy(c)) for c in anp.rep]
    while len(coeffs_desc) < 4:
        coeffs_desc.insert(0, sp.Rational(0))
    c3, c2, c1, c0 = coeffs_desc[-4:]
    return (c0, c1, c2, c3)


def _rewrite_in_phi_basis(
    expr: sp.Expr, phi_symbol: sp.Symbol = _PHI_DISPLAY
) -> sp.Expr:
    """Express an element of :math:`\\mathbb{Q}(\\sqrt{\\phi})` in the basis :math:`\\{1, \\sqrt{\\phi}, \\phi, \\phi\\sqrt{\\phi}\\}`."""
    coeffs = _kepler_basis_coeffs(expr)
    if coeffs is None:
        return expr.subs({SQRT_PHI: sp.sqrt(phi_symbol), PHI: phi_symbol})
    c0, c1, c2, c3 = coeffs
    sqrt_phi_sym = sp.sqrt(phi_symbol)
    rebuilt = (
        c0
        + c1 * sqrt_phi_sym
        + c2 * phi_symbol
        + c3 * phi_symbol * sqrt_phi_sym
    )
    num, den = sp.fraction(sp.together(rebuilt))
    if den == 1:
        return num
    return num / den


def reduce_homogeneous_triple(
    u: sp.Expr,
    v: sp.Expr,
    w: sp.Expr,
    tri: SymbolicTriangle,
) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    """Reduce a homogeneous triple :math:`(u : v : w)` by clearing rational factors."""
    vals = [tri.simplify(u), tri.simplify(v), tri.simplify(w)]
    if all(zero_test(x) for x in vals):
        return (sp.Integer(0), sp.Integer(0), sp.Integer(0))

    if all(x.is_Rational for x in vals):
        rats = [sp.Rational(x) for x in vals]
        lcm_den = reduce(math.lcm, [int(r.q) for r in rats], 1)
        ints = [int(r * lcm_den) for r in rats]
        non_zero = [abs(n) for n in ints if n != 0]
        g = reduce(math.gcd, non_zero) if non_zero else 1
        ints = [n // g for n in ints]
        if all(n <= 0 for n in ints) or sum(ints) < 0:
            ints = [-n for n in ints]
        return (sp.Integer(ints[0]), sp.Integer(ints[1]), sp.Integer(ints[2]))

    # Check if pairwise ratios are exact rationals
    anchor_idx = next((i for i, x in enumerate(vals) if not zero_test(x)), None)
    if anchor_idx is not None:
        anchor = vals[anchor_idx]
        ratios = [tri.simplify(x / anchor) for x in vals]
        if all(r.is_Rational for r in ratios):
            return reduce_homogeneous_triple(ratios[0], ratios[1], ratios[2], tri)

    # For Kepler Q(sqrt(phi)), clear denominators & common GCD in the {1, sqrt(phi), phi, phi*sqrt(phi)} basis
    if tri.key.startswith("kepler"):
        basis_rows = [_kepler_basis_coeffs(x) for x in vals]
        if all(row is not None for row in basis_rows):
            all_rats = [c for row in basis_rows if row is not None for c in row]
            lcm_den = reduce(math.lcm, [int(c.q) for c in all_rats], 1)
            ints_all = [abs(int(c * lcm_den)) for c in all_rats if c != 0]
            g = reduce(math.gcd, ints_all) if ints_all else 1
            factor = sp.Rational(lcm_den, g)
            scaled_k = [tri.simplify(x * factor) for x in vals]
            total_k = tri.simplify(scaled_k[0] + scaled_k[1] + scaled_k[2])
            if not zero_test(total_k) and exact_sign(total_k) < 0:
                scaled_k = [tri.simplify(-x) for x in scaled_k]
            return (scaled_k[0], scaled_k[1], scaled_k[2])

    # Clear integer denominators if present
    nums_dens = [sp.fraction(sp.together(x)) for x in vals]
    if all(d.is_Integer for _, d in nums_dens):
        lcm_d = reduce(math.lcm, [abs(int(d)) for _, d in nums_dens], 1)
        scaled = [tri.simplify(x * lcm_d) for x in vals]
    else:
        scaled = vals

    total = tri.simplify(scaled[0] + scaled[1] + scaled[2])
    if not zero_test(total) and exact_sign(total) < 0:
        scaled = [tri.simplify(-x) for x in scaled]
    return (scaled[0], scaled[1], scaled[2])


# ---------------------------------------------------------------------------
# Exact Closed-Form Homogeneous Barycentric Generators f(a, b, c, S_A, S_B, S_C, S)
# ---------------------------------------------------------------------------

SymbolicCyclicFn = Callable[
    [sp.Expr, sp.Expr, sp.Expr, sp.Expr, sp.Expr, sp.Expr, sp.Expr], sp.Expr
]

_SQRT3 = sp.sqrt(3)

EXACT_CYCLIC_BARYCENTRICS: dict[int, SymbolicCyclicFn] = {
    # Collection 1: Classical & Ancient Centers (X_1 - X_19)
    1: lambda a, b, c, SA, SB, SC, S: a,
    2: lambda a, b, c, SA, SB, SC, S: sp.Integer(1),
    3: lambda a, b, c, SA, SB, SC, S: a**2 * SA,
    4: lambda a, b, c, SA, SB, SC, S: SB * SC,
    5: lambda a, b, c, SA, SB, SC, S: S**2 + SB * SC,
    6: lambda a, b, c, SA, SB, SC, S: a**2,
    7: lambda a, b, c, SA, SB, SC, S: (a + b - c) * (c + a - b),
    8: lambda a, b, c, SA, SB, SC, S: b + c - a,
    9: lambda a, b, c, SA, SB, SC, S: a * (b + c - a),
    10: lambda a, b, c, SA, SB, SC, S: b + c,
    11: lambda a, b, c, SA, SB, SC, S: (b + c - a) * (b - c) ** 2,
    12: lambda a, b, c, SA, SB, SC, S: (b + c) ** 2 * (a + b - c) * (c + a - b),
    13: lambda a, b, c, SA, SB, SC, S: (S + _SQRT3 * SB) * (S + _SQRT3 * SC),
    14: lambda a, b, c, SA, SB, SC, S: (S - _SQRT3 * SB) * (S - _SQRT3 * SC),
    15: lambda a, b, c, SA, SB, SC, S: a**2 * (S + _SQRT3 * SA),
    16: lambda a, b, c, SA, SB, SC, S: a**2 * (S - _SQRT3 * SA),
    17: lambda a, b, c, SA, SB, SC, S: (SB + _SQRT3 * S) * (SC + _SQRT3 * S),
    18: lambda a, b, c, SA, SB, SC, S: (SB - _SQRT3 * S) * (SC - _SQRT3 * S),
    19: lambda a, b, c, SA, SB, SC, S: a * SB * SC,
    # Key Companion Centers for Central Lines, Conjugates, and Inversions
    20: lambda a, b, c, SA, SB, SC, S: S**2 - sp.Integer(2) * SB * SC,
    21: lambda a, b, c, SA, SB, SC, S: a * (b + c - a) * (SB + SC),
    25: lambda a, b, c, SA, SB, SC, S: a**2 * SB * SC,
    31: lambda a, b, c, SA, SB, SC, S: a**3,
    32: lambda a, b, c, SA, SB, SC, S: a**4,
    35: lambda a, b, c, SA, SB, SC, S: a**2 * (sp.Integer(2) * SA + b * c),
    36: lambda a, b, c, SA, SB, SC, S: a**2 * (sp.Integer(2) * SA - b * c),
    37: lambda a, b, c, SA, SB, SC, S: a * (b + c),
    38: lambda a, b, c, SA, SB, SC, S: a * (b**2 + c**2),
    39: lambda a, b, c, SA, SB, SC, S: a**2 * (b**2 + c**2),
    40: lambda a, b, c, SA, SB, SC, S: a * (
        a**3 + a**2 * (b + c) - a * (b + c) ** 2 - (b + c) * (b - c) ** 2
    ),
    42: lambda a, b, c, SA, SB, SC, S: a**2 * (b + c),
    44: lambda a, b, c, SA, SB, SC, S: a * (b + c - sp.Integer(2) * a),
    54: lambda a, b, c, SA, SB, SC, S: a**2 * (S**2 - SB * SC),
    55: lambda a, b, c, SA, SB, SC, S: a**2 * (b + c - a),
    56: lambda a, b, c, SA, SB, SC, S: a**2 * (a + b - c) * (c + a - b),
    57: lambda a, b, c, SA, SB, SC, S: a * (a + b - c) * (c + a - b),
    63: lambda a, b, c, SA, SB, SC, S: a * SA,
    69: lambda a, b, c, SA, SB, SC, S: SA,
    75: lambda a, b, c, SA, SB, SC, S: b * c,
    76: lambda a, b, c, SA, SB, SC, S: b**2 * c**2,
    85: lambda a, b, c, SA, SB, SC, S: b**2 * c**2 * (b + c - a),
    86: lambda a, b, c, SA, SB, SC, S: b * c * (a + b) * (c + a),
    95: lambda a, b, c, SA, SB, SC, S: b**2 * c**2 * SB * SC,
}


@dataclass(frozen=True)
class SymbolicCenterRecord:
    """Exact symbolic coordinates and invariants for center ``X_num`` on a triangle."""

    num: int
    triangle_key: str
    bary: tuple[sp.Expr, sp.Expr, sp.Expr]
    norm_bary: tuple[sp.Expr, sp.Expr, sp.Expr]
    trilinear: tuple[sp.Expr, sp.Expr, sp.Expr]
    xy: tuple[sp.Expr, sp.Expr]
    sub_areas: tuple[sp.Expr, sp.Expr, sp.Expr]
    search_value: sp.Expr

    @property
    def is_kepler(self) -> bool:
        """Return whether this record belongs to the Kepler golden triangle."""
        return self.triangle_key.startswith("kepler")

    def xy_latex(self) -> str:
        """Return ``(x, y)`` formatted as LaTeX."""
        kx = format_symbolic_latex(self.xy[0], kepler_phi=self.is_kepler)
        ky = format_symbolic_latex(self.xy[1], kepler_phi=self.is_kepler)
        return rf"\left({kx},\; {ky}\right)"

    def xy_pretty(self) -> str:
        """Return ``(x, y)`` formatted as compact Unicode."""
        px = format_symbolic_pretty(self.xy[0], kepler_phi=self.is_kepler)
        py = format_symbolic_pretty(self.xy[1], kepler_phi=self.is_kepler)
        return f"({px}, {py})"

    def trilinear_latex(self) -> str:
        """Return homogeneous trilinears formatted as LaTeX."""
        parts = [
            format_symbolic_latex(t, kepler_phi=self.is_kepler)
            for t in self.trilinear
        ]
        return " : ".join(parts)

    def trilinear_pretty(self) -> str:
        """Return homogeneous trilinears formatted as Unicode."""
        parts = [
            format_symbolic_pretty(t, kepler_phi=self.is_kepler)
            for t in self.trilinear
        ]
        return " : ".join(parts)

    def bary_latex(self) -> str:
        """Return homogeneous barycentrics formatted as LaTeX."""
        parts = [
            format_symbolic_latex(b, kepler_phi=self.is_kepler)
            for b in self.bary
        ]
        return " : ".join(parts)

    def bary_pretty(self) -> str:
        """Return homogeneous barycentrics formatted as Unicode."""
        parts = [
            format_symbolic_pretty(b, kepler_phi=self.is_kepler)
            for b in self.bary
        ]
        return " : ".join(parts)

    def search_latex(self) -> str:
        """Return the exact Kimberling search value as LaTeX."""
        return format_symbolic_latex(self.search_value, kepler_phi=self.is_kepler)

    def approx_xy(self) -> tuple[float, float]:
        """Return secondary float approximation of ``(x, y)`` for SVG layout."""
        return (float(self.xy[0].evalf()), float(self.xy[1].evalf()))

    def approx_search_value(self) -> float:
        """Return float approximation of ``search_value``."""
        return float(self.search_value.evalf())

    def to_cache_dict(self) -> dict[str, Any]:
        """Serialize exact SymPy expressions via ``sp.srepr``."""
        return {
            "num": self.num,
            "triangle_key": self.triangle_key,
            "bary": [sp.srepr(x) for x in self.bary],
            "norm_bary": [sp.srepr(x) for x in self.norm_bary],
            "trilinear": [sp.srepr(x) for x in self.trilinear],
            "xy": [sp.srepr(x) for x in self.xy],
            "sub_areas": [sp.srepr(x) for x in self.sub_areas],
            "search_value": sp.srepr(self.search_value),
        }

    @classmethod
    def from_cache_dict(cls, data: dict[str, Any]) -> SymbolicCenterRecord:
        """Deserialize exact SymPy expressions from ``sp.srepr`` strings."""
        bary = tuple(sp.sympify(s) for s in data["bary"])
        norm_bary = tuple(sp.sympify(s) for s in data["norm_bary"])
        trilinear = tuple(sp.sympify(s) for s in data["trilinear"])
        xy = tuple(sp.sympify(s) for s in data["xy"])
        sub_areas = tuple(sp.sympify(s) for s in data["sub_areas"])
        return cls(
            num=int(data["num"]),
            triangle_key=str(data["triangle_key"]),
            bary=(bary[0], bary[1], bary[2]),
            norm_bary=(norm_bary[0], norm_bary[1], norm_bary[2]),
            trilinear=(trilinear[0], trilinear[1], trilinear[2]),
            xy=(xy[0], xy[1]),
            sub_areas=(sub_areas[0], sub_areas[1], sub_areas[2]),
            search_value=sp.sympify(data["search_value"]),
        )


class CenterSymbolicRegistry:
    """Exact symbolic evaluator and persistent cache for ETC triangle centers.

    Parameters
    ----------
    triangle :
        A :class:`SymbolicTriangle` instance or canonical preset name
        (``"heronian"``, ``"right"``, ``"kepler"``, ``"kimberling"``).
    cache_dir :
        Directory where per-triangle JSON cache files are stored. Pass ``None``
        to disable disk persistence (in-memory only).
    """

    def __init__(
        self,
        triangle: SymbolicTriangle | str = "heronian",
        *,
        cache_dir: Path | str | None = DEFAULT_SYMBOLIC_CACHE_DIR,
    ) -> None:
        if isinstance(triangle, str):
            self.triangle = get_canonical_triangle(triangle)
        else:
            self.triangle = triangle

        self.cache_dir = Path(cache_dir) if cache_dir is not None else None
        self._records: dict[int, SymbolicCenterRecord] = {}
        self._dirty = False
        if self.cache_dir is not None:
            self._load_disk_cache()

    @property
    def cache_file(self) -> Path | None:
        """Path to this triangle's JSON cache file."""
        if self.cache_dir is None:
            return None
        safe_key = re.sub(r"[^A-Za-z0-9_-]", "_", self.triangle.key)
        return self.cache_dir / f"{safe_key}.json"

    def _triangle_signature(self) -> dict[str, str]:
        t = self.triangle
        return {
            "a": sp.srepr(t.a),
            "b": sp.srepr(t.b),
            "c": sp.srepr(t.c),
            "A": sp.srepr(t.A_xy),
            "B": sp.srepr(t.B_xy),
            "C": sp.srepr(t.C_xy),
        }

    def _load_disk_cache(self) -> None:
        cfile = self.cache_file
        if cfile is None or not cfile.is_file():
            return
        try:
            payload = json.loads(cfile.read_text(encoding="utf-8"))
            if payload.get("schema_version") != _CACHE_SCHEMA_VERSION:
                return
            if payload.get("signature") != self._triangle_signature():
                return
            for num_str, rec_data in (payload.get("records") or {}).items():
                self._records[int(num_str)] = SymbolicCenterRecord.from_cache_dict(
                    rec_data
                )
        except (OSError, ValueError, TypeError, KeyError, sp.SympifyError):
            return

    def save_cache(self) -> None:
        """Persist cached symbolic center records to disk if modified."""
        cfile = self.cache_file
        if cfile is None or not self._dirty:
            return
        cfile.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "schema_version": _CACHE_SCHEMA_VERSION,
            "triangle_key": self.triangle.key,
            "signature": self._triangle_signature(),
            "records": {
                str(k): self._records[k].to_cache_dict()
                for k in sorted(self._records)
            },
        }
        cfile.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        self._dirty = False

    def has_exact_formula(self, num: int) -> bool:
        """Return whether center ``X_num`` has a built-in closed-form generator."""
        return num in EXACT_CYCLIC_BARYCENTRICS

    def evaluate_barycentrics(
        self, num: int, raw_bary: tuple[sp.Expr, sp.Expr, sp.Expr] | None = None
    ) -> SymbolicCenterRecord:
        """Evaluate and cache a center from either ``EXACT_CYCLIC_BARYCENTRICS`` or ``raw_bary``."""
        if raw_bary is None and num in self._records:
            return self._records[num]

        tri = self.triangle
        if raw_bary is None:
            if num not in EXACT_CYCLIC_BARYCENTRICS:
                raise KeyError(
                    f"No built-in exact symbolic generator for X_{num}; "
                    f"provide raw_bary or a cyclic SymPy expression."
                )
            fn = EXACT_CYCLIC_BARYCENTRICS[num]
            a, b, c = tri.a, tri.b, tri.c
            SA, SB, SC = tri.S_A, tri.S_B, tri.S_C
            S = tri.two_area
            u_raw = fn(a, b, c, SA, SB, SC, S)
            v_raw = fn(b, c, a, SB, SC, SA, S)
            w_raw = fn(c, a, b, SC, SA, SB, S)
        else:
            u_raw, v_raw, w_raw = raw_bary

        bary = reduce_homogeneous_triple(u_raw, v_raw, w_raw, tri)
        raw_trilin = tri.bary_to_trilinear(*bary)
        trilinear = reduce_homogeneous_triple(*raw_trilin, tri)
        norm_bary = tri.normalize_bary(*bary)
        xy = tri.bary_to_cartesian(*bary)
        sub_areas = tri.cartesian_to_sub_areas(*xy)
        search_val = tri.kimberling_search_value(*bary)

        rec = SymbolicCenterRecord(
            num=num,
            triangle_key=tri.key,
            bary=bary,
            norm_bary=norm_bary,
            trilinear=trilinear,
            xy=xy,
            sub_areas=sub_areas,
            search_value=search_val,
        )
        if raw_bary is None:
            self._records[num] = rec
            self._dirty = True
            self.save_cache()
        return rec

    def get(self, num: int) -> SymbolicCenterRecord:
        """Return the exact :class:`SymbolicCenterRecord` for ``X_num``."""
        return self.evaluate_barycentrics(num)

    def evaluate_cyclic_sympy(
        self,
        num: int,
        first_component: sp.Expr,
        *,
        is_trilinear: bool = False,
        cache: bool = True,
    ) -> SymbolicCenterRecord:
        """Evaluate an arbitrary cyclic SymPy expression in ``(a, b, c, A, B, C, S_A, S_B, S_C, S, r, R, s)``."""
        if cache and num in self._records:
            return self._records[num]

        tri = self.triangle
        a_s, b_s, c_s = sp.symbols("a b c", positive=True)
        A_s, B_s, C_s = sp.symbols("A B C", real=True)
        SA_s, SB_s, SC_s, S_s = sp.symbols("S_A S_B S_C S", real=True)
        r_s, R_s, s_s = sp.symbols("r R s", positive=True)

        expanded = sp.expand_trig(first_component)
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
        }
        alg = clean_expr(expanded.subs(trig_subs))

        def _eval_perm(
            pa: sp.Expr,
            pb: sp.Expr,
            pc: sp.Expr,
            pSA: sp.Expr,
            pSB: sp.Expr,
            pSC: sp.Expr,
        ) -> sp.Expr:
            sub_map = {
                a_s: pa,
                b_s: pb,
                c_s: pc,
                SA_s: pSA,
                SB_s: pSB,
                SC_s: pSC,
                S_s: tri.two_area,
                r_s: tri.r,
                R_s: tri.R,
                s_s: tri.s,
            }
            return tri.simplify(alg.subs(sub_map))

        c1 = _eval_perm(tri.a, tri.b, tri.c, tri.S_A, tri.S_B, tri.S_C)
        c2 = _eval_perm(tri.b, tri.c, tri.a, tri.S_B, tri.S_C, tri.S_A)
        c3 = _eval_perm(tri.c, tri.a, tri.b, tri.S_C, tri.S_A, tri.S_B)
        if is_trilinear:
            c1, c2, c3 = tri.trilinear_to_bary(c1, c2, c3)

        rec = self.evaluate_barycentrics(num, raw_bary=(c1, c2, c3))
        if cache:
            self._records[num] = rec
            self._dirty = True
            self.save_cache()
        return rec

    def warm_collection_1(self) -> dict[int, SymbolicCenterRecord]:
        """Evaluate and cache all Collection 1 centers (`X_1`–`X_19`) plus key companions."""
        target_nums = list(range(1, 21)) + [35, 36, 40, 55, 56, 57, 75]
        out: dict[int, SymbolicCenterRecord] = {}
        for k in target_nums:
            out[k] = self.get(k)
        self.save_cache()
        return out
