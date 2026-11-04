"""GEOMETOR construction model for X_1883 = ZOSMA TRANSFORM OF X_595."""

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
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01883(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1883 = ZOSMA TRANSFORM OF X_595 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center"])
    X_1828 = point_from_barycentrics(model, A, B, C, 0.087301587, 0.19047619, 0.72222222, ID="X_1828", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    central_line(model, X_10, X_1828, 10, 1828)
    X_1883 = intersect_lines(model, X_2, X_3, X_10, X_1828, ID="X_1883", classes=["selected", "target"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    X_1877 = point_from_barycentrics(model, A, B, C, -0.11111111, 1.2901611e-16, 1.1111111, ID="X_1877", classes=["center", "incident"])
    central_line(model, X_12, X_1877, 12, 1877, incident=True)
    return promote_point_to_top(model, X_1883)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1883 on the given reference triangle."""
    model = create_model('X_1883 = ZOSMA TRANSFORM OF X_595')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01883(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01883.json"))
    write_center_svg(
        model_acute,
        here / "x-01883.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
