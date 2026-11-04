"""GEOMETOR construction model for X_1510 = NAPOLEON CROSSDIFFERENCE."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01510(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1510 = NAPOLEON CROSSDIFFERENCE on reference triangle ABC."""
    X_930 = eval_barycentric_point(model, A, B, C, '1/((b**(2) - c**(2))*(a**(4) + b**(4) + c**(4) - 2*a**(2)*b**(2) - 2*a**(2)*c**(2) - b**(2)*c**(2)))', ID="X_930", classes=["center"])
    X_1510 = isogonal_conjugate(model, A, B, C, X_930, ID="X_1510", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    X_1291 = eval_barycentric_point(model, A, B, C, 'a**(2)/((b**(2) - c**(2))*(a**(12) - 4*a**(10)*(b**(2) + c**(2)) + 5*a**(8)*(b**(4) + b**(2)*c**(2) + c**(4)) + a**(6)*b**(2)*c**(2)*(b**(2) + c**(2)) - a**(4)*(5*b**(8) - b**(6)*c**(2) + 2*b**(4)*c**(4) - b**(2)*c**(6) + 5*c**(8)) + a**(2)*(b**(2) - c**(2))**(2)*(4*b**(6) + 3*b**(4)*c**(2) + 3*b**(2)*c**(4) + 4*c**(6)) - (b**(2) - c**(2))**(4)*(b**(2) + c**(2))**(2)))', ID="X_1291", classes=["center", "incident"])
    central_line(model, X_110, X_1291, 110, 1291, incident=True)
    return promote_point_to_top(model, X_1510)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1510 on the given reference triangle."""
    model = create_model('X_1510 = NAPOLEON CROSSDIFFERENCE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01510(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01510.json"))
    write_center_svg(
        model_acute,
        here / "x-01510.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
