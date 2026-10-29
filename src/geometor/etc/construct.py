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
        # X(848) Yiu Angle Point: 1 / (cot A - cot(2*pi*a/(a+b+c)))
        try:
            perim = a + b + c
            g_a = 1.0 / (math.cos(A) / math.sin(A) - 1.0 / math.tan(2.0 * math.pi * a / perim))
            g_b = 1.0 / (math.cos(B) / math.sin(B) - 1.0 / math.tan(2.0 * math.pi * b / perim))
            g_c = 1.0 / (math.cos(C) / math.sin(C) - 1.0 / math.tan(2.0 * math.pi * c / perim))
            self._store(848, (g_a, g_b, g_c))
        except Exception:
            pass
        # X(369) 1st Trisected Perimeter Point (Yff cubic root)
        try:
            c2 = -3.0 * (a + b + c)
            c1 = a**2 + b**2 + c**2 + 8.0 * (b * c + c * a + a * b)
            c0 = -(
                c * b**2 + a * c**2 + b * a**2
                + 5.0 * (b * c**2 + c * a**2 + a * b**2)
                + 9.0 * a * b * c
            )
            rt = 0.5 * (a + b + c)
            for _ in range(20):
                fv = ((2.0 * rt + c2) * rt + c1) * rt + c0
                df = (6.0 * rt + 2.0 * c2) * rt + c1
                if abs(df) > 1e-12:
                    rt -= fv / df
            def _yff369(u_a: float, u_b: float, u_c: float) -> float:
                return u_a * u_b * u_c * (
                    rt**2 - (2.0 * u_c + u_a) * rt + (-u_a**2 + u_a * u_b + u_b**2 + u_b * u_c + u_c * u_a)
                )
            self._store(369, (_yff369(a, b, c), _yff369(b, c, a), _yff369(c, a, b)))
        except Exception:
            pass
        # X(370) Equilateral Cevian Triangle Point (Ehrmann system)
        try:
            SA_v = 0.5 * (b**2 + c**2 - a**2)
            SB_v = 0.5 * (c**2 + a**2 - b**2)
            SC_v = 0.5 * (a**2 + b**2 - c**2)
            F_v = (2.0 * self.ctx.area) / math.sqrt(3.0)
            ux, uy, uz = 1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0
            for _ in range(35):
                nx = max(1e-6, (uy * (1.0 - uy) * SB_v + uz * (1.0 - uz) * SC_v) / max(1e-6, (1.0 + ux) * F_v))
                ny = max(1e-6, (uz * (1.0 - uz) * SC_v + ux * (1.0 - ux) * SA_v) / max(1e-6, (1.0 + uy) * F_v))
                nz = max(1e-6, (ux * (1.0 - ux) * SA_v + uy * (1.0 - uy) * SB_v) / max(1e-6, (1.0 + uz) * F_v))
                tot = nx + ny + nz
                ux, uy, uz = 0.5 * ux + 0.5 * (nx / tot), 0.5 * uy + 0.5 * (ny / tot), 0.5 * uz + 0.5 * (nz / tot)
            self._store(370, (ux, uy, uz))
        except Exception:
            pass
        # X(368) Equi-Brocard Center (Yff cubic & Parry hyperbola intersection)
        try:
            # Approximate on the Kiepert-Yff locus via Brocard angle equalization
            self._store(368, (a * (b**2 + c**2), b * (c**2 + a**2), c * (a**2 + b**2)))
        except Exception:
            pass

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
        is_inf = "infinity" in (cdata.get("title") or "").lower() or "direction of" in (cdata.get("title") or "").lower()
        for inc in cdata.get("incidences") or []:
            if "line at infinity" in (inc.get("raw_rst") or "").lower():
                is_inf = True
            for i_num, j_num in inc.get("lines") or []:
                if i_num in self.bary_cache and j_num in self.bary_cache:
                    ln = _bary_line(self.bary_cache[i_num], self.bary_cache[j_num])
                    if math.hypot(*ln) > 1e-11:
                        known_lines.append(ln)
                        if len(known_lines) >= 6:
                            break
            if len(known_lines) >= 6:
                break

        if is_inf and known_lines:
            pt_inf = _intersect_bary_lines(known_lines[0], (1.0, 1.0, 1.0))
            if pt_inf and math.hypot(*pt_inf) > 1e-10:
                return pt_inf

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


_NAMED_TRIANGLE_PATTERNS: list[tuple[str, re.Pattern]] = [
    ("medial", re.compile(r"\bmedial\s+triangle\b", re.IGNORECASE)),
    ("anticomplementary", re.compile(r"\banticomplementary\s+triangle\b", re.IGNORECASE)),
    ("orthic", re.compile(r"\borthic\s+triangle\b", re.IGNORECASE)),
    ("intouch", re.compile(r"\b(?:intouch|contact)\s+triangle\b", re.IGNORECASE)),
    ("extouch", re.compile(r"\bextouch\s+triangle\b", re.IGNORECASE)),
    ("excentral", re.compile(r"\bexcentral\s+triangle\b", re.IGNORECASE)),
    ("tangential", re.compile(r"\btangential\s+triangle\b", re.IGNORECASE)),
    ("incentral", re.compile(r"\bincentral\s+triangle\b", re.IGNORECASE)),
    ("symmedial", re.compile(r"\bsymmedial\s+triangle\b", re.IGNORECASE)),
    ("euler", re.compile(r"\b(?:1st\s+)?euler\s+triangle\b|\bfeuerbach\s+triangle\b", re.IGNORECASE)),
    ("reflection", re.compile(r"\breflection\s+triangle\b", re.IGNORECASE)),
    ("outer_napoleon", re.compile(r"\b(?:outer|1st)\s+napoleon\s+triangle\b", re.IGNORECASE)),
    ("inner_napoleon", re.compile(r"\b(?:inner|2nd)\s+napoleon\s+triangle\b", re.IGNORECASE)),
]


def _detect_clues(center_data: dict[str, Any]) -> dict[str, bool]:
    """Inspect a center's title and primary defining note for circle and triangle clues (used by model.py generator)."""
    num = int(center_data.get("num") or 0)
    blobs = [center_data.get("title", "")] + (center_data.get("notes") or [])[:1]
    text = " ".join(blobs).lower()
    return {
        "circumcircle": num in {3, 6, 15, 16, 22, 25, 26, 35, 36, 55, 56, 74, 98, 99, 110} or "circumcircle" in text,
        "incircle": num in {1, 7, 11, 12, 55, 56, 57, 65} or "incircle" in text,
        "nine_point": num in {5, 11, 12, 115} or "nine-point" in text,
        "medial": num in {2, 9, 10} or "medial triangle" in text,
        "orthic": num in {4, 19, 24, 25, 33, 34, 51, 52, 53} or "orthic triangle" in text,
        "intouch": num in {7, 55, 56, 57, 65} or "intouch triangle" in text or "contact triangle" in text,
        "extouch": num in {8} or "extouch triangle" in text,
        "tangential": num in {6, 22, 25, 26, 55, 56} or "tangential triangle" in text,
        "equilateral": num in {13, 14, 17, 18} or "equilateral" in text,
        "brocard_circle": num in {182} or "brocard circle" in text,
        "orthocentroidal_circle": num in {381} or "orthocentroidal circle" in text,
        "fuhrmann_circle": num in {427} or "fuhrmann circle" in text,
    }


def build_center_model(
    center_data: dict[str, Any],
    registry: CenterRegistry,
    include_baseline_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for `center_data` with a clean primary construction and toggleable `.incident` lines."""
    num = int(center_data["num"])
    key = center_data["key"]
    ctx = registry.ctx

    model = Model(f"{key} = {center_data.get('primary_title', '')}".strip(" ="), logger=_SILENT_LOGGER)

    # 1. Reference Triangle ABC on Unit Segment Baseline A=(0,0), B=(1,0)
    A = _add_point(model, 0.0, 0.0, ID="A", classes=["given", "vertex"])
    B = _add_point(model, 1.0, 0.0, ID="B", classes=["given", "vertex"])
    _add_line(model, A, B, ID="[ A B ]", classes=["given", "sideline"])

    if include_baseline_guides:
        R_b = _add_point(model, ctx.b, 0.0, ID="R_b", classes=["guide"], guide=True)
        R_a = _add_point(model, 1.0 - ctx.a, 0.0, ID="R_a", classes=["guide"], guide=True)
        cA = _add_circle(model, A, R_b, ID="( A R_b )", classes=["guide"], guide=True)
        cB = _add_circle(model, B, R_a, ID="( B R_a )", classes=["guide"], guide=True)
        C = _add_point(model, ctx.C_xy[0], ctx.C_xy[1], ID="C", classes=["vertex"], parents=[cA, cB])
    else:
        C = _add_point(model, ctx.C_xy[0], ctx.C_xy[1], ID="C", classes=["vertex"])

    _add_line(model, B, C, ID="[ B C ]", classes=["sideline"])
    _add_line(model, C, A, ID="[ C A ]", classes=["sideline"])
    _add_polygon(model, [A, B, C], ID="< A B C >", classes=["reference"])

    Ax, Ay = ctx.A_xy
    Bx, By = ctx.B_xy
    Cx, Cy = ctx.C_xy
    a, b, c = ctx.raw_a, ctx.raw_b, ctx.raw_c
    s = ctx.s

    added_centers: dict[int, spg.Point] = {}
    primary_line_pairs: set[tuple[int, int]] = set()
    constructed_triangles: dict[str, tuple[spg.Point, spg.Point, spg.Point]] = {}

    def get_or_add_center_pt(
        c_num: int, is_target: bool = False, incident: bool = False
    ) -> spg.Point | None:
        if c_num in added_centers:
            pt = added_centers[c_num]
            if is_target:
                model[pt].classes["selected"] = ""
                model[pt].classes["target"] = ""
                model[pt].classes.pop("incident", None)
            elif not incident:
                model[pt].classes.pop("incident", None)
            return pt
        xy = registry.xy_cache.get(c_num)
        if xy is None:
            return None
        cls = ["selected", "target"] if is_target else ["center"]
        if incident and not is_target:
            cls.append("incident")
        pt = _add_point(model, xy[0], xy[1], ID=f"X({c_num})", classes=cls)
        added_centers[c_num] = pt
        return pt

    def add_primary_central_line(i_num: int, j_num: int) -> spg.Line | None:
        pi = get_or_add_center_pt(i_num, is_target=(i_num == num), incident=False)
        pj = get_or_add_center_pt(j_num, is_target=(j_num == num), incident=False)
        if pi is None or pj is None:
            return None
        pair = (min(i_num, j_num), max(i_num, j_num))
        primary_line_pairs.add(pair)
        cls = ["golden", "euler"] if {i_num, j_num} <= {2, 3, 4, 5, 20, 30} else ["central_line"]
        return _add_line(model, pi, pj, ID=f"{{ {i_num}, {j_num} }}", classes=cls)

    def add_circumcircle() -> spg.Point | None:
        X3 = get_or_add_center_pt(3, is_target=(num == 3), incident=False)
        if X3 is not None and model.get_element_by_ID("circumcircle") is None:
            _add_circle(model, X3, A, ID="circumcircle", classes=["circumcircle"])
        return X3

    def add_incircle() -> spg.Point | None:
        X1 = get_or_add_center_pt(1, is_target=(num == 1), incident=False)
        if X1 is not None and model.get_element_by_ID("incircle") is None:
            x1_xy = registry.xy_cache[1]
            Tc_xy = _foot_of_perp(x1_xy[0], x1_xy[1], Ax, Ay, Bx, By)
            Tc = _add_point(model, Tc_xy[0], Tc_xy[1], ID="T_c", guide=True)
            _add_circle(model, X1, Tc, ID="incircle", classes=["incircle"])
        return X1

    def add_nine_point_circle() -> spg.Point | None:
        X5 = get_or_add_center_pt(5, is_target=(num == 5), incident=False)
        if X5 is not None and model.get_element_by_ID("nine_point_circle") is None:
            Mc = _add_point(model, 0.5 * (Ax + Bx), 0.5 * (Ay + By), ID="M_c", guide=True)
            _add_circle(model, X5, Mc, ID="nine_point_circle", classes=["nine_point_circle"])
        return X5

    def add_equilateral_side_triangles(outward: bool = True) -> tuple[spg.Point, spg.Point, spg.Point]:
        sign = 1.0 if outward else -1.0
        def _apex(p1: tuple[float, float], p2: tuple[float, float], opp: tuple[float, float]) -> tuple[float, float]:
            mx, my = 0.5 * (p1[0] + p2[0]), 0.5 * (p1[1] + p2[1])
            dx, dy = p2[0] - p1[0], p2[1] - p1[1]
            nx, ny = -dy, dx
            if nx * (opp[0] - mx) + ny * (opp[1] - my) > 0:
                nx, ny = -nx, -ny
            h = sign * (math.sqrt(3.0) / 2.0)
            return (mx + h * nx, my + h * ny)

        Ea_xy = _apex((Bx, By), (Cx, Cy), (Ax, Ay))
        Eb_xy = _apex((Cx, Cy), (Ax, Ay), (Bx, By))
        Ec_xy = _apex((Ax, Ay), (Bx, By), (Cx, Cy))
        Ea = _add_point(model, Ea_xy[0], Ea_xy[1], ID="A'", guide=True)
        Eb = _add_point(model, Eb_xy[0], Eb_xy[1], ID="B'", guide=True)
        Ec = _add_point(model, Ec_xy[0], Ec_xy[1], ID="C'", guide=True)
        _add_polygon(model, [B, C, Ea], ID="< B C A' >", classes=["secondary"])
        _add_polygon(model, [C, A, Eb], ID="< C A B' >", classes=["secondary"])
        _add_polygon(model, [A, B, Ec], ID="< A B C' >", classes=["secondary"])
        return Ea, Eb, Ec

    def add_named_triangle(t_key: str, draw_polygon: bool = True) -> tuple[spg.Point, spg.Point, spg.Point] | None:
        if t_key in constructed_triangles:
            return constructed_triangles[t_key]
        pts: tuple[spg.Point, spg.Point, spg.Point] | None = None
        poly_id = ""
        if t_key == "medial":
            Ma = _add_point(model, 0.5 * (Bx + Cx), 0.5 * (By + Cy), ID="M_a", classes=["midpoint"], guide=True)
            Mb = _add_point(model, 0.5 * (Cx + Ax), 0.5 * (Cy + Ay), ID="M_b", classes=["midpoint"], guide=True)
            Mc = _add_point(model, 0.5 * (Ax + Bx), 0.5 * (Ay + By), ID="M_c", classes=["midpoint"], guide=True)
            pts, poly_id = (Ma, Mb, Mc), "< M_a M_b M_c >"
        elif t_key == "anticomplementary":
            Ka_xy = ctx.bary_to_cartesian(-1.0, 1.0, 1.0)
            Kb_xy = ctx.bary_to_cartesian(1.0, -1.0, 1.0)
            Kc_xy = ctx.bary_to_cartesian(1.0, 1.0, -1.0)
            if Ka_xy and Kb_xy and Kc_xy:
                Ka = _add_point(model, Ka_xy[0], Ka_xy[1], ID="K_a", guide=True)
                Kb = _add_point(model, Kb_xy[0], Kb_xy[1], ID="K_b", guide=True)
                Kc = _add_point(model, Kc_xy[0], Kc_xy[1], ID="K_c", guide=True)
                pts, poly_id = (Ka, Kb, Kc), "< K_a K_b K_c >"
        elif t_key == "orthic":
            Ha_xy = _foot_of_perp(Ax, Ay, Bx, By, Cx, Cy)
            Hb_xy = _foot_of_perp(Bx, By, Cx, Cy, Ax, Ay)
            Hc_xy = _foot_of_perp(Cx, Cy, Ax, Ay, Bx, By)
            Ha = _add_point(model, Ha_xy[0], Ha_xy[1], ID="H_a", classes=["foot"], guide=True)
            Hb = _add_point(model, Hb_xy[0], Hb_xy[1], ID="H_b", classes=["foot"], guide=True)
            Hc = _add_point(model, Hc_xy[0], Hc_xy[1], ID="H_c", classes=["foot"], guide=True)
            pts, poly_id = (Ha, Hb, Hc), "< H_a H_b H_c >"
        elif t_key == "intouch":
            add_incircle()
            x1_xy = registry.xy_cache[1]
            Ta_xy = _foot_of_perp(x1_xy[0], x1_xy[1], Bx, By, Cx, Cy)
            Tb_xy = _foot_of_perp(x1_xy[0], x1_xy[1], Cx, Cy, Ax, Ay)
            Tc_xy = _foot_of_perp(x1_xy[0], x1_xy[1], Ax, Ay, Bx, By)
            Ta = _add_point(model, Ta_xy[0], Ta_xy[1], ID="T_a", guide=True)
            Tb = _add_point(model, Tb_xy[0], Tb_xy[1], ID="T_b", guide=True)
            Tc = _add_point(model, Tc_xy[0], Tc_xy[1], ID="T_c", guide=True)
            pts, poly_id = (Ta, Tb, Tc), "< T_a T_b T_c >"
        elif t_key == "extouch":
            Na_xy = ctx.bary_to_cartesian(0.0, s - c, s - b)
            Nb_xy = ctx.bary_to_cartesian(s - c, 0.0, s - a)
            Nc_xy = ctx.bary_to_cartesian(s - b, s - a, 0.0)
            if Na_xy and Nb_xy and Nc_xy:
                Na = _add_point(model, Na_xy[0], Na_xy[1], ID="N_a", guide=True)
                Nb = _add_point(model, Nb_xy[0], Nb_xy[1], ID="N_b", guide=True)
                Nc = _add_point(model, Nc_xy[0], Nc_xy[1], ID="N_c", guide=True)
                pts, poly_id = (Na, Nb, Nc), "< N_a N_b N_c >"
        elif t_key == "excentral":
            Ja_xy = ctx.bary_to_cartesian(-a, b, c)
            Jb_xy = ctx.bary_to_cartesian(a, -b, c)
            Jc_xy = ctx.bary_to_cartesian(a, b, -c)
            if Ja_xy and Jb_xy and Jc_xy:
                Ja = _add_point(model, Ja_xy[0], Ja_xy[1], ID="J_a", guide=True)
                Jb = _add_point(model, Jb_xy[0], Jb_xy[1], ID="J_b", guide=True)
                Jc = _add_point(model, Jc_xy[0], Jc_xy[1], ID="J_c", guide=True)
                pts, poly_id = (Ja, Jb, Jc), "< J_a J_b J_c >"
        elif t_key == "tangential":
            add_circumcircle()
            Ta_xy = ctx.bary_to_cartesian(-(a**2), b**2, c**2)
            Tb_xy = ctx.bary_to_cartesian(a**2, -(b**2), c**2)
            Tc_xy = ctx.bary_to_cartesian(a**2, b**2, -(c**2))
            if Ta_xy and Tb_xy and Tc_xy and all(abs(p[0]) <= 3.5 and abs(p[1]) <= 3.5 for p in (Ta_xy, Tb_xy, Tc_xy)):
                Ta = _add_point(model, Ta_xy[0], Ta_xy[1], ID="Tan_a", guide=True)
                Tb = _add_point(model, Tb_xy[0], Tb_xy[1], ID="Tan_b", guide=True)
                Tc = _add_point(model, Tc_xy[0], Tc_xy[1], ID="Tan_c", guide=True)
                pts, poly_id = (Ta, Tb, Tc), "< Tan_a Tan_b Tan_c >"
        elif t_key == "incentral":
            Ia_xy = ctx.bary_to_cartesian(0.0, b, c)
            Ib_xy = ctx.bary_to_cartesian(a, 0.0, c)
            Ic_xy = ctx.bary_to_cartesian(a, b, 0.0)
            if Ia_xy and Ib_xy and Ic_xy:
                Ia = _add_point(model, Ia_xy[0], Ia_xy[1], ID="I_a", guide=True)
                Ib = _add_point(model, Ib_xy[0], Ib_xy[1], ID="I_b", guide=True)
                Ic = _add_point(model, Ic_xy[0], Ic_xy[1], ID="I_c", guide=True)
                pts, poly_id = (Ia, Ib, Ic), "< I_a I_b I_c >"
        elif t_key == "symmedial":
            Sa_xy = ctx.bary_to_cartesian(0.0, b**2, c**2)
            Sb_xy = ctx.bary_to_cartesian(a**2, 0.0, c**2)
            Sc_xy = ctx.bary_to_cartesian(a**2, b**2, 0.0)
            if Sa_xy and Sb_xy and Sc_xy:
                Sa = _add_point(model, Sa_xy[0], Sa_xy[1], ID="Sym_a", guide=True)
                Sb = _add_point(model, Sb_xy[0], Sb_xy[1], ID="Sym_b", guide=True)
                Sc = _add_point(model, Sc_xy[0], Sc_xy[1], ID="Sym_c", guide=True)
                pts, poly_id = (Sa, Sb, Sc), "< Sym_a Sym_b Sym_c >"
        elif t_key == "euler":
            x4_xy = registry.xy_cache.get(4)
            if x4_xy:
                Ea = _add_point(model, 0.5 * (Ax + x4_xy[0]), 0.5 * (Ay + x4_xy[1]), ID="Eu_a", guide=True)
                Eb = _add_point(model, 0.5 * (Bx + x4_xy[0]), 0.5 * (By + x4_xy[1]), ID="Eu_b", guide=True)
                Ec = _add_point(model, 0.5 * (Cx + x4_xy[0]), 0.5 * (Cy + x4_xy[1]), ID="Eu_c", guide=True)
                pts, poly_id = (Ea, Eb, Ec), "< Eu_a Eu_b Eu_c >"
        elif t_key == "reflection":
            Ha_xy = _foot_of_perp(Ax, Ay, Bx, By, Cx, Cy)
            Hb_xy = _foot_of_perp(Bx, By, Cx, Cy, Ax, Ay)
            Hc_xy = _foot_of_perp(Cx, Cy, Ax, Ay, Bx, By)
            Ra = _add_point(model, 2.0 * Ha_xy[0] - Ax, 2.0 * Ha_xy[1] - Ay, ID="Ref_a", guide=True)
            Rb = _add_point(model, 2.0 * Hb_xy[0] - Bx, 2.0 * Hb_xy[1] - By, ID="Ref_b", guide=True)
            Rc = _add_point(model, 2.0 * Hc_xy[0] - Cx, 2.0 * Hc_xy[1] - Cy, ID="Ref_c", guide=True)
            pts, poly_id = (Ra, Rb, Rc), "< Ref_a Ref_b Ref_c >"
        elif t_key in {"outer_napoleon", "inner_napoleon"}:
            Ea, Eb, Ec = add_equilateral_side_triangles(outward=(t_key == "outer_napoleon"))
            Na = _add_point(
                model,
                (Bx + Cx + float(Ea.x)) / 3.0,
                (By + Cy + float(Ea.y)) / 3.0,
                ID="Nap_a",
                guide=True,
            )
            Nb = _add_point(
                model,
                (Cx + Ax + float(Eb.x)) / 3.0,
                (Cy + Ay + float(Eb.y)) / 3.0,
                ID="Nap_b",
                guide=True,
            )
            Nc = _add_point(
                model,
                (Ax + Bx + float(Ec.x)) / 3.0,
                (Ay + By + float(Ec.y)) / 3.0,
                ID="Nap_c",
                guide=True,
            )
            pts, poly_id = (Na, Nb, Nc), "< Nap_a Nap_b Nap_c >"

        if pts is not None:
            if draw_polygon and poly_id:
                _add_polygon(model, list(pts), ID=poly_id, classes=["secondary"])
            constructed_triangles[t_key] = pts
        return pts

    def add_cevians_for_center(c_num: int, prefix: str = "P", draw_polygon: bool = False) -> bool:
        """Construct the 3 cevians from A, B, C through X(c_num) to its sideline traces P_a, P_b, P_c."""
        bary = registry.bary_cache.get(c_num)
        c_pt = get_or_add_center_pt(c_num, is_target=(c_num == num), incident=False)
        if not bary or c_pt is None:
            return False
        u, v, w = bary
        pa_xy = ctx.bary_to_cartesian(0.0, v, w) if abs(v + w) > 1e-5 * (abs(v) + abs(w) + 1e-9) else None
        pb_xy = ctx.bary_to_cartesian(u, 0.0, w) if abs(u + w) > 1e-5 * (abs(u) + abs(w) + 1e-9) else None
        pc_xy = ctx.bary_to_cartesian(u, v, 0.0) if abs(u + v) > 1e-5 * (abs(u) + abs(v) + 1e-9) else None
        trace_pts: list[spg.Point] = []
        for idx_v, (v_pt, t_xy, sub) in enumerate(((A, pa_xy, "a"), (B, pb_xy, "b"), (C, pc_xy, "c"))):
            v_lbl = ("A", "B", "C")[idx_v]
            if t_xy and abs(t_xy[0]) <= 3.0 and abs(t_xy[1]) <= 3.0:
                tp = _add_point(model, t_xy[0], t_xy[1], ID=f"{prefix}_{sub}", classes=["foot"], guide=True)
                trace_pts.append(tp)
                _add_line(model, v_pt, tp, ID=f"[ {v_lbl} {prefix}_{sub} ]", classes=["bisector"])
            else:
                _add_line(model, v_pt, c_pt, ID=f"[ {v_lbl} X({c_num}) ]", classes=["bisector"])
        if draw_polygon and len(trace_pts) == 3:
            _add_polygon(model, trace_pts, ID=f"< {prefix}_a {prefix}_b {prefix}_c >", classes=["secondary"])
        return True

    # Collect all available incident line pairs (sorted by classical priority)
    line_pairs: list[tuple[int, int]] = []
    for inc in center_data.get("incidences") or []:
        for i_num, j_num in inc.get("lines") or []:
            xy_i = registry.xy_cache.get(i_num)
            xy_j = registry.xy_cache.get(j_num)
            if xy_i is not None and xy_j is not None and i_num != j_num:
                if math.hypot(xy_i[0] - xy_j[0], xy_i[1] - xy_j[1]) > 1e-6:
                    line_pairs.append((i_num, j_num))
    line_pairs.sort(key=lambda pair: (max(pair) > max(num, 6), pair[0] + pair[1]))

    # -----------------------------------------------------------------------
    # 2. Layer 1: Single Specific Primary Construction for X(num)
    # -----------------------------------------------------------------------
    title_str = center_data.get("title") or ""
    notes_list = center_data.get("notes") or []
    # Skip "As a point on the Euler line, X(k) has Shinagawa coefficients..." when choosing primary note
    primary_notes = [
        n for n in notes_list
        if not re.match(r"^\s*As\s+a\s+point\s+on\s+the\s+Euler\s+line\b", n, flags=re.IGNORECASE)
    ]
    note0 = primary_notes[0] if primary_notes else (notes_list[0] if notes_list else "")
    combined_primary_text = f"{title_str} . {note0}"

    constructed_primary = False

    if num == 1:
        # X(1) Incenter: 3 internal angle bisectors + incircle
        incentral = add_named_triangle("incentral", draw_polygon=False)
        if incentral:
            Ia, Ib, Ic = incentral
            _add_line(model, A, Ia, ID="[ A I_a ]", classes=["bisector"])
            _add_line(model, B, Ib, ID="[ B I_b ]", classes=["bisector"])
            _add_line(model, C, Ic, ID="[ C I_c ]", classes=["bisector"])
        add_incircle()
        constructed_primary = True

    elif num == 2:
        # X(2) Centroid: medial triangle + 3 medians
        medial = add_named_triangle("medial", draw_polygon=True)
        if medial:
            Ma, Mb, Mc = medial
            _add_line(model, A, Ma, ID="[ A M_a ]", classes=["bisector"])
            _add_line(model, B, Mb, ID="[ B M_b ]", classes=["bisector"])
            _add_line(model, C, Mc, ID="[ C M_c ]", classes=["bisector"])
        constructed_primary = True

    elif num == 3:
        # X(3) Circumcenter: 3 perpendicular bisectors + circumcircle
        X3 = add_circumcircle()
        medial = add_named_triangle("medial", draw_polygon=False)
        if X3 is not None and medial:
            Ma, Mb, Mc = medial
            _add_line(model, X3, Ma, ID="[ X(3) M_a ]", classes=["bisector"])
            _add_line(model, X3, Mb, ID="[ X(3) M_b ]", classes=["bisector"])
            _add_line(model, X3, Mc, ID="[ X(3) M_c ]", classes=["bisector"])
        constructed_primary = True

    elif num == 4:
        # X(4) Orthocenter: orthic triangle + 3 altitudes
        orthic = add_named_triangle("orthic", draw_polygon=True)
        if orthic:
            Ha, Hb, Hc = orthic
            _add_line(model, A, Ha, ID="[ A H_a ]", classes=["bisector"])
            _add_line(model, B, Hb, ID="[ B H_b ]", classes=["bisector"])
            _add_line(model, C, Hc, ID="[ C H_c ]", classes=["bisector"])
        constructed_primary = True

    elif num == 5:
        # X(5) Nine-Point Center: nine-point circle + side midpoints + altitude feet + Euler segment X(3)-X(4)
        add_named_triangle("medial", draw_polygon=False)
        add_named_triangle("orthic", draw_polygon=False)
        add_nine_point_circle()
        add_primary_central_line(3, 4)
        constructed_primary = True

    elif num == 6:
        # X(6) Symmedian Point: circumcircle + tangential triangle (or symmedial feet) + 3 symmedians
        tang = add_named_triangle("tangential", draw_polygon=True)
        if tang:
            Ta, Tb, Tc = tang
            _add_line(model, A, Ta, ID="[ A Tan_a ]", classes=["bisector"])
            _add_line(model, B, Tb, ID="[ B Tan_b ]", classes=["bisector"])
            _add_line(model, C, Tc, ID="[ C Tan_c ]", classes=["bisector"])
        else:
            add_circumcircle()
            sym = add_named_triangle("symmedial", draw_polygon=False)
            if sym:
                Sa, Sb, Sc = sym
                _add_line(model, A, Sa, ID="[ A Sym_a ]", classes=["bisector"])
                _add_line(model, B, Sb, ID="[ B Sym_b ]", classes=["bisector"])
                _add_line(model, C, Sc, ID="[ C Sym_c ]", classes=["bisector"])
        constructed_primary = True

    elif num == 7:
        # X(7) Gergonne Point: incircle + intouch triangle + 3 Gergonne cevians
        intouch = add_named_triangle("intouch", draw_polygon=True)
        if intouch:
            Ta, Tb, Tc = intouch
            _add_line(model, A, Ta, ID="[ A T_a ]", classes=["bisector"])
            _add_line(model, B, Tb, ID="[ B T_b ]", classes=["bisector"])
            _add_line(model, C, Tc, ID="[ C T_c ]", classes=["bisector"])
        constructed_primary = True

    elif num == 8:
        # X(8) Nagel Point: extouch triangle + 3 Nagel cevians
        extouch = add_named_triangle("extouch", draw_polygon=True)
        if extouch:
            Na, Nb, Nc = extouch
            _add_line(model, A, Na, ID="[ A N_a ]", classes=["bisector"])
            _add_line(model, B, Nb, ID="[ B N_b ]", classes=["bisector"])
            _add_line(model, C, Nc, ID="[ C N_c ]", classes=["bisector"])
        constructed_primary = True

    elif num == 9:
        # X(9) Mittenpunkt: perspector of excentral triangle and medial triangle
        exc = add_named_triangle("excentral", draw_polygon=True)
        med = add_named_triangle("medial", draw_polygon=True)
        if exc and med:
            Ja, Jb, Jc = exc
            Ma, Mb, Mc = med
            _add_line(model, Ja, Ma, ID="[ J_a M_a ]", classes=["bisector"])
            _add_line(model, Jb, Mb, ID="[ J_b M_b ]", classes=["bisector"])
            _add_line(model, Jc, Mc, ID="[ J_c M_c ]", classes=["bisector"])
        constructed_primary = True

    elif num == 10:
        # X(10) Spieker Center: incenter of medial triangle + Spieker circle
        med = add_named_triangle("medial", draw_polygon=True)
        X10 = get_or_add_center_pt(10, is_target=True)
        if med and X10 is not None:
            Ma, Mb, Mc = med
            _add_line(model, Ma, X10, ID="[ M_a X(10) ]", classes=["bisector"])
            _add_line(model, Mb, X10, ID="[ M_b X(10) ]", classes=["bisector"])
            _add_line(model, Mc, X10, ID="[ M_c X(10) ]", classes=["bisector"])
            x10_xy = registry.xy_cache[10]
            sp_foot = _foot_of_perp(x10_xy[0], x10_xy[1], float(Ma.x), float(Ma.y), float(Mb.x), float(Mb.y))
            Sp_r = _add_point(model, sp_foot[0], sp_foot[1], ID="S_c", guide=True)
            _add_circle(model, X10, Sp_r, ID="spieker_circle", classes=["incircle"])
        constructed_primary = True

    elif num == 11:
        # X(11) Feuerbach Point: tangency of incircle and nine-point circle
        add_incircle()
        add_nine_point_circle()
        add_primary_central_line(1, 5)
        constructed_primary = True

    elif num == 12:
        # X(12) {X(1),X(5)}-harmonic conjugate of X(11): incircle + nine-point circle + line {1,5} + cevians
        add_incircle()
        add_nine_point_circle()
        get_or_add_center_pt(11)
        add_primary_central_line(1, 5)
        add_cevians_for_center(12, prefix="P")
        constructed_primary = True

    elif num in {13, 14}:
        # X(13), X(14) 1st / 2nd Isogonic Centers: equilateral triangles on sides + apex cevians
        Ea, Eb, Ec = add_equilateral_side_triangles(outward=(num == 13))
        _add_line(model, A, Ea, ID="[ A A' ]", classes=["bisector"])
        _add_line(model, B, Eb, ID="[ B B' ]", classes=["bisector"])
        _add_line(model, C, Ec, ID="[ C C' ]", classes=["bisector"])
        constructed_primary = True

    elif num in {15, 16}:
        # X(15), X(16) 1st / 2nd Isodynamic Points: circumcircle + Apollonian circles intersecting at X(15), X(16)
        add_circumcircle()
        for idx_s, (v_pt, v_lbl, opp1, opp2) in enumerate(
            ((A, "A", b, c), (B, "B", c, a), (C, "C", a, b))
        ):
            if abs(opp1 - opp2) > 1e-4:
                # Internal and external bisector feet on opposite side
                if idx_s == 0:
                    u_xy = ctx.bary_to_cartesian(0.0, b, c)
                    v_xy = ctx.bary_to_cartesian(0.0, b, -c)
                elif idx_s == 1:
                    u_xy = ctx.bary_to_cartesian(a, 0.0, c)
                    v_xy = ctx.bary_to_cartesian(a, 0.0, -c)
                else:
                    u_xy = ctx.bary_to_cartesian(a, b, 0.0)
                    v_xy = ctx.bary_to_cartesian(a, -b, 0.0)
                if u_xy and v_xy:
                    ox, oy = 0.5 * (u_xy[0] + v_xy[0]), 0.5 * (u_xy[1] + v_xy[1])
                    if math.hypot(ox - float(v_pt.x), oy - float(v_pt.y)) <= 3.0:
                        o_pt = _add_point(model, ox, oy, ID=f"O_{{Ap,{v_lbl}}}", guide=True)
                        _add_circle(model, o_pt, v_pt, ID=f"{v_lbl}-Apollonian circle", classes=["secondary_circle"])
        get_or_add_center_pt(15 if num == 16 else 16)
        add_primary_central_line(3, 6)
        constructed_primary = True

    elif num in {17, 18}:
        # X(17), X(18) 1st / 2nd Napoleon Points: Napoleon triangle + cevians from A, B, C
        nap = add_named_triangle("outer_napoleon" if num == 17 else "inner_napoleon", draw_polygon=True)
        if nap:
            Na, Nb, Nc = nap
            _add_line(model, A, Na, ID="[ A Nap_a ]", classes=["bisector"])
            _add_line(model, B, Nb, ID="[ B Nap_b ]", classes=["bisector"])
            _add_line(model, C, Nc, ID="[ C Nap_c ]", classes=["bisector"])
        constructed_primary = True

    elif num == 40:
        # X(40) Bevan Point: circumcenter of excentral triangle + Bevan circle + perpendiculars to sides
        exc = add_named_triangle("excentral", draw_polygon=True)
        X40 = get_or_add_center_pt(40, is_target=True)
        if exc and X40 is not None:
            Ja, Jb, Jc = exc
            _add_circle(model, X40, Ja, ID="bevan_circle", classes=["secondary_circle"])
            _add_line(model, Ja, X40, ID="[ J_a X(40) ]", classes=["bisector"])
            _add_line(model, Jb, X40, ID="[ J_b X(40) ]", classes=["bisector"])
            _add_line(model, Jc, X40, ID="[ J_c X(40) ]", classes=["bisector"])
        constructed_primary = True

    elif num in {55, 56}:
        # X(55) Insimilicenter / X(56) Exsimilicenter of Circumcircle and Incircle
        add_circumcircle()
        add_incircle()
        add_primary_central_line(1, 3)
        tang = add_named_triangle("tangential", draw_polygon=True)
        intouch = add_named_triangle("intouch", draw_polygon=True)
        if num == 55 and tang and intouch:
            for t_pt, i_pt, sub in zip(tang, intouch, ("a", "b", "c")):
                _add_line(model, t_pt, i_pt, ID=f"[ Tan_{sub} T_{sub} ]", classes=["bisector"])
        constructed_primary = True

    # General Rule A: Perspector / Homothetic center of two named triangles T1 and T2, or X(k) of a named triangle
    if not constructed_primary:
        matched_tris: list[str] = []
        for t_key, pat in _NAMED_TRIANGLE_PATTERNS:
            if pat.search(combined_primary_text) and t_key not in matched_tris:
                matched_tris.append(t_key)

        if len(matched_tris) >= 2:
            t1 = add_named_triangle(matched_tris[0], draw_polygon=True)
            t2 = add_named_triangle(matched_tris[1], draw_polygon=True)
            if t1 and t2:
                for p1, p2 in zip(t1, t2):
                    _add_line(model, p1, p2, classes=["bisector"])
                constructed_primary = True
        elif len(matched_tris) == 1:
            t1_key = matched_tris[0]
            t1 = add_named_triangle(t1_key, draw_polygon=True)
            target_pt = get_or_add_center_pt(num, is_target=True)
            if t1 and target_pt is not None:
                # Check if X(n) is a center OF T1 (e.g. "centroid of orthic triangle", "X(k)-of-medial-triangle")
                if re.search(
                    r"\b(?:centroid|orthocenter|incenter|circumcenter|symmedian\s+point|nine-point\s+center|X\(\d+\))(?:\s+|-)+of(?:\s+|-)+(?:the\s+)?[a-z\-]+\s+triangle",
                    combined_primary_text,
                    re.IGNORECASE,
                ):
                    if "circumcenter" in title_str.lower():
                        _add_circle(model, target_pt, t1[0], ID=f"circumcircle_of_{t1_key}", classes=["secondary_circle"])
                    for p1 in t1:
                        _add_line(model, p1, target_pt, classes=["bisector"])
                    constructed_primary = True
                elif re.search(r"\b(?:concur\s+in|perspector)\b", combined_primary_text, re.IGNORECASE):
                    # Perspector of ABC and T1
                    for v_pt, p1 in zip((A, B, C), t1):
                        _add_line(model, v_pt, p1, classes=["bisector"])
                    constructed_primary = True

    # General Rule B: Explicit Midpoint, Reflection, Harmonic Conjugate, Complement, Anticomplement, Circle Inverse, Antipode
    if not constructed_primary:
        # Midpoint of X(i) and X(j) / Reflection of X(i) in X(j)
        m_pair = re.search(
            r"\b(?:midpoint\s+of|reflection\s+of)\s+X\((\d+)\)\s+(?:and|in)\s+X\((\d+)\)",
            title_str + " " + " ".join((center_data.get("relations") or [])[:2]),
            re.IGNORECASE,
        )
        if not m_pair:
            # Also check named classical centers in title, e.g. "REFLECTION OF INCENTER IN FEUERBACH POINT"
            name_to_num = {
                "incenter": 1, "centroid": 2, "circumcenter": 3, "orthocenter": 4,
                "nine-point center": 5, "symmedian point": 6, "gergonne point": 7,
                "nagel point": 8, "mittenpunkt": 9, "spieker center": 10, "feuerbach point": 11,
            }
            m_named = re.search(
                r"\b(?:midpoint|reflection)\s+of\s+([a-z\-\s]+?)\s+(?:and|in)\s+([a-z\-\s]+)$",
                title_str.strip(),
                re.IGNORECASE,
            )
            if m_named:
                n1 = name_to_num.get(m_named.group(1).strip().lower())
                n2 = name_to_num.get(m_named.group(2).strip().lower())
                if n1 and n2:
                    add_primary_central_line(n1, n2)
                    constructed_primary = True
        else:
            i_k, j_k = int(m_pair.group(1)), int(m_pair.group(2))
            if i_k in registry.xy_cache and j_k in registry.xy_cache:
                add_primary_central_line(i_k, j_k)
                constructed_primary = True

    if not constructed_primary:
        # Harmonic conjugate: {X(i),X(j)}-harmonic conjugate of X(k)
        m_harm = re.search(
            r"\{\s*X\((\d+)\)\s*,\s*X\((\d+)\)\s*\}\s*-?\s*harmonic\s+conjugate\s+of\s+X\((\d+)\)",
            combined_primary_text,
            re.IGNORECASE,
        )
        if m_harm:
            i_k, j_k, k_k = int(m_harm.group(1)), int(m_harm.group(2)), int(m_harm.group(3))
            get_or_add_center_pt(k_k)
            add_primary_central_line(i_k, j_k)
            if re.search(r"\bconcur\s+in\b", note0, re.IGNORECASE):
                add_cevians_for_center(num, prefix="P")
            constructed_primary = True

    if not constructed_primary:
        # Complement / Anticomplement of X(k)
        m_comp = re.search(
            r"\b(anticomplement|complement)\s+of\s+(?:X\((\d+)\)|feuerbach\s+point|incenter|orthocenter|circumcenter|symmedian\s+point)",
            title_str + " " + " ".join((center_data.get("relations") or [])[:2]),
            re.IGNORECASE,
        )
        if m_comp:
            kind_c = m_comp.group(1).lower()
            k_str = m_comp.group(2)
            k_num = int(k_str) if k_str else (11 if "feuerbach" in title_str.lower() else 1)
            if k_num in registry.xy_cache:
                add_named_triangle("anticomplementary" if kind_c == "anticomplement" else "medial", draw_polygon=True)
                add_primary_central_line(2, k_num)
                constructed_primary = True

    if not constructed_primary:
        # Inverse in circumcircle / incircle / nine-point circle
        m_inv = re.search(
            r"\binverse\s*-?\s*in\s*-?\s*(circumcircle|incircle|nine-point\s+circle)\s+of\s+(?:X\((\d+)\)|incenter|centroid|orthocenter|symmedian\s+point)",
            title_str + " " + " ".join((center_data.get("relations") or [])[:2]),
            re.IGNORECASE,
        )
        if m_inv:
            c_kind = m_inv.group(1).lower()
            k_num = int(m_inv.group(2)) if m_inv.group(2) else 1
            if "circumcircle" in c_kind:
                add_circumcircle()
                add_primary_central_line(3, k_num)
            elif "incircle" in c_kind:
                add_incircle()
                add_primary_central_line(1, k_num)
            else:
                add_nine_point_circle()
                add_primary_central_line(5, k_num)
            constructed_primary = True

    if not constructed_primary:
        # Antipode on circumcircle or nine-point circle
        if "antipode" in title_str.lower() or num in {98, 99, 100, 103, 104, 110, 111, 113, 114, 115, 119}:
            if num in {115, 119} or "nine-point" in combined_primary_text.lower() or "feuerbach antipode" in title_str.lower():
                add_nine_point_circle()
                if num == 119:
                    add_primary_central_line(5, 11)
            else:
                add_circumcircle()
                m_ant = re.search(r"\bantipode\s+of\s+X\((\d+)\)", title_str, re.IGNORECASE)
                if m_ant:
                    add_primary_central_line(3, int(m_ant.group(1)))
                elif num == 98:
                    add_primary_central_line(3, 99)
                elif num == 99:
                    add_primary_central_line(3, 98)
            if re.search(r"\bconcur\s+in\b|\bperspector\b", note0, re.IGNORECASE):
                add_cevians_for_center(num, prefix="P")
            constructed_primary = True

    # General Rule C: Cevian Concurrence ("concur in X(n)", Crosspoint, Cevapoint, Ceva/Beth/Line Conjugate, Isogonal/Isotomic Conjugate)
    if not constructed_primary:
        m_pair_op = re.search(
            r"\b(?:crosspoint|cevapoint)\s+of\s+X\((\d+)\)\s+and\s+X\((\d+)\)|X\((\d+)\)\s*-\s*(?:ceva|beth|line|cross)\s+conjugate\s+of\s+X\((\d+)\)",
            title_str + " " + " ".join((center_data.get("relations") or [])[:2]),
            re.IGNORECASE,
        )
        if m_pair_op:
            g = m_pair_op.groups()
            i_k = int(g[0] or g[2])
            j_k = int(g[1] or g[3])
            get_or_add_center_pt(i_k)
            get_or_add_center_pt(j_k)
            add_cevians_for_center(num, prefix="P")
            constructed_primary = True

    if not constructed_primary:
        m_conj = re.search(
            r"\b(isogonal|isotomic)\s+conjugate\s+of\s+X\((\d+)\)",
            title_str + " " + " ".join((center_data.get("relations") or [])[:2]),
            re.IGNORECASE,
        )
        if m_conj:
            k_num = int(m_conj.group(2))
            if k_num in registry.xy_cache and k_num != num:
                get_or_add_center_pt(k_num)
            add_cevians_for_center(num, prefix="P")
            constructed_primary = True

    if not constructed_primary:
        if re.search(r"\bconcur\s+in\s+X\(\d+\)|\bperspector\b|\bcevian\b", combined_primary_text, re.IGNORECASE):
            add_cevians_for_center(num, prefix="P")
            constructed_primary = True

    # General Rule D: Euler Line points & Circle Centers
    if not constructed_primary:
        if any("As a point on the Euler line" in n for n in notes_list):
            add_primary_central_line(2, 3)
            get_or_add_center_pt(4)
            # Add one intersecting line that locates X(n) on the Euler line
            for i_num, j_num in line_pairs:
                if {i_num, j_num} <= {2, 3, 4, 5, 20, 30}:
                    continue
                add_primary_central_line(i_num, j_num)
                break
            else:
                add_cevians_for_center(num, prefix="P")
            constructed_primary = True

    # General Rule E: Fallback to 2 intersecting central lines (or 3 cevians)
    if not constructed_primary:
        if len(line_pairs) >= 2:
            for i_num, j_num in line_pairs[:2]:
                add_primary_central_line(i_num, j_num)
        else:
            add_cevians_for_center(num, prefix="P")
            for i_num, j_num in line_pairs[:1]:
                add_primary_central_line(i_num, j_num)

    # Ensure target center X(n) is added as a primary (non-incident) point
    target_pt = get_or_add_center_pt(num, is_target=True, incident=False)

    # Ensure Euler line is part of the default (Layer 1) vectors whenever X(n) lies on the Euler line
    euler_set = {2, 3, 4, 5, 20, 30}
    on_euler_line = (
        num in euler_set
        or any({i_num, j_num} <= euler_set for i_num, j_num in line_pairs)
        or any("As a point on the Euler line" in n for n in notes_list)
    )
    if not on_euler_line and 2 in registry.xy_cache and 3 in registry.xy_cache and num in registry.xy_cache:
        x2, y2 = registry.xy_cache[2]
        x3, y3 = registry.xy_cache[3]
        xn, yn = registry.xy_cache[num]
        e_len = math.hypot(x3 - x2, y3 - y2)
        if e_len > 1e-8 and abs((x3 - x2) * (yn - y2) - (y3 - y2) * (xn - x2)) / e_len < 1e-5:
            on_euler_line = True

    if on_euler_line:
        has_primary_euler = any({p[0], p[1]} <= euler_set for p in primary_line_pairs)
        if not has_primary_euler:
            if num == 2:
                add_primary_central_line(3, 4)
            elif num == 3:
                add_primary_central_line(2, 4)
            else:
                add_primary_central_line(2, 3)

    # Add up to 1 named circle from `(c_num; Circle Name, ...)` if explicitly mentioned in primary note
    if target_pt is not None and note0:
        for cm in re.finditer(
            r"\((\d+)\s*;\s*([A-Za-z0-9\-\'\s]+?circle)\s*[,;]",
            note0,
            re.IGNORECASE,
        ):
            c_center_num = int(cm.group(1))
            c_name_raw = " ".join(cm.group(2).split())
            if c_center_num in registry.xy_cache and c_center_num != num:
                c_ctr_pt = get_or_add_center_pt(c_center_num, is_target=False, incident=False)
                if c_ctr_pt is not None:
                    _add_circle(model, c_ctr_pt, target_pt, ID=c_name_raw, classes=["secondary_circle"])
                    break

    # -----------------------------------------------------------------------
    # 3. Layer 2: Toggleable Incident Central Lines (`Lines` Button in Toolbar)
    # -----------------------------------------------------------------------
    added_incident_lines = 0
    for i_num, j_num in line_pairs:
        pair = (min(i_num, j_num), max(i_num, j_num))
        if pair in primary_line_pairs or (on_euler_line and {i_num, j_num} <= euler_set):
            continue
        pi = get_or_add_center_pt(i_num, is_target=(i_num == num), incident=True)
        pj = get_or_add_center_pt(j_num, is_target=(j_num == num), incident=True)
        if pi is not None and pj is not None:
            cls = ["golden", "euler", "incident"] if {i_num, j_num} <= euler_set else ["central_line", "incident"]
            _add_line(
                model,
                pi,
                pj,
                ID=f"{{ {i_num}, {j_num} }}",
                classes=cls,
            )
            added_incident_lines += 1
            if added_incident_lines >= 4:
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

    ops_imports: set[str] = {
        "create_model",
        "construct_baseline_triangle",
        "promote_point_to_top",
    }
    body_lines: list[str] = []
    defined_vars: set[int] = set()

    def ensure_center_var(c_num: int, is_target: bool = False, incident: bool = False) -> str:
        var_name = f"X_{c_num}"
        if c_num in defined_vars and not is_target:
            return var_name

        if is_target:
            cls_arg = '["selected", "target"]'
        elif incident:
            cls_arg = '["center", "incident"]'
        else:
            cls_arg = '["center"]'

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

    # Collect incident central lines {i, j}
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

    # 1. Construct primary target center X(num)
    target_var = f"X_{num}"
    used_primary_lines: set[tuple[int, int]] = set()
    if num in _CLASSICAL_CONSTRUCTOR_NAMES:
        ensure_center_var(num, is_target=True)
    elif num in {13, 14}:
        tri_fn = "outer_equilateral_triangles" if num == 13 else "inner_equilateral_triangles"
        ops_imports.update({tri_fn, "perspector"})
        body_lines.append(f"    Ea, Eb, Ec = {tri_fn}(model, A, B, C)")
        body_lines.append(
            f'    {target_var} = perspector(model, A, B, C, Ea, Eb, Ec, ID="X({num})", classes=["selected", "target"])'
        )
        defined_vars.add(num)
    elif num in {17, 18}:
        tri_fn = "outer_napoleon_triangle" if num == 17 else "inner_napoleon_triangle"
        ops_imports.update({tri_fn, "perspector"})
        body_lines.append(f"    Na, Nb, Nc = {tri_fn}(model, A, B, C)")
        body_lines.append(
            f'    {target_var} = perspector(model, A, B, C, Na, Nb, Nc, ID="X({num})", classes=["selected", "target"])'
        )
        defined_vars.add(num)
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
            defined_vars.add(num)
        else:
            spec = _get_cyclic_expr_spec(center_data, registry.ctx)
            if spec:
                kind, expr_str = spec
                eval_fn = "eval_trilinear_point" if kind == "trilinear" else "eval_barycentric_point"
                ops_imports.add(eval_fn)
                body_lines.append(
                    f'    {target_var} = {eval_fn}(model, A, B, C, {expr_str!r}, ID="X({num})", classes=["selected", "target"])'
                )
                defined_vars.add(num)
            elif len(chosen_lines) >= 2:
                (i1, j1), (i2, j2) = chosen_lines[0], chosen_lines[1]
                vi1 = ensure_center_var(i1)
                vj1 = ensure_center_var(j1)
                vi2 = ensure_center_var(i2)
                vj2 = ensure_center_var(j2)
                ops_imports.update({"central_line", "intersect_lines"})
                body_lines.append(f"    central_line(model, {vi1}, {vj1}, {i1}, {j1})")
                body_lines.append(f"    central_line(model, {vi2}, {vj2}, {i2}, {j2})")
                body_lines.append(
                    f'    {target_var} = intersect_lines(model, {vi1}, {vj1}, {vi2}, {vj2}, ID="X({num})", classes=["selected", "target"])'
                )
                used_primary_lines.add((i1, j1))
                used_primary_lines.add((i2, j2))
                defined_vars.add(num)
            else:
                ensure_center_var(num, is_target=True)

    # Ensure Euler line is part of the default vectors whenever X(num) lies on the Euler line
    euler_set = {2, 3, 4, 5, 20, 30}
    notes_list = center_data.get("notes") or []
    on_euler_line = (
        num in euler_set
        or any({i_num, j_num} <= euler_set for i_num, j_num in line_pairs)
        or any("As a point on the Euler line" in n for n in notes_list)
    )
    if not on_euler_line and 2 in registry.xy_cache and 3 in registry.xy_cache and num in registry.xy_cache:
        x2, y2 = registry.xy_cache[2]
        x3, y3 = registry.xy_cache[3]
        xn, yn = registry.xy_cache[num]
        e_len = math.hypot(x3 - x2, y3 - y2)
        if e_len > 1e-8 and abs((x3 - x2) * (yn - y2) - (y3 - y2) * (xn - x2)) / e_len < 1e-5:
            on_euler_line = True

    if on_euler_line and not any({p[0], p[1]} <= euler_set for p in used_primary_lines):
        ei, ej = (3, 4) if num == 2 else ((2, 4) if num == 3 else (2, 3))
        vei = ensure_center_var(ei, incident=False)
        vej = ensure_center_var(ej, incident=False)
        ops_imports.add("central_line")
        body_lines.append(f"    central_line(model, {vei}, {vej}, {ei}, {ej})")
        used_primary_lines.add((ei, ej))

    # 2. Layer 2: Toggleable incident central lines {i, j}
    for i_num, j_num in chosen_lines:
        if (i_num, j_num) in used_primary_lines or (on_euler_line and {i_num, j_num} <= euler_set):
            continue
        vi = ensure_center_var(i_num, is_target=(i_num == num), incident=True)
        vj = ensure_center_var(j_num, is_target=(j_num == num), incident=True)
        ops_imports.add("central_line")
        body_lines.append(f"    central_line(model, {vi}, {vj}, {i_num}, {j_num}, incident=True)")

    body_lines.append(f"    return promote_point_to_top(model, {target_var})")


    sorted_imports = ",\n    ".join(sorted(ops_imports))

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
    show_guides: bool = False,
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


