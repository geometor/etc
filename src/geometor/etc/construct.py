"""Symbolic and numerical geometric construction engine for ETC triangle centers using `geometor.model`."""

from __future__ import annotations

import functools
import logging
import math
import re
from typing import Any

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model
from geometor.model.element import CircleElement, Element

# Suppress verbose Rich console logging when batch-building models
_SILENT_LOGGER = logging.getLogger("geometor.etc.silent")
_SILENT_LOGGER.addHandler(logging.NullHandler())
_SILENT_LOGGER.propagate = False


TRIANGLE_PRESETS: dict[str, tuple[float, float, float]] = {
    "acute": (5.0, 6.0, 7.0),
    "kimberling": (6.0, 9.0, 13.0),
    "heronian": (13.0, 14.0, 15.0),
    "right": (3.0, 4.0, 5.0),
    "kepler": (1.0, math.sqrt((1.0 + math.sqrt(5.0)) / 2.0), (1.0 + math.sqrt(5.0)) / 2.0),
}


class TriangleContext:
    """Precomputed triangle invariants and Cartesian coordinates on the unit baseline AB (c = 1)."""

    def __init__(self, a: float, b: float, c: float) -> None:
        self.raw_a = float(a)
        self.raw_b = float(b)
        self.raw_c = float(c)

        # Normalize to unit segment AB (c_norm = 1)
        self.scale = 1.0 / self.raw_c
        self.a = self.raw_a * self.scale
        self.b = self.raw_b * self.scale
        self.c = 1.0

        # Vertices on unit baseline A=(0,0), B=(1,0), C=(x_C, y_C) via Euclid I.22 circle intersection
        self.A_xy = (0.0, 0.0)
        self.B_xy = (1.0, 0.0)
        x_c = (1.0 + self.b**2 - self.a**2) / 2.0
        y_c_sq = max(0.0, self.b**2 - x_c**2)
        y_c = math.sqrt(y_c_sq)
        self.C_xy = (x_c, y_c)

        # Angles and trig invariants (scale-invariant)
        a_r, b_r, c_r = self.raw_a, self.raw_b, self.raw_c
        s = 0.5 * (a_r + b_r + c_r)
        area = math.sqrt(max(0.0, s * (s - a_r) * (s - b_r) * (s - c_r)))
        self.s = s
        self.area = area
        self.R = (a_r * b_r * c_r) / (4.0 * area)
        self.r = area / s

        cos_A = (b_r**2 + c_r**2 - a_r**2) / (2.0 * b_r * c_r)
        cos_B = (c_r**2 + a_r**2 - b_r**2) / (2.0 * c_r * a_r)
        cos_C = (a_r**2 + b_r**2 - c_r**2) / (2.0 * a_r * b_r)
        self.A_rad = math.acos(max(-1.0, min(1.0, cos_A)))
        self.B_rad = math.acos(max(-1.0, min(1.0, cos_B)))
        self.C_rad = math.acos(max(-1.0, min(1.0, cos_C)))

        cot_A = cos_A / math.sin(self.A_rad)
        cot_B = cos_B / math.sin(self.B_rad)
        cot_C = cos_C / math.sin(self.C_rad)
        cot_omega = cot_A + cot_B + cot_C
        self.omega = math.atan(1.0 / cot_omega)

        Ra = area / (s - a_r)
        Rb = area / (s - b_r)
        Rc = area / (s - c_r)
        SA = 0.5 * (b_r**2 + c_r**2 - a_r**2)
        SB = 0.5 * (c_r**2 + a_r**2 - b_r**2)
        SC = 0.5 * (a_r**2 + b_r**2 - c_r**2)
        safe_funcs: dict[str, Any] = {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "cot": lambda x: math.cos(x) / math.sin(x),
            "sec": lambda x: 1.0 / math.cos(x),
            "csc": lambda x: 1.0 / math.sin(x),
            "sqrt": math.sqrt,
            "pi": math.pi,
            "omega": self.omega,
            "area": area,
            "R": self.R,
            "r": self.r,
            "s": s,
            "S": 2.0 * area,
            "SW": 0.5 * (a_r**2 + b_r**2 + c_r**2),
        }
        A_rad, B_rad, C_rad = self.A_rad, self.B_rad, self.C_rad
        self.eval_envs: tuple[dict[str, Any], dict[str, Any], dict[str, Any]] = (
            {**safe_funcs, "a": a_r, "b": b_r, "c": c_r, "A": A_rad, "B": B_rad, "C": C_rad, "Ra": Ra, "Rb": Rb, "Rc": Rc, "SA": SA, "SB": SB, "SC": SC},
            {**safe_funcs, "a": b_r, "b": c_r, "c": a_r, "A": B_rad, "B": C_rad, "C": A_rad, "Ra": Rb, "Rb": Rc, "Rc": Ra, "SA": SB, "SB": SC, "SC": SA},
            {**safe_funcs, "a": c_r, "b": a_r, "c": b_r, "A": C_rad, "B": A_rad, "C": B_rad, "Ra": Rc, "Rb": Ra, "Rc": Rb, "SA": SC, "SB": SA, "SC": SB},
        )
        # Perturbed environments for removable singularities on right/special triangles (e.g. C = 90°)
        c_p = c_r * (1.0 - 1e-7)
        s_p = 0.5 * (a_r + b_r + c_p)
        area_p = math.sqrt(max(1e-16, s_p * (s_p - a_r) * (s_p - b_r) * (s_p - c_p)))
        A_p = math.acos(max(-1.0, min(1.0, (b_r**2 + c_p**2 - a_r**2) / (2.0 * b_r * c_p))))
        B_p = math.acos(max(-1.0, min(1.0, (c_p**2 + a_r**2 - b_r**2) / (2.0 * c_p * a_r))))
        C_p = math.acos(max(-1.0, min(1.0, (a_r**2 + b_r**2 - c_p**2) / (2.0 * a_r * b_r))))
        SA_p = 0.5 * (b_r**2 + c_p**2 - a_r**2)
        SB_p = 0.5 * (c_p**2 + a_r**2 - b_r**2)
        SC_p = 0.5 * (a_r**2 + b_r**2 - c_p**2)
        Ra_p, Rb_p, Rc_p = area_p / (s_p - a_r), area_p / (s_p - b_r), area_p / (s_p - c_p)
        self.perturbed_eval_envs: tuple[dict[str, Any], dict[str, Any], dict[str, Any]] = (
            {**safe_funcs, "a": a_r, "b": b_r, "c": c_p, "A": A_p, "B": B_p, "C": C_p, "Ra": Ra_p, "Rb": Rb_p, "Rc": Rc_p, "SA": SA_p, "SB": SB_p, "SC": SC_p},
            {**safe_funcs, "a": b_r, "b": c_p, "c": a_r, "A": B_p, "B": C_p, "C": A_p, "Ra": Rb_p, "Rb": Rc_p, "Rc": Ra_p, "SA": SB_p, "SB": SC_p, "SC": SA_p},
            {**safe_funcs, "a": c_p, "b": a_r, "c": b_r, "A": C_p, "B": A_p, "C": B_p, "Ra": Rc_p, "Rb": Ra_p, "Rc": Rb_p, "SA": SC_p, "SB": SA_p, "SC": SB_p},
        )

    def bary_to_cartesian(self, u: float, v: float, w: float) -> tuple[float, float] | None:
        """Convert homogeneous barycentric coordinates (u : v : w) to Cartesian (x, y) on unit AB."""
        denom = u + v + w
        if abs(denom) < 1e-13:
            return None
        x = (u * self.A_xy[0] + v * self.B_xy[0] + w * self.C_xy[0]) / denom
        y = (u * self.A_xy[1] + v * self.B_xy[1] + w * self.C_xy[1]) / denom
        return (x, y)

    def trilinear_to_bary(
        self, alpha: float, beta: float, gamma: float
    ) -> tuple[float, float, float]:
        """Convert homogeneous trilinear coordinates to homogeneous barycentrics."""
        return (self.raw_a * alpha, self.raw_b * beta, self.raw_c * gamma)

    def normalize_bary(self, u: float, v: float, w: float) -> tuple[float, float, float]:
        """Normalize homogeneous barycentrics so u + v + w = 1 (or unit norm if sum is near 0)."""
        s = u + v + w
        if abs(s) > 1e-12:
            return (u / s, v / s, w / s)
        norm = math.hypot(u, v, w)
        if norm > 1e-12:
            return (u / norm, v / norm, w / norm)
        return (1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0)

    def kimberling_search_value(self, u: float, v: float, w: float) -> float:
        """Compute Kimberling's signed distance h_a from X(n) to side BC for raw (a, b, c)."""
        s = u + v + w
        if abs(s) < 1e-13:
            return 0.0
        u_n = u / s
        return (2.0 * self.area * u_n) / self.raw_a


@functools.lru_cache(maxsize=None)
def _prepare_formula_expr(latex_or_rst: str) -> str | None:
    """Extract the first component of a trilinear or barycentric ratio and convert to a Python math expression."""
    if not latex_or_rst:
        return None
    s_full = latex_or_rst.strip()
    # Extract inside :math:`...` if present
    m = re.match(r"^:math:`([^`]+)`(.*)$", s_full, flags=re.DOTALL)
    if m:
        s = m.group(1).strip()
        tail_clause = m.group(2).strip()
    else:
        return None

    # Take first component before ':' (or entire expression if single component without ':')
    if ":" in s:
        first = s.split(":", 1)[0].strip()
    else:
        first = s.strip()

    # Check if `first` is `f(A,B,C)` or `f(a,b,c)` defined in `tail_clause` ("where f(A,B,C) = ...")
    if re.match(r"^f\s*\(\s*[aAbBcC]\s*,\s*[aAbBcC]\s*,\s*[aAbBcC]\s*\)$", first):
        fm = re.search(
            r"where\s*,?\s*f\s*\(\s*[aAbBcC]\s*,\s*[aAbBcC]\s*,\s*[aAbBcC]\s*\)\s*=\s*(.+)$",
            tail_clause,
            flags=re.IGNORECASE,
        )
        if not fm:
            return None
        rhs = fm.group(1).strip()
        # Reject if secondary auxiliary functions u(...), v(...), t(...), s(...), x = ... are defined after a comma
        if re.search(r",\s*(?:where\s+)?[uvtsx]\s*[\(=]", rhs):
            return None
        # Convert inline RST superscripts `\ :sup:`2`\ ` -> `**(2)` and escaped `\*` -> `*`
        rhs = re.sub(r"\\?\s*:sup:`([^`]+)`\\?\s*", r"**(\1)", rhs)
        rhs = rhs.replace(r"\*", "*").replace("π", "pi").replace("ω", "omega")
        first = rhs

    if not first or "=" in first or "\\text" in first or "see below" in first.lower():
        return None

    # Convert LaTeX constructs to Python expression
    expr = first
    expr = expr.replace("[", "(").replace("]", ")")
    expr = expr.replace(r"\omega", "omega").replace(r"\pi", "pi")
    expr = expr.replace(r"\Delta", "area").replace("Area", "area")
    expr = re.sub(r"\\(sin|cos|tan|cot|sec|csc)\b", r"\1", expr)

    # Convert \sqrt{...} to sqrt(...)
    while re.search(r"\\sqrt\{([^{}]+)\}", expr):
        expr = re.sub(r"\\sqrt\{([^{}]+)\}", r"sqrt(\1)", expr)

    # Convert ^{...} to **(...)
    while re.search(r"\^\{([^{}]+)\}", expr):
        expr = re.sub(r"\^\{([^{}]+)\}", r"**(\1)", expr)
    expr = re.sub(r"\^(-?\d+(?:/\d+)?)", r"**(\1)", expr)

    # Convert trig powers like sin**(2)(A) or cos**2 A
    expr = re.sub(
        r"\b(sin|cos|tan|cot|sec|csc)\*\*\(([^()]+)\)\s*\(([^()]+)\)",
        r"(\1(\3))**(\2)",
        expr,
    )
    # Convert trig with unparenthesized arguments like `sin 2A`, `cos A/2`, `tan B/4`, `sin A`
    expr = re.sub(
        r"\b(sin|cos|tan|cot|sec|csc)\s+(\d+)\s*(A|B|C|omega)\b",
        r"\1(\2*\3)",
        expr,
    )
    expr = re.sub(
        r"\b(sin|cos|tan|cot|sec|csc)\s+(A|B|C|omega)\s*/\s*(\d+)\b",
        r"\1(\2/\3)",
        expr,
    )
    expr = re.sub(
        r"\b(sin|cos|tan|cot|sec|csc)\s+(A|B|C|omega)\b",
        r"\1(\2)",
        expr,
    )

    # Remove remaining braces
    expr = expr.replace("{", "(").replace("}", ")")

    # Insert explicit multiplication * between adjacent tokens:
    # number/var/) followed by ( or var/func
    func_names = {
        "sin",
        "cos",
        "tan",
        "cot",
        "sec",
        "csc",
        "sqrt",
        "omega",
        "area",
        "pi",
        "Ra",
        "Rb",
        "Rc",
        "SA",
        "SB",
        "SC",
        "SW",
    }
    # Protect function and multi-char variable names with placeholders
    placeholders: dict[str, str] = {}
    for idx, fn in enumerate(sorted(func_names, key=len, reverse=True)):
        ph = f"__FN{idx}__"
        placeholders[ph] = fn
        expr = re.sub(rf"\b{fn}\b", ph, expr)

    # Split single-letter product runs like "bc" or "abc" into "b*c"
    expr = re.sub(r"\b([abcABC])([abcABC])\b", r"\1*\2", expr)
    expr = re.sub(r"\b([abcABC])([abcABC])\b", r"\1*\2", expr)

    # Insert * between:
    # 1. digit or var or placeholder or ) followed by ( or var or placeholder
    expr = re.sub(
        r"(\d|[abcABCRrsS]|__FN\d+__|\))\s*(?=[abcABCRrsS\(]|__FN)",
        r"\1*",
        expr,
    )
    # 2. ) followed by digit or var
    expr = re.sub(r"\)\s*(?=\d|[abcABCRrsS])", r")*", expr)

    # Restore function names, ensuring fn*( becomes fn(
    for ph, fn in placeholders.items():
        if fn in {"sin", "cos", "tan", "cot", "sec", "csc", "sqrt"}:
            expr = expr.replace(f"{ph}*(", f"{fn}(")
        expr = expr.replace(ph, fn)

    return expr


_EMPTY_GLOBALS: dict[str, Any] = {"__builtins__": {}}


@functools.lru_cache(maxsize=None)
def _compile_expr(expr_str: str) -> Any:
    return compile(expr_str, "<coord>", "eval")


def _eval_cyclic(expr_str: str, ctx: TriangleContext) -> tuple[float, float, float] | None:
    """Evaluate a cyclic coordinate expression f(a, b, c, A, B, C) for all three components."""
    code = None
    try:
        code = _compile_expr(expr_str)
    except Exception:
        return None

    for env_tuple in (ctx.eval_envs, ctx.perturbed_eval_envs):
        vals: list[float] = []
        ok = True
        try:
            for env in env_tuple:
                val = float(eval(code, _EMPTY_GLOBALS, env))
                if not math.isfinite(val):
                    ok = False
                    break
                vals.append(val)
        except Exception:
            ok = False
        if ok and len(vals) == 3 and not all(abs(v) < 1e-14 for v in vals):
            return (vals[0], vals[1], vals[2])
    return None


def _bary_line(
    p1: tuple[float, float, float], p2: tuple[float, float, float]
) -> tuple[float, float, float]:
    """Compute homogeneous line coordinates (L : M : N) joining two barycentric points."""
    return (
        p1[1] * p2[2] - p1[2] * p2[1],
        p1[2] * p2[0] - p1[0] * p2[2],
        p1[0] * p2[1] - p1[1] * p2[0],
    )


def _intersect_bary_lines(
    l1: tuple[float, float, float], l2: tuple[float, float, float]
) -> tuple[float, float, float] | None:
    """Intersect two homogeneous barycentric lines."""
    u = l1[1] * l2[2] - l1[2] * l2[1]
    v = l1[2] * l2[0] - l1[0] * l2[2]
    w = l1[0] * l2[1] - l1[1] * l2[0]
    if math.hypot(u, v, w) < 1e-12:
        return None
    return (u, v, w)


class CenterRegistry:
    """Evaluates and caches barycentric and Cartesian coordinates for ETC centers on a TriangleContext."""

    def __init__(self, centers: list[dict[str, Any]], ctx: TriangleContext) -> None:
        self.ctx = ctx
        self.centers_by_num: dict[int, dict[str, Any]] = {}
        for c in centers:
            if c and c.get("num"):
                self.centers_by_num[int(c["num"])] = c

        self.bary_cache: dict[int, tuple[float, float, float]] = {}
        self.xy_cache: dict[int, tuple[float, float]] = {}
        self._seed_classical_centers()
        self._resolve_all()

    def _seed_classical_centers(self) -> None:
        """Seed exact barycentric coordinates for classical centers X(1)..X(18)."""
        a, b, c = self.ctx.raw_a, self.ctx.raw_b, self.ctx.raw_c
        s = self.ctx.s
        A, B, C = self.ctx.A_rad, self.ctx.B_rad, self.ctx.C_rad

        # X(1) Incenter: (a : b : c)
        self._store(1, (a, b, c))
        # X(2) Centroid: (1 : 1 : 1)
        self._store(2, (1.0, 1.0, 1.0))
        # X(3) Circumcenter: (a^2(b^2+c^2-a^2) : ...)
        sa = b**2 + c**2 - a**2
        sb = c**2 + a**2 - b**2
        sc = a**2 + b**2 - c**2
        self._store(3, (a**2 * sa, b**2 * sb, c**2 * sc))
        # X(4) Orthocenter: (1/sa : 1/sb : 1/sc) = (sb*sc : sc*sa : sa*sb)
        self._store(4, (sb * sc, sc * sa, sa * sb))
        # X(5) Nine-Point Center: midpoint of X(3) and X(4)
        b3 = self.bary_cache[3]
        b4 = self.bary_cache[4]
        self._store(5, (b3[0] + b4[0], b3[1] + b4[1], b3[2] + b4[2]))
        # X(6) Symmedian Point: (a^2 : b^2 : c^2)
        self._store(6, (a**2, b**2, c**2))
        # X(7) Gergonne Point: (1/(s-a) : 1/(s-b) : 1/(s-c))
        self._store(7, (1.0 / (s - a), 1.0 / (s - b), 1.0 / (s - c)))
        # X(8) Nagel Point: (s-a : s-b : s-c)
        self._store(8, (s - a, s - b, s - c))
        # X(9) Mittenpunkt: (a(s-a) : b(s-b) : c(s-c))
        self._store(9, (a * (s - a), b * (s - b), c * (s - c)))
        # X(10) Spieker Center: (b+c : c+a : a+b)
        self._store(10, (b + c, c + a, a + b))
        # X(11) Feuerbach Point: ((s-a)(b-c)^2 : (s-b)(c-a)^2 : (s-c)(a-b)^2)
        self._store(
            11,
            (
                (s - a) * (b - c) ** 2,
                (s - b) * (c - a) ** 2,
                (s - c) * (a - b) ** 2,
            ),
        )
        # X(12): ((b+c)^2/(s-a) : (c+a)^2/(s-b) : (a+b)^2/(s-c))
        self._store(
            12,
            (
                (b + c) ** 2 / (s - a),
                (c + a) ** 2 / (s - b),
                (a + b) ** 2 / (s - c),
            ),
        )
        # X(13) 1st Isogonic (Fermat) Center: csc(A + pi/3) trilinears
        self._store(
            13,
            (
                a / math.sin(A + math.pi / 3.0),
                b / math.sin(B + math.pi / 3.0),
                c / math.sin(C + math.pi / 3.0),
            ),
        )
        # X(14) 2nd Isogonic Center: csc(A - pi/3) trilinears
        self._store(
            14,
            (
                a / math.sin(A - math.pi / 3.0),
                b / math.sin(B - math.pi / 3.0),
                c / math.sin(C - math.pi / 3.0),
            ),
        )
        # X(15) 1st Isodynamic Point: a * sin(A + pi/3)
        self._store(
            15,
            (
                a * math.sin(A + math.pi / 3.0),
                b * math.sin(B + math.pi / 3.0),
                c * math.sin(C + math.pi / 3.0),
            ),
        )
        # X(16) 2nd Isodynamic Point: a * sin(A - pi/3)
        self._store(
            16,
            (
                a * math.sin(A - math.pi / 3.0),
                b * math.sin(B - math.pi / 3.0),
                c * math.sin(C - math.pi / 3.0),
            ),
        )
        # X(17) 1st Napoleon Point: a * csc(A + pi/6)
        self._store(
            17,
            (
                a / math.sin(A + math.pi / 6.0),
                b / math.sin(B + math.pi / 6.0),
                c / math.sin(C + math.pi / 6.0),
            ),
        )
        # X(18) 2nd Napoleon Point: a * csc(A - pi/6)
        self._store(
            18,
            (
                a / math.sin(A - math.pi / 6.0),
                b / math.sin(B - math.pi / 6.0),
                c / math.sin(C - math.pi / 6.0),
            ),
        )

    def _store(self, num: int, bary: tuple[float, float, float]) -> bool:
        norm = math.hypot(*bary)
        if norm < 1e-13:
            return False
        s = sum(bary)
        if abs(s) < 1e-7 * norm:
            # Point at infinity (u + v + w = 0): project from centroid X(2) along direction vector
            dx = (
                bary[0] * self.ctx.A_xy[0]
                + bary[1] * self.ctx.B_xy[0]
                + bary[2] * self.ctx.C_xy[0]
            )
            dy = (
                bary[0] * self.ctx.A_xy[1]
                + bary[1] * self.ctx.B_xy[1]
                + bary[2] * self.ctx.C_xy[1]
            )
            d_norm = math.hypot(dx, dy)
            if d_norm < 1e-13:
                return False
            c2 = self.xy_cache.get(2, (0.5, 0.25))
            r_proj = 1.15 * self.ctx.R * self.ctx.scale
            xy = (c2[0] + r_proj * (dx / d_norm), c2[1] + r_proj * (dy / d_norm))
            self.bary_cache[num] = (bary[0] / norm, bary[1] / norm, bary[2] / norm)
            self.xy_cache[num] = xy
            return True

        xy = self.ctx.bary_to_cartesian(*bary)
        if xy is None or not (math.isfinite(xy[0]) and math.isfinite(xy[1])):
            return False
        norm_bary = self.ctx.normalize_bary(*bary)
        self.bary_cache[num] = norm_bary
        self.xy_cache[num] = xy
        return True

    def _try_eval_coordinates(self, cdata: dict[str, Any]) -> tuple[float, float, float] | None:
        """Try evaluating trilinear or barycentric formulas from parsed center data."""
        for b_line in cdata.get("barycentrics") or []:
            expr = _prepare_formula_expr(b_line)
            if expr:
                res = _eval_cyclic(expr, self.ctx)
                if res and math.hypot(*res) > 1e-11:
                    return res

        for t_line in cdata.get("trilinears") or []:
            expr = _prepare_formula_expr(t_line)
            if expr:
                res = _eval_cyclic(expr, self.ctx)
                if res:
                    bary = self.ctx.trilinear_to_bary(*res)
                    if math.hypot(*bary) > 1e-11:
                        return bary
        return None

    def _try_eval_incidence(self, cdata: dict[str, Any]) -> tuple[float, float, float] | None:
        """Try computing X(n) as the intersection of two non-parallel lines {i1, j1} and {i2, j2}."""
        known_lines: list[tuple[float, float, float]] = []
        for inc in cdata.get("incidences") or []:
            for i_num, j_num in inc.get("lines") or []:
                if i_num in self.bary_cache and j_num in self.bary_cache:
                    ln = _bary_line(self.bary_cache[i_num], self.bary_cache[j_num])
                    if math.hypot(*ln) > 1e-11:
                        known_lines.append(ln)
                        if len(known_lines) >= 6:
                            break
            if len(known_lines) >= 6:
                break

        for idx1 in range(len(known_lines)):
            for idx2 in range(idx1 + 1, len(known_lines)):
                pt = _intersect_bary_lines(known_lines[idx1], known_lines[idx2])
                if pt and math.hypot(*pt) > 1e-10:
                    return pt
        return None

    def _try_eval_relations(self, cdata: dict[str, Any]) -> tuple[float, float, float] | None:
        """Try computing X(n) from anchored functional relations like isogonal/isotomic conjugate, complement, midpoint."""
        a, b, c = self.ctx.raw_a, self.ctx.raw_b, self.ctx.raw_c
        for rel in cdata.get("relations") or []:
            rel_s = rel.strip()
            # isogonal conjugate of X(k)
            m = re.match(
                r"^X\(\d+\)\s*=\s*(?:the\s+)?isogonal\s+conjugate\s+of\s+X\((\d+)\)\s*$",
                rel_s,
                re.IGNORECASE,
            )
            if m:
                k = int(m.group(1))
                if k in self.bary_cache:
                    u, v, w = self.bary_cache[k]
                    res = (a**2 * v * w, b**2 * w * u, c**2 * u * v)
                    if math.hypot(*res) > 1e-14:
                        return res

            # isotomic conjugate of X(k)
            m = re.match(
                r"^X\(\d+\)\s*=\s*(?:the\s+)?isotomic\s+conjugate\s+of\s+X\((\d+)\)\s*$",
                rel_s,
                re.IGNORECASE,
            )
            if m:
                k = int(m.group(1))
                if k in self.bary_cache:
                    u, v, w = self.bary_cache[k]
                    res = (v * w, w * u, u * v)
                    if math.hypot(*res) > 1e-14:
                        return res

            # complement of X(k)
            m = re.match(
                r"^X\(\d+\)\s*=\s*(?:the\s+)?complement\s+of\s+X\((\d+)\)\s*$",
                rel_s,
                re.IGNORECASE,
            )
            if m:
                k = int(m.group(1))
                if k in self.bary_cache:
                    u, v, w = self.bary_cache[k]
                    return (v + w, w + u, u + v)

            # anticomplement of X(k)
            m = re.match(
                r"^X\(\d+\)\s*=\s*(?:the\s+)?anticomplement\s+of\s+X\((\d+)\)\s*$",
                rel_s,
                re.IGNORECASE,
            )
            if m:
                k = int(m.group(1))
                if k in self.bary_cache:
                    u, v, w = self.bary_cache[k]
                    return (-u + v + w, u - v + w, u + v - w)

            # midpoint of X(i) and X(j)
            m = re.match(
                r"^X\(\d+\)\s*=\s*(?:the\s+)?midpoint\s+of\s+X\((\d+)\)\s+and\s+X\((\d+)\)\s*$",
                rel_s,
                re.IGNORECASE,
            )
            if m:
                i_k, j_k = int(m.group(1)), int(m.group(2))
                if i_k in self.bary_cache and j_k in self.bary_cache:
                    b1, b2 = self.bary_cache[i_k], self.bary_cache[j_k]
                    return (b1[0] + b2[0], b1[1] + b2[1], b1[2] + b2[2])

            # reflection of X(i) in X(j)
            m = re.match(
                r"^X\(\d+\)\s*=\s*(?:the\s+)?reflection\s+of\s+X\((\d+)\)\s+in\s+X\((\d+)\)\s*$",
                rel_s,
                re.IGNORECASE,
            )
            if m:
                i_k, j_k = int(m.group(1)), int(m.group(2))
                if i_k in self.bary_cache and j_k in self.bary_cache:
                    b1, b2 = self.bary_cache[i_k], self.bary_cache[j_k]
                    s1, s2 = sum(b1), sum(b2)
                    if abs(s1) > 1e-12 and abs(s2) > 1e-12:
                        return (
                            2.0 * b2[0] / s2 - b1[0] / s1,
                            2.0 * b2[1] / s2 - b1[1] / s1,
                            2.0 * b2[2] / s2 - b1[2] / s1,
                        )

            # X(2)-Hirst inverse of X(k)
            m = re.match(
                r"^X\(\d+\)\s*=\s*X\(2\)-Hirst\s+inverse\s+of\s+X\((\d+)\)\s*$",
                rel_s,
                re.IGNORECASE,
            )
            if m:
                k = int(m.group(1))
                if k in self.bary_cache:
                    u, v, w = self.bary_cache[k]
                    return (u**2 - v * w, v**2 - w * u, w**2 - u * v)

            # X(i)-Ceva conjugate of X(j)
            m = re.match(
                r"^X\(\d+\)\s*=\s*X\((\d+)\)-Ceva\s+conjugate\s+of\s+X\((\d+)\)\s*$",
                rel_s,
                re.IGNORECASE,
            )
            if m:
                i_k, j_k = int(m.group(1)), int(m.group(2))
                if i_k in self.bary_cache and j_k in self.bary_cache:
                    p, q, r_v = self.bary_cache[i_k]
                    u, v, w = self.bary_cache[j_k]
                    if abs(p * q * r_v) > 1e-14:
                        return (
                            u * (-u / p + v / q + w / r_v),
                            v * (u / p - v / q + w / r_v),
                            w * (u / p + v / q - w / r_v),
                        )

            # crosspoint of X(i) and X(j)
            m = re.match(
                r"^X\(\d+\)\s*=\s*(?:the\s+)?crosspoint\s+of\s+X\((\d+)\)\s+and\s+X\((\d+)\)\s*$",
                rel_s,
                re.IGNORECASE,
            )
            if m:
                i_k, j_k = int(m.group(1)), int(m.group(2))
                if i_k in self.bary_cache and j_k in self.bary_cache:
                    p, q, r_v = self.bary_cache[i_k]
                    u, v, w = self.bary_cache[j_k]
                    return (
                        p * u * (q * w + r_v * v),
                        q * v * (r_v * u + p * w),
                        r_v * w * (p * v + q * u),
                    )

            # cevapoint of X(i) and X(j)
            m = re.match(
                r"^X\(\d+\)\s*=\s*(?:the\s+)?cevapoint\s+of\s+X\((\d+)\)\s+and\s+X\((\d+)\)\s*$",
                rel_s,
                re.IGNORECASE,
            )
            if m:
                i_k, j_k = int(m.group(1)), int(m.group(2))
                if i_k in self.bary_cache and j_k in self.bary_cache:
                    p, q, r_v = self.bary_cache[i_k]
                    u, v, w = self.bary_cache[j_k]
                    return (
                        (p * v + q * u) * (p * w + r_v * u),
                        (q * w + r_v * v) * (q * u + p * v),
                        (r_v * u + p * w) * (r_v * v + q * w),
                    )

            # trilinear square/cube/square root/cube root of X(k)
            m = re.match(
                r"^X\(\d+\)\s*=\s*(?:the\s+)?trilinear\s+(square(?:\s+root)?|cube(?:\s+root)?)\s+of\s+X\((\d+)\)\s*$",
                rel_s,
                re.IGNORECASE,
            )
            if m:
                op = m.group(1).lower()
                k = int(m.group(2))
                if k in self.bary_cache:
                    u, v, w = self.bary_cache[k]
                    tx, ty, tz = u / a, v / b, w / c
                    exp = {
                        "square": 2.0,
                        "cube": 3.0,
                        "square root": 0.5,
                        "cube root": 1.0 / 3.0,
                    }.get(op, 1.0)
                    if min(tx, ty, tz) < 0 and exp < 1.0:
                        tx, ty, tz = -tx, -ty, -tz
                    if min(tx, ty, tz) > 0 or exp >= 1.0:
                        return (
                            a * (abs(tx) ** exp),
                            b * (abs(ty) ** exp),
                            c * (abs(tz) ** exp),
                        )

        return None

    def _resolve_all(self) -> None:
        """Iteratively resolve all centers in the registry using coordinates first, then incidences and relations."""
        sorted_nums = sorted(self.centers_by_num.keys())
        for _pass in range(4):
            progressed = False
            for num in sorted_nums:
                if num in self.bary_cache:
                    continue
                cdata = self.centers_by_num[num]
                bary = (
                    self._try_eval_coordinates(cdata)
                    or self._try_eval_incidence(cdata)
                    or self._try_eval_relations(cdata)
                )
                if bary and self._store(num, bary):
                    progressed = True
            if not progressed:
                break

        # Final fallback for centers with open/implicit definitions (e.g. X(368) "reasonable trilinears are sought")
        for num in sorted_nums:
            if num in self.bary_cache:
                continue
            cdata = self.centers_by_num[num]
            placed = False
            for inc in cdata.get("incidences") or []:
                for i_num, j_num in inc.get("lines") or []:
                    if i_num in self.bary_cache and j_num in self.bary_cache:
                        bi, bj = self.bary_cache[i_num], self.bary_cache[j_num]
                        if self._store(num, (bi[0] + bj[0], bi[1] + bj[1], bi[2] + bj[2])):
                            placed = True
                            break
                if placed:
                    break
            if not placed:
                self._store(num, (1.0, 1.0, 1.0))


# ---------------------------------------------------------------------------
# Fast Model Construction Helpers (compatible with `geometor.model.Model`)
# ---------------------------------------------------------------------------


def _add_point(
    model: Model,
    x: float,
    y: float,
    ID: str,
    classes: list[str] | None = None,
    parents: list[Any] | None = None,
    guide: bool = False,
) -> spg.Point:
    """Add a Point element directly to a `geometor.model.Model` with float/SymPy precision."""
    existing = model.get_element_by_ID(ID)
    if existing is not None and isinstance(existing, spg.Point):
        if classes:
            for c in classes:
                model[existing].classes[c] = ""
        if not guide:
            model[existing].guide = False
        return existing

    rx = round(float(x), 8)
    ry = round(float(y), 8)
    pt = spg.Point(sp.Float(rx), sp.Float(ry), evaluate=False)
    step = 0
    while pt in model and model[pt].ID != ID:
        step += 1
        pt = spg.Point(sp.Float(rx + step * 1e-7), sp.Float(ry), evaluate=False)
    el = Element(
        pt,
        parents=parents or [],
        classes=classes or [],
        ID=ID,
        guide=guide,
    )
    super(Model, model).__setitem__(pt, el)
    return pt


def _add_line(
    model: Model,
    pt1: spg.Point,
    pt2: spg.Point,
    ID: str = "",
    classes: list[str] | None = None,
    guide: bool = False,
) -> spg.Line | None:
    """Add a Line element between two points in `model`."""
    if pt1 == pt2 or math.hypot(float(pt1.x) - float(pt2.x), float(pt1.y) - float(pt2.y)) < 1e-5:
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


def _add_circle(
    model: Model,
    pt_center: spg.Point,
    pt_radius: spg.Point,
    ID: str = "",
    classes: list[str] | None = None,
    guide: bool = False,
) -> spg.Circle | None:
    """Add a CircleElement to `model` defined by center point and radius point."""
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


def _add_polygon(
    model: Model,
    pts: list[spg.Point],
    ID: str = "",
    classes: list[str] | None = None,
) -> spg.Polygon:
    """Add a Polygon element to `model`."""
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


def _add_segment(
    model: Model,
    pt1: spg.Point,
    pt2: spg.Point,
    ID: str = "",
    classes: list[str] | None = None,
) -> spg.Segment | None:
    """Add a Segment element to `model`."""
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


def _foot_of_perp(
    px: float, py: float, x1: float, y1: float, x2: float, y2: float
) -> tuple[float, float]:
    """Compute orthogonal projection of (px, py) onto line through (x1, y1) and (x2, y2)."""
    dx, dy = x2 - x1, y2 - y1
    len_sq = dx * dx + dy * dy
    if len_sq < 1e-14:
        return (x1, y1)
    t = ((px - x1) * dx + (py - y1) * dy) / len_sq
    return (x1 + t * dx, y1 + t * dy)


def _detect_clues(center_data: dict[str, Any]) -> dict[str, bool]:
    """Inspect a center's title and primary defining note for circle and triangle clues."""
    num = int(center_data.get("num") or 0)
    blobs = [center_data.get("title", "")] + (center_data.get("notes") or [])[:1]
    text = " ".join(blobs).lower()

    has_circumcircle = (
        num in {3, 6, 13, 14, 15, 16, 19, 20, 22, 23, 24, 25, 26, 55, 56, 74, 98, 99, 100}
        or "circumcircle" in text
        or "circumcenter" in text
        or "tarry" in text
        or "steiner" in text
    )
    has_incircle = (
        num in {1, 7, 8, 9, 11, 12, 55, 56, 57, 65}
        or "incircle" in text
        or "incenter" in text
        or "feuerbach" in text
        or "intouch" in text
    )
    has_nine_point = (
        num in {5, 11, 12}
        or "nine-point" in text
        or "feuerbach" in text
    )
    has_medial = (
        num in {2, 5, 9, 10}
        or "medial triangle" in text
        or "spieker" in text
        or "complement of" in text
    )
    has_orthic = (
        num in {4, 5, 19, 24, 25, 51, 52, 53, 54}
        or "orthic triangle" in text
        or "altitude" in text
    )
    has_intouch = (
        num in {1, 7, 55, 56, 57, 65}
        or "intouch triangle" in text
        or "contact triangle" in text
        or "gergonne" in text
    )
    has_extouch = (
        num in {8}
        or "extouch triangle" in text
        or "nagel" in text
    )
    has_tangential = (
        num in {6, 22, 25, 26}
        or "tangential triangle" in text
        or "symmedian" in text
    )
    has_equilateral = (
        num in {13, 14, 15, 16, 17, 18}
        or "equilateral" in text
        or "fermat" in text
        or "isogonic" in text
        or "napoleon" in text
    )
    has_brocard_circle = (
        num in {15, 16, 182}
        or "brocard circle" in text
    )
    has_orthocentroidal_circle = (
        num in {381}
        or "orthocentroidal circle" in text
    )
    has_fuhrmann_circle = (
        num in {427}
        or "fuhrmann circle" in text
    )

    return {
        "circumcircle": has_circumcircle,
        "incircle": has_incircle,
        "nine_point": has_nine_point,
        "medial": has_medial,
        "orthic": has_orthic,
        "intouch": has_intouch,
        "extouch": has_extouch,
        "tangential": has_tangential,
        "equilateral": has_equilateral,
        "brocard_circle": has_brocard_circle,
        "orthocentroidal_circle": has_orthocentroidal_circle,
        "fuhrmann_circle": has_fuhrmann_circle,
    }


def build_center_model(
    center_data: dict[str, Any],
    registry: CenterRegistry,
    include_baseline_guides: bool = True,
) -> Model:
    """Build a `geometor.model.Model` for `center_data` starting from the unit segment AB."""
    num = int(center_data["num"])
    key = center_data["key"]
    ctx = registry.ctx

    model = Model(f"{key} = {center_data.get('primary_title', '')}".strip(" ="), logger=_SILENT_LOGGER)

    # 1. Unit Segment Baseline A=(0,0), B=(1,0)
    A = _add_point(model, 0.0, 0.0, ID="A", classes=["given", "vertex"])
    B = _add_point(model, 1.0, 0.0, ID="B", classes=["given", "vertex"])
    _add_line(model, A, B, ID="[ A B ]", classes=["given", "sideline"])

    # 2. Euclid I.22 Guide Circles on Unit Segment AB to construct Vertex C
    if include_baseline_guides and num <= 5:
        R_b = _add_point(model, ctx.b, 0.0, ID="R_b", classes=["guide"], guide=True)
        R_a = _add_point(model, 1.0 - ctx.a, 0.0, ID="R_a", classes=["guide"], guide=True)
        cA = _add_circle(model, A, R_b, ID="( A R_b )", classes=["guide"], guide=True)
        cB = _add_circle(model, B, R_a, ID="( B R_a )", classes=["guide"], guide=True)
        C = _add_point(
            model,
            ctx.C_xy[0],
            ctx.C_xy[1],
            ID="C",
            classes=["vertex"],
            parents=[cA, cB],
        )
    else:
        C = _add_point(
            model,
            ctx.C_xy[0],
            ctx.C_xy[1],
            ID="C",
            classes=["vertex"],
        )

    _add_line(model, B, C, ID="[ B C ]", classes=["sideline"])
    _add_line(model, C, A, ID="[ C A ]", classes=["sideline"])
    _add_polygon(model, [A, B, C], ID="< A B C >", classes=["reference"])

    clues = _detect_clues(center_data)
    added_centers: dict[int, spg.Point] = {}

    def get_or_add_center_pt(c_num: int, is_target: bool = False) -> spg.Point | None:
        if c_num in added_centers:
            if is_target:
                model[added_centers[c_num]].classes["selected"] = ""
                model[added_centers[c_num]].classes["target"] = ""
            return added_centers[c_num]
        xy = registry.xy_cache.get(c_num)
        if xy is None:
            return None
        cls = ["selected", "target"] if is_target else ["center"]
        pt = _add_point(model, xy[0], xy[1], ID=f"X({c_num})", classes=cls)
        added_centers[c_num] = pt
        return pt

    # 3. Construct secondary triangles and circles indicated by clues
    Ax, Ay = ctx.A_xy
    Bx, By = ctx.B_xy
    Cx, Cy = ctx.C_xy

    # Medial triangle & Medians
    if clues["medial"] or clues["nine_point"]:
        Ma = _add_point(model, 0.5 * (Bx + Cx), 0.5 * (By + Cy), ID="M_a", classes=["midpoint"], guide=True)
        Mb = _add_point(model, 0.5 * (Cx + Ax), 0.5 * (Cy + Ay), ID="M_b", classes=["midpoint"], guide=True)
        Mc = _add_point(model, 0.5 * (Ax + Bx), 0.5 * (Ay + By), ID="M_c", classes=["midpoint"], guide=True)
        if clues["medial"]:
            _add_polygon(model, [Ma, Mb, Mc], ID="< M_a M_b M_c >", classes=["secondary"])
        if num == 2:
            _add_line(model, A, Ma, ID="[ A M_a ]", classes=["bisector"])
            _add_line(model, B, Mb, ID="[ B M_b ]", classes=["bisector"])
            _add_line(model, C, Mc, ID="[ C M_c ]", classes=["bisector"])

    # Orthic triangle & Altitudes
    if clues["orthic"]:
        Ha_xy = _foot_of_perp(Ax, Ay, Bx, By, Cx, Cy)
        Hb_xy = _foot_of_perp(Bx, By, Cx, Cy, Ax, Ay)
        Hc_xy = _foot_of_perp(Cx, Cy, Ax, Ay, Bx, By)
        Ha = _add_point(model, Ha_xy[0], Ha_xy[1], ID="H_a", classes=["foot"], guide=True)
        Hb = _add_point(model, Hb_xy[0], Hb_xy[1], ID="H_b", classes=["foot"], guide=True)
        Hc = _add_point(model, Hc_xy[0], Hc_xy[1], ID="H_c", classes=["foot"], guide=True)
        _add_polygon(model, [Ha, Hb, Hc], ID="< H_a H_b H_c >", classes=["secondary"])
        if num == 4:
            _add_line(model, A, Ha, ID="[ A H_a ]", classes=["bisector"])
            _add_line(model, B, Hb, ID="[ B H_b ]", classes=["bisector"])
            _add_line(model, C, Hc, ID="[ C H_c ]", classes=["bisector"])

    # Circumcircle & Perpendicular Bisectors
    if clues["circumcircle"]:
        X3 = get_or_add_center_pt(3, is_target=(num == 3))
        if X3 is not None:
            if num == 3:
                Ma = _add_point(model, 0.5 * (Bx + Cx), 0.5 * (By + Cy), ID="M_a", guide=True)
                Mb = _add_point(model, 0.5 * (Cx + Ax), 0.5 * (Cy + Ay), ID="M_b", guide=True)
                Mc = _add_point(model, 0.5 * (Ax + Bx), 0.5 * (Ay + By), ID="M_c", guide=True)
                _add_line(model, X3, Ma, ID="[ X(3) M_a ]", classes=["bisector"])
                _add_line(model, X3, Mb, ID="[ X(3) M_b ]", classes=["bisector"])
                _add_line(model, X3, Mc, ID="[ X(3) M_c ]", classes=["bisector"])
            _add_circle(model, X3, A, ID="circumcircle", classes=["circumcircle"])

    # Incircle & Intouch Triangle
    if clues["incircle"] or clues["intouch"]:
        X1 = get_or_add_center_pt(1, is_target=(num == 1))
        if X1 is not None:
            x1_xy = registry.xy_cache[1]
            Ta_xy = _foot_of_perp(x1_xy[0], x1_xy[1], Bx, By, Cx, Cy)
            Tb_xy = _foot_of_perp(x1_xy[0], x1_xy[1], Cx, Cy, Ax, Ay)
            Tc_xy = _foot_of_perp(x1_xy[0], x1_xy[1], Ax, Ay, Bx, By)
            Ta = _add_point(model, Ta_xy[0], Ta_xy[1], ID="T_a", guide=True)
            Tb = _add_point(model, Tb_xy[0], Tb_xy[1], ID="T_b", guide=True)
            Tc = _add_point(model, Tc_xy[0], Tc_xy[1], ID="T_c", guide=True)
            _add_circle(model, X1, Tc, ID="incircle", classes=["incircle"])
            if clues["intouch"]:
                _add_polygon(model, [Ta, Tb, Tc], ID="< T_a T_b T_c >", classes=["secondary"])
            if num == 1:
                _add_line(model, A, X1, ID="[ A X(1) ]", classes=["bisector"])
                _add_line(model, B, X1, ID="[ B X(1) ]", classes=["bisector"])
                _add_line(model, C, X1, ID="[ C X(1) ]", classes=["bisector"])
            elif num == 7:
                _add_line(model, A, Ta, ID="[ A T_a ]", classes=["bisector"])
                _add_line(model, B, Tb, ID="[ B T_b ]", classes=["bisector"])
                _add_line(model, C, Tc, ID="[ C T_c ]", classes=["bisector"])

    # Extouch Triangle & Nagel Cevians
    if clues["extouch"]:
        a, b, c = ctx.raw_a, ctx.raw_b, ctx.raw_c
        s = ctx.s
        Na_xy = ctx.bary_to_cartesian(0.0, s - c, s - b)
        Nb_xy = ctx.bary_to_cartesian(s - c, 0.0, s - a)
        Nc_xy = ctx.bary_to_cartesian(s - b, s - a, 0.0)
        if Na_xy and Nb_xy and Nc_xy:
            Na = _add_point(model, Na_xy[0], Na_xy[1], ID="N_a", guide=True)
            Nb = _add_point(model, Nb_xy[0], Nb_xy[1], ID="N_b", guide=True)
            Nc = _add_point(model, Nc_xy[0], Nc_xy[1], ID="N_c", guide=True)
            _add_polygon(model, [Na, Nb, Nc], ID="< N_a N_b N_c >", classes=["secondary"])
            if num == 8:
                _add_line(model, A, Na, ID="[ A N_a ]", classes=["bisector"])
                _add_line(model, B, Nb, ID="[ B N_b ]", classes=["bisector"])
                _add_line(model, C, Nc, ID="[ C N_c ]", classes=["bisector"])

    # Nine-Point Circle
    if clues["nine_point"]:
        X5 = get_or_add_center_pt(5, is_target=(num == 5))
        if X5 is not None:
            Mc_pt = model.get_element_by_ID("M_c")
            if Mc_pt is None:
                Mc_pt = _add_point(
                    model, 0.5 * (Ax + Bx), 0.5 * (Ay + By), ID="M_c", guide=True
                )
            _add_circle(model, X5, Mc_pt, ID="nine_point_circle", classes=["nine_point_circle"])

    # Spieker Circle (incircle of medial triangle) for X(10)
    if num == 10:
        X10 = get_or_add_center_pt(10, is_target=True)
        if X10 is not None:
            x10_xy = registry.xy_cache[10]
            Ma_xy = (0.5 * (Bx + Cx), 0.5 * (By + Cy))
            Mb_xy = (0.5 * (Cx + Ax), 0.5 * (Cy + Ay))
            sp_foot = _foot_of_perp(x10_xy[0], x10_xy[1], Ma_xy[0], Ma_xy[1], Mb_xy[0], Mb_xy[1])
            Sp_r = _add_point(model, sp_foot[0], sp_foot[1], ID="S_c", guide=True)
            _add_circle(model, X10, Sp_r, ID="spieker_circle", classes=["incircle"])

    # Brocard Circle (diameter X(3)X(6), center X(182))
    if clues.get("brocard_circle"):
        X3 = get_or_add_center_pt(3, is_target=(num == 3))
        X6 = get_or_add_center_pt(6, is_target=(num == 6))
        if X3 is not None and X6 is not None:
            x3_xy = registry.xy_cache[3]
            x6_xy = registry.xy_cache[6]
            X182 = _add_point(
                model,
                0.5 * (x3_xy[0] + x6_xy[0]),
                0.5 * (x3_xy[1] + x6_xy[1]),
                ID="X(182)",
                classes=["selected", "target"] if num == 182 else ["center"],
                guide=(num != 182),
            )
            added_centers[182] = X182
            _add_circle(model, X182, X3, ID="brocard_circle", classes=["secondary_circle"])

    # Orthocentroidal Circle (diameter X(2)X(4), center X(381))
    if clues.get("orthocentroidal_circle"):
        X2 = get_or_add_center_pt(2, is_target=(num == 2))
        X4 = get_or_add_center_pt(4, is_target=(num == 4))
        if X2 is not None and X4 is not None:
            x2_xy = registry.xy_cache[2]
            x4_xy = registry.xy_cache[4]
            X381 = _add_point(
                model,
                0.5 * (x2_xy[0] + x4_xy[0]),
                0.5 * (x2_xy[1] + x4_xy[1]),
                ID="X(381)",
                classes=["selected", "target"] if num == 381 else ["center"],
                guide=(num != 381),
            )
            added_centers[381] = X381
            _add_circle(model, X381, X2, ID="orthocentroidal_circle", classes=["secondary_circle"])

    # Fuhrmann Circle (diameter X(4)X(8), center X(427))
    if clues.get("fuhrmann_circle"):
        X4 = get_or_add_center_pt(4, is_target=(num == 4))
        X8 = get_or_add_center_pt(8, is_target=(num == 8))
        if X4 is not None and X8 is not None:
            x4_xy = registry.xy_cache[4]
            x8_xy = registry.xy_cache[8]
            X427 = _add_point(
                model,
                0.5 * (x4_xy[0] + x8_xy[0]),
                0.5 * (x4_xy[1] + x8_xy[1]),
                ID="X(427)",
                classes=["selected", "target"] if num == 427 else ["center"],
                guide=(num != 427),
            )
            added_centers[427] = X427
            _add_circle(model, X427, X4, ID="fuhrmann_circle", classes=["secondary_circle"])

    # Equilateral apexes for Fermat / Isodynamic / Napoleon points (X(13)..X(18))
    if clues["equilateral"]:
        sign = -1.0 if num in {14, 16, 18} else 1.0
        # Construct equilateral apexes on BC, CA, AB
        def _equilateral_apex(
            p1: tuple[float, float], p2: tuple[float, float], opp: tuple[float, float]
        ) -> tuple[float, float]:
            mx, my = 0.5 * (p1[0] + p2[0]), 0.5 * (p1[1] + p2[1])
            dx, dy = p2[0] - p1[0], p2[1] - p1[1]
            # Outward normal relative to opp
            nx, ny = -dy, dx
            if nx * (opp[0] - mx) + ny * (opp[1] - my) > 0:
                nx, ny = -nx, -ny
            h_factor = sign * (math.sqrt(3.0) / 2.0)
            return (mx + h_factor * nx, my + h_factor * ny)

        Ea_xy = _equilateral_apex((Bx, By), (Cx, Cy), (Ax, Ay))
        Eb_xy = _equilateral_apex((Cx, Cy), (Ax, Ay), (Bx, By))
        Ec_xy = _equilateral_apex((Ax, Ay), (Bx, By), (Cx, Cy))
        Ea = _add_point(model, Ea_xy[0], Ea_xy[1], ID="A'", guide=True)
        Eb = _add_point(model, Eb_xy[0], Eb_xy[1], ID="B'", guide=True)
        Ec = _add_point(model, Ec_xy[0], Ec_xy[1], ID="C'", guide=True)
        _add_polygon(model, [B, C, Ea], ID="< B C A' >", classes=["secondary"])
        _add_polygon(model, [C, A, Eb], ID="< C A B' >", classes=["secondary"])
        _add_polygon(model, [A, B, Ec], ID="< A B C' >", classes=["secondary"])
        if num in {13, 14}:
            _add_line(model, A, Ea, ID="[ A A' ]", classes=["bisector"])
            _add_line(model, B, Eb, ID="[ B B' ]", classes=["bisector"])
            _add_line(model, C, Ec, ID="[ C C' ]", classes=["bisector"])

    # 4. Add primary incident central lines {i, j} that construct or locate X(n)
    line_pairs: list[tuple[int, int]] = []
    for inc in center_data.get("incidences") or []:
        for i_num, j_num in inc.get("lines") or []:
            xy_i = registry.xy_cache.get(i_num)
            xy_j = registry.xy_cache.get(j_num)
            if xy_i is not None and xy_j is not None and i_num != j_num:
                if math.hypot(xy_i[0] - xy_j[0], xy_i[1] - xy_j[1]) > 1e-6:
                    line_pairs.append((i_num, j_num))

    # Prioritize lines whose defining centers are classical or precede num
    line_pairs.sort(key=lambda pair: (max(pair) > max(num, 6), pair[0] + pair[1]))
    chosen_lines = line_pairs[:3]

    for i_num, j_num in chosen_lines:
        pi = get_or_add_center_pt(i_num, is_target=(i_num == num))
        pj = get_or_add_center_pt(j_num, is_target=(j_num == num))
        if pi is not None and pj is not None:
            cls = ["golden", "euler"] if {i_num, j_num} <= {2, 3, 4, 5, 20, 30} else ["central_line"]
            _add_line(
                model,
                pi,
                pj,
                ID=f"{{ {i_num}, {j_num} }}",
                classes=cls,
            )

    # 5. Ensure target center X(n) is added last (topmost in SVG points group)
    target_pt = get_or_add_center_pt(num, is_target=True)

    # 5b. Add named circles from `(c_num; Circle Name, ...)` in notes if c_num is resolved
    if target_pt is not None:
        notes_text = " ".join(center_data.get("notes") or [])
        added_named_circles = 0
        for cm in re.finditer(
            r"\((\d+)\s*;\s*([A-Za-z0-9\-\'\s]+?circle)\s*[,;]",
            notes_text,
            re.IGNORECASE,
        ):
            c_center_num = int(cm.group(1))
            c_name_raw = " ".join(cm.group(2).split())
            if c_center_num in registry.xy_cache and c_center_num != num:
                c_ctr_pt = get_or_add_center_pt(c_center_num, is_target=False)
                if c_ctr_pt is not None:
                    _add_circle(
                        model,
                        c_ctr_pt,
                        target_pt,
                        ID=c_name_raw,
                        classes=["secondary_circle"],
                    )
                    added_named_circles += 1
                    if added_named_circles >= 2:
                        break

    if target_pt is not None:
        # Re-insert target_pt at the end of model dict so it renders on top
        el_data = model.pop(target_pt)
        super(Model, model).__setitem__(target_pt, el_data)

    return model


# ---------------------------------------------------------------------------
# Composable Python `model.py` Code Generator for Per-Center Folders
# ---------------------------------------------------------------------------

_CLASSICAL_CONSTRUCTOR_NAMES: dict[int, str] = {
    1: "incenter_of",
    2: "centroid_of",
    3: "circumcenter_of",
    4: "orthocenter_of",
    5: "nine_point_center_of",
    6: "symmedian_point_of",
    7: "gergonne_point_of",
    8: "nagel_point_of",
    9: "mittenpunkt_of",
    10: "spieker_center_of",
    11: "feuerbach_point_of",
}


def _get_cyclic_expr_spec(
    cdata: dict[str, Any], ctx: TriangleContext
) -> tuple[str, str] | None:
    """Return ('trilinear' | 'barycentric', expr_str) if `cdata` has an evaluable cyclic formula."""
    for t_line in cdata.get("trilinears") or []:
        expr = _prepare_formula_expr(t_line)
        if expr:
            res = _eval_cyclic(expr, ctx)
            if res and math.hypot(*res) > 1e-11:
                return ("trilinear", expr)
    for b_line in cdata.get("barycentrics") or []:
        expr = _prepare_formula_expr(b_line)
        if expr:
            res = _eval_cyclic(expr, ctx)
            if res and math.hypot(*res) > 1e-11:
                return ("barycentric", expr)
    return None


def _match_relation_spec(
    cdata: dict[str, Any], known_nums: set[int]
) -> tuple[str, list[int]] | None:
    """Return (operator_name, [arg_center_nums]) if `cdata` has a primary functional relation."""
    patterns: list[tuple[str, str]] = [
        ("isogonal_conjugate", r"^X\(\d+\)\s*=\s*(?:the\s+)?isogonal\s+conjugate\s+of\s+X\((\d+)\)\s*$"),
        ("isotomic_conjugate", r"^X\(\d+\)\s*=\s*(?:the\s+)?isotomic\s+conjugate\s+of\s+X\((\d+)\)\s*$"),
        ("complement", r"^X\(\d+\)\s*=\s*(?:the\s+)?complement\s+of\s+X\((\d+)\)\s*$"),
        ("anticomplement", r"^X\(\d+\)\s*=\s*(?:the\s+)?anticomplement\s+of\s+X\((\d+)\)\s*$"),
        ("midpoint", r"^X\(\d+\)\s*=\s*(?:the\s+)?midpoint\s+of\s+X\((\d+)\)\s+and\s+X\((\d+)\)\s*$"),
        ("reflection_in_point", r"^X\(\d+\)\s*=\s*(?:the\s+)?reflection\s+of\s+X\((\d+)\)\s+in\s+X\((\d+)\)\s*$"),
        ("ceva_conjugate", r"^X\(\d+\)\s*=\s*X\((\d+)\)-Ceva\s+conjugate\s+of\s+X\((\d+)\)\s*$"),
        ("crosspoint", r"^X\(\d+\)\s*=\s*(?:the\s+)?crosspoint\s+of\s+X\((\d+)\)\s+and\s+X\((\d+)\)\s*$"),
        ("cevapoint", r"^X\(\d+\)\s*=\s*(?:the\s+)?cevapoint\s+of\s+X\((\d+)\)\s+and\s+X\((\d+)\)\s*$"),
    ]
    for rel in cdata.get("relations") or []:
        rel_s = rel.strip()
        for op_name, pat in patterns:
            m = re.match(pat, rel_s, re.IGNORECASE)
            if m:
                args = [int(g) for g in m.groups()]
                if all(k in known_nums for k in args):
                    return (op_name, args)
    return None


def generate_center_model_py(
    center_data: dict[str, Any],
    registry: CenterRegistry,
) -> str:
    """Generate a standalone, composable `geometor.model` Python script (`model.py`) for `center_data`."""
    num = int(center_data["num"])
    key = center_data["key"]
    title = center_data.get("primary_title") or center_data.get("title") or key
    full_title = f"{key} = {title}" if title and title != key else key
    fn_name = f"construct_x_{num:05d}"

    clues = _detect_clues(center_data)
    ops_imports: set[str] = {
        "create_model",
        "construct_baseline_triangle",
        "promote_point_to_top",
    }
    body_lines: list[str] = []
    defined_vars: set[int] = set()

    def ensure_center_var(c_num: int, is_target: bool = False) -> str:
        var_name = f"X_{c_num}"
        if c_num in defined_vars and not is_target:
            return var_name

        cls_arg = '["selected", "target"]' if is_target else '["center"]'
        if c_num in _CLASSICAL_CONSTRUCTOR_NAMES:
            op_fn = _CLASSICAL_CONSTRUCTOR_NAMES[c_num]
            ops_imports.add(op_fn)
            extra = ""
            if is_target:
                if c_num == 1:
                    extra = ", draw_bisectors=True, draw_incircle=True"
                elif c_num == 2:
                    extra = ", draw_medians=True"
                elif c_num == 3:
                    extra = ", draw_bisectors=True, draw_circumcircle=True"
                elif c_num == 4:
                    extra = ", draw_altitudes=True"
                elif c_num == 5:
                    extra = ", draw_circle=True"
                elif c_num == 6:
                    extra = ", draw_symmedians=True"
                elif c_num in {7, 8}:
                    extra = ", draw_cevians=True"
                elif c_num == 10:
                    extra = ", draw_circle=True"
                elif c_num == 11:
                    extra = ", draw_circles=True"
            body_lines.append(
                f'    {var_name} = {op_fn}(model, A, B, C, ID="X({c_num})", classes={cls_arg}{extra})'
            )
            defined_vars.add(c_num)
            return var_name

        c_obj = registry.centers_by_num.get(c_num)
        if c_obj:
            spec = _get_cyclic_expr_spec(c_obj, registry.ctx)
            if spec:
                kind, expr_str = spec
                eval_fn = "eval_trilinear_point" if kind == "trilinear" else "eval_barycentric_point"
                ops_imports.add(eval_fn)
                body_lines.append(
                    f'    {var_name} = {eval_fn}(model, A, B, C, {expr_str!r}, ID="X({c_num})", classes={cls_arg})'
                )
                defined_vars.add(c_num)
                return var_name

        bary = registry.bary_cache.get(c_num, (1.0, 1.0, 1.0))
        ops_imports.add("point_from_barycentrics")
        body_lines.append(
            f'    {var_name} = point_from_barycentrics(model, A, B, C, {bary[0]:.8g}, {bary[1]:.8g}, {bary[2]:.8g}, ID="X({c_num})", classes={cls_arg})'
        )
        defined_vars.add(c_num)
        return var_name

    # 1. Secondary derived triangles and circles from clues (for non-classical or supplementary context)
    if clues["medial"] and num != 2 and num != 10:
        ops_imports.add("medial_triangle")
        body_lines.append("    medial_triangle(model, A, B, C)")
    if clues["orthic"] and num != 4:
        ops_imports.add("orthic_triangle")
        body_lines.append("    orthic_triangle(model, A, B, C)")
    if clues["intouch"] and num not in {1, 7}:
        ops_imports.add("intouch_triangle")
        body_lines.append("    intouch_triangle(model, A, B, C)")
    elif clues["incircle"] and num not in {1, 7, 11}:
        ops_imports.add("incircle")
        body_lines.append("    incircle(model, A, B, C)")
    if clues["extouch"] and num != 8:
        ops_imports.add("extouch_triangle")
        body_lines.append("    extouch_triangle(model, A, B, C)")
    if clues["tangential"] and num != 6:
        ops_imports.add("tangential_triangle")
        body_lines.append("    tangential_triangle(model, A, B, C)")
    elif clues["circumcircle"] and num not in {3, 6}:
        ops_imports.add("circumcircle")
        body_lines.append("    circumcircle(model, A, B, C)")
    if clues["nine_point"] and num not in {5, 11}:
        ops_imports.add("nine_point_circle")
        body_lines.append("    nine_point_circle(model, A, B, C)")
    if clues["equilateral"] and num not in {13, 14, 17, 18}:
        if num == 16:
            ops_imports.add("inner_equilateral_triangles")
            body_lines.append("    inner_equilateral_triangles(model, A, B, C)")
        else:
            ops_imports.add("outer_equilateral_triangles")
            body_lines.append("    outer_equilateral_triangles(model, A, B, C)")

    # 2. Incident central lines {i, j}
    line_pairs: list[tuple[int, int]] = []
    for inc in center_data.get("incidences") or []:
        for i_num, j_num in inc.get("lines") or []:
            xy_i = registry.xy_cache.get(i_num)
            xy_j = registry.xy_cache.get(j_num)
            if xy_i is not None and xy_j is not None and i_num != j_num:
                if math.hypot(xy_i[0] - xy_j[0], xy_i[1] - xy_j[1]) > 1e-6:
                    line_pairs.append((i_num, j_num))
    line_pairs.sort(key=lambda pair: (max(pair) > max(num, 6), pair[0] + pair[1]))
    chosen_lines = line_pairs[:3]

    for i_num, j_num in chosen_lines:
        vi = ensure_center_var(i_num, is_target=(i_num == num))
        vj = ensure_center_var(j_num, is_target=(j_num == num))
        ops_imports.add("central_line")
        body_lines.append(f"    central_line(model, {vi}, {vj}, {i_num}, {j_num})")

    # 3. Construct target center X(num)
    target_var = f"X_{num}"
    if num in _CLASSICAL_CONSTRUCTOR_NAMES:
        ensure_center_var(num, is_target=True)
    elif num in {13, 14}:
        tri_fn = "outer_equilateral_triangles" if num == 13 else "inner_equilateral_triangles"
        ops_imports.update({tri_fn, "perspector"})
        body_lines.append(f"    Ea, Eb, Ec = {tri_fn}(model, A, B, C)")
        body_lines.append(
            f'    {target_var} = perspector(model, A, B, C, Ea, Eb, Ec, ID="X({num})", classes=["selected", "target"])'
        )
    elif num in {17, 18}:
        tri_fn = "outer_napoleon_triangle" if num == 17 else "inner_napoleon_triangle"
        ops_imports.update({tri_fn, "perspector"})
        body_lines.append(f"    Na, Nb, Nc = {tri_fn}(model, A, B, C)")
        body_lines.append(
            f'    {target_var} = perspector(model, A, B, C, Na, Nb, Nc, ID="X({num})", classes=["selected", "target"])'
        )
    else:
        rel_spec = _match_relation_spec(center_data, set(registry.bary_cache.keys()))
        if rel_spec and all(k < num or k in defined_vars for k in rel_spec[1]):
            op_name, arg_nums = rel_spec
            arg_vars = [ensure_center_var(k) for k in arg_nums]
            ops_imports.add(op_name)
            if op_name in {"midpoint", "reflection_in_point"}:
                body_lines.append(
                    f'    {target_var} = {op_name}(model, {arg_vars[0]}, {arg_vars[1]}, ID="X({num})", classes=["selected", "target"], guide=False)'
                )
            elif len(arg_vars) == 1:
                body_lines.append(
                    f'    {target_var} = {op_name}(model, A, B, C, {arg_vars[0]}, ID="X({num})", classes=["selected", "target"])'
                )
            else:
                body_lines.append(
                    f'    {target_var} = {op_name}(model, A, B, C, {arg_vars[0]}, {arg_vars[1]}, ID="X({num})", classes=["selected", "target"])'
                )
        else:
            spec = _get_cyclic_expr_spec(center_data, registry.ctx)
            if spec:
                kind, expr_str = spec
                eval_fn = "eval_trilinear_point" if kind == "trilinear" else "eval_barycentric_point"
                ops_imports.add(eval_fn)
                body_lines.append(
                    f'    {target_var} = {eval_fn}(model, A, B, C, {expr_str!r}, ID="X({num})", classes=["selected", "target"])'
                )
            elif len(chosen_lines) >= 2:
                (i1, j1), (i2, j2) = chosen_lines[0], chosen_lines[1]
                ops_imports.add("intersect_lines")
                body_lines.append(
                    f'    {target_var} = intersect_lines(model, X_{i1}, X_{j1}, X_{i2}, X_{j2}, ID="X({num})", classes=["selected", "target"])'
                )
            else:
                ensure_center_var(num, is_target=True)

    body_lines.append(f"    return promote_point_to_top(model, {target_var})")

    sorted_imports = ",\n    ".join(sorted(ops_imports))
    show_guides_default = "True" if num <= 5 else "False"

    code = f'''"""GEOMETOR construction model for {full_title}."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    {sorted_imports},
)
from geometor.etc.render import write_center_svg


def {fn_name}(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct {full_title} on reference triangle ABC."""
{chr(10).join(body_lines)}


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = {show_guides_default},
) -> Model:
    """Build a `geometor.model.Model` for {key} on the given reference triangle."""
    model = create_model({full_title!r})
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    {fn_name}(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-{num:05d}.json"))
    write_center_svg(
        model_acute,
        here / "x-{num:05d}.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
'''
    return code

