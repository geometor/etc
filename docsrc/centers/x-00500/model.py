"""GEOMETOR construction model for X(500) = ORTHOCENTER OF THE INCENTRAL TRIANGLE."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00500(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(500) = ORTHOCENTER OF THE INCENTRAL TRIANGLE on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X(35)", classes=["center"])
    X_500 = crosspoint(model, A, B, C, X_1, X_35, ID="X(500)", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center", "incident"])
    central_line(model, X_1, X_30, 1, 30, incident=True)
    X_651 = eval_trilinear_point(model, A, B, C, '1/(cos(B) - cos(C))', ID="X(651)", classes=["center", "incident"])
    X_943 = eval_trilinear_point(model, A, B, C, '1/(2*a*b*c + (b + c)*(a - b + c)*(a + b - c))', ID="X(943)", classes=["center", "incident"])
    central_line(model, X_651, X_943, 651, 943, incident=True)
    return promote_point_to_top(model, X_500)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(500) on the given reference triangle."""
    model = create_model('X(500) = ORTHOCENTER OF THE INCENTRAL TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00500(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00500.json"))
    write_center_svg(
        model_acute,
        here / "x-00500.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
