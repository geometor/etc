"""GEOMETOR construction model for X(134) = X(107)-OF-ORTHIC-TRIANGLE."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00134(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(134) = X(107)-OF-ORTHIC-TRIANGLE on reference triangle ABC."""
    X_134 = point_from_barycentrics(model, A, B, C, 0.20948933, 0.10124204, 0.68926863, ID="X(134)", classes=["selected", "target"])
    X_52 = eval_trilinear_point(model, A, B, C, 'cos(2*A)*cos(B - C)', ID="X(52)", classes=["center", "incident"])
    X_128 = point_from_barycentrics(model, A, B, C, 0.43052912, -0.045594157, 0.61506504, ID="X(128)", classes=["center", "incident"])
    central_line(model, X_52, X_128, 52, 128, incident=True)
    return promote_point_to_top(model, X_134)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(134) on the given reference triangle."""
    model = create_model('X(134) = X(107)-OF-ORTHIC-TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00134(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00134.json"))
    write_center_svg(
        model_acute,
        here / "x-00134.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
