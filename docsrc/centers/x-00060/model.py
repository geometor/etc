"""GEOMETOR construction model for X(60) = ISOGONAL CONJUGATE OF X(12)."""

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
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00060(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(60) = ISOGONAL CONJUGATE OF X(12) on reference triangle ABC."""
    circumcircle(model, A, B, C)
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X(36)", classes=["center"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X(58)", classes=["center"])
    central_line(model, X_36, X_58, 36, 58)
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X(28)", classes=["center"])
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X(81)", classes=["center"])
    central_line(model, X_28, X_81, 28, 81)
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X(12)", classes=["center"])
    X_60 = isogonal_conjugate(model, A, B, C, X_12, ID="X(60)", classes=["selected", "target"])
    return promote_point_to_top(model, X_60)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(60) on the given reference triangle."""
    model = create_model('X(60) = ISOGONAL CONJUGATE OF X(12)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00060(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00060.json"))
    write_center_svg(
        model_acute,
        here / "x-00060.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
