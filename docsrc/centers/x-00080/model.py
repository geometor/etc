"""GEOMETOR construction model for X(80) = REFLECTION OF INCENTER IN FEUERBACH POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcircle,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    incircle,
    isogonal_conjugate,
    nine_point_center_of,
    nine_point_circle,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00080(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(80) = REFLECTION OF INCENTER IN FEUERBACH POINT on reference triangle ABC."""
    incircle(model, A, B, C)
    circumcircle(model, A, B, C)
    nine_point_circle(model, A, B, C)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center"])
    central_line(model, X_1, X_5, 1, 5)
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X(21)", classes=["center"])
    central_line(model, X_10, X_21, 10, 21)
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X(65)", classes=["center"])
    X_79 = eval_trilinear_point(model, A, B, C, '1/(1 + 2*cos(A))', ID="X(79)", classes=["center"])
    central_line(model, X_65, X_79, 65, 79)
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X(36)", classes=["center"])
    X_80 = isogonal_conjugate(model, A, B, C, X_36, ID="X(80)", classes=["selected", "target"])
    return promote_point_to_top(model, X_80)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(80) on the given reference triangle."""
    model = create_model('X(80) = REFLECTION OF INCENTER IN FEUERBACH POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00080(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00080.json"))
    write_center_svg(
        model_acute,
        here / "x-00080.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
