"""GEOMETOR construction model for X(430) = EULER X(81)-5th-SUBSTITUTION POINT."""

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
    eval_barycentric_point,
    eval_trilinear_point,
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00430(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(430) = EULER X(81)-5th-SUBSTITUTION POINT on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_118 = point_from_barycentrics(model, A, B, C, 0.28918651, -0.056547619, 0.76736111, ID="X(118)", classes=["center"])
    X_136 = eval_barycentric_point(model, A, B, C, '(b**(2) - c**(2))**(2)*(a**(4) + b**(4) + c**(4) - 2*a**(2)*b**(2) - 2*a**(2)*c**(2))/(a**(2) - b**(2) - c**(2))', ID="X(136)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    central_line(model, X_118, X_136, 118, 136)
    X_430 = intersect_lines(model, X_2, X_3, X_118, X_136, ID="X(430)", classes=["selected", "target"])
    X_210 = eval_trilinear_point(model, A, B, C, '(b + c)*(b + c - a)', ID="X(210)", classes=["center", "incident"])
    X_594 = eval_trilinear_point(model, A, B, C, '(b + c)**(2)/a', ID="X(594)", classes=["center", "incident"])
    central_line(model, X_210, X_594, 210, 594, incident=True)
    return promote_point_to_top(model, X_430)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(430) on the given reference triangle."""
    model = create_model('X(430) = EULER X(81)-5th-SUBSTITUTION POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00430(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00430.json"))
    write_center_svg(
        model_acute,
        here / "x-00430.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
