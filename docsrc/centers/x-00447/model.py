"""GEOMETOR construction model for X(447) = X(2)-HIRST INVERSE OF X(27)."""

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


def construct_x_00447(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(447) = X(2)-HIRST INVERSE OF X(27) on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_340 = eval_barycentric_point(model, A, B, C, '((a**(2) - b**(2) - c**(2))**(2) - b**(2)*c**(2))/(b**(2) + c**(2) - a**(2))', ID="X(340)", classes=["center"])
    X_540 = point_from_barycentrics(model, A, B, C, -0.66946852, -0.070060659, 0.73952918, ID="X(540)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    central_line(model, X_340, X_540, 340, 540)
    X_447 = intersect_lines(model, X_2, X_3, X_340, X_540, ID="X(447)", classes=["selected", "target"])
    X_350 = eval_trilinear_point(model, A, B, C, '(a**(2) - b*c)*b**(2)*c**(2)', ID="X(350)", classes=["center", "incident"])
    X_811 = eval_barycentric_point(model, A, B, C, 'csc(2*A)*csc(B - C)', ID="X(811)", classes=["center", "incident"])
    central_line(model, X_350, X_811, 350, 811, incident=True)
    return promote_point_to_top(model, X_447)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(447) on the given reference triangle."""
    model = create_model('X(447) = X(2)-HIRST INVERSE OF X(27)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00447(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00447.json"))
    write_center_svg(
        model_acute,
        here / "x-00447.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
