"""GEOMETOR construction model for X(543) = DIRECTION OF VECTOR AX + BX + CX, where X = X(99)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00543(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(543) = DIRECTION OF VECTOR AX + BX + CX, where X = X(99) on reference triangle ABC."""
    X_543 = eval_barycentric_point(model, A, B, C, '2*a**(4) - b**(4) - c**(4) - 2*a**(2)*b**(2) - 2*a**(2)*c**(2) + 4*b**(2)*c**(2)', ID="X(543)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    central_line(model, X_2, X_99, 2, 99, incident=True)
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A + omega )', ID="X(98)", classes=["center", "incident"])
    X_376 = eval_trilinear_point(model, A, B, C, '5*cos(A) - cos(B - C)', ID="X(376)", classes=["center", "incident"])
    central_line(model, X_98, X_376, 98, 376, incident=True)
    X_114 = point_from_barycentrics(model, A, B, C, 0.37082211, -0.060960354, 0.69013825, ID="X(114)", classes=["center", "incident"])
    X_381 = eval_trilinear_point(model, A, B, C, '2*cos(B - C) - cos(A)', ID="X(381)", classes=["center", "incident"])
    central_line(model, X_114, X_381, 114, 381, incident=True)
    return promote_point_to_top(model, X_543)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(543) on the given reference triangle."""
    model = create_model('X(543) = DIRECTION OF VECTOR AX + BX + CX, where X = X(99)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00543(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00543.json"))
    write_center_svg(
        model_acute,
        here / "x-00543.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
