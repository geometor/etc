"""GEOMETOR construction model for X(529) = DIRECTION OF VECTOR AX + BX + CX, where X = X(12)."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00529(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(529) = DIRECTION OF VECTOR AX + BX + CX, where X = X(12) on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X(12)", classes=["center"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X(511)", classes=["center"])
    central_line(model, X_2, X_12, 2, 12)
    central_line(model, X_30, X_511, 30, 511)
    X_529 = intersect_lines(model, X_2, X_12, X_30, X_511, ID="X(529)", classes=["selected", "target"])
    X_495 = eval_trilinear_point(model, A, B, C, '2 + cos(B - C)', ID="X(495)", classes=["center", "incident"])
    X_993 = point_from_barycentrics(model, A, B, C, 0.38398693, 0.35294118, 0.2630719, ID="X(993)", classes=["center", "incident"])
    central_line(model, X_495, X_993, 495, 993, incident=True)
    return promote_point_to_top(model, X_529)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(529) on the given reference triangle."""
    model = create_model('X(529) = DIRECTION OF VECTOR AX + BX + CX, where X = X(12)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00529(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00529.json"))
    write_center_svg(
        model_acute,
        here / "x-00529.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
