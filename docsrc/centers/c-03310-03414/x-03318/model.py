"""GEOMETOR construction model for X_3318 = INCIRCLE TRANSFORM T(X_603)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    incenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_03318(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3318 = INCIRCLE TRANSFORM T(X_603) on reference triangle ABC."""
    X_1359 = point_from_barycentrics(model, A, B, C, 0.11264368, 0.11034483, 0.77701149, ID="X_1359", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_3318 = reflection_in_point(model, X_1359, X_1, ID="X_3318", classes=["selected", "target"], guide=False)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_123 = eval_trilinear_point(model, A, B, C, '(csc(A))*(sec(B) - sec(C))*((sec(A))*((sin(B))**(2) - (sin(C))**(2)) + sin(C)*tan(C) - sin(B)*tan(B))', ID="X_123", classes=["center", "incident"])
    central_line(model, X_11, X_123, 11, 123, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center", "incident"])
    central_line(model, X_55, X_108, 55, 108, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_1295 = point_from_barycentrics(model, A, B, C, 0.79525862, 0.88362069, -0.67887931, ID="X_1295", classes=["center", "incident"])
    central_line(model, X_56, X_1295, 56, 1295, incident=True)
    return promote_point_to_top(model, X_3318)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3318 on the given reference triangle."""
    model = create_model('X_3318 = INCIRCLE TRANSFORM T(X_603)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03318(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03318.json"))
    write_center_svg(
        model_acute,
        here / "x-03318.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
