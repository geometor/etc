"""Fast, 100% exact algebraic-field evaluator for ETC triangle centers.

Evaluates arbitrary ETC homogeneous trilinear/barycentric expressions and
algebraic relation graphs directly inside each canonical reference triangle's
exact number field — zero floating-point drift, zero SymPy expression-tree
blowup, and ~500x faster than symbolic expression simplification:

1. ``heronian`` (15, 13, 14)   : Q          (and Q(sqrt(3)) when trig pi/3 appears)
2. ``right``    (5, 3, 4)      : Q          (and Q(sqrt(3)))
3. ``equilateral`` (2, 2, 2)   : Q(sqrt(3))
4. ``kimberling`` (6, 9, 13)   : Q(sqrt(35)) (and Q(sqrt(35), sqrt(3)))
5. ``kepler``   (phi, 1, s_phi): Q(sqrt(phi)), alpha^4 = alpha^2 + 1
6. ``golden``   (phi, phi, 1)  : Q(tau),       tau^4 = 10*tau^2 - 5
7. ``gnomon``   (1, 1, phi)    : Q(tau),       tau^4 = 10*tau^2 - 5

For the small subset of ETC centers involving genuinely transcendental or
non-field expressions (e.g. ``cos(A/3)``, ``arcsin``, cubic roots), falls back
explicitly to 50-digit ``mpmath`` evaluation tagged ``precision="mpmath-50"``
while never injecting floats into ``geometor.model``.
"""

from __future__ import annotations

import ast
import functools
import math
import re
import time
from dataclasses import dataclass
from fractions import Fraction
from typing import Any

import mpmath as mp
import sympy as sp

from .construct import _prepare_formula_expr
from .symbolic_cache import EXACT_CYCLIC_BARYCENTRICS
from .triangles import PHI, SQRT_3, SQRT_35, SQRT_PHI, TAU

_F0 = Fraction(0)
_F1 = Fraction(1)
_F2 = Fraction(2)
_HALF = Fraction(1, 2)


class OutsideFieldError(ValueError):
    """Raised when an expression leaves the triangle's exact algebraic field."""


# ---------------------------------------------------------------------------
# Exact Integer / Rational Square Root Helpers
# ---------------------------------------------------------------------------


def _isqrt_exact(n: int) -> int | None:
    if n < 0:
        return None
    r = math.isqrt(n)
    return r if r * r == n else None


def _frac_sqrt_exact(q: Fraction) -> Fraction | None:
    if q < 0:
        return None
    if q == 0:
        return _F0
    rn = _isqrt_exact(q.numerator)
    if rn is None:
        return None
    rd = _isqrt_exact(q.denominator)
    if rd is None:
        return None
    return Fraction(rn, rd)


def _frac_to_sympy(q: Fraction) -> sp.Rational:
    return sp.Rational(q.numerator, q.denominator)


def _int_gcd(a: int, b: int) -> int:
    return math.gcd(abs(a), abs(b))


def _frac_latex(q: Fraction) -> str:
    if q.denominator == 1:
        return str(q.numerator)
    if q.numerator < 0:
        return rf"-\frac{{{-q.numerator}}}{{{q.denominator}}}"
    return rf"\frac{{{q.numerator}}}{{{q.denominator}}}"


def _frac_digits(q: Fraction) -> int:
    bits = max(q.numerator.bit_length(), q.denominator.bit_length())
    return (bits * 30103) // 100000 + 1


def _safe_mpf_to_float(m: mp.mpf) -> float:
    if not mp.isfinite(m):
        return math.nan
    if m == 0:
        return 0.0
    try:
        return float(m)
    except OverflowError:
        return math.inf if m > 0 else -math.inf


# ---------------------------------------------------------------------------
# Exact Base Field Elements: Q, Q(sqrt(d)), Q(alpha | alpha^4 = p*alpha^2 + q)
# ---------------------------------------------------------------------------


class QElem:
    """Exact element of Q backed by ``fractions.Fraction``."""

    __slots__ = ("val",)
    field_kind = "Q"

    def __init__(self, val: Fraction | int) -> None:
        self.val: Fraction = val if isinstance(val, Fraction) else Fraction(val)

    def is_zero(self) -> bool:
        return self.val == 0

    def __bool__(self) -> bool:
        return self.val != 0

    def __eq__(self, other: object) -> bool:
        if isinstance(other, QElem):
            return self.val == other.val
        if isinstance(other, (int, Fraction)):
            return self.val == other
        return NotImplemented

    def __neg__(self) -> QElem:
        return QElem(-self.val)

    def __pos__(self) -> QElem:
        return self

    def __add__(self, other: Any) -> Any:
        if isinstance(other, QElem):
            return QElem(self.val + other.val)
        if isinstance(other, (int, Fraction)):
            return QElem(self.val + other)
        return NotImplemented

    def __radd__(self, other: Any) -> Any:
        return self.__add__(other)

    def __sub__(self, other: Any) -> Any:
        if isinstance(other, QElem):
            return QElem(self.val - other.val)
        if isinstance(other, (int, Fraction)):
            return QElem(self.val - other)
        return NotImplemented

    def __rsub__(self, other: Any) -> Any:
        if isinstance(other, (int, Fraction)):
            return QElem(other - self.val)
        return NotImplemented

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, QElem):
            return QElem(self.val * other.val)
        if isinstance(other, (int, Fraction)):
            return QElem(self.val * other)
        return NotImplemented

    def __rmul__(self, other: Any) -> Any:
        return self.__mul__(other)

    def __truediv__(self, other: Any) -> Any:
        if isinstance(other, QElem):
            if other.val == 0:
                raise ZeroDivisionError("division by zero in QElem")
            return QElem(self.val / other.val)
        if isinstance(other, (int, Fraction)):
            if other == 0:
                raise ZeroDivisionError("division by zero in QElem")
            return QElem(self.val / other)
        return NotImplemented

    def __rtruediv__(self, other: Any) -> Any:
        if self.val == 0:
            raise ZeroDivisionError("division by zero in QElem")
        if isinstance(other, (int, Fraction)):
            return QElem(other / self.val)
        return NotImplemented

    def __pow__(self, exp: Any) -> Any:
        if isinstance(exp, int):
            if abs(exp) > 24:
                raise OutsideFieldError(f"Exponent {exp} exceeds exact ring cap")
            if exp == 0:
                return QElem(_F1)
            if exp < 0 and self.val == 0:
                raise ZeroDivisionError("0 to negative power in QElem")
            if abs(exp) > 1 and _frac_digits(self.val) * abs(exp) > 2500:
                raise OutsideFieldError("Intermediate QElem exceeded digit cap")
            return QElem(self.val**exp)
        if isinstance(exp, QElem):
            exp = exp.val
        if isinstance(exp, Fraction):
            if exp.denominator == 1:
                return self ** int(exp.numerator)
            if exp.denominator == 2:
                rt = self.sqrt_exact()
                return rt ** int(exp.numerator)
        raise OutsideFieldError(f"Non-integer power {exp!r} in QElem")

    def sqrt_exact(self) -> Any:
        rt = _frac_sqrt_exact(self.val)
        if rt is not None:
            return QElem(rt)
        # Check if self.val = 3 * r^2 -> r * sqrt(3) in ExtSqrt3Elem
        rt3 = _frac_sqrt_exact(self.val / 3)
        if rt3 is not None:
            return ExtSqrt3Elem(QElem(_F0), QElem(rt3))
        raise OutsideFieldError(f"sqrt({self.val}) not in Q(sqrt(3))")

    def sign(self) -> int:
        return 1 if self.val > 0 else (-1 if self.val < 0 else 0)

    def to_float(self) -> float:
        if self.max_digits() > 280:
            return _safe_mpf_to_float(self.to_mpf(50))
        try:
            return float(self.val)
        except OverflowError:
            return _safe_mpf_to_float(self.to_mpf(50))

    def to_mpf(self, dps: int = 50) -> mp.mpf:
        with mp.workdps(dps):
            return mp.mpf(self.val.numerator) / mp.mpf(self.val.denominator)

    def rat_coeffs(self) -> tuple[Fraction, ...]:
        return (self.val,)

    def scale_rational(self, factor: Fraction) -> QElem:
        return QElem(self.val * factor)

    def to_sympy(self) -> sp.Expr:
        return _frac_to_sympy(self.val)

    def to_latex(self) -> str:
        return _frac_latex(self.val)

    def max_digits(self) -> int:
        return _frac_digits(self.val)

    def __repr__(self) -> str:
        return f"Q({self.val})"


class QuadElem:
    """Exact element ``c0 + c1 * sqrt(d)`` in quadratic field ``Q(sqrt(d))``."""

    __slots__ = ("c0", "c1", "d")
    field_kind = "Quad"

    def __init__(self, c0: Fraction | int, c1: Fraction | int, d: int) -> None:
        self.c0: Fraction = c0 if isinstance(c0, Fraction) else Fraction(c0)
        self.c1: Fraction = c1 if isinstance(c1, Fraction) else Fraction(c1)
        self.d: int = d

    def is_zero(self) -> bool:
        return self.c0 == 0 and self.c1 == 0

    def __bool__(self) -> bool:
        return self.c0 != 0 or self.c1 != 0

    def __eq__(self, other: object) -> bool:
        if isinstance(other, QuadElem):
            return self.d == other.d and self.c0 == other.c0 and self.c1 == other.c1
        if isinstance(other, (int, Fraction)):
            return self.c1 == 0 and self.c0 == other
        return NotImplemented

    def __neg__(self) -> QuadElem:
        return QuadElem(-self.c0, -self.c1, self.d)

    def __pos__(self) -> QuadElem:
        return self

    def __add__(self, other: Any) -> Any:
        if isinstance(other, QuadElem):
            if self.d != other.d:
                raise OutsideFieldError("Mismatched quadratic fields")
            return QuadElem(self.c0 + other.c0, self.c1 + other.c1, self.d)
        if isinstance(other, (int, Fraction)):
            return QuadElem(self.c0 + other, self.c1, self.d)
        return NotImplemented

    def __radd__(self, other: Any) -> Any:
        return self.__add__(other)

    def __sub__(self, other: Any) -> Any:
        if isinstance(other, QuadElem):
            if self.d != other.d:
                raise OutsideFieldError("Mismatched quadratic fields")
            return QuadElem(self.c0 - other.c0, self.c1 - other.c1, self.d)
        if isinstance(other, (int, Fraction)):
            return QuadElem(self.c0 - other, self.c1, self.d)
        return NotImplemented

    def __rsub__(self, other: Any) -> Any:
        if isinstance(other, (int, Fraction)):
            return QuadElem(other - self.c0, -self.c1, self.d)
        return NotImplemented

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, QuadElem):
            if self.d != other.d:
                raise OutsideFieldError("Mismatched quadratic fields")
            return QuadElem(
                self.c0 * other.c0 + self.d * self.c1 * other.c1,
                self.c0 * other.c1 + self.c1 * other.c0,
                self.d,
            )
        if isinstance(other, (int, Fraction)):
            return QuadElem(self.c0 * other, self.c1 * other, self.d)
        return NotImplemented

    def __rmul__(self, other: Any) -> Any:
        return self.__mul__(other)

    def inv(self) -> QuadElem:
        norm = self.c0 * self.c0 - self.d * self.c1 * self.c1
        if norm == 0:
            raise ZeroDivisionError("division by zero in QuadElem")
        return QuadElem(self.c0 / norm, -self.c1 / norm, self.d)

    def __truediv__(self, other: Any) -> Any:
        if isinstance(other, QuadElem):
            return self * other.inv()
        if isinstance(other, (int, Fraction)):
            if other == 0:
                raise ZeroDivisionError("division by zero in QuadElem")
            return QuadElem(self.c0 / other, self.c1 / other, self.d)
        return NotImplemented

    def __rtruediv__(self, other: Any) -> Any:
        if isinstance(other, (int, Fraction)):
            return self.inv() * other
        return NotImplemented

    def __pow__(self, exp: Any) -> Any:
        if isinstance(exp, QuadElem):
            if exp.c1 != 0:
                raise OutsideFieldError("Irrational exponent")
            exp = exp.c0
        if isinstance(exp, Fraction):
            if exp.denominator == 1:
                exp = int(exp.numerator)
            elif exp.denominator == 2:
                return self.sqrt_exact() ** int(exp.numerator)
            else:
                raise OutsideFieldError(f"Unsupported fractional exponent {exp}")
        if not isinstance(exp, int):
            raise OutsideFieldError(f"Unsupported exponent {exp!r}")
        if abs(exp) > 24:
            raise OutsideFieldError(f"Exponent {exp} exceeds exact ring cap")
        if exp == 0:
            return QuadElem(_F1, _F0, self.d)
        if exp < 0:
            return self.inv() ** (-exp)
        base = self
        res = QuadElem(_F1, _F0, self.d)
        n = exp
        while n > 0:
            if n & 1:
                res = res * base
            n >>= 1
            if n:
                base = base * base
                if base.max_digits() > 2500:
                    raise OutsideFieldError("Intermediate QuadElem exceeded digit cap")
        return res

    def sqrt_exact(self) -> Any:
        if self.is_zero():
            return self
        if self.c1 == 0:
            rt = _frac_sqrt_exact(self.c0)
            if rt is not None:
                return QuadElem(rt, _F0, self.d)
            rtd = _frac_sqrt_exact(self.c0 / self.d)
            if rtd is not None:
                return QuadElem(_F0, rtd, self.d)
            if self.d != 3:
                rt3 = _frac_sqrt_exact(self.c0 / 3)
                if rt3 is not None:
                    return ExtSqrt3Elem(QuadElem(_F0, _F0, self.d), QuadElem(rt3, _F0, self.d))
                rt3d = _frac_sqrt_exact(self.c0 / (3 * self.d))
                if rt3d is not None:
                    return ExtSqrt3Elem(QuadElem(_F0, _F0, self.d), QuadElem(_F0, rt3d, self.d))
            raise OutsideFieldError(f"sqrt({self}) outside Quad({self.d})(sqrt(3))")
        # General sqrt(a + b*sqrt(d)) in Q(sqrt(d)):
        # Exists iff norm = a^2 - d*b^2 = r^2 and (a + r)/2 = u^2 (or (a + r)/(2d) = v^2)
        norm = self.c0 * self.c0 - self.d * self.c1 * self.c1
        r = _frac_sqrt_exact(norm)
        if r is not None:
            for sgn in (1, -1):
                half_sum = (self.c0 + sgn * r) / 2
                u = _frac_sqrt_exact(half_sum)
                if u is not None and u != 0:
                    v = self.c1 / (2 * u)
                    cand = QuadElem(u, v, self.d)
                    return cand if cand.sign() >= 0 else -cand
                v = _frac_sqrt_exact(half_sum / self.d)
                if v is not None and v != 0:
                    u = self.c1 / (2 * v)
                    cand = QuadElem(u, v, self.d)
                    return cand if cand.sign() >= 0 else -cand
        raise OutsideFieldError(f"sqrt({self}) outside Quad({self.d})")

    def sign(self) -> int:
        if self.is_zero():
            return 0
        if self.c1 == 0:
            return 1 if self.c0 > 0 else -1
        if self.c0 == 0:
            return 1 if self.c1 > 0 else -1
        s0 = 1 if self.c0 > 0 else -1
        s1 = 1 if self.c1 > 0 else -1
        if s0 == s1:
            return s0
        diff = self.c0 * self.c0 - self.d * self.c1 * self.c1
        return s0 if diff > 0 else s1

    def to_float(self) -> float:
        if self.max_digits() > 40:
            return _safe_mpf_to_float(self.to_mpf(50))
        return float(self.c0) + float(self.c1) * math.sqrt(self.d)

    def to_mpf(self, dps: int = 50) -> mp.mpf:
        with mp.workdps(dps):
            m0 = mp.mpf(self.c0.numerator) / mp.mpf(self.c0.denominator)
            m1 = mp.mpf(self.c1.numerator) / mp.mpf(self.c1.denominator)
            return m0 + m1 * mp.sqrt(self.d)

    def rat_coeffs(self) -> tuple[Fraction, ...]:
        return (self.c0, self.c1)

    def scale_rational(self, factor: Fraction) -> QuadElem:
        return QuadElem(self.c0 * factor, self.c1 * factor, self.d)

    def to_sympy(self) -> sp.Expr:
        rad = SQRT_3 if self.d == 3 else (SQRT_35 if self.d == 35 else sp.sqrt(self.d))
        if self.c1 == 0:
            return _frac_to_sympy(self.c0)
        if self.c0 == 0:
            return _frac_to_sympy(self.c1) * rad
        return _frac_to_sympy(self.c0) + _frac_to_sympy(self.c1) * rad

    def to_latex(self) -> str:
        if self.c1 == 0:
            return _frac_latex(self.c0)
        rad = rf"\sqrt{{{self.d}}}"
        c1_abs = abs(self.c1)
        if c1_abs == 1:
            t1 = rad
        elif c1_abs.denominator == 1:
            t1 = f"{c1_abs.numerator}{rad}"
        elif c1_abs.numerator == 1:
            t1 = rf"\frac{{{rad}}}{{{c1_abs.denominator}}}"
        else:
            t1 = rf"\frac{{{c1_abs.numerator}{rad}}}{{{c1_abs.denominator}}}"
        if self.c0 == 0:
            return f"-{t1}" if self.c1 < 0 else t1
        sign_str = " - " if self.c1 < 0 else " + "
        return f"{_frac_latex(self.c0)}{sign_str}{t1}"

    def max_digits(self) -> int:
        return max(_frac_digits(self.c0), _frac_digits(self.c1))

    def __repr__(self) -> str:
        return f"Quad({self.c0} + {self.c1}*sqrt({self.d}))"


@dataclass(frozen=True)
class BiquadSpec:
    """Specification for degree-4 biquadratic field ``Q(alpha)`` with ``alpha^4 = p*alpha^2 + q``."""

    name: str
    p: int
    q: int
    alpha_float: float
    alpha_sym: sp.Expr
    latex_basis: tuple[str, str, str, str]

    def alpha_mpf(self, dps: int = 50) -> mp.mpf:
        with mp.workdps(dps):
            # alpha^2 = (p + sqrt(p^2 + 4q)) / 2
            u = (mp.mpf(self.p) + mp.sqrt(mp.mpf(self.p * self.p + 4 * self.q))) / 2
            return mp.sqrt(u)


KEPLER_BIQUAD = BiquadSpec(
    name="kepler",
    p=1,
    q=1,
    alpha_float=math.sqrt((1.0 + math.sqrt(5.0)) / 2.0),
    alpha_sym=SQRT_PHI,
    latex_basis=("1", r"\sqrt{\phi}", r"\phi", r"\phi\sqrt{\phi}"),
)

PENTAGON_BIQUAD = BiquadSpec(
    name="pentagon",
    p=10,
    q=-5,
    alpha_float=math.sqrt(5.0 + 2.0 * math.sqrt(5.0)),
    alpha_sym=TAU,
    latex_basis=("1", r"\tau", r"\tau^2", r"\tau^3"),
)


class BiquadElem:
    """Exact element ``c0 + c1*a + c2*a^2 + c3*a^3`` in ``Q[a] / (a^4 - p*a^2 - q)``."""

    __slots__ = ("c0", "c1", "c2", "c3", "spec")
    field_kind = "Biquad"

    def __init__(
        self,
        c0: Fraction | int,
        c1: Fraction | int,
        c2: Fraction | int,
        c3: Fraction | int,
        spec: BiquadSpec,
    ) -> None:
        self.c0: Fraction = c0 if isinstance(c0, Fraction) else Fraction(c0)
        self.c1: Fraction = c1 if isinstance(c1, Fraction) else Fraction(c1)
        self.c2: Fraction = c2 if isinstance(c2, Fraction) else Fraction(c2)
        self.c3: Fraction = c3 if isinstance(c3, Fraction) else Fraction(c3)
        self.spec = spec

    def is_zero(self) -> bool:
        return self.c0 == 0 and self.c1 == 0 and self.c2 == 0 and self.c3 == 0

    def __bool__(self) -> bool:
        return not self.is_zero()

    def __eq__(self, other: object) -> bool:
        if isinstance(other, BiquadElem):
            return (
                self.spec is other.spec
                and self.c0 == other.c0
                and self.c1 == other.c1
                and self.c2 == other.c2
                and self.c3 == other.c3
            )
        if isinstance(other, (int, Fraction)):
            return self.c1 == 0 and self.c2 == 0 and self.c3 == 0 and self.c0 == other
        return NotImplemented

    def __neg__(self) -> BiquadElem:
        return BiquadElem(-self.c0, -self.c1, -self.c2, -self.c3, self.spec)

    def __pos__(self) -> BiquadElem:
        return self

    def __add__(self, other: Any) -> Any:
        if isinstance(other, BiquadElem):
            if self.spec is not other.spec:
                raise OutsideFieldError("Mismatched biquadratic fields")
            return BiquadElem(
                self.c0 + other.c0,
                self.c1 + other.c1,
                self.c2 + other.c2,
                self.c3 + other.c3,
                self.spec,
            )
        if isinstance(other, (int, Fraction)):
            return BiquadElem(self.c0 + other, self.c1, self.c2, self.c3, self.spec)
        return NotImplemented

    def __radd__(self, other: Any) -> Any:
        return self.__add__(other)

    def __sub__(self, other: Any) -> Any:
        if isinstance(other, BiquadElem):
            if self.spec is not other.spec:
                raise OutsideFieldError("Mismatched biquadratic fields")
            return BiquadElem(
                self.c0 - other.c0,
                self.c1 - other.c1,
                self.c2 - other.c2,
                self.c3 - other.c3,
                self.spec,
            )
        if isinstance(other, (int, Fraction)):
            return BiquadElem(self.c0 - other, self.c1, self.c2, self.c3, self.spec)
        return NotImplemented

    def __rsub__(self, other: Any) -> Any:
        if isinstance(other, (int, Fraction)):
            return BiquadElem(other - self.c0, -self.c1, -self.c2, -self.c3, self.spec)
        return NotImplemented

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, BiquadElem):
            if self.spec is not other.spec:
                raise OutsideFieldError("Mismatched biquadratic fields")
            a0, a1, a2, a3 = self.c0, self.c1, self.c2, self.c3
            b0, b1, b2, b3 = other.c0, other.c1, other.c2, other.c3
            p, q = self.spec.p, self.spec.q
            # Polynomial product d0..d6 reduced modulo a^4 = p*a^2 + q
            d0 = a0 * b0
            d1 = a0 * b1 + a1 * b0
            d2 = a0 * b2 + a1 * b1 + a2 * b0
            d3 = a0 * b3 + a1 * b2 + a2 * b1 + a3 * b0
            d4 = a1 * b3 + a2 * b2 + a3 * b1
            d5 = a2 * b3 + a3 * b2
            d6 = a3 * b3
            # a^6 = p*a^4 + q*a^2 = (p^2 + q)*a^2 + p*q
            # a^5 = p*a^3 + q*a
            # a^4 = p*a^2 + q
            r0 = d0 + q * d4 + (p * q) * d6
            r1 = d1 + q * d5
            r2 = d2 + p * d4 + (p * p + q) * d6
            r3 = d3 + p * d5
            return BiquadElem(r0, r1, r2, r3, self.spec)
        if isinstance(other, (int, Fraction)):
            return BiquadElem(
                self.c0 * other, self.c1 * other, self.c2 * other, self.c3 * other, self.spec
            )
        return NotImplemented

    def __rmul__(self, other: Any) -> Any:
        return self.__mul__(other)

    def inv(self) -> BiquadElem:
        """Exact O(1) inversion via tower Q(u)(alpha) where u = alpha^2, u^2 = p*u + q."""
        if self.is_zero():
            raise ZeroDivisionError("division by zero in BiquadElem")
        e0, o0, e1, o1 = self.c0, self.c1, self.c2, self.c3
        p, q = self.spec.p, self.spec.q
        # E = e0 + e1*u, O = o0 + o1*u; E^2 - u*O^2 = A + B*u in Q(u)
        # E^2 = (e0^2 + q*e1^2) + (2*e0*e1 + p*e1^2)*u
        ee0 = e0 * e0 + q * e1 * e1
        ee1 = 2 * e0 * e1 + p * e1 * e1
        # O^2 = (o0^2 + q*o1^2) + (2*o0*o1 + p*o1^2)*u
        oo0 = o0 * o0 + q * o1 * o1
        oo1 = 2 * o0 * o1 + p * o1 * o1
        # u * O^2 = (q*oo1) + (oo0 + p*oo1)*u
        A = ee0 - q * oo1
        B = ee1 - (oo0 + p * oo1)
        # Invert A + B*u in Q(u): (A + B*u)^{-1} = ((A + p*B) - B*u) / (A^2 + p*A*B - q*B^2)
        den = A * A + p * A * B - q * B * B
        if den == 0:
            raise ZeroDivisionError("singular element in BiquadElem")
        i0 = (A + p * B) / den
        i1 = -B / den
        # Multiply (E - alpha*O) by (i0 + i1*u)
        # E * (i0 + i1*u) = (e0*i0 + q*e1*i1) + (e0*i1 + e1*i0 + p*e1*i1)*u
        r0 = e0 * i0 + q * e1 * i1
        r2 = e0 * i1 + e1 * i0 + p * e1 * i1
        # (-O) * (i0 + i1*u)
        r1 = -(o0 * i0 + q * o1 * i1)
        r3 = -(o0 * i1 + o1 * i0 + p * o1 * i1)
        return BiquadElem(r0, r1, r2, r3, self.spec)

    def __truediv__(self, other: Any) -> Any:
        if isinstance(other, BiquadElem):
            return self * other.inv()
        if isinstance(other, (int, Fraction)):
            if other == 0:
                raise ZeroDivisionError("division by zero in BiquadElem")
            return BiquadElem(
                self.c0 / other, self.c1 / other, self.c2 / other, self.c3 / other, self.spec
            )
        return NotImplemented

    def __rtruediv__(self, other: Any) -> Any:
        if isinstance(other, (int, Fraction)):
            return self.inv() * other
        return NotImplemented

    def __pow__(self, exp: Any) -> Any:
        if isinstance(exp, BiquadElem):
            if exp.c1 != 0 or exp.c2 != 0 or exp.c3 != 0:
                raise OutsideFieldError("Irrational exponent in BiquadElem")
            exp = exp.c0
        if isinstance(exp, Fraction):
            if exp.denominator == 1:
                exp = int(exp.numerator)
            elif exp.denominator == 2:
                return self.sqrt_exact() ** int(exp.numerator)
            else:
                raise OutsideFieldError(f"Unsupported fractional exponent {exp}")
        if not isinstance(exp, int):
            raise OutsideFieldError(f"Unsupported exponent {exp!r}")
        if abs(exp) > 24:
            raise OutsideFieldError(f"Exponent {exp} exceeds exact ring cap")
        if exp == 0:
            return BiquadElem(_F1, _F0, _F0, _F0, self.spec)
        if exp < 0:
            return self.inv() ** (-exp)
        base = self
        res = BiquadElem(_F1, _F0, _F0, _F0, self.spec)
        n = exp
        while n > 0:
            if n & 1:
                res = res * base
            n >>= 1
            if n:
                base = base * base
                if base.max_digits() > 2500:
                    raise OutsideFieldError("Intermediate BiquadElem exceeded digit cap")
        return res

    def sqrt_exact(self) -> Any:
        """Compute exact sqrt in Q(alpha) or Q(alpha)(sqrt(3)) for common rational/subfield squares."""
        if self.is_zero():
            return self
        # Pure rational case
        if self.c1 == 0 and self.c2 == 0 and self.c3 == 0:
            rt = _frac_sqrt_exact(self.c0)
            if rt is not None:
                return BiquadElem(rt, _F0, _F0, _F0, self.spec)
            # Check 5 * r^2 (sqrt(5) lies in both Kepler and Pentagon!)
            rt5 = _frac_sqrt_exact(self.c0 / 5)
            if rt5 is not None:
                if self.spec is KEPLER_BIQUAD:
                    # sqrt(5) = 2*phi - 1 = (-1, 0, 2, 0)
                    return BiquadElem(-rt5, _F0, 2 * rt5, _F0, self.spec)
                if self.spec is PENTAGON_BIQUAD:
                    # sqrt(5) = (tau^2 - 5)/2 = (-5/2, 0, 1/2, 0)
                    return BiquadElem(Fraction(-5, 2) * rt5, _F0, _HALF * rt5, _F0, self.spec)
            # Check 3 * r^2 -> r * sqrt(3) in ExtSqrt3Elem
            rt3 = _frac_sqrt_exact(self.c0 / 3)
            if rt3 is not None:
                zero_b = BiquadElem(_F0, _F0, _F0, _F0, self.spec)
                return ExtSqrt3Elem(zero_b, BiquadElem(rt3, _F0, _F0, _F0, self.spec))
        # Element in quadratic subfield Q(u) = Q(sqrt(5)): c1 == c3 == 0
        if self.c1 == 0 and self.c3 == 0:
            # Check if self = r^2 * u = r^2 * alpha^2 -> r * alpha
            if self.c0 == 0:
                rt = _frac_sqrt_exact(self.c2)
                if rt is not None:
                    return BiquadElem(_F0, rt, _F0, _F0, self.spec)
            # Convert self = c0 + c2*u to a + b*sqrt(5)
            if self.spec is KEPLER_BIQUAD:
                a5 = self.c0 + self.c2 * _HALF
                b5 = self.c2 * _HALF
            else:
                # u = tau^2 = 5 + 2*sqrt(5)
                a5 = self.c0 + 5 * self.c2
                b5 = 2 * self.c2
            q5 = QuadElem(a5, b5, 5)
            try:
                rt_q5 = q5.sqrt_exact()
                if isinstance(rt_q5, QuadElem):
                    # Map a + b*sqrt(5) back into BiquadElem
                    if self.spec is KEPLER_BIQUAD:
                        return BiquadElem(rt_q5.c0 - rt_q5.c1, _F0, 2 * rt_q5.c1, _F0, self.spec)
                    return BiquadElem(
                        rt_q5.c0 - Fraction(5, 2) * rt_q5.c1, _F0, _HALF * rt_q5.c1, _F0, self.spec
                    )
            except OutsideFieldError:
                pass
            # Also check if self / u is a square in Q(sqrt(5)), i.e. sqrt(self) = alpha * sqrt(self/u)
            u_elem = BiquadElem(_F0, _F0, _F1, _F0, self.spec)
            quot = self / u_elem
            if quot.c1 == 0 and quot.c3 == 0:
                if self.spec is KEPLER_BIQUAD:
                    qa5 = quot.c0 + quot.c2 * _HALF
                    qb5 = quot.c2 * _HALF
                else:
                    qa5 = quot.c0 + 5 * quot.c2
                    qb5 = 2 * quot.c2
                try:
                    rt_q = QuadElem(qa5, qb5, 5).sqrt_exact()
                    if isinstance(rt_q, QuadElem):
                        if self.spec is KEPLER_BIQUAD:
                            root_q = BiquadElem(rt_q.c0 - rt_q.c1, _F0, 2 * rt_q.c1, _F0, self.spec)
                        else:
                            root_q = BiquadElem(
                                rt_q.c0 - Fraction(5, 2) * rt_q.c1,
                                _F0,
                                _HALF * rt_q.c1,
                                _F0,
                                self.spec,
                            )
                        cand = root_q * BiquadElem(_F0, _F1, _F0, _F0, self.spec)
                        return cand if cand.sign() >= 0 else -cand
                except OutsideFieldError:
                    pass
        raise OutsideFieldError(f"sqrt({self}) outside Biquad({self.spec.name})")

    def sign(self) -> int:
        if self.is_zero():
            return 0
        for dps in (50, 150, 400):
            with mp.workdps(dps):
                a = self.spec.alpha_mpf(dps)
                m0 = mp.mpf(self.c0.numerator) / mp.mpf(self.c0.denominator)
                m1 = mp.mpf(self.c1.numerator) / mp.mpf(self.c1.denominator)
                m2 = mp.mpf(self.c2.numerator) / mp.mpf(self.c2.denominator)
                m3 = mp.mpf(self.c3.numerator) / mp.mpf(self.c3.denominator)
                scale = max(abs(m0), abs(m1) * a, abs(m2) * a * a, abs(m3) * a * a * a)
                val = m0 + a * (m1 + a * (m2 + a * m3))
                if abs(val) > scale * mp.mpf(10) ** (-(dps // 3)):
                    return 1 if val > 0 else -1
        # Exact fallback via SymPy if near-cancellation occurs
        s_val = self.to_sympy().evalf(500)
        return 1 if s_val > 0 else (-1 if s_val < 0 else 0)

    def to_float(self) -> float:
        if self.max_digits() > 40:
            return _safe_mpf_to_float(self.to_mpf(50))
        a = self.spec.alpha_float
        return float(self.c0) + a * (float(self.c1) + a * (float(self.c2) + a * float(self.c3)))

    def to_mpf(self, dps: int = 50) -> mp.mpf:
        with mp.workdps(dps):
            a = self.spec.alpha_mpf(dps)
            m0 = mp.mpf(self.c0.numerator) / mp.mpf(self.c0.denominator)
            m1 = mp.mpf(self.c1.numerator) / mp.mpf(self.c1.denominator)
            m2 = mp.mpf(self.c2.numerator) / mp.mpf(self.c2.denominator)
            m3 = mp.mpf(self.c3.numerator) / mp.mpf(self.c3.denominator)
            return m0 + a * (m1 + a * (m2 + a * m3))

    def rat_coeffs(self) -> tuple[Fraction, ...]:
        return (self.c0, self.c1, self.c2, self.c3)

    def scale_rational(self, factor: Fraction) -> BiquadElem:
        return BiquadElem(
            self.c0 * factor,
            self.c1 * factor,
            self.c2 * factor,
            self.c3 * factor,
            self.spec,
        )

    def to_sympy(self) -> sp.Expr:
        if self.spec is KEPLER_BIQUAD:
            return (
                _frac_to_sympy(self.c0)
                + _frac_to_sympy(self.c1) * SQRT_PHI
                + _frac_to_sympy(self.c2) * PHI
                + _frac_to_sympy(self.c3) * PHI * SQRT_PHI
            )
        # Pentagon: tau^2 = 5 + 2*sqrt(5), tau^3 = (5 + 2*sqrt(5))*tau
        a = self.spec.alpha_sym
        return (
            _frac_to_sympy(self.c0)
            + _frac_to_sympy(self.c1) * a
            + _frac_to_sympy(self.c2) * (sp.Integer(5) + sp.Integer(2) * sp.sqrt(5))
            + _frac_to_sympy(self.c3) * a**3
        )

    def to_latex(self) -> str:
        # Format cleanly in compact canonical basis
        if self.spec is KEPLER_BIQUAD:
            basis = self.spec.latex_basis
            coeffs = (self.c0, self.c1, self.c2, self.c3)
        else:
            # Rewrite Pentagon element cleanly in (1, sqrt(5), tau, tau*sqrt(5)) basis!
            # c0 + c1*tau + c2*(5 + 2*sqrt(5)) + c3*(5 + 2*sqrt(5))*tau
            k0 = self.c0 + 5 * self.c2
            k1 = 2 * self.c2
            k2 = self.c1 + 5 * self.c3
            k3 = 2 * self.c3
            basis = ("1", r"\sqrt{5}", r"\tau", r"\tau\sqrt{5}")
            coeffs = (k0, k1, k2, k3)
        parts: list[str] = []
        for c, b in zip(coeffs, basis, strict=True):
            if c == 0:
                continue
            neg = c < 0
            ca = abs(c)
            if b == "1":
                term = _frac_latex(ca)
            elif ca == 1:
                term = b
            elif ca.denominator == 1:
                term = f"{ca.numerator}{b}"
            elif ca.numerator == 1:
                term = rf"\frac{{{b}}}{{{ca.denominator}}}"
            else:
                term = rf"\frac{{{ca.numerator}{b}}}{{{ca.denominator}}}"
            if not parts:
                parts.append(f"-{term}" if neg else term)
            else:
                parts.append(f" - {term}" if neg else f" + {term}")
        return "".join(parts) if parts else "0"

    def max_digits(self) -> int:
        return max(
            _frac_digits(self.c0),
            _frac_digits(self.c1),
            _frac_digits(self.c2),
            _frac_digits(self.c3),
        )

    def __repr__(self) -> str:
        return f"Biquad({self.spec.name}: {self.c0}, {self.c1}, {self.c2}, {self.c3})"


class ExtSqrt3Elem:
    """Quadratic extension ``c0 + c1 * sqrt(3)`` over any base exact field ``K``."""

    __slots__ = ("c0", "c1")
    field_kind = "ExtSqrt3"

    def __init__(self, c0: Any, c1: Any) -> None:
        self.c0 = c0
        self.c1 = c1

    def _zero_base(self) -> Any:
        return self.c0 * _F0

    def _lift(self, other: Any) -> ExtSqrt3Elem:
        if isinstance(other, ExtSqrt3Elem):
            return other
        if isinstance(other, (int, Fraction)):
            return ExtSqrt3Elem(self.c0 * _F0 + other, self._zero_base())
        if isinstance(other, (QElem, QuadElem, BiquadElem)):
            return ExtSqrt3Elem(other, other * _F0)
        raise OutsideFieldError(f"Cannot lift {type(other).__name__} into ExtSqrt3Elem")

    def is_zero(self) -> bool:
        return self.c0.is_zero() and self.c1.is_zero()

    def __bool__(self) -> bool:
        return not self.is_zero()

    def __eq__(self, other: object) -> bool:
        if isinstance(other, ExtSqrt3Elem):
            return self.c0 == other.c0 and self.c1 == other.c1
        if isinstance(other, (int, Fraction, QElem, QuadElem, BiquadElem)):
            return self.c1.is_zero() and self.c0 == other
        return NotImplemented

    def __neg__(self) -> ExtSqrt3Elem:
        return ExtSqrt3Elem(-self.c0, -self.c1)

    def __pos__(self) -> ExtSqrt3Elem:
        return self

    def __add__(self, other: Any) -> ExtSqrt3Elem:
        o = self._lift(other)
        return ExtSqrt3Elem(self.c0 + o.c0, self.c1 + o.c1)

    def __radd__(self, other: Any) -> ExtSqrt3Elem:
        return self.__add__(other)

    def __sub__(self, other: Any) -> ExtSqrt3Elem:
        o = self._lift(other)
        return ExtSqrt3Elem(self.c0 - o.c0, self.c1 - o.c1)

    def __rsub__(self, other: Any) -> ExtSqrt3Elem:
        o = self._lift(other)
        return ExtSqrt3Elem(o.c0 - self.c0, o.c1 - self.c1)

    def __mul__(self, other: Any) -> ExtSqrt3Elem:
        o = self._lift(other)
        return ExtSqrt3Elem(
            self.c0 * o.c0 + (self.c1 * o.c1) * 3,
            self.c0 * o.c1 + self.c1 * o.c0,
        )

    def __rmul__(self, other: Any) -> ExtSqrt3Elem:
        return self.__mul__(other)

    def inv(self) -> ExtSqrt3Elem:
        norm = self.c0 * self.c0 - (self.c1 * self.c1) * 3
        if norm.is_zero():
            raise ZeroDivisionError("division by zero in ExtSqrt3Elem")
        return ExtSqrt3Elem(self.c0 / norm, -self.c1 / norm)

    def __truediv__(self, other: Any) -> ExtSqrt3Elem:
        o = self._lift(other)
        return self * o.inv()

    def __rtruediv__(self, other: Any) -> ExtSqrt3Elem:
        o = self._lift(other)
        return o * self.inv()

    def __pow__(self, exp: Any) -> ExtSqrt3Elem:
        if isinstance(exp, ExtSqrt3Elem):
            if not exp.c1.is_zero():
                raise OutsideFieldError("Irrational exponent in ExtSqrt3Elem")
            exp = exp.c0
        if isinstance(exp, (QElem, QuadElem, BiquadElem)):
            coeffs = exp.rat_coeffs()
            if any(c != 0 for c in coeffs[1:]):
                raise OutsideFieldError("Irrational exponent in ExtSqrt3Elem")
            exp = coeffs[0]
        if isinstance(exp, Fraction):
            if exp.denominator == 1:
                exp = int(exp.numerator)
            elif exp.denominator == 2:
                return self.sqrt_exact() ** int(exp.numerator)
            else:
                raise OutsideFieldError(f"Unsupported fractional exponent {exp}")
        if not isinstance(exp, int):
            raise OutsideFieldError(f"Unsupported exponent {exp!r}")
        if abs(exp) > 24:
            raise OutsideFieldError(f"Exponent {exp} exceeds exact ring cap")
        if exp == 0:
            return ExtSqrt3Elem(self.c0 * _F0 + _F1, self._zero_base())
        if exp < 0:
            return self.inv() ** (-exp)
        base = self
        res = ExtSqrt3Elem(self.c0 * _F0 + _F1, self._zero_base())
        n = exp
        while n > 0:
            if n & 1:
                res = res * base
            n >>= 1
            if n:
                base = base * base
                if base.max_digits() > 2500:
                    raise OutsideFieldError("Intermediate ExtSqrt3Elem exceeded digit cap")
        return res

    def sqrt_exact(self) -> ExtSqrt3Elem:
        if self.c1.is_zero():
            rt = self.c0.sqrt_exact()
            return rt if isinstance(rt, ExtSqrt3Elem) else ExtSqrt3Elem(rt, self._zero_base())
        raise OutsideFieldError(f"sqrt({self}) outside ExtSqrt3")

    def sign(self) -> int:
        if self.is_zero():
            return 0
        if self.c1.is_zero():
            return self.c0.sign()
        if self.c0.is_zero():
            return self.c1.sign()
        s0, s1 = self.c0.sign(), self.c1.sign()
        if s0 == s1:
            return s0
        diff = self.c0 * self.c0 - (self.c1 * self.c1) * 3
        return s0 if diff.sign() > 0 else s1

    def to_float(self) -> float:
        if self.max_digits() > 40:
            return _safe_mpf_to_float(self.to_mpf(50))
        return self.c0.to_float() + self.c1.to_float() * math.sqrt(3.0)

    def to_mpf(self, dps: int = 50) -> mp.mpf:
        with mp.workdps(dps):
            return self.c0.to_mpf(dps) + self.c1.to_mpf(dps) * mp.sqrt(3)

    def rat_coeffs(self) -> tuple[Fraction, ...]:
        return self.c0.rat_coeffs() + self.c1.rat_coeffs()

    def scale_rational(self, factor: Fraction) -> Any:
        if self.c1.is_zero():
            return self.c0.scale_rational(factor)
        return ExtSqrt3Elem(self.c0.scale_rational(factor), self.c1.scale_rational(factor))

    def to_sympy(self) -> sp.Expr:
        if self.c1.is_zero():
            return self.c0.to_sympy()
        if self.c0.is_zero():
            return self.c1.to_sympy() * SQRT_3
        return self.c0.to_sympy() + self.c1.to_sympy() * SQRT_3

    def to_latex(self) -> str:
        if self.c1.is_zero():
            return self.c0.to_latex()
        c1_ltx = self.c1.to_latex()
        needs_par = (" + " in c1_ltx) or (" - " in c1_ltx)
        if c1_ltx == "1":
            t1 = r"\sqrt{3}"
        elif c1_ltx == "-1":
            t1 = r"-\sqrt{3}"
        elif needs_par:
            t1 = rf"\left({c1_ltx}\right)\sqrt{{3}}"
        else:
            t1 = rf"{c1_ltx}\sqrt{{3}}"
        if self.c0.is_zero():
            return t1
        c0_ltx = self.c0.to_latex()
        if t1.startswith("-"):
            return f"{c0_ltx} - {t1[1:]}"
        return f"{c0_ltx} + {t1}"

    def max_digits(self) -> int:
        return max(self.c0.max_digits(), self.c1.max_digits())

    def __repr__(self) -> str:
        return f"ExtSqrt3({self.c0} + {self.c1}*sqrt(3))"


# ---------------------------------------------------------------------------
# Exact Linear Angle Algebra (for exact sin/cos/tan/cot/sec/csc composition)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class AngleLinear:
    """Exact linear combination ``cA*A + cB*B + cC*C + cw*omega + cpi*pi``."""

    cA: Fraction = _F0
    cB: Fraction = _F0
    cC: Fraction = _F0
    cw: Fraction = _F0
    cpi: Fraction = _F0

    def __neg__(self) -> AngleLinear:
        return AngleLinear(-self.cA, -self.cB, -self.cC, -self.cw, -self.cpi)

    def __pos__(self) -> AngleLinear:
        return self

    def __add__(self, other: Any) -> AngleLinear:
        if isinstance(other, AngleLinear):
            return AngleLinear(
                self.cA + other.cA,
                self.cB + other.cB,
                self.cC + other.cC,
                self.cw + other.cw,
                self.cpi + other.cpi,
            )
        raise OutsideFieldError(f"Cannot add angle and {type(other).__name__}")

    def __sub__(self, other: Any) -> AngleLinear:
        if isinstance(other, AngleLinear):
            return self + (-other)
        raise OutsideFieldError(f"Cannot subtract angle and {type(other).__name__}")

    def _to_rat(self, scalar: Any) -> Fraction:
        if isinstance(scalar, int):
            return Fraction(scalar)
        if isinstance(scalar, Fraction):
            return scalar
        if isinstance(scalar, QElem):
            return scalar.val
        if isinstance(scalar, (QuadElem, BiquadElem, ExtSqrt3Elem)):
            rc = scalar.rat_coeffs()
            if all(c == 0 for c in rc[1:]):
                return rc[0]
        raise OutsideFieldError(f"Non-rational angle multiplier {scalar!r}")

    def __mul__(self, other: Any) -> AngleLinear:
        k = self._to_rat(other)
        return AngleLinear(self.cA * k, self.cB * k, self.cC * k, self.cw * k, self.cpi * k)

    def __rmul__(self, other: Any) -> AngleLinear:
        return self.__mul__(other)

    def __truediv__(self, other: Any) -> AngleLinear:
        k = self._to_rat(other)
        if k == 0:
            raise ZeroDivisionError("division by zero in AngleLinear")
        return AngleLinear(self.cA / k, self.cB / k, self.cC / k, self.cw / k, self.cpi / k)


def _cs_mul(p1: tuple[Any, Any], p2: tuple[Any, Any]) -> tuple[Any, Any]:
    return (p1[0] * p2[0] - p1[1] * p2[1], p1[0] * p2[1] + p1[1] * p2[0])


def _cs_pow(pair: tuple[Any, Any], n: int, one: Any, zero: Any) -> tuple[Any, Any]:
    if n == 0:
        return (one, zero)
    if n < 0:
        pair = (pair[0], -pair[1])
        n = -n
    res = (one, zero)
    base = pair
    while n > 0:
        if n & 1:
            res = _cs_mul(res, base)
        n >>= 1
        if n:
            base = _cs_mul(base, base)
    return res


def _reduce_exact_triple(vals: tuple[Any, Any, Any]) -> tuple[Any, Any, Any]:
    """Scale a homogeneous exact triple by rational LCM/GCD to clean integral form."""
    if all(v.is_zero() for v in vals):
        z = vals[0] * _F0
        return (z, z, z)

    # First, if any non-zero entry is a non-rational field element and pairwise ratios are rational,
    # cancel the common field factor!
    anchor = next(v for v in vals if not v.is_zero())
    if not isinstance(anchor, QElem):
        try:
            ratios = [v / anchor for v in vals]
            rat_only: list[Fraction] = []
            ok_rat = True
            for r in ratios:
                rc = r.rat_coeffs()
                if all(c == 0 for c in rc[1:]):
                    rat_only.append(rc[0])
                else:
                    ok_rat = False
                    break
            if ok_rat:
                lcm_d = functools.reduce(math.lcm, [r.denominator for r in rat_only], 1)
                ints = [int(r * lcm_d) for r in rat_only]
                nz = [abs(n) for n in ints if n != 0]
                g = functools.reduce(math.gcd, nz) if nz else 1
                ints = [n // g for n in ints]
                if all(n <= 0 for n in ints) or sum(ints) < 0:
                    ints = [-n for n in ints]
                base_zero = vals[0] * _F0
                if isinstance(base_zero, ExtSqrt3Elem):
                    base_zero = base_zero.c0
                return (base_zero + ints[0], base_zero + ints[1], base_zero + ints[2])
        except ZeroDivisionError:
            pass

    all_rats: list[Fraction] = []
    for v in vals:
        all_rats.extend(v.rat_coeffs())
    lcm_d = functools.reduce(math.lcm, [c.denominator for c in all_rats if c != 0], 1)
    nz_ints = [abs(int(c * lcm_d)) for c in all_rats if c != 0]
    g = functools.reduce(math.gcd, nz_ints) if nz_ints else 1
    factor = Fraction(lcm_d, g)
    scaled = tuple(v.scale_rational(factor) for v in vals)
    total = scaled[0] + scaled[1] + scaled[2]
    if not total.is_zero() and total.sign() < 0:
        scaled = (-scaled[0], -scaled[1], -scaled[2])
    return (scaled[0], scaled[1], scaled[2])


# ---------------------------------------------------------------------------
# Exact Triangle Field Environment (All 7 Canonical Triangles)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ExactEvalResult:
    """Compact exact (or 50-digit mpmath fallback) evaluation result for one triangle."""

    triangle_key: str
    precision: str  # "exact" | "mpmath-50"
    bary: tuple[Any, Any, Any] | None  # Exact field elements if exact, else None
    trilinear: tuple[Any, Any, Any] | None
    xy: tuple[Any, Any] | None
    search_value: Any | None
    approx_xy: tuple[float, float]
    approx_bary: tuple[float, float, float]
    approx_search: float
    is_indeterminate: bool = False
    is_ideal: bool = False
    symmetry_note: str = ""
    field_tag: str = ""
    bary_latex: str = ""
    trilinear_latex: str = ""
    xy_latex: str = ""
    search_latex: str = ""


class ExactTriangleField:
    """Fast exact algebraic field context for one canonical reference triangle."""

    def __init__(self, key: str) -> None:
        self.key = key
        self._eval_ops: int = 0
        self._eval_deadline: float = 0.0
        self.is_equilateral = key == "equilateral"
        self.is_isosceles = key in {"golden", "gnomon", "equilateral"}
        self.is_right = key in {"right", "kepler"}

        if key == "heronian":
            self.label = "Heronian (15, 13, 14)"
            self.field_latex = r"\mathbb{Q}"
            self.zero: Any = QElem(_F0)
            self.one: Any = QElem(_F1)
            self.sqrt3: Any = ExtSqrt3Elem(QElem(_F0), QElem(_F1))
            self.a = QElem(15)
            self.b = QElem(13)
            self.c = QElem(14)
            self.A_xy = (QElem(0), QElem(0))
            self.B_xy = (QElem(14), QElem(0))
            self.C_xy = (QElem(5), QElem(12))
            self.area = QElem(84)
        elif key == "right":
            self.label = "Right (5, 3, 4)"
            self.field_latex = r"\mathbb{Q}"
            self.zero = QElem(_F0)
            self.one = QElem(_F1)
            self.sqrt3 = ExtSqrt3Elem(QElem(_F0), QElem(_F1))
            self.a = QElem(5)
            self.b = QElem(3)
            self.c = QElem(4)
            self.A_xy = (QElem(0), QElem(0))
            self.B_xy = (QElem(4), QElem(0))
            self.C_xy = (QElem(0), QElem(3))
            self.area = QElem(6)
        elif key == "equilateral":
            self.label = "Equilateral (2, 2, 2)"
            self.field_latex = r"\mathbb{Q}(\sqrt{3})"
            self.zero = QuadElem(_F0, _F0, 3)
            self.one = QuadElem(_F1, _F0, 3)
            self.sqrt3 = QuadElem(_F0, _F1, 3)
            self.a = QuadElem(2, 0, 3)
            self.b = QuadElem(2, 0, 3)
            self.c = QuadElem(2, 0, 3)
            self.A_xy = (self.zero, self.zero)
            self.B_xy = (QuadElem(2, 0, 3), self.zero)
            self.C_xy = (self.one, self.sqrt3)
            self.area = self.sqrt3
        elif key == "kimberling":
            self.label = "Kimberling (6, 9, 13)"
            self.field_latex = r"\mathbb{Q}(\sqrt{35})"
            self.zero = QuadElem(_F0, _F0, 35)
            self.one = QuadElem(_F1, _F0, 35)
            self.sqrt3 = ExtSqrt3Elem(self.zero, self.one)
            self.a = QuadElem(6, 0, 35)
            self.b = QuadElem(9, 0, 35)
            self.c = QuadElem(13, 0, 35)
            self.A_xy = (self.zero, self.zero)
            self.B_xy = (QuadElem(13, 0, 35), self.zero)
            self.C_xy = (QuadElem(Fraction(107, 13), 0, 35), QuadElem(0, Fraction(8, 13), 35))
            self.area = QuadElem(0, 4, 35)
        elif key == "kepler":
            self.label = "Kepler (φ, 1, √φ)"
            self.field_latex = r"\mathbb{Q}(\sqrt{\phi})"
            sp_k = KEPLER_BIQUAD
            self.zero = BiquadElem(0, 0, 0, 0, sp_k)
            self.one = BiquadElem(1, 0, 0, 0, sp_k)
            self.sqrt3 = ExtSqrt3Elem(self.zero, self.one)
            s_phi = BiquadElem(0, 1, 0, 0, sp_k)
            phi = BiquadElem(0, 0, 1, 0, sp_k)
            self.a = phi
            self.b = self.one
            self.c = s_phi
            self.A_xy = (self.zero, self.zero)
            self.B_xy = (s_phi, self.zero)
            self.C_xy = (self.zero, self.one)
            self.area = s_phi * _HALF
        elif key == "golden":
            self.label = "Golden (φ, φ, 1)"
            self.field_latex = r"\mathbb{Q}(\sqrt{5 + 2\sqrt{5}})"
            sp_p = PENTAGON_BIQUAD
            self.zero = BiquadElem(0, 0, 0, 0, sp_p)
            self.one = BiquadElem(1, 0, 0, 0, sp_p)
            self.sqrt3 = ExtSqrt3Elem(self.zero, self.one)
            phi = BiquadElem(Fraction(-3, 4), 0, Fraction(1, 4), 0, sp_p)
            tau = BiquadElem(0, 1, 0, 0, sp_p)
            self.a = phi
            self.b = phi
            self.c = self.one
            self.A_xy = (self.zero, self.zero)
            self.B_xy = (self.one, self.zero)
            self.C_xy = (self.one * _HALF, tau * _HALF)
            self.area = tau * Fraction(1, 4)
        elif key == "gnomon":
            self.label = "Gnomon (1, 1, φ)"
            self.field_latex = r"\mathbb{Q}(\sqrt{5 + 2\sqrt{5}})"
            sp_p = PENTAGON_BIQUAD
            self.zero = BiquadElem(0, 0, 0, 0, sp_p)
            self.one = BiquadElem(1, 0, 0, 0, sp_p)
            self.sqrt3 = ExtSqrt3Elem(self.zero, self.one)
            phi = BiquadElem(Fraction(-3, 4), 0, Fraction(1, 4), 0, sp_p)
            tau = BiquadElem(0, 1, 0, 0, sp_p)
            h_gnom = BiquadElem(0, Fraction(11, 8), 0, Fraction(-1, 8), sp_p)
            self.a = self.one
            self.b = self.one
            self.c = phi
            self.A_xy = (self.zero, self.zero)
            self.B_xy = (phi, self.zero)
            self.C_xy = (phi * _HALF, h_gnom)
            self.area = (tau * Fraction(1, 4)) / phi
        else:
            raise KeyError(f"Unknown canonical triangle preset {key!r}")

        # Precompute exact triangle invariants
        self.two_area = self.area * 2
        self.S = self.two_area
        self.Qa = self.a * self.a
        self.Qb = self.b * self.b
        self.Qc = self.c * self.c
        self.SA = (self.Qb + self.Qc - self.Qa) * _HALF
        self.SB = (self.Qc + self.Qa - self.Qb) * _HALF
        self.SC = (self.Qa + self.Qb - self.Qc) * _HALF
        self.SW = (self.Qa + self.Qb + self.Qc) * _HALF
        self.s = (self.a + self.b + self.c) * _HALF
        self.r = self.area / self.s
        self.R = (self.a * self.b * self.c) / (self.area * 4)
        self.Ra = self.area / (self.s - self.a)
        self.Rb = self.area / (self.s - self.b)
        self.Rc = self.area / (self.s - self.c)

        # Exact (cos, sin) pairs for angles A, B, C
        self.cs_A = (self.SA / (self.b * self.c), self.S / (self.b * self.c))
        self.cs_B = (self.SB / (self.c * self.a), self.S / (self.c * self.a))
        self.cs_C = (self.SC / (self.a * self.b), self.S / (self.a * self.b))

        # Exact (cos, sin) for pi/6 and pi/3
        self.cs_pi6 = (self.sqrt3 * _HALF, self.one * _HALF)
        self.cs_pi3 = (self.one * _HALF, self.sqrt3 * _HALF)
        self.cs_pi2 = (self.zero, self.one)

        # Optional exact invariants that may or may not have square roots in K
        self.OH_sq = self.R * self.R * 9 - (self.Qa + self.Qb + self.Qc)
        self.OI_sq = self.R * (self.R - self.r * 2)
        self.OH = self._try_sqrt(self.OH_sq)
        self.OI = self._try_sqrt(self.OI_sq)
        self.J = (self.OH / self.R) if self.OH is not None else None
        self.Q_moses = (
            self.OH_sq * self.R * (self.r * 4 - self.R) * 4
            + (self.OH_sq - self.R * self.R * 3 + self.r * (self.r + self.R) * 4) ** 2
        )
        # Brocard (cos omega, sin omega) if sqrt(S^2 + SW^2) lies in K
        broc_norm_sq = self.S * self.S + self.SW * self.SW
        broc_norm = self._try_sqrt(broc_norm_sq)
        self.cs_omega = (
            (self.SW / broc_norm, self.S / broc_norm) if broc_norm is not None else None
        )
        # Eccentricity e = sqrt(1 - 4*sin^2(omega))
        e_sq = self.one - (self.S * self.S * 4) / broc_norm_sq
        self.ecc = self._try_sqrt(e_sq)
        # Steiner K
        s26 = (
            self.Qa * (self.Qb**3 + self.Qc**3)
            + self.Qb * (self.Qc**3 + self.Qa**3)
            + self.Qc * (self.Qa**3 + self.Qb**3)
        )
        k_sq = (
            self.Qa**4
            + self.Qb**4
            + self.Qc**4
            - s26
            + self.Qa * self.Qb * self.Qc * (self.Qa + self.Qb + self.Qc)
        )
        k_rt = self._try_sqrt(k_sq)
        self.K_steiner = (k_rt * _HALF) if k_rt is not None else None

        # Exact half-angle tangents tan(A/2) = r / (s - a)
        self.tan_half = (
            self.r / (self.s - self.a),
            self.r / (self.s - self.b),
            self.r / (self.s - self.c),
        )

        # Build the 3 cyclic exact variable environments
        self._build_cyclic_envs()

        # Precompute 50-digit mpmath context for non-algebraic fallback
        self._mp_env = self._build_mp_envs(dps=50)

    def _try_sqrt(self, elem: Any) -> Any | None:
        try:
            return elem.sqrt_exact()
        except OutsideFieldError:
            return None

    def _build_cyclic_envs(self) -> None:
        base_common: dict[str, Any] = {
            "pi": AngleLinear(cpi=_F1),
            "omega": AngleLinear(cw=_F1),
            "area": self.area,
            "D": self.area,
            "S": self.S,
            "SW": self.SW,
            "R": self.R,
            "r": self.r,
            "s": self.s,
            "Q": self.Q_moses,
        }
        if self.OH is not None:
            base_common["OH"] = self.OH
            base_common["d"] = self.OH
        if self.OI is not None:
            base_common["OI"] = self.OI
        if self.J is not None:
            base_common["J"] = self.J
        if self.ecc is not None:
            base_common["e"] = self.ecc
        if self.K_steiner is not None:
            base_common["K"] = self.K_steiner

        ang_A = AngleLinear(cA=_F1)
        ang_B = AngleLinear(cB=_F1)
        ang_C = AngleLinear(cC=_F1)

        self.cyclic_envs: tuple[dict[str, Any], dict[str, Any], dict[str, Any]] = (
            {
                **base_common,
                "a": self.a,
                "b": self.b,
                "c": self.c,
                "A": ang_A,
                "B": ang_B,
                "C": ang_C,
                "SA": self.SA,
                "SB": self.SB,
                "SC": self.SC,
                "U": self.SA,
                "V": self.SB,
                "W": self.SC,
                "Ra": self.Ra,
                "Rb": self.Rb,
                "Rc": self.Rc,
            },
            {
                **base_common,
                "a": self.b,
                "b": self.c,
                "c": self.a,
                "A": ang_B,
                "B": ang_C,
                "C": ang_A,
                "SA": self.SB,
                "SB": self.SC,
                "SC": self.SA,
                "U": self.SB,
                "V": self.SC,
                "W": self.SA,
                "Ra": self.Rb,
                "Rb": self.Rc,
                "Rc": self.Ra,
            },
            {
                **base_common,
                "a": self.c,
                "b": self.a,
                "c": self.b,
                "A": ang_C,
                "B": ang_A,
                "C": ang_B,
                "SA": self.SC,
                "SB": self.SA,
                "SC": self.SB,
                "U": self.SC,
                "V": self.SA,
                "W": self.SB,
                "Ra": self.Rc,
                "Rb": self.Ra,
                "Rc": self.Rb,
            },
        )

    def _build_mp_envs(self, dps: int = 50) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
        with mp.workdps(dps):
            a = self.a.to_mpf(dps)
            b = self.b.to_mpf(dps)
            c = self.c.to_mpf(dps)
            area = self.area.to_mpf(dps)
            S = 2 * area
            s = (a + b + c) / 2
            R = (a * b * c) / (4 * area)
            r = area / s
            SA = (b * b + c * c - a * a) / 2
            SB = (c * c + a * a - b * b) / 2
            SC = (a * a + b * b - c * c) / 2
            SW = (a * a + b * b + c * c) / 2
            A = mp.acos(max(mp.mpf(-1), min(mp.mpf(1), SA / (b * c))))
            B = mp.acos(max(mp.mpf(-1), min(mp.mpf(1), SB / (c * a))))
            C = mp.acos(max(mp.mpf(-1), min(mp.mpf(1), SC / (a * b))))
            omega = mp.atan(S / SW)
            ecc = mp.sqrt(max(mp.mpf(0), 1 - 4 * mp.sin(omega) ** 2))
            OH = mp.sqrt(max(mp.mpf(0), 9 * R * R - (a * a + b * b + c * c)))
            OI = mp.sqrt(max(mp.mpf(0), R * (R - 2 * r)))
            Ra, Rb, Rc = area / (s - a), area / (s - b), area / (s - c)
            Q_m = 4 * (OH * OH) * R * (4 * r - R) + (OH * OH - 3 * R * R + 4 * r * (r + R)) ** 2
            s26 = (
                (a * a) * (b**6 + c**6)
                + (b * b) * (c**6 + a**6)
                + (c * c) * (a**6 + b**6)
            )
            K_s = (
                mp.sqrt(
                    max(
                        mp.mpf(0),
                        a**8 + b**8 + c**8 - s26 + (a * a) * (b * b) * (c * c) * (a * a + b * b + c * c),
                    )
                )
                / 2
            )
            common = {
                "sin": mp.sin,
                "cos": mp.cos,
                "tan": mp.tan,
                "cot": mp.cot,
                "sec": mp.sec,
                "csc": mp.csc,
                "sqrt": mp.sqrt,
                "pi": mp.pi,
                "omega": omega,
                "e": ecc,
                "area": area,
                "D": area,
                "R": R,
                "r": r,
                "s": s,
                "S": S,
                "SW": SW,
                "OH": OH,
                "OI": OI,
                "d": OH,
                "J": OH / R,
                "Q": Q_m,
                "K": K_s,
            }
            return (
                {**common, "a": a, "b": b, "c": c, "A": A, "B": B, "C": C, "Ra": Ra, "Rb": Rb, "Rc": Rc, "SA": SA, "SB": SB, "SC": SC, "U": SA, "V": SB, "W": SC},
                {**common, "a": b, "b": c, "c": a, "A": B, "B": C, "C": A, "Ra": Rb, "Rb": Rc, "Rc": Ra, "SA": SB, "SB": SC, "SC": SA, "U": SB, "V": SC, "W": SA},
                {**common, "a": c, "b": a, "c": b, "A": C, "B": A, "C": B, "Ra": Rc, "Rb": Ra, "Rc": Rb, "SA": SC, "SB": SA, "SC": SB, "U": SC, "V": SA, "W": SB},
            )

    def _eval_angle_cs(self, ang: AngleLinear) -> tuple[Any, Any]:
        """Compute exact ``(cos(ang), sin(ang))`` inside the triangle's field (or ExtSqrt3)."""
        if not isinstance(ang, AngleLinear):
            raise OutsideFieldError("Trig argument is not a linear combination of angles")

        # Handle single pure half-angle A/2, B/2, C/2 directly if exact square exists
        if ang.cw == 0 and ang.cpi == 0:
            nonzeros = [
                (idx, c)
                for idx, c in enumerate((ang.cA, ang.cB, ang.cC))
                if c != 0
            ]
            if len(nonzeros) == 1 and abs(nonzeros[0][1]) == _HALF:
                idx, coef = nonzeros[0]
                cos_base = (self.cs_A[0], self.cs_B[0], self.cs_C[0])[idx]
                c_half = ((self.one + cos_base) * _HALF).sqrt_exact()
                s_half = ((self.one - cos_base) * _HALF).sqrt_exact()
                return (c_half, s_half if coef > 0 else -s_half)

        # Require integer multiples of A, B, C, omega and multiples of pi/6
        if (
            ang.cA.denominator != 1
            or ang.cB.denominator != 1
            or ang.cC.denominator != 1
            or ang.cw.denominator != 1
        ):
            raise OutsideFieldError(f"Non-integer angle multiple {ang}")

        nA, nB, nC, nw = int(ang.cA), int(ang.cB), int(ang.cC), int(ang.cw)
        if nw != 0 and self.cs_omega is None:
            raise OutsideFieldError("Linear sin/cos(omega) leaves base field")

        # Reduce cpi modulo 2 into multiples of 1/6 (pi/6 = 30 deg)
        cpi_mod = ang.cpi % 2
        if (cpi_mod * 6).denominator != 1:
            raise OutsideFieldError(f"Non-(pi/6) rational angle {ang.cpi}*pi")
        n_pi6 = int(cpi_mod * 6)

        res = (self.one, self.zero)
        if nA:
            res = _cs_mul(res, _cs_pow(self.cs_A, nA, self.one, self.zero))
        if nB:
            res = _cs_mul(res, _cs_pow(self.cs_B, nB, self.one, self.zero))
        if nC:
            res = _cs_mul(res, _cs_pow(self.cs_C, nC, self.one, self.zero))
        if nw and self.cs_omega is not None:
            res = _cs_mul(res, _cs_pow(self.cs_omega, nw, self.one, self.zero))
        if n_pi6:
            res = _cs_mul(res, _cs_pow(self.cs_pi6, n_pi6, self.one, self.zero))
        return res

    def _eval_trig(self, fn: str, arg: Any) -> Any:
        if not isinstance(arg, AngleLinear):
            raise OutsideFieldError(f"{fn}({arg!r}) not an AngleLinear")

        # Fast exact paths for tan/cot of omega and half-angles A/2, B/2, C/2 (always in K!)
        if fn in {"tan", "cot"}:
            if arg.cA == 0 and arg.cB == 0 and arg.cC == 0 and arg.cpi == 0 and abs(arg.cw) == 1:
                t_val = (self.S / self.SW) * (1 if arg.cw > 0 else -1)
                return t_val if fn == "tan" else (self.one / t_val)
            if arg.cw == 0 and arg.cpi == 0:
                nz = [(i, c) for i, c in enumerate((arg.cA, arg.cB, arg.cC)) if c != 0]
                if len(nz) == 1 and abs(nz[0][1]) == _HALF:
                    idx, coef = nz[0]
                    t_val = self.tan_half[idx] if coef > 0 else -self.tan_half[idx]
                    return t_val if fn == "tan" else (self.one / t_val)

        c_val, s_val = self._eval_angle_cs(arg)
        if fn == "sin":
            return s_val
        if fn == "cos":
            return c_val
        if fn == "tan":
            return s_val / c_val
        if fn == "cot":
            return c_val / s_val
        if fn == "sec":
            return self.one / c_val
        if fn == "csc":
            return self.one / s_val
        raise OutsideFieldError(f"Unknown trig function {fn}")

    def _eval_ast_node(self, node: ast.AST, env: dict[str, Any]) -> Any:
        if isinstance(node, ast.Expression):
            return self._eval_ast_node(node.body, env)
        if isinstance(node, ast.Constant):
            val = node.value
            if isinstance(val, int):
                return self.zero + val
            if isinstance(val, float):
                # Only exact decimal literals like 0.5 -> Fraction
                return self.zero + Fraction(str(val))
            raise OutsideFieldError(f"Unsupported constant {val!r}")
        if isinstance(node, ast.Name):
            if node.id not in env:
                raise OutsideFieldError(f"Unknown symbol {node.id!r}")
            return env[node.id]
        if isinstance(node, ast.UnaryOp):
            operand = self._eval_ast_node(node.operand, env)
            if isinstance(node.op, ast.USub):
                return -operand
            if isinstance(node.op, ast.UAdd):
                return +operand
            raise OutsideFieldError(f"Unsupported unary op {type(node.op).__name__}")
        if isinstance(node, ast.BinOp):
            # Special optimization: sin(A/2)**2, cos(A/2)**2, sin(omega)**2, cos(omega)**2
            if isinstance(node.op, ast.Pow):
                right = self._eval_ast_node(node.right, env)
                exp_int = self._as_exact_int(right)
                if (
                    exp_int is not None
                    and exp_int % 2 == 0
                    and isinstance(node.left, ast.Call)
                    and isinstance(node.left.func, ast.Name)
                    and len(node.left.args) == 1
                ):
                    fn_name = node.left.func.id
                    if fn_name in {"sin", "cos", "sec", "csc"}:
                        arg_val = self._eval_ast_node(node.left.args[0], env)
                        sq_val = self._try_even_trig_square(fn_name, arg_val)
                        if sq_val is not None:
                            return sq_val ** (exp_int // 2)
                left = self._eval_ast_node(node.left, env)
                res = left**right
                if hasattr(res, "max_digits") and res.max_digits() > 500:
                    raise OutsideFieldError("Intermediate result exceeded 500-digit exact cap")
                return res
            left = self._eval_ast_node(node.left, env)
            right = self._eval_ast_node(node.right, env)
            if isinstance(node.op, ast.Add):
                res = left + right
            elif isinstance(node.op, ast.Sub):
                res = left - right
            elif isinstance(node.op, ast.Mult):
                res = left * right
            elif isinstance(node.op, ast.Div):
                res = left / right
            else:
                raise OutsideFieldError(f"Unsupported binary op {type(node.op).__name__}")
            if self._eval_deadline > 0.0:
                self._eval_ops += 1
                if (self._eval_ops & 31) == 0 and time.monotonic() > self._eval_deadline:
                    raise OutsideFieldError("Per-center exact evaluation deadline exceeded")
            if hasattr(res, "max_digits") and res.max_digits() > 500:
                raise OutsideFieldError("Intermediate result exceeded 500-digit exact cap")
            return res
        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name) or len(node.args) != 1:
                raise OutsideFieldError("Unsupported function call")
            fn_name = node.func.id
            arg_val = self._eval_ast_node(node.args[0], env)
            if fn_name == "sqrt":
                return arg_val.sqrt_exact()
            if fn_name in {"sin", "cos", "tan", "cot", "sec", "csc"}:
                return self._eval_trig(fn_name, arg_val)
            raise OutsideFieldError(f"Unsupported function {fn_name}")
        raise OutsideFieldError(f"Unsupported AST node {type(node).__name__}")

    def _as_exact_int(self, val: Any) -> int | None:
        if isinstance(val, int):
            return val
        if isinstance(val, (QElem, QuadElem, BiquadElem, ExtSqrt3Elem)):
            rc = val.rat_coeffs()
            if all(c == 0 for c in rc[1:]) and rc[0].denominator == 1:
                return int(rc[0].numerator)
        return None

    def _try_even_trig_square(self, fn_name: str, arg: Any) -> Any | None:
        """Evaluate exact ``sin^2`` / ``cos^2`` for half-angles ``A/2`` and Brocard ``omega``."""
        if not isinstance(arg, AngleLinear):
            return None
        # omega
        if arg.cA == 0 and arg.cB == 0 and arg.cC == 0 and arg.cpi == 0 and abs(arg.cw) == 1:
            denom = self.S * self.S + self.SW * self.SW
            if fn_name == "sin":
                return (self.S * self.S) / denom
            if fn_name == "cos":
                return (self.SW * self.SW) / denom
            if fn_name == "csc":
                return denom / (self.S * self.S)
            if fn_name == "sec":
                return denom / (self.SW * self.SW)
        # Half-angle A/2, B/2, C/2
        if arg.cw == 0 and arg.cpi == 0:
            nz = [(i, c) for i, c in enumerate((arg.cA, arg.cB, arg.cC)) if c != 0]
            if len(nz) == 1 and abs(nz[0][1]) == _HALF:
                idx = nz[0][0]
                cos_b = (self.cs_A[0], self.cs_B[0], self.cs_C[0])[idx]
                if fn_name == "cos":
                    return (self.one + cos_b) * _HALF
                if fn_name == "sin":
                    return (self.one - cos_b) * _HALF
                if fn_name == "sec":
                    return self.one / ((self.one + cos_b) * _HALF)
                if fn_name == "csc":
                    return self.one / ((self.one - cos_b) * _HALF)
        return None

    @staticmethod
    @functools.cache
    def _parse_ast(expr_str: str) -> ast.Expression:
        return ast.parse(expr_str, mode="eval")

    def eval_cyclic_exact(
        self,
        expr_str: str,
        *,
        is_trilinear: bool = False,
        xyz: tuple[Any, Any, Any] | None = None,
        uvw: tuple[Any, Any, Any] | None = None,
        timeout_sec: float = 0.15,
    ) -> tuple[Any, Any, Any]:
        """Evaluate a cyclic Python expression exactly in this triangle's field."""
        tree = self._parse_ast(expr_str)
        xyz_rots: tuple[dict[str, Any], dict[str, Any], dict[str, Any]] | None = None
        if xyz is not None or uvw is not None:
            tx, ty, tz = xyz if xyz is not None else uvw  # type: ignore[misc]
            tu, tv, tw = uvw if uvw is not None else xyz  # type: ignore[misc]
            xyz_rots = (
                {"x": tx, "y": ty, "z": tz, "u": tu, "v": tv, "w": tw},
                {"x": ty, "y": tz, "z": tx, "u": tv, "v": tw, "w": tu},
                {"x": tz, "y": tx, "z": ty, "u": tw, "v": tu, "w": tv},
            )
        self._eval_ops = 0
        self._eval_deadline = (time.monotonic() + timeout_sec) if timeout_sec > 0 else 0.0
        try:
            vals: list[Any] = []
            for idx in range(3):
                env = {**self.cyclic_envs[idx], **xyz_rots[idx]} if xyz_rots else self.cyclic_envs[idx]
                val = self._eval_ast_node(tree, env)
                if isinstance(val, AngleLinear):
                    raise OutsideFieldError("Expression evaluated to bare AngleLinear")
                vals.append(val)
        finally:
            self._eval_deadline = 0.0
        c1, c2, c3 = vals[0], vals[1], vals[2]
        if is_trilinear:
            c1, c2, c3 = self.a * c1, self.b * c2, self.c * c3
        return _reduce_exact_triple((c1, c2, c3))

    def eval_cyclic_mpmath(
        self,
        expr_str: str,
        *,
        is_trilinear: bool = False,
        xyz: tuple[mp.mpf, mp.mpf, mp.mpf] | None = None,
        uvw: tuple[mp.mpf, mp.mpf, mp.mpf] | None = None,
        dps: int = 50,
    ) -> tuple[mp.mpf, mp.mpf, mp.mpf] | None:
        """50-digit ``mpmath`` fallback for transcendental or non-field formulas."""
        try:
            code = compile(expr_str, "<mp-coord>", "eval")
        except (SyntaxError, ValueError, TypeError):
            return None
        xyz_rots = None
        if xyz is not None or uvw is not None:
            tx, ty, tz = xyz if xyz is not None else uvw  # type: ignore[misc]
            tu, tv, tw = uvw if uvw is not None else xyz  # type: ignore[misc]
            xyz_rots = (
                {"x": tx, "y": ty, "z": tz, "u": tu, "v": tv, "w": tw},
                {"x": ty, "y": tz, "z": tx, "u": tv, "v": tw, "w": tu},
                {"x": tz, "y": tx, "z": ty, "u": tw, "v": tu, "w": tv},
            )
        with mp.workdps(dps):
            out: list[mp.mpf] = []
            try:
                for idx in range(3):
                    env = {**self._mp_env[idx], **xyz_rots[idx]} if xyz_rots else self._mp_env[idx]
                    v = eval(code, {"__builtins__": {}}, env)
                    if isinstance(v, mp.mpc):
                        if abs(v.imag) > mp.mpf("1e-25"):
                            return None
                        v = v.real
                    mv = mp.mpf(v)
                    if not mp.isfinite(mv) or not isinstance(mv._mpf_[2], int) or abs(mv._mpf_[2]) > 4000:
                        return None
                    out.append(mv)
            except (
                ArithmeticError,
                ValueError,
                TypeError,
                KeyError,
                NameError,
                OverflowError,
                AttributeError,
                RecursionError,
            ):
                return None
            c1, c2, c3 = out[0], out[1], out[2]
            if is_trilinear:
                c1 *= self._mp_env[0]["a"]
                c2 *= self._mp_env[0]["b"]
                c3 *= self._mp_env[0]["c"]
            max_abs = max(abs(c1), abs(c2), abs(c3))
            if max_abs == 0:
                return (mp.mpf(0), mp.mpf(0), mp.mpf(0))
            return (c1 / max_abs, c2 / max_abs, c3 / max_abs)

    @staticmethod
    @functools.cache
    def _builtin_expr_str(num: int) -> str:
        fn = EXACT_CYCLIC_BARYCENTRICS[num]
        a_s, b_s, c_s, sa_s, sb_s, sc_s, s_s = sp.symbols("a b c SA SB SC S")
        return str(fn(a_s, b_s, c_s, sa_s, sb_s, sc_s, s_s))

    def eval_builtin_exact(self, num: int) -> tuple[Any, Any, Any]:
        """Evaluate a built-in ``EXACT_CYCLIC_BARYCENTRICS`` center directly in this field."""
        return self.eval_cyclic_exact(self._builtin_expr_str(num), is_trilinear=False)

    def package_exact_bary(self, bary_raw: tuple[Any, Any, Any]) -> ExactEvalResult:
        """Package an exact homogeneous barycentric triple into a full ``ExactEvalResult``."""
        bary = _reduce_exact_triple(bary_raw)
        u, v, w = bary
        has_sqrt3_ext = any(isinstance(x, ExtSqrt3Elem) and not x.c1.is_zero() for x in bary)
        field_tag = (
            (self.field_latex + r"(\sqrt{3})") if has_sqrt3_ext else self.field_latex
        )

        if u.is_zero() and v.is_zero() and w.is_zero():
            note = (
                "Indeterminate (0 : 0 : 0) under equilateral D₃ symmetry"
                if self.is_equilateral
                else "Indeterminate homogeneous triple (0 : 0 : 0)"
            )
            return ExactEvalResult(
                triangle_key=self.key,
                precision="exact",
                bary=bary,
                trilinear=bary,
                xy=(self.zero, self.zero),
                search_value=self.zero,
                approx_xy=(math.nan, math.nan),
                approx_bary=(0.0, 0.0, 0.0),
                approx_search=math.nan,
                is_indeterminate=True,
                symmetry_note=note,
                field_tag=field_tag,
                bary_latex="0 : 0 : 0",
                trilinear_latex="0 : 0 : 0",
                xy_latex=r"\text{indeterminate } (0:0:0)",
                search_latex=r"\text{indeterminate}",
            )

        trilin = _reduce_exact_triple((u / self.a, v / self.b, w / self.c))
        total = u + v + w
        if total.is_zero():
            # Ideal point on the line at infinity (normalize in 50-digit mpmath to avoid float overflow)
            with mp.workdps(50):
                mu, mv, mw = u.to_mpf(50), v.to_mpf(50), w.to_mpf(50)
                bn = mp.sqrt(mu * mu + mv * mv + mw * mw)
                if bn == 0 or not mp.isfinite(bn):
                    approx_b = (0.0, 0.0, 0.0)
                else:
                    approx_b = (
                        _safe_mpf_to_float(mu / bn),
                        _safe_mpf_to_float(mv / bn),
                        _safe_mpf_to_float(mw / bn),
                    )
            return ExactEvalResult(
                triangle_key=self.key,
                precision="exact",
                bary=bary,
                trilinear=trilin,
                xy=None,
                search_value=None,
                approx_xy=(math.nan, math.nan),
                approx_bary=approx_b,
                approx_search=math.nan,
                is_ideal=True,
                symmetry_note="Ideal point on the line at infinity (u + v + w = 0)",
                field_tag=field_tag,
                bary_latex=_format_triple_latex(bary),
                trilinear_latex=_format_triple_latex(trilin),
                xy_latex=r"\infty \;\text{(line at infinity)}",
                search_latex=r"\infty",
            )

        un, vn, wn = u / total, v / total, w / total
        px = un * self.A_xy[0] + vn * self.B_xy[0] + wn * self.C_xy[0]
        py = un * self.A_xy[1] + vn * self.B_xy[1] + wn * self.C_xy[1]
        search_val = (self.two_area * un) / self.a

        sym_note = ""
        if self.is_equilateral:
            sym_note = "Coalesces to symmetry center O under equilateral D₃ symmetry"
        elif self.is_isosceles and (u - v).is_zero():
            sym_note = "Lies on the vertical axis of symmetry"

        return ExactEvalResult(
            triangle_key=self.key,
            precision="exact",
            bary=bary,
            trilinear=trilin,
            xy=(px, py),
            search_value=search_val,
            approx_xy=(px.to_float(), py.to_float()),
            approx_bary=(un.to_float(), vn.to_float(), wn.to_float()),
            approx_search=search_val.to_float(),
            symmetry_note=sym_note,
            field_tag=field_tag,
            bary_latex=_format_triple_latex(bary),
            trilinear_latex=_format_triple_latex(trilin),
            xy_latex=_format_xy_latex(px, py),
            search_latex=_format_scalar_latex(search_val),
        )

    def package_mpmath_bary(
        self, bary_mp: tuple[mp.mpf, mp.mpf, mp.mpf], dps: int = 50
    ) -> ExactEvalResult:
        """Package a 50-digit ``mpmath`` fallback barycentric triple."""
        with mp.workdps(dps):
            u, v, w = bary_mp
            norm = mp.sqrt(u * u + v * v + w * w)
            if norm < mp.mpf("1e-35"):
                return ExactEvalResult(
                    triangle_key=self.key,
                    precision="mpmath-50",
                    bary=None,
                    trilinear=None,
                    xy=None,
                    search_value=None,
                    approx_xy=(math.nan, math.nan),
                    approx_bary=(0.0, 0.0, 0.0),
                    approx_search=math.nan,
                    is_indeterminate=True,
                    symmetry_note="Indeterminate (0 : 0 : 0)",
                    field_tag=r"\mathbb{R}_{50}",
                )
            tot = u + v + w
            if abs(tot) < norm * mp.mpf("1e-20"):
                return ExactEvalResult(
                    triangle_key=self.key,
                    precision="mpmath-50",
                    bary=None,
                    trilinear=None,
                    xy=None,
                    search_value=None,
                    approx_xy=(math.nan, math.nan),
                    approx_bary=(
                        _safe_mpf_to_float(u / norm),
                        _safe_mpf_to_float(v / norm),
                        _safe_mpf_to_float(w / norm),
                    ),
                    approx_search=math.nan,
                    is_ideal=True,
                    symmetry_note="Ideal point on the line at infinity (u + v + w = 0)",
                    field_tag=r"\mathbb{R}_{50}",
                    xy_latex=r"\infty \;\text{(line at infinity)}",
                    search_latex=r"\infty",
                )
            un, vn, wn = u / tot, v / tot, w / tot
            Ax, Ay = self.A_xy[0].to_mpf(dps), self.A_xy[1].to_mpf(dps)
            Bx, By = self.B_xy[0].to_mpf(dps), self.B_xy[1].to_mpf(dps)
            Cx, Cy = self.C_xy[0].to_mpf(dps), self.C_xy[1].to_mpf(dps)
            px = un * Ax + vn * Bx + wn * Cx
            py = un * Ay + vn * By + wn * Cy
            a_m = self.a.to_mpf(dps)
            b_m = self.b.to_mpf(dps)
            c_m = self.c.to_mpf(dps)
            s_val = (self.two_area.to_mpf(dps) * un) / a_m
            t1, t2, t3 = un / a_m, vn / b_m, wn / c_m
            tn = max(abs(t1), abs(t2), abs(t3)) or mp.mpf(1)
            px_f, py_f = _safe_mpf_to_float(px), _safe_mpf_to_float(py)
            un_f, vn_f, wn_f = (
                _safe_mpf_to_float(un),
                _safe_mpf_to_float(vn),
                _safe_mpf_to_float(wn),
            )
            sv_f = _safe_mpf_to_float(s_val)
            t1_f, t2_f, t3_f = (
                _safe_mpf_to_float(t1 / tn),
                _safe_mpf_to_float(t2 / tn),
                _safe_mpf_to_float(t3 / tn),
            )
            return ExactEvalResult(
                triangle_key=self.key,
                precision="mpmath-50",
                bary=None,
                trilinear=None,
                xy=None,
                search_value=None,
                approx_xy=(px_f, py_f),
                approx_bary=(un_f, vn_f, wn_f),
                approx_search=sv_f,
                field_tag=r"\mathbb{R}_{50}",
                bary_latex=f"{un_f:.6g} : {vn_f:.6g} : {wn_f:.6g}",
                trilinear_latex=f"{t1_f:.6g} : {t2_f:.6g} : {t3_f:.6g}",
                xy_latex=rf"\approx \left({px_f:.8f},\; {py_f:.8f}\right)",
                search_latex=rf"\approx {sv_f:.12f}",
            )


def _format_scalar_latex(elem: Any, max_digits: int = 18) -> str:
    if elem.max_digits() <= max_digits:
        return elem.to_latex()
    return rf"\approx {elem.to_float():.10g}"


def _format_triple_latex(triple: tuple[Any, Any, Any], max_digits: int = 18) -> str:
    if max(x.max_digits() for x in triple) <= max_digits:
        return " : ".join(x.to_latex() for x in triple)
    # Compact normalized numeric display via 50-digit mpmath (overflow- & cancellation-safe)
    with mp.workdps(50):
        mps = [x.to_mpf(50) for x in triple]
        scale = max(abs(v) for v in mps)
        if scale == 0 or not mp.isfinite(scale):
            return "0 : 0 : 0"
        flts = [_safe_mpf_to_float(v / scale) for v in mps]
    return " : ".join(f"{v:.6g}" for v in flts)


def _format_xy_latex(px: Any, py: Any, max_digits: int = 18) -> str:
    if max(px.max_digits(), py.max_digits()) <= max_digits:
        return rf"\left({px.to_latex()},\; {py.to_latex()}\right)"
    return rf"\approx \left({px.to_float():.8f},\; {py.to_float():.8f}\right)"


# ---------------------------------------------------------------------------
# Exact Algebraic Relation Propagator & Corpus Resolver
# ---------------------------------------------------------------------------


_CANONICAL_TRIANGLE_ORDER: tuple[str, ...] = (
    "heronian",
    "right",
    "kepler",
    "kimberling",
    "golden",
    "gnomon",
    "equilateral",
)

_FIELD_CACHE: dict[str, ExactTriangleField] = {}


def get_triangle_field(key: str) -> ExactTriangleField:
    """Return the cached :class:`ExactTriangleField` for preset ``key``."""
    if key not in _FIELD_CACHE:
        _FIELD_CACHE[key] = ExactTriangleField(key)
    return _FIELD_CACHE[key]


def _extract_published_search_value(cdata: dict[str, Any]) -> float | None:
    """Extract Clark Kimberling's published 6-9-13 search number from parsed center data."""
    sv = cdata.get("search_value")
    if isinstance(sv, (int, float)) and math.isfinite(sv):
        return float(sv)
    if isinstance(sv, str):
        m = re.search(r"([+-]?\d+\.\d{4,})", sv)
        if m:
            try:
                return float(m.group(1))
            except ValueError:
                pass
    # Also scan trilinears / notes for "Barycentrics" / "6, 9, 13" or search number patterns
    for fld in ("trilinears", "notes"):
        for item in cdata.get(fld) or []:
            if not isinstance(item, str):
                continue
            m = re.search(r"6,\s*9,\s*13[^0-9+-]*([+-]?\d+\.\d{5,})", item)
            if m:
                try:
                    return float(m.group(1))
                except ValueError:
                    pass
    return None


def _exact_bary_line(
    p1: tuple[Any, Any, Any], p2: tuple[Any, Any, Any]
) -> tuple[Any, Any, Any]:
    return (
        p1[1] * p2[2] - p1[2] * p2[1],
        p1[2] * p2[0] - p1[0] * p2[2],
        p1[0] * p2[1] - p1[1] * p2[0],
    )


def _exact_triple_nonzero(t: tuple[Any, Any, Any]) -> bool:
    return not (t[0].is_zero() and t[1].is_zero() and t[2].is_zero())


def _is_huge_triple(t: tuple[Any, Any, Any], digit_cap: int = 1200) -> bool:
    """Guard against pathological integer-growth chains in exact propagation."""
    return max(x.max_digits() for x in t) > digit_cap


class ExactCorpusResolver:
    """Resolves a batch of parsed ETC centers across one canonical triangle field.

    Uses exact field arithmetic first (built-ins -> direct formulas -> exact
    algebraic relations -> exact incidence intersections) and falls back cleanly
    to 50-digit ``mpmath`` only when an expression leaves ``K(sqrt(3))``.
    """

    def __init__(
        self,
        centers_by_num: dict[int, dict[str, Any]],
        triangle_key: str,
        *,
        seed_exact: dict[int, tuple[Any, Any, Any]] | None = None,
    ) -> None:
        self.field = get_triangle_field(triangle_key)
        self.centers_by_num = centers_by_num
        self.exact_bary: dict[int, tuple[Any, Any, Any]] = {}
        self.mp_bary: dict[int, tuple[mp.mpf, mp.mpf, mp.mpf]] = {}
        self.zero_div_poles: set[int] = set()
        self.results: dict[int, ExactEvalResult] = {}

        if seed_exact:
            self.exact_bary.update(seed_exact)
        self._seed_builtins()

    def _seed_builtins(self) -> None:
        for num in sorted(EXACT_CYCLIC_BARYCENTRICS):
            if num in self.exact_bary:
                continue
            try:
                bary = self.field.eval_builtin_exact(num)
                self.exact_bary[num] = bary
            except (OutsideFieldError, ZeroDivisionError):
                pass

    def _extract_xyz_uvw_exact(
        self, line: str
    ) -> tuple[
        tuple[Any, Any, Any] | None,
        tuple[Any, Any, Any] | None,
        bool,
    ]:
        mx = re.search(
            r"(?:x\s*:\s*y\s*:\s*z`?\s*=\s*(?::ref:`[^`]*<X_(\d+)>`|X(?:_|\()(\d+))|\b[xyz]\(\s*(\d+)\s*\))",
            line,
            flags=re.IGNORECASE,
        )
        mu = re.search(
            r"u\s*:\s*v\s*:\s*w`?\s*=\s*(?::ref:`[^`]*<X_(\d+)>`|X(?:_|\()(\d+))",
            line,
            flags=re.IGNORECASE,
        )
        xyz = None
        uvw = None
        f = self.field
        if mx:
            kx = int(mx.group(1) or mx.group(2) or mx.group(3))
            if kx not in self.exact_bary:
                return (None, None, False)
            ux, vx, wx = self.exact_bary[kx]
            xyz = (ux / f.a, vx / f.b, wx / f.c)
        if mu:
            ku = int(mu.group(1) or mu.group(2))
            if ku not in self.exact_bary:
                return (None, None, False)
            uu, vu, wu = self.exact_bary[ku]
            uvw = (uu / f.a, vu / f.b, wu / f.c)
        return (xyz, uvw, True)

    def _extract_xyz_uvw_mp(
        self, line: str, dps: int = 50
    ) -> tuple[
        tuple[mp.mpf, mp.mpf, mp.mpf] | None,
        tuple[mp.mpf, mp.mpf, mp.mpf] | None,
        bool,
    ]:
        mx = re.search(
            r"(?:x\s*:\s*y\s*:\s*z`?\s*=\s*(?::ref:`[^`]*<X_(\d+)>`|X(?:_|\()(\d+))|\b[xyz]\(\s*(\d+)\s*\))",
            line,
            flags=re.IGNORECASE,
        )
        mu = re.search(
            r"u\s*:\s*v\s*:\s*w`?\s*=\s*(?::ref:`[^`]*<X_(\d+)>`|X(?:_|\()(\d+))",
            line,
            flags=re.IGNORECASE,
        )
        xyz = None
        uvw = None
        a_m, b_m, c_m = self.field._mp_env[0]["a"], self.field._mp_env[0]["b"], self.field._mp_env[0]["c"]

        def _get_mp(k: int) -> tuple[mp.mpf, mp.mpf, mp.mpf] | None:
            if k in self.exact_bary:
                eb = self.exact_bary[k]
                if _exact_triple_nonzero(eb):
                    return (eb[0].to_mpf(dps), eb[1].to_mpf(dps), eb[2].to_mpf(dps))
            return self.mp_bary.get(k)

        if mx:
            kx = int(mx.group(1) or mx.group(2) or mx.group(3))
            b = _get_mp(kx)
            if b is None:
                return (None, None, False)
            xyz = (b[0] / a_m, b[1] / b_m, b[2] / c_m)
        if mu:
            ku = int(mu.group(1) or mu.group(2))
            b = _get_mp(ku)
            if b is None:
                return (None, None, False)
            uvw = (b[0] / a_m, b[1] / b_m, b[2] / c_m)
        return (xyz, uvw, True)

    def _try_exact_coordinates(self, cdata: dict[str, Any]) -> tuple[Any, Any, Any] | None:
        num = int(cdata.get("num") or 0)
        had_zero_div = False
        candidates: list[tuple[int, int, tuple[Any, Any, Any]]] = []
        for fld, is_tril in (("barycentrics", False), ("trilinears", True)):
            for raw_line in cdata.get(fld) or []:
                expr = _prepare_formula_expr(raw_line)
                if not expr:
                    continue
                xyz, uvw, ready = self._extract_xyz_uvw_exact(raw_line)
                if not ready:
                    continue
                try:
                    bary = self.field.eval_cyclic_exact(
                        expr, is_trilinear=is_tril, xyz=xyz, uvw=uvw
                    )
                    if not _is_huge_triple(bary):
                        if _exact_triple_nonzero(bary):
                            sc, checked = self._score_exact_collinearity_pair(cdata, bary)
                            if checked == 0 or sc >= 1:
                                return bary
                            candidates.append((sc, checked, bary))
                        else:
                            had_zero_div = True
                except ZeroDivisionError:
                    had_zero_div = True
                except (OutsideFieldError, SyntaxError, ValueError, TypeError):
                    continue

        if candidates:
            candidates.sort(key=lambda item: item[0], reverse=True)
            best_sc, checked, best = candidates[0]
            # Self-heal formula typos/ambiguities if >= 2 known exact lines exist and formula hits 0
            if checked >= 2 and best_sc == 0:
                for alt in (self._try_exact_relations(cdata), self._try_exact_incidence(cdata)):
                    if alt is not None:
                        alt_sc, _ = self._score_exact_collinearity_pair(cdata, alt)
                        if alt_sc >= 2:
                            return alt
            return best

        if had_zero_div and num > 0:
            self.zero_div_poles.add(num)
        return None

    def _try_exact_relations(self, cdata: dict[str, Any]) -> tuple[Any, Any, Any] | None:
        """Exact algebraic relation evaluation in the triangle's number field."""
        f = self.field
        a, b, c = f.a, f.b, f.c
        title_s = re.sub(r"\bX_(\d+)", r"X(\1)", (cdata.get("title") or "").strip())

        def _get(k: int) -> tuple[Any, Any, Any] | None:
            t = self.exact_bary.get(k)
            if t is None or not _exact_triple_nonzero(t):
                return None
            return t

        # Title-based exact algebraic transforms
        m_sar = re.match(
            r"^(1st|2nd|3rd)\s+SARAGOSSA\s+POINT\s+OF\s+X\((\d+)\)$", title_s, re.IGNORECASE
        )
        if m_sar:
            which = m_sar.group(1).lower()
            pt = _get(int(m_sar.group(2)))
            if pt is not None:
                u, v, w = pt
                tx, ty, tz = u / a, v / b, w / c
                try:
                    if which == "1st":
                        return _reduce_exact_triple(
                            (
                                f.Qa / (tx * (b * tz + c * ty)),
                                f.Qb / (ty * (c * tx + a * tz)),
                                f.Qc / (tz * (a * ty + b * tx)),
                            )
                        )
                    if which == "2nd":
                        return _reduce_exact_triple(
                            (
                                f.Qa * tx * ((f.Qb * tz * tz + f.Qc * ty * ty) * tx + tx * ty * tz * b * c + a * ty * tz * (b * tz + c * ty)),
                                f.Qb * ty * ((f.Qc * tx * tx + f.Qa * tz * tz) * ty + ty * tz * tx * c * a + b * tz * tx * (c * tx + a * tz)),
                                f.Qc * tz * ((f.Qa * ty * ty + f.Qb * tx * tx) * tz + tz * tx * ty * a * b + c * tx * ty * (a * ty + b * tx)),
                            )
                        )
                    return _reduce_exact_triple(
                        (
                            f.Qa * tx * ((f.Qb * tz * tz + f.Qc * ty * ty) * tx + a * ty * tz * (b * tz + c * ty)),
                            f.Qb * ty * ((f.Qc * tx * tx + f.Qa * tz * tz) * ty + b * tz * tx * (c * tx + a * tz)),
                            f.Qc * tz * ((f.Qa * ty * ty + f.Qb * tx * tx) * tz + c * tx * ty * (a * ty + b * tx)),
                        )
                    )
                except ZeroDivisionError:
                    pass

        m_col = re.match(r"^COLLINGS\s+TRANSFORM\s+OF\s+X\((\d+)\)$", title_s, re.IGNORECASE)
        if m_col:
            pt = _get(int(m_col.group(1)))
            if pt is not None:
                u, v, w = pt
                tx, ty, tz = u / a, v / b, w / c
                try:
                    return _reduce_exact_triple(
                        (
                            a / (b * tz * (u + v - w) - c * ty * (u + w - v)),
                            b / (c * tx * (v + w - u) - a * tz * (v + u - w)),
                            c / (a * ty * (w + u - v) - b * tx * (w + v - u)),
                        )
                    )
                except ZeroDivisionError:
                    pass

        m_bri = re.match(r"^BRISSE\s+TRANSFORM\s+OF\s+X\((\d+)\)$", title_s, re.IGNORECASE)
        if m_bri:
            pt = _get(int(m_bri.group(1)))
            if pt is not None:
                u, v, w = pt
                try:
                    return _reduce_exact_triple(
                        (
                            (f.Qa * f.Qa) / ((b + c - a) * u * u),
                            (f.Qb * f.Qb) / ((c + a - b) * v * v),
                            (f.Qc * f.Qc) / ((a + b - c) * w * w),
                        )
                    )
                except ZeroDivisionError:
                    pass

        m_tcc = re.match(r"^TCC-PERSPECTOR\s+OF\s+X\((\d+)\)$", title_s, re.IGNORECASE)
        if m_tcc:
            pt = _get(int(m_tcc.group(1)))
            if pt is not None:
                u, v, w = pt
                try:
                    qa, qb, qc = (f.Qa * f.Qa) / (u * u), (f.Qb * f.Qb) / (v * v), (f.Qc * f.Qc) / (w * w)
                    return _reduce_exact_triple(
                        (f.Qa * (qb + qc - qa), f.Qb * (qc + qa - qb), f.Qc * (qa + qb - qc))
                    )
                except ZeroDivisionError:
                    pass

        m_dc = re.match(r"^(DC|CD)\(\s*X\((\d+)\)\s*\)$", title_s, re.IGNORECASE)
        if m_dc:
            kind = m_dc.group(1).upper()
            pt = _get(int(m_dc.group(2)))
            if pt is not None:
                u, v, w = pt
                tx, ty, tz = u / a, v / b, w / c
                try:
                    if kind == "DC":
                        return _reduce_exact_triple(
                            (
                                a * ty * tz / (b * ty + c * tz),
                                b * tz * tx / (c * tz + a * tx),
                                c * tx * ty / (a * tx + b * ty),
                            )
                        )
                    abc = a * b * c
                    return _reduce_exact_triple(
                        (
                            abc / (-a / tx + b / ty + c / tz),
                            abc / (a / tx - b / ty + c / tz),
                            abc / (a / tx + b / ty - c / tz),
                        )
                    )
                except ZeroDivisionError:
                    pass

        m_iso = re.match(r"^X\((\d+)\)-ISOCONJUGATE\s+OF\s+X\((\d+)\)$", title_s, re.IGNORECASE)
        if m_iso:
            p1, p2 = _get(int(m_iso.group(1))), _get(int(m_iso.group(2)))
            if p1 is not None and p2 is not None:
                try:
                    return _reduce_exact_triple(
                        (
                            (a * f.Qa) / (p1[0] * p2[0]),
                            (b * f.Qb) / (p1[1] * p2[1]),
                            (c * f.Qc) / (p1[2] * p2[2]),
                        )
                    )
                except ZeroDivisionError:
                    pass

        # Functional relations list
        for rel in cdata.get("relations") or []:
            rel_s = re.sub(r"\bX_(\d+)", r"X(\1)", rel.strip())
            try:
                m = re.match(
                    r"^X\(\d+\)\s*=\s*(?:the\s+)?isogonal\s+conjugate\s+of\s+X\((\d+)\)\s*$",
                    rel_s,
                    re.IGNORECASE,
                )
                if m:
                    pt = _get(int(m.group(1)))
                    if pt is not None:
                        u, v, w = pt
                        res = (f.Qa * v * w, f.Qb * w * u, f.Qc * u * v)
                        if _exact_triple_nonzero(res) and not _is_huge_triple(res):
                            return _reduce_exact_triple(res)

                m = re.match(
                    r"^X\(\d+\)\s*=\s*(?:the\s+)?isotomic\s+conjugate\s+of\s+X\((\d+)\)\s*$",
                    rel_s,
                    re.IGNORECASE,
                )
                if m:
                    pt = _get(int(m.group(1)))
                    if pt is not None:
                        u, v, w = pt
                        res = (v * w, w * u, u * v)
                        if _exact_triple_nonzero(res) and not _is_huge_triple(res):
                            return _reduce_exact_triple(res)

                m = re.match(
                    r"^X\(\d+\)\s*=\s*(?:the\s+)?complement\s+of\s+X\((\d+)\)\s*$",
                    rel_s,
                    re.IGNORECASE,
                )
                if m:
                    pt = _get(int(m.group(1)))
                    if pt is not None:
                        u, v, w = pt
                        return _reduce_exact_triple((v + w, w + u, u + v))

                m = re.match(
                    r"^X\(\d+\)\s*=\s*(?:the\s+)?anticomplement\s+of\s+X\((\d+)\)\s*$",
                    rel_s,
                    re.IGNORECASE,
                )
                if m:
                    pt = _get(int(m.group(1)))
                    if pt is not None:
                        u, v, w = pt
                        return _reduce_exact_triple((-u + v + w, u - v + w, u + v - w))

                m = re.match(
                    r"^X\(\d+\)\s*=\s*(?:the\s+)?midpoint\s+of\s+X\((\d+)\)\s+and\s+X\((\d+)\)\s*$",
                    rel_s,
                    re.IGNORECASE,
                )
                if m:
                    p1, p2 = _get(int(m.group(1))), _get(int(m.group(2)))
                    if p1 is not None and p2 is not None:
                        s1, s2 = p1[0] + p1[1] + p1[2], p2[0] + p2[1] + p2[2]
                        if not s1.is_zero() and not s2.is_zero():
                            res = (
                                p1[0] * s2 + p2[0] * s1,
                                p1[1] * s2 + p2[1] * s1,
                                p1[2] * s2 + p2[2] * s1,
                            )
                            if not _is_huge_triple(res):
                                return _reduce_exact_triple(res)

                m = re.match(
                    r"^X\(\d+\)\s*=\s*(?:the\s+)?reflection\s+of\s+X\((\d+)\)\s+in\s+X\((\d+)\)\s*$",
                    rel_s,
                    re.IGNORECASE,
                )
                if m:
                    p1, p2 = _get(int(m.group(1))), _get(int(m.group(2)))
                    if p1 is not None and p2 is not None:
                        s1, s2 = p1[0] + p1[1] + p1[2], p2[0] + p2[1] + p2[2]
                        if not s1.is_zero() and not s2.is_zero():
                            res = (
                                p2[0] * s1 * 2 - p1[0] * s2,
                                p2[1] * s1 * 2 - p1[1] * s2,
                                p2[2] * s1 * 2 - p1[2] * s2,
                            )
                            if not _is_huge_triple(res):
                                return _reduce_exact_triple(res)

                m = re.match(
                    r"^X\(\d+\)\s*=\s*X\(2\)-Hirst\s+inverse\s+of\s+X\((\d+)\)\s*$",
                    rel_s,
                    re.IGNORECASE,
                )
                if m:
                    pt = _get(int(m.group(1)))
                    if pt is not None:
                        u, v, w = pt
                        res = (u * u - v * w, v * v - w * u, w * w - u * v)
                        if not _is_huge_triple(res):
                            return _reduce_exact_triple(res)

                m = re.match(
                    r"^X\(\d+\)\s*=\s*X\((\d+)\)-Ceva\s+conjugate\s+of\s+X\((\d+)\)\s*$",
                    rel_s,
                    re.IGNORECASE,
                )
                if m:
                    p1, p2 = _get(int(m.group(1))), _get(int(m.group(2)))
                    if p1 is not None and p2 is not None:
                        p, q, rv = p1
                        u, v, w = p2
                        if not (p.is_zero() or q.is_zero() or rv.is_zero()):
                            res = (
                                u * (-u / p + v / q + w / rv),
                                v * (u / p - v / q + w / rv),
                                w * (u / p + v / q - w / rv),
                            )
                            if not _is_huge_triple(res):
                                return _reduce_exact_triple(res)

                m = re.match(
                    r"^X\(\d+\)\s*=\s*(?:the\s+)?crosspoint\s+of\s+X\((\d+)\)\s+and\s+X\((\d+)\)\s*$",
                    rel_s,
                    re.IGNORECASE,
                )
                if m:
                    p1, p2 = _get(int(m.group(1))), _get(int(m.group(2)))
                    if p1 is not None and p2 is not None:
                        p, q, rv = p1
                        u, v, w = p2
                        res = (
                            p * u * (q * w + rv * v),
                            q * v * (rv * u + p * w),
                            rv * w * (p * v + q * u),
                        )
                        if not _is_huge_triple(res):
                            return _reduce_exact_triple(res)

                m = re.match(
                    r"^X\(\d+\)\s*=\s*(?:the\s+)?cevapoint\s+of\s+X\((\d+)\)\s+and\s+X\((\d+)\)\s*$",
                    rel_s,
                    re.IGNORECASE,
                )
                if m:
                    p1, p2 = _get(int(m.group(1))), _get(int(m.group(2)))
                    if p1 is not None and p2 is not None:
                        p, q, rv = p1
                        u, v, w = p2
                        res = (
                            (p * v + q * u) * (p * w + rv * u),
                            (q * w + rv * v) * (q * u + p * v),
                            (rv * u + p * w) * (rv * v + q * w),
                        )
                        if not _is_huge_triple(res):
                            return _reduce_exact_triple(res)
            except (ZeroDivisionError, OutsideFieldError):
                continue
        return None

    def _try_exact_incidence(self, cdata: dict[str, Any]) -> tuple[Any, Any, Any] | None:
        known_lines: list[tuple[Any, Any, Any]] = []
        for inc in cdata.get("incidences") or []:
            for i_num, j_num in inc.get("lines") or []:
                p1 = self.exact_bary.get(i_num)
                p2 = self.exact_bary.get(j_num)
                if p1 is not None and p2 is not None and _exact_triple_nonzero(p1) and _exact_triple_nonzero(p2):
                    ln = _exact_bary_line(p1, p2)
                    if _exact_triple_nonzero(ln) and not _is_huge_triple(ln):
                        known_lines.append(_reduce_exact_triple(ln))
                        if len(known_lines) >= 6:
                            break
            if len(known_lines) >= 6:
                break
        if not known_lines:
            return None

        title_low = (cdata.get("title") or "").lower()
        is_inf = "infinity" in title_low or "direction of" in title_low
        if is_inf:
            inf_ln = (self.field.one, self.field.one, self.field.one)
            pt = _exact_bary_line(known_lines[0], inf_ln)
            if _exact_triple_nonzero(pt) and not _is_huge_triple(pt):
                return _reduce_exact_triple(pt)

        if len(known_lines) >= 2:
            for idx1 in range(len(known_lines)):
                for idx2 in range(idx1 + 1, len(known_lines)):
                    pt = _exact_bary_line(known_lines[idx1], known_lines[idx2])
                    if _exact_triple_nonzero(pt) and not _is_huge_triple(pt):
                        return _reduce_exact_triple(pt)
        return None

    def _score_exact_collinearity_pair(
        self, cdata: dict[str, Any], cand: tuple[Any, Any, Any], limit: int = 6
    ) -> tuple[int, int]:
        """Return ``(hits, checked)`` for exact projective collinearity ``det(P_i, P_j, cand) == 0``."""
        hits = 0
        checked = 0
        for inc in cdata.get("incidences") or []:
            for i_num, j_num in inc.get("lines") or []:
                p1 = self.exact_bary.get(i_num)
                p2 = self.exact_bary.get(j_num)
                if (
                    p1 is None
                    or p2 is None
                    or not _exact_triple_nonzero(p1)
                    or not _exact_triple_nonzero(p2)
                ):
                    continue
                ln = _exact_bary_line(p1, p2)
                if not _exact_triple_nonzero(ln):
                    continue
                dot = ln[0] * cand[0] + ln[1] * cand[1] + ln[2] * cand[2]
                if dot.is_zero():
                    hits += 1
                checked += 1
                if checked >= limit:
                    return (hits, checked)
        return (hits, checked)

    def audit_exact_collinearity(self, max_lines_per_center: int = 4) -> dict[str, Any]:
        """Verify exact zero-determinant collinearity across all resolved centers."""
        tested_centers = 0
        passed_centers = 0
        failed_centers: list[tuple[int, int, int]] = []
        for num, bary in sorted(self.exact_bary.items()):
            cdata = self.centers_by_num.get(num)
            if not cdata or not _exact_triple_nonzero(bary):
                continue
            checked = 0
            hits = 0
            for inc in cdata.get("incidences") or []:
                for i_num, j_num in inc.get("lines") or []:
                    p1 = self.exact_bary.get(i_num)
                    p2 = self.exact_bary.get(j_num)
                    if (
                        p1 is None
                        or p2 is None
                        or not _exact_triple_nonzero(p1)
                        or not _exact_triple_nonzero(p2)
                    ):
                        continue
                    ln = _exact_bary_line(p1, p2)
                    if not _exact_triple_nonzero(ln):
                        continue
                    dot = ln[0] * bary[0] + ln[1] * bary[1] + ln[2] * bary[2]
                    checked += 1
                    if dot.is_zero():
                        hits += 1
                    if checked >= max_lines_per_center:
                        break
                if checked >= max_lines_per_center:
                    break
            if checked > 0:
                tested_centers += 1
                if hits == checked:
                    passed_centers += 1
                else:
                    failed_centers.append((num, hits, checked))
        return {
            "tested_centers": tested_centers,
            "passed_centers": passed_centers,
            "failed_count": len(failed_centers),
            "failed_sample": failed_centers[:25],
        }

    def _get_mp_bary(self, k: int, dps: int = 50) -> tuple[mp.mpf, mp.mpf, mp.mpf] | None:
        if k in self.exact_bary:
            eb = self.exact_bary[k]
            if _exact_triple_nonzero(eb):
                return (eb[0].to_mpf(dps), eb[1].to_mpf(dps), eb[2].to_mpf(dps))
        return self.mp_bary.get(k)

    def _norm_mp_triple(
        self, triple: tuple[mp.mpf, mp.mpf, mp.mpf]
    ) -> tuple[mp.mpf, mp.mpf, mp.mpf] | None:
        c1, c2, c3 = triple
        if not (mp.isfinite(c1) and mp.isfinite(c2) and mp.isfinite(c3)):
            return None
        m = max(abs(c1), abs(c2), abs(c3))
        if m == 0 or not mp.isfinite(m):
            return None
        return (c1 / m, c2 / m, c3 / m)

    def _try_mpmath_coordinates(self, cdata: dict[str, Any]) -> tuple[mp.mpf, mp.mpf, mp.mpf] | None:
        for fld, is_tril in (("barycentrics", False), ("trilinears", True)):
            for raw_line in cdata.get(fld) or []:
                expr = _prepare_formula_expr(raw_line)
                if not expr:
                    continue
                xyz, uvw, ready = self._extract_xyz_uvw_mp(raw_line)
                if not ready:
                    continue
                res = self.field.eval_cyclic_mpmath(expr, is_trilinear=is_tril, xyz=xyz, uvw=uvw)
                if res is not None:
                    return res
        return None

    def _try_mpmath_relations(
        self, cdata: dict[str, Any], dps: int = 50
    ) -> tuple[mp.mpf, mp.mpf, mp.mpf] | None:
        with mp.workdps(dps):
            a_m = self.field._mp_env[0]["a"]
            b_m = self.field._mp_env[0]["b"]
            c_m = self.field._mp_env[0]["c"]
            for rel in cdata.get("relations") or []:
                rel_s = re.sub(r"\bX_(\d+)", r"X(\1)", rel.strip())
                try:
                    m = re.match(
                        r"^X\(\d+\)\s*=\s*(?:the\s+)?isogonal\s+conjugate\s+of\s+X\((\d+)\)\s*$",
                        rel_s,
                        re.IGNORECASE,
                    )
                    if m:
                        pt = self._get_mp_bary(int(m.group(1)), dps)
                        if pt:
                            u, v, w = pt
                            return self._norm_mp_triple((a_m * a_m * v * w, b_m * b_m * w * u, c_m * c_m * u * v))

                    m = re.match(
                        r"^X\(\d+\)\s*=\s*(?:the\s+)?isotomic\s+conjugate\s+of\s+X\((\d+)\)\s*$",
                        rel_s,
                        re.IGNORECASE,
                    )
                    if m:
                        pt = self._get_mp_bary(int(m.group(1)), dps)
                        if pt:
                            u, v, w = pt
                            return self._norm_mp_triple((v * w, w * u, u * v))

                    m = re.match(
                        r"^X\(\d+\)\s*=\s*(?:the\s+)?complement\s+of\s+X\((\d+)\)\s*$",
                        rel_s,
                        re.IGNORECASE,
                    )
                    if m:
                        pt = self._get_mp_bary(int(m.group(1)), dps)
                        if pt:
                            u, v, w = pt
                            return self._norm_mp_triple((v + w, w + u, u + v))

                    m = re.match(
                        r"^X\(\d+\)\s*=\s*(?:the\s+)?anticomplement\s+of\s+X\((\d+)\)\s*$",
                        rel_s,
                        re.IGNORECASE,
                    )
                    if m:
                        pt = self._get_mp_bary(int(m.group(1)), dps)
                        if pt:
                            u, v, w = pt
                            return self._norm_mp_triple((-u + v + w, u - v + w, u + v - w))

                    m = re.match(
                        r"^X\(\d+\)\s*=\s*(?:the\s+)?midpoint\s+of\s+X\((\d+)\)\s+and\s+X\((\d+)\)\s*$",
                        rel_s,
                        re.IGNORECASE,
                    )
                    if m:
                        p1 = self._get_mp_bary(int(m.group(1)), dps)
                        p2 = self._get_mp_bary(int(m.group(2)), dps)
                        if p1 and p2:
                            s1, s2 = sum(p1), sum(p2)
                            if abs(s1) > mp.mpf("1e-25") and abs(s2) > mp.mpf("1e-25"):
                                return self._norm_mp_triple(
                                    (p1[0] / s1 + p2[0] / s2, p1[1] / s1 + p2[1] / s2, p1[2] / s1 + p2[2] / s2)
                                )

                    m = re.match(
                        r"^X\(\d+\)\s*=\s*(?:the\s+)?reflection\s+of\s+X\((\d+)\)\s+in\s+X\((\d+)\)\s*$",
                        rel_s,
                        re.IGNORECASE,
                    )
                    if m:
                        p1 = self._get_mp_bary(int(m.group(1)), dps)
                        p2 = self._get_mp_bary(int(m.group(2)), dps)
                        if p1 and p2:
                            s1, s2 = sum(p1), sum(p2)
                            if abs(s1) > mp.mpf("1e-25") and abs(s2) > mp.mpf("1e-25"):
                                return self._norm_mp_triple(
                                    (
                                        2 * p2[0] / s2 - p1[0] / s1,
                                        2 * p2[1] / s2 - p1[1] / s1,
                                        2 * p2[2] / s2 - p1[2] / s1,
                                    )
                                )
                except (ArithmeticError, ValueError, TypeError):
                    continue
        return None

    def _try_mpmath_incidence(
        self, cdata: dict[str, Any], dps: int = 50
    ) -> tuple[mp.mpf, mp.mpf, mp.mpf] | None:
        with mp.workdps(dps):
            lines: list[tuple[mp.mpf, mp.mpf, mp.mpf]] = []
            for inc in cdata.get("incidences") or []:
                for i_num, j_num in inc.get("lines") or []:
                    p1 = self._get_mp_bary(i_num, dps)
                    p2 = self._get_mp_bary(j_num, dps)
                    if p1 and p2:
                        ln = self._norm_mp_triple(
                            (
                                p1[1] * p2[2] - p1[2] * p2[1],
                                p1[2] * p2[0] - p1[0] * p2[2],
                                p1[0] * p2[1] - p1[1] * p2[0],
                            )
                        )
                        if ln:
                            lines.append(ln)
                            if len(lines) >= 6:
                                break
                if len(lines) >= 6:
                    break
            if len(lines) >= 2:
                for idx1 in range(len(lines)):
                    for idx2 in range(idx1 + 1, len(lines)):
                        l1, l2 = lines[idx1], lines[idx2]
                        pt = self._norm_mp_triple(
                            (
                                l1[1] * l2[2] - l1[2] * l2[1],
                                l1[2] * l2[0] - l1[0] * l2[2],
                                l1[0] * l2[1] - l1[1] * l2[0],
                            )
                        )
                        if pt:
                            return pt
        return None

    def _symmetry_pole_result(self) -> ExactEvalResult:
        f = self.field
        if f.is_equilateral:
            note = "Indeterminate / pole under equilateral D₃ symmetry (a = b = c)"
        elif f.is_isosceles:
            note = "Indeterminate / pole under isosceles symmetry (a = b)"
        elif f.is_right:
            note = "Indeterminate / pole under right-angle degeneracy (∠A = 90°)"
        else:
            note = "Indeterminate algebraic pole (0 / 0)"
        return ExactEvalResult(
            triangle_key=f.key,
            precision="exact",
            bary=(f.zero, f.zero, f.zero),
            trilinear=(f.zero, f.zero, f.zero),
            xy=(f.zero, f.zero),
            search_value=f.zero,
            approx_xy=(math.nan, math.nan),
            approx_bary=(0.0, 0.0, 0.0),
            approx_search=math.nan,
            is_indeterminate=True,
            symmetry_note=note,
            field_tag=f.field_latex,
            bary_latex="0 : 0 : 0",
            trilinear_latex="0 : 0 : 0",
            xy_latex=r"\text{indeterminate } (0:0:0)",
            search_latex=r"\text{indeterminate}",
        )

    @staticmethod
    def _has_coord_center_dep(cdata: dict[str, Any]) -> bool:
        for fld in ("barycentrics", "trilinears"):
            for raw_line in cdata.get(fld) or []:
                if re.search(
                    r"(?:[xu]\s*:\s*[yv]\s*:\s*[zw]|\b[xyz]\(\s*\d+\s*\))",
                    raw_line,
                    flags=re.IGNORECASE,
                ):
                    return True
        return False

    def resolve_all(self, max_passes: int = 5) -> dict[int, ExactEvalResult]:
        """Resolve all centers in ``centers_by_num`` (exact first, then 50-digit fallback)."""
        sorted_nums = sorted(self.centers_by_num)
        verbose = len(sorted_nums) >= 10_000
        t_all = time.perf_counter()
        exact_coord_skip: set[int] = set()
        mp_coord_skip: set[int] = set()

        for p_idx in range(max_passes):
            progressed = False
            for idx, num in enumerate(sorted_nums, 1):
                if num in self.exact_bary:
                    continue
                cdata = self.centers_by_num[num]
                bary = None
                if num not in exact_coord_skip:
                    bary = self._try_exact_coordinates(cdata)
                    if bary is None and not self._has_coord_center_dep(cdata):
                        exact_coord_skip.add(num)
                if bary is None:
                    bary = self._try_exact_relations(cdata) or self._try_exact_incidence(cdata)
                if bary is not None:
                    self.exact_bary[num] = bary
                    self.zero_div_poles.discard(num)
                    progressed = True
                if verbose and p_idx == 0 and idx % 20_000 == 0:
                    print(
                        f"    [{self.field.key}] pass 1: {idx}/{len(sorted_nums)} "
                        f"(exact={len(self.exact_bary)}, {time.perf_counter() - t_all:.1f}s)",
                        flush=True,
                    )
            if verbose:
                print(
                    f"    [{self.field.key}] exact pass {p_idx + 1} done: "
                    f"exact={len(self.exact_bary)} ({time.perf_counter() - t_all:.1f}s)",
                    flush=True,
                )
            if not progressed:
                break

        # 50-digit mpmath fallback ONLY for centers unresolved in exact field (and not symmetry poles)
        for p_idx in range(4):
            progressed = False
            for num in sorted_nums:
                if num in self.exact_bary or num in self.mp_bary or num in self.zero_div_poles:
                    continue
                cdata = self.centers_by_num[num]
                mp_b = None
                if num not in mp_coord_skip:
                    mp_b = self._try_mpmath_coordinates(cdata)
                    if mp_b is None and not self._has_coord_center_dep(cdata):
                        mp_coord_skip.add(num)
                if mp_b is None:
                    mp_b = self._try_mpmath_relations(cdata) or self._try_mpmath_incidence(cdata)
                if mp_b is not None:
                    self.mp_bary[num] = mp_b
                    progressed = True
            if not progressed:
                break

        if verbose:
            print(
                f"    [{self.field.key}] mp50 done: exact={len(self.exact_bary)}, "
                f"mp50={len(self.mp_bary)}, poles={len(self.zero_div_poles)} "
                f"({time.perf_counter() - t_all:.1f}s)",
                flush=True,
            )

        # Package results
        out: dict[int, ExactEvalResult] = {}
        for num in sorted_nums:
            if num in self.exact_bary:
                out[num] = self.field.package_exact_bary(self.exact_bary[num])
            elif num in self.mp_bary:
                out[num] = self.field.package_mpmath_bary(self.mp_bary[num])
            elif num in self.zero_div_poles:
                out[num] = self._symmetry_pole_result()
        self.results = out
        return out
