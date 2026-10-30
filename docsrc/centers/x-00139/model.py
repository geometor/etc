"""GEOMETOR construction model for X(139) = X(112)-OF-ORTHIC-TRIANGLE."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00139(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(139) = X(112)-OF-ORTHIC-TRIANGLE on reference triangle ABC."""
    X_52 = eval_trilinear_point(model, A, B, C, 'cos(2*A)*cos(B - C)', ID="X(52)", classes=["center"])
    X_129 = point_from_barycentrics(model, A, B, C, 0.22802261, -0.036048578, 0.80802596, ID="X(129)", classes=["center"])
    X_53 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(B - C)', ID="X(53)", classes=["center"])
    X_128 = point_from_barycentrics(model, A, B, C, 0.43052912, -0.045594157, 0.61506504, ID="X(128)", classes=["center"])
    central_line(model, X_52, X_129, 52, 129)
    central_line(model, X_53, X_128, 53, 128)
    X_139 = intersect_lines(model, X_52, X_129, X_53, X_128, ID="X(139)", classes=["selected", "target"])
    return promote_point_to_top(model, X_139)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(139) on the given reference triangle."""
    model = create_model('X(139) = X(112)-OF-ORTHIC-TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00139(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00139.json"))
    write_center_svg(
        model_acute,
        here / "x-00139.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
