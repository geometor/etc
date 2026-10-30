"""GEOMETOR construction model for X(351) = CENTER OF THE PARRY CIRCLE."""

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


def construct_x_00351(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(351) = CENTER OF THE PARRY CIRCLE on reference triangle ABC."""
    X_187 = eval_trilinear_point(model, A, B, C, 'a*(2*a**(2) - b**(2) - c**(2))', ID="X(187)", classes=["center"])
    X_237 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A + omega )', ID="X(237)", classes=["center"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center"])
    X_526 = eval_trilinear_point(model, A, B, C, '(1 + 2*cos(2*A))*sin(B - C)', ID="X(526)", classes=["center"])
    central_line(model, X_187, X_237, 187, 237)
    central_line(model, X_110, X_526, 110, 526)
    X_351 = intersect_lines(model, X_187, X_237, X_110, X_526, ID="X(351)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_804 = eval_trilinear_point(model, A, B, C, 'a **(-3)*(b**(2) - c**(2)) + a**(1)*(b **(-2) - c **(-2))', ID="X(804)", classes=["center", "incident"])
    central_line(model, X_2, X_804, 2, 804, incident=True)
    return promote_point_to_top(model, X_351)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(351) on the given reference triangle."""
    model = create_model('X(351) = CENTER OF THE PARRY CIRCLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00351(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00351.json"))
    write_center_svg(
        model_acute,
        here / "x-00351.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
