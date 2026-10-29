"""GEOMETOR construction model for X(1) = INCENTER."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    feuerbach_point_of,
    incenter_of,
    mittenpunkt_of,
    nagel_point_of,
    nine_point_center_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00001(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(1) = INCENTER on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center"])
    central_line(model, X_2, X_8, 2, 8)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center"])
    central_line(model, X_6, X_9, 6, 9)
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X(11)", classes=["center"])
    central_line(model, X_5, X_11, 5, 11)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["selected", "target"], draw_bisectors=True, draw_incircle=True)
    return promote_point_to_top(model, X_1)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = True,
) -> Model:
    """Build a `geometor.model.Model` for X(1) on the given reference triangle."""
    model = create_model('X(1) = INCENTER')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00001(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00001.json"))
    write_center_svg(
        model_acute,
        here / "x-00001.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
