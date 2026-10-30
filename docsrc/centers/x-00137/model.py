"""GEOMETOR construction model for X(137) = X(110)-OF-ORTHIC-TRIANGLE."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nine_point_center_of,
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_00137(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(137) = X(110)-OF-ORTHIC-TRIANGLE on reference triangle ABC."""
    X_128 = point_from_barycentrics(model, A, B, C, 0.43052912, -0.045594157, 0.61506504, ID="X(128)", classes=["center"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center"])
    X_137 = reflection_in_point(model, X_128, X_5, ID="X(137)", classes=["selected", "target"], guide=False)
    central_line(model, X_5, X_128, 5, 128, incident=True)
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X(51)", classes=["center", "incident"])
    X_129 = point_from_barycentrics(model, A, B, C, 0.22802261, -0.036048578, 0.80802596, ID="X(129)", classes=["center", "incident"])
    central_line(model, X_51, X_129, 51, 129, incident=True)
    X_53 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(B - C)', ID="X(53)", classes=["center", "incident"])
    X_138 = point_from_barycentrics(model, A, B, C, 0.092526257, 0.069481522, 0.83799222, ID="X(138)", classes=["center", "incident"])
    central_line(model, X_53, X_138, 53, 138, incident=True)
    return promote_point_to_top(model, X_137)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(137) on the given reference triangle."""
    model = create_model('X(137) = X(110)-OF-ORTHIC-TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00137(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00137.json"))
    write_center_svg(
        model_acute,
        here / "x-00137.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
