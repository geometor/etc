"""GEOMETOR construction model for X_1359 = BRISSE TRANSFORM OF X_102."""

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
    intersect_lines,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01359(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1359 = BRISSE TRANSFORM OF X_102 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center"])
    X_123 = eval_trilinear_point(model, A, B, C, '(csc(A))*(sec(B) - sec(C))*((sec(A))*((sin(B))**(2) - (sin(C))**(2)) + sin(C)*tan(C) - sin(B)*tan(B))', ID="X_123", classes=["center"])
    central_line(model, X_4, X_11, 4, 11)
    central_line(model, X_12, X_123, 12, 123)
    X_1359 = intersect_lines(model, X_4, X_11, X_12, X_123, ID="X_1359", classes=["selected", "target"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_1295 = point_from_barycentrics(model, A, B, C, 0.79525862, 0.88362069, -0.67887931, ID="X_1295", classes=["center", "incident"])
    central_line(model, X_55, X_1295, 55, 1295, incident=True)
    return promote_point_to_top(model, X_1359)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1359 on the given reference triangle."""
    model = create_model('X_1359 = BRISSE TRANSFORM OF X_102')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01359(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01359.json"))
    write_center_svg(
        model_acute,
        here / "x-01359.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
