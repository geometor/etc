"""GEOMETOR construction model for X_2823 = ISOGONAL CONJUGATE OF X_2739."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02823(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2823 = ISOGONAL CONJUGATE OF X_2739 on reference triangle ABC."""
    X_2739 = point_from_barycentrics(model, A, B, C, 1.0237069, 0.42672414, -0.45043103, ID="X_2739", classes=["center"])
    X_2823 = isogonal_conjugate(model, A, B, C, X_2739, ID="X_2823", classes=["selected", "target"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center", "incident"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    central_line(model, X_33, X_57, 33, 57, incident=True)
    X_118 = point_from_barycentrics(model, A, B, C, 0.28918651, -0.056547619, 0.76736111, ID="X_118", classes=["center", "incident"])
    X_123 = eval_trilinear_point(model, A, B, C, '(csc(A))*(sec(B) - sec(C))*((sec(A))*((sin(B))**(2) - (sin(C))**(2)) + sin(C)*tan(C) - sin(B)*tan(B))', ID="X_123", classes=["center", "incident"])
    central_line(model, X_118, X_123, 118, 123, incident=True)
    X_152 = eval_barycentric_point(model, A, B, C, 'a**(8) - a**(7)*(b + c) + a**(6)*(2*b**(2) + b*c + 2*c**(2)) - a**(5)*(5*b**(3) - b**(2)*c - b*c**(2) + 5*c**(3)) - a**(4)*b*c*(b**(2) - 6*b*c + c**(2)) + a**(3)*(5*b**(5) + b**(4)*c - 6*b**(3)*c**(2) - 6*b**(2)*c**(3) + b*c**(4) + 5*c**(5)) - a**(2)*(2*b**(6) + b**(5)*c + 2*b**(4)*c**(2) - 10*b**(3)*c**(3) + 2*b**(2)*c**(4) + b*c**(5) + 2*c**(6)) + a*(b**(7) - b**(6)*c - 3*b**(5)*c**(2) + 3*b**(4)*c**(3) + 3*b**(3)*c**(4) - 3*b**(2)*c**(5) - b*c**(6) + c**(7)) - b**(8) + b**(7)*c + 2*b**(6)*c**(2) - b**(5)*c**(3) - 2*b**(4)*c**(4) - b**(3)*c**(5) + 2*b**(2)*c**(6) + b*c**(7) - c**(8)', ID="X_152", classes=["center", "incident"])
    X_329 = eval_trilinear_point(model, A, B, C, '( -1 - cos(A) + cos(B) + cos(C))*(csc(A))', ID="X_329", classes=["center", "incident"])
    central_line(model, X_152, X_329, 152, 329, incident=True)
    return promote_point_to_top(model, X_2823)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2823 on the given reference triangle."""
    model = create_model('X_2823 = ISOGONAL CONJUGATE OF X_2739')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02823(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02823.json"))
    write_center_svg(
        model_acute,
        here / "x-02823.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
