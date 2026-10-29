"""GEOMETOR construction model for X(151) = REFLECTION OF X(20) IN X(109)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00151(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(151) = REFLECTION OF X(20) IN X(109) on reference triangle ABC."""
    X_151 = eval_barycentric_point(model, A, B, C, 'a**(12) + a**(11)*(b + c) + a**(10)*b*c + a**(9)*(3*b**(3) - b**(2)*c - b*c**(2) + 3*c**(3)) - a**(8)*(3*b**(4) + b**(3)*c + b*c**(3) + 3*c**(4)) - 2*a**(7)*(7*b**(5) + b**(4)*c - 4*b**(3)*c**(2) - 4*b**(2)*c**(3) + b*c**(4) + 7*c**(5)) - 2*a**(6)*b*c*(b**(4) - 2*b**(3)*c - 6*b**(2)*c**(2) - 2*b*c**(3) + c**(4)) + 2*a**(5)*(7*b**(7) + b**(6)*c - 5*b**(5)*c**(2) - 3*b**(4)*c**(3) - 3*b**(3)*c**(4) - 5*b**(2)*c**(5) + b*c**(6) + 7*c**(7)) + a**(4)*(3*b**(8) + 2*b**(7)*c - 4*b**(6)*c**(2) - 2*b**(5)*c**(3) + 2*b**(4)*c**(4) - 2*b**(3)*c**(5) - 4*b**(2)*c**(6) + 2*b*c**(7) + 3*c**(8)) - a**(3)*(3*b**(9) - b**(8)*c + 8*b**(6)*c**(3) - 10*b**(5)*c**(4) - 10*b**(4)*c**(5) + 8*b**(3)*c**(6) - b*c**(8) + 3*c**(9)) + a**(2)*b*c*(b**(8) - 4*b**(7)*c - 12*b**(6)*c**(2) + 4*b**(5)*c**(3) + 22*b**(4)*c**(4) + 4*b**(3)*c**(5) - 12*b**(2)*c**(6) - 4*b*c**(7) + c**(8)) - a*(b**(11) + b**(10)*c - 3*b**(9)*c**(2) - 3*b**(8)*c**(3) + 2*b**(7)*c**(4) + 2*b**(6)*c**(5) + 2*b**(5)*c**(6) + 2*b**(4)*c**(7) - 3*b**(3)*c**(8) - 3*b**(2)*c**(9) + b*c**(10) + c**(11)) - b**(12) - b**(11)*c + 4*b**(10)*c**(2) + 3*b**(9)*c**(3) - 7*b**(8)*c**(4) - 2*b**(7)*c**(5) + 8*b**(6)*c**(6) - 2*b**(5)*c**(7) - 7*b**(4)*c**(8) + 3*b**(3)*c**(9) + 4*b**(2)*c**(10) - b*c**(11) - c**(12)', ID="X(151)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_102 = eval_trilinear_point(model, A, B, C, '1/(sin(B)*(sec(A) - sec(B)) + sin(C)*(sec(A) - sec(C)))', ID="X(102)", classes=["center", "incident"])
    central_line(model, X_2, X_102, 2, 102, incident=True)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X(20)", classes=["center", "incident"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X(109)", classes=["center", "incident"])
    central_line(model, X_20, X_109, 20, 109, incident=True)
    X_49 = eval_trilinear_point(model, A, B, C, 'cos(3*A)', ID="X(49)", classes=["center", "incident"])
    X_962 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(4) + 2*a**(3)*(b + c) - 4*a**(2)*b*c - (b + c)*(b - c)**(2)*(2*a + b + c))', ID="X(962)", classes=["center", "incident"])
    central_line(model, X_49, X_962, 49, 962, incident=True)
    return promote_point_to_top(model, X_151)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(151) on the given reference triangle."""
    model = create_model('X(151) = REFLECTION OF X(20) IN X(109)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00151(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00151.json"))
    write_center_svg(
        model_acute,
        here / "x-00151.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
