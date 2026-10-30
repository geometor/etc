"""GEOMETOR construction model for X(702) = EVEN (- 4, 0) INFINITY POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00702(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(702) = EVEN (- 4, 0) INFINITY POINT on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_308 = eval_trilinear_point(model, A, B, C, 'b**(3)*c**(3)/(b**(2) + c**(2))', ID="X(308)", classes=["center"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X(511)", classes=["center"])
    central_line(model, X_2, X_308, 2, 308)
    central_line(model, X_30, X_511, 30, 511)
    X_702 = intersect_lines(model, X_2, X_308, X_30, X_511, ID="X(702)", classes=["selected", "target"])
    return promote_point_to_top(model, X_702)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(702) on the given reference triangle."""
    model = create_model('X(702) = EVEN (- 4, 0) INFINITY POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00702(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00702.json"))
    write_center_svg(
        model_acute,
        here / "x-00702.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
