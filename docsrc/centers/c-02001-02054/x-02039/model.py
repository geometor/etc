"""GEOMETOR construction model for X_2039 = 1st NINE-POINT-CIRCLE-KIEPERT-ASYMPTOTES INTERSECTION."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    midpoint,
    nine_point_center_of,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02039(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2039 = 1st NINE-POINT-CIRCLE-KIEPERT-ASYMPTOTES INTERSECTION on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_1380 = eval_trilinear_point(model, A, B, C, 'e*cos(A) + cos(A +  omega  )', ID="X_1380", classes=["center"])
    X_2039 = midpoint(model, X_4, X_1380, ID="X_2039", classes=["selected", "target"], guide=False)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X_141", classes=["center", "incident"])
    central_line(model, X_5, X_141, 5, 141, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_1349 = eval_trilinear_point(model, A, B, C, 'e*cos(B - C) - cos(A -  omega  )', ID="X_1349", classes=["center", "incident"])
    central_line(model, X_3, X_1349, 3, 1349, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_1348 = eval_trilinear_point(model, A, B, C, 'e*cos(B - C) + cos(A -  omega  )', ID="X_1348", classes=["center", "incident"])
    central_line(model, X_6, X_1348, 6, 1348, incident=True)
    return promote_point_to_top(model, X_2039)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2039 on the given reference triangle."""
    model = create_model('X_2039 = 1st NINE-POINT-CIRCLE-KIEPERT-ASYMPTOTES INTERSECTION')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02039(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02039.json"))
    write_center_svg(
        model_acute,
        here / "x-02039.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
