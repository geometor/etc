"""GEOMETOR construction model for X_1341 = EXSIMILICENTER(CIRCUMCIRCLE, BROCARD CIRCLE)."""

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
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01341(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1341 = EXSIMILICENTER(CIRCUMCIRCLE, BROCARD CIRCLE) on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_1348 = eval_trilinear_point(model, A, B, C, 'e*cos(B - C) + cos(A -  omega  )', ID="X_1348", classes=["center"])
    central_line(model, X_3, X_6, 3, 6)
    central_line(model, X_2, X_1348, 2, 1348)
    X_1341 = intersect_lines(model, X_3, X_6, X_2, X_1348, ID="X_1341", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_1349 = eval_trilinear_point(model, A, B, C, 'e*cos(B - C) - cos(A -  omega  )', ID="X_1349", classes=["center", "incident"])
    central_line(model, X_4, X_1349, 4, 1349, incident=True)
    return promote_point_to_top(model, X_1341)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1341 on the given reference triangle."""
    model = create_model('X_1341 = EXSIMILICENTER(CIRCUMCIRCLE, BROCARD CIRCLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01341(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01341.json"))
    write_center_svg(
        model_acute,
        here / "x-01341.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
