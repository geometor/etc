"""GEOMETOR construction model for X(429) = EULER X(58)-5th-SUBSTITUTION POINT."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00429(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(429) = EULER X(58)-5th-SUBSTITUTION POINT on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X(12)", classes=["center"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    central_line(model, X_12, X_37, 12, 37)
    X_429 = intersect_lines(model, X_2, X_3, X_12, X_37, ID="X(429)", classes=["selected", "target"])
    X_119 = eval_trilinear_point(model, A, B, C, '(csc(A))*(-1 + cos(B) + cos(C))*(sin(2*B) + sin(2*C) + 2*(-1 + cos(A))*(sin(B) + sin(C)))', ID="X(119)", classes=["center", "incident"])
    X_136 = eval_barycentric_point(model, A, B, C, '(b**(2) - c**(2))**(2)*(a**(4) + b**(4) + c**(4) - 2*a**(2)*b**(2) - 2*a**(2)*c**(2))/(a**(2) - b**(2) - c**(2))', ID="X(136)", classes=["center", "incident"])
    central_line(model, X_119, X_136, 119, 136, incident=True)
    return promote_point_to_top(model, X_429)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(429) on the given reference triangle."""
    model = create_model('X(429) = EULER X(58)-5th-SUBSTITUTION POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00429(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00429.json"))
    write_center_svg(
        model_acute,
        here / "x-00429.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
