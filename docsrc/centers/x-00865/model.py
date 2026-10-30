"""GEOMETOR construction model for X(865) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(512)."""

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
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00865(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(865) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(512) on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_351 = point_from_barycentrics(model, A, B, C, -1.104798, 0.16783217, 1.9369658, ID="X(351)", classes=["center"])
    X_888 = eval_barycentric_point(model, A, B, C, 'a**(2)*(b**(2) - c**(2))*(a**(2)*b**(2) + a**(2)*c**(2) - 2*b**(2)*c**(2))', ID="X(888)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    central_line(model, X_351, X_888, 351, 888)
    X_865 = intersect_lines(model, X_2, X_3, X_351, X_888, ID="X(865)", classes=["selected", "target"])
    return promote_point_to_top(model, X_865)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(865) on the given reference triangle."""
    model = create_model('X(865) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(512)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00865(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00865.json"))
    write_center_svg(
        model_acute,
        here / "x-00865.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
