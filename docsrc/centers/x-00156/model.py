"""GEOMETOR construction model for X(156) = X(5)-OF-TANGENTIAL-TRIANGLE."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    midpoint,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00156(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(156) = X(5)-OF-TANGENTIAL-TRIANGLE on reference triangle ABC."""
    X_26 = eval_trilinear_point(model, A, B, C, 'a*(b**(2)*cos(2*B) + c**(2)*cos(2*C) - a**(2)*cos(2*A))', ID="X(26)", classes=["center"])
    X_155 = eval_barycentric_point(model, A, B, C, 'a**(2)*SA*(a**(2)*(SA**(2) - SB*SC) - SA*(SB**(2) + SC**(2)))', ID="X(155)", classes=["center"])
    X_156 = midpoint(model, X_26, X_155, ID="X(156)", classes=["selected", "target"], guide=False)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_49 = eval_trilinear_point(model, A, B, C, 'cos(3*A)', ID="X(49)", classes=["center", "incident"])
    central_line(model, X_4, X_49, 4, 49, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X(74)", classes=["center", "incident"])
    central_line(model, X_3, X_74, 3, 74, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X(25)", classes=["center", "incident"])
    X_143 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cos(2*C - 2*A) + cos(2*A - 2*B))', ID="X(143)", classes=["center", "incident"])
    central_line(model, X_25, X_143, 25, 143, incident=True)
    return promote_point_to_top(model, X_156)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(156) on the given reference triangle."""
    model = create_model('X(156) = X(5)-OF-TANGENTIAL-TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00156(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00156.json"))
    write_center_svg(
        model_acute,
        here / "x-00156.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
