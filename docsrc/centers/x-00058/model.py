"""GEOMETOR construction model for X(58) = ISOGONAL CONJUGATE OF X(10)."""

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
    incenter_of,
    incircle,
    isogonal_conjugate,
    promote_point_to_top,
    spieker_center_of,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00058(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(58) = ISOGONAL CONJUGATE OF X(10) on reference triangle ABC."""
    incircle(model, A, B, C)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    central_line(model, X_3, X_6, 3, 6)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X(21)", classes=["center"])
    central_line(model, X_1, X_21, 1, 21)
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X(28)", classes=["center"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X(34)", classes=["center"])
    central_line(model, X_28, X_34, 28, 34)
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center"])
    X_58 = isogonal_conjugate(model, A, B, C, X_10, ID="X(58)", classes=["selected", "target"])
    return promote_point_to_top(model, X_58)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(58) on the given reference triangle."""
    model = create_model('X(58) = ISOGONAL CONJUGATE OF X(10)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00058(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00058.json"))
    write_center_svg(
        model_acute,
        here / "x-00058.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
