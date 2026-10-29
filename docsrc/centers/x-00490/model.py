"""GEOMETOR construction model for X(490) = CEVAPOINT OF X(20) AND X(488)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    cevapoint,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00490(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(490) = CEVAPOINT OF X(20) AND X(488) on reference triangle ABC."""
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X(20)", classes=["center"])
    X_488 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 + csc(A)*sin(B)*sin(C))', ID="X(488)", classes=["center"])
    X_490 = cevapoint(model, A, B, C, X_20, X_488, ID="X(490)", classes=["selected", "target"])
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X(64)", classes=["center", "incident"])
    central_line(model, X_20, X_64, 20, 64, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    central_line(model, X_4, X_488, 4, 488, incident=True)
    X_376 = eval_trilinear_point(model, A, B, C, '5*cos(A) - cos(B - C)', ID="X(376)", classes=["center", "incident"])
    X_487 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 - csc(A)*sin(B)*sin(C))', ID="X(487)", classes=["center", "incident"])
    central_line(model, X_376, X_487, 376, 487, incident=True)
    return promote_point_to_top(model, X_490)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(490) on the given reference triangle."""
    model = create_model('X(490) = CEVAPOINT OF X(20) AND X(488)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00490(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00490.json"))
    write_center_svg(
        model_acute,
        here / "x-00490.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
