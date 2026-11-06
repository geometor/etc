"""GEOMETOR construction model for X_3850 = X_140com(EULER TRIANGLE)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    midpoint,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03850(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3850 = X_140com(EULER TRIANGLE) on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_140 = eval_trilinear_point(model, A, B, C, '2*cos(A) + cos(B - C)', ID="X_140", classes=["center"])
    X_3850 = midpoint(model, X_4, X_140, ID="X_3850", classes=["selected", "target"], guide=False)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_399 = eval_trilinear_point(model, A, B, C, '5*cos(A) - 4*cos(B)*cos(C) - 8*sin(B)*sin(C)*(cos(A))**(2)', ID="X_399", classes=["center", "incident"])
    X_1199 = point_from_barycentrics(model, A, B, C, 0.23978233, 0.34288074, 0.41733693, ID="X_1199", classes=["center", "incident"])
    central_line(model, X_399, X_1199, 399, 1199, incident=True)
    X_355 = eval_trilinear_point(model, A, B, C, 'a*cos(A) - (b + c)*cos(B - C)', ID="X_355", classes=["center", "incident"])
    X_3633 = eval_trilinear_point(model, A, B, C, 'b*c*(5*a - 2*b - 2*c)', ID="X_3633", classes=["center", "incident"])
    central_line(model, X_355, X_3633, 355, 3633, incident=True)
    return promote_point_to_top(model, X_3850)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3850 on the given reference triangle."""
    model = create_model('X_3850 = X_140com(EULER TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03850(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03850.json"))
    write_center_svg(
        model_acute,
        here / "x-03850.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
