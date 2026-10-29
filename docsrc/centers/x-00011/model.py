"""GEOMETOR construction model for X(11) = FEUERBACH POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcircle,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    incenter_of,
    medial_triangle,
    nine_point_center_of,
    orthic_triangle,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00011(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(11) = FEUERBACH POINT on reference triangle ABC."""
    medial_triangle(model, A, B, C)
    orthic_triangle(model, A, B, C)
    circumcircle(model, A, B, C)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center"])
    central_line(model, X_1, X_5, 1, 5)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X(55)", classes=["center"])
    central_line(model, X_2, X_55, 2, 55)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X(56)", classes=["center"])
    central_line(model, X_4, X_56, 4, 56)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X(11)", classes=["selected", "target"], draw_circles=True)
    return promote_point_to_top(model, X_11)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(11) on the given reference triangle."""
    model = create_model('X(11) = FEUERBACH POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00011(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00011.json"))
    write_center_svg(
        model_acute,
        here / "x-00011.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
