"""GEOMETOR construction model for X(36) = INVERSE-IN-CIRCUMCIRCLE OF INCENTER."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    circumcircle,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    incenter_of,
    incircle,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00036(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(36) = INVERSE-IN-CIRCUMCIRCLE OF INCENTER on reference triangle ABC."""
    incircle(model, A, B, C)
    circumcircle(model, A, B, C)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_1, X_3, 1, 3)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X(11)", classes=["center"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center"])
    central_line(model, X_11, X_30, 11, 30)
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X(24)", classes=["center"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X(34)", classes=["center"])
    central_line(model, X_24, X_34, 24, 34)
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X(36)", classes=["selected", "target"])
    return promote_point_to_top(model, X_36)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(36) on the given reference triangle."""
    model = create_model('X(36) = INVERSE-IN-CIRCUMCIRCLE OF INCENTER')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00036(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00036.json"))
    write_center_svg(
        model_acute,
        here / "x-00036.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
