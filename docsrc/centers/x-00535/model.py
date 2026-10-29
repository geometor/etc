"""GEOMETOR construction model for X(535) = DIRECTION OF VECTOR AX + BX + CX, where X = X(36)."""

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


def construct_x_00535(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(535) = DIRECTION OF VECTOR AX + BX + CX, where X = X(36) on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X(36)", classes=["center"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X(511)", classes=["center"])
    central_line(model, X_2, X_36, 2, 36)
    central_line(model, X_30, X_511, 30, 511)
    X_535 = intersect_lines(model, X_2, X_36, X_30, X_511, ID="X(535)", classes=["selected", "target"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X(63)", classes=["center", "incident"])
    X_484 = eval_trilinear_point(model, A, B, C, '1 + 2*(cos(A) - cos(B) - cos(C))', ID="X(484)", classes=["center", "incident"])
    central_line(model, X_63, X_484, 63, 484, incident=True)
    return promote_point_to_top(model, X_535)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(535) on the given reference triangle."""
    model = create_model('X(535) = DIRECTION OF VECTOR AX + BX + CX, where X = X(36)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00535(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00535.json"))
    write_center_svg(
        model_acute,
        here / "x-00535.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
