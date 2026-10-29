"""GEOMETOR construction model for X(56) = EXSIMILICENTER(CIRCUMCIRCLE, INCIRCLE)."""

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
    feuerbach_point_of,
    incenter_of,
    midpoint,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00056(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(56) = EXSIMILICENTER(CIRCUMCIRCLE, INCIRCLE) on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X(46)", classes=["center"])
    X_56 = midpoint(model, X_1, X_46, ID="X(56)", classes=["selected", "target"], guide=False)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    central_line(model, X_1, X_3, 1, 3, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X(12)", classes=["center", "incident"])
    central_line(model, X_2, X_12, 2, 12, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X(11)", classes=["center", "incident"])
    central_line(model, X_4, X_11, 4, 11, incident=True)
    return promote_point_to_top(model, X_56)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(56) on the given reference triangle."""
    model = create_model('X(56) = EXSIMILICENTER(CIRCUMCIRCLE, INCIRCLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00056(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00056.json"))
    write_center_svg(
        model_acute,
        here / "x-00056.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
