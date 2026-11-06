"""GEOMETOR construction model for X_3565 = 2nd MOSES CIRCUMCIRCLE POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_03565(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3565 = 2nd MOSES CIRCUMCIRCLE POINT on reference triangle ABC."""
    X_3563 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b**(2)*(cos(C))**(2) + c**(2)*(cos(B))**(2) - b*c*cos(A))', ID="X_3563", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_3565 = reflection_in_point(model, X_3563, X_3, ID="X_3565", classes=["selected", "target"], guide=False)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center", "incident"])
    central_line(model, X_20, X_98, 20, 98, incident=True)
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X_22", classes=["center", "incident"])
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X_111", classes=["center", "incident"])
    central_line(model, X_22, X_111, 22, 111, incident=True)
    X_376 = eval_trilinear_point(model, A, B, C, '5*cos(A) - cos(B - C)', ID="X_376", classes=["center", "incident"])
    X_1300 = eval_trilinear_point(model, A, B, C, '(sec(A))/(1 + cos(2*B) + cos(2*C))', ID="X_1300", classes=["center", "incident"])
    central_line(model, X_376, X_1300, 376, 1300, incident=True)
    return promote_point_to_top(model, X_3565)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3565 on the given reference triangle."""
    model = create_model('X_3565 = 2nd MOSES CIRCUMCIRCLE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03565(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03565.json"))
    write_center_svg(
        model_acute,
        here / "x-03565.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
