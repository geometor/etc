"""GEOMETOR construction model for X(541) = DIRECTION OF VECTOR AX + BX + CX, where X = X(74)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00541(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(541) = DIRECTION OF VECTOR AX + BX + CX, where X = X(74) on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X(74)", classes=["center"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center"])
    X_376 = eval_trilinear_point(model, A, B, C, '5*cos(A) - cos(B - C)', ID="X(376)", classes=["center"])
    central_line(model, X_2, X_74, 2, 74)
    central_line(model, X_110, X_376, 110, 376)
    X_541 = intersect_lines(model, X_2, X_74, X_110, X_376, ID="X(541)", classes=["selected", "target"])
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X(125)", classes=["center", "incident"])
    X_381 = eval_trilinear_point(model, A, B, C, '2*cos(B - C) - cos(A)', ID="X(381)", classes=["center", "incident"])
    central_line(model, X_125, X_381, 125, 381, incident=True)
    return promote_point_to_top(model, X_541)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(541) on the given reference triangle."""
    model = create_model('X(541) = DIRECTION OF VECTOR AX + BX + CX, where X = X(74)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00541(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00541.json"))
    write_center_svg(
        model_acute,
        here / "x-00541.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
