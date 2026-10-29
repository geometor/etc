"""GEOMETOR construction model for X(100) = ANTICOMPLEMENT OF FEUERBACH POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    anticomplement,
    central_line,
    centroid_of,
    circumcenter_of,
    circumcircle,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    incircle,
    medial_triangle,
    nagel_point_of,
    nine_point_circle,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00100(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(100) = ANTICOMPLEMENT OF FEUERBACH POINT on reference triangle ABC."""
    medial_triangle(model, A, B, C)
    incircle(model, A, B, C)
    circumcircle(model, A, B, C)
    nine_point_circle(model, A, B, C)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center"])
    central_line(model, X_3, X_8, 3, 8)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X(11)", classes=["center"])
    central_line(model, X_2, X_11, 2, 11)
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X(21)", classes=["center"])
    central_line(model, X_10, X_21, 10, 21)
    X_100 = anticomplement(model, A, B, C, X_11, ID="X(100)", classes=["selected", "target"])
    return promote_point_to_top(model, X_100)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(100) on the given reference triangle."""
    model = create_model('X(100) = ANTICOMPLEMENT OF FEUERBACH POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00100(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00100.json"))
    write_center_svg(
        model_acute,
        here / "x-00100.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
