"""GEOMETOR construction model for X(544) = DIRECTION OF VECTOR AX + BX + CX, where X = X(101)."""

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


def construct_x_00544(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(544) = DIRECTION OF VECTOR AX + BX + CX, where X = X(101) on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center"])
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X(103)", classes=["center"])
    X_376 = eval_trilinear_point(model, A, B, C, '5*cos(A) - cos(B - C)', ID="X(376)", classes=["center"])
    central_line(model, X_2, X_101, 2, 101)
    central_line(model, X_103, X_376, 103, 376)
    X_544 = intersect_lines(model, X_2, X_101, X_103, X_376, ID="X(544)", classes=["selected", "target"])
    X_118 = point_from_barycentrics(model, A, B, C, 0.28918651, -0.056547619, 0.76736111, ID="X(118)", classes=["center", "incident"])
    X_381 = eval_trilinear_point(model, A, B, C, '2*cos(B - C) - cos(A)', ID="X(381)", classes=["center", "incident"])
    central_line(model, X_118, X_381, 118, 381, incident=True)
    return promote_point_to_top(model, X_544)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(544) on the given reference triangle."""
    model = create_model('X(544) = DIRECTION OF VECTOR AX + BX + CX, where X = X(101)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00544(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00544.json"))
    write_center_svg(
        model_acute,
        here / "x-00544.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
