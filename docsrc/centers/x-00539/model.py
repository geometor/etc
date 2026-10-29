"""GEOMETOR construction model for X(539) = DIRECTION OF VECTOR AX + BX + CX, where X = X(54)."""

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


def construct_x_00539(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(539) = DIRECTION OF VECTOR AX + BX + CX, where X = X(54) on reference triangle ABC."""
    X_539 = eval_barycentric_point(model, A, B, C, '(a**(2) - b**(2) - c**(2))*(2*a**(8) - 4*a**(6)*(b**(2) + c**(2)) + 3*a**(4)*(b**(4) + c**(4)) - 2*a**(2)*(b**(2) - c**(2))**(2)*(b**(2) + c**(2)) + (b**(2) - c**(2))**(4))', ID="X(539)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X(54)", classes=["center", "incident"])
    central_line(model, X_2, X_54, 2, 54, incident=True)
    X_155 = eval_barycentric_point(model, A, B, C, 'a**(2)*SA*(a**(2)*(SA**(2) - SB*SC) - SA*(SB**(2) + SC**(2)))', ID="X(155)", classes=["center", "incident"])
    X_195 = eval_trilinear_point(model, A, B, C, 'a*(a**(8) + b**(8) + c**(8) - 4*a**(6)*(b**(2) + c**(2)) + a**(4)*(6*b**(4) + 6*c**(4) + 5*b**(2)*c**(2)) - a**(2)*(4*b**(6) + 4*c**(6) - b**(4)*c**(2) - b**(2)*c**(4)) - 2*b**(2)*c**(2)*(b**(4) + c**(4) - b**(2)*c**(2)))', ID="X(195)", classes=["center", "incident"])
    central_line(model, X_155, X_195, 155, 195, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X(511)", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    return promote_point_to_top(model, X_539)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(539) on the given reference triangle."""
    model = create_model('X(539) = DIRECTION OF VECTOR AX + BX + CX, where X = X(54)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00539(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00539.json"))
    write_center_svg(
        model_acute,
        here / "x-00539.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
