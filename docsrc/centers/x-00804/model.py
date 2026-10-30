"""GEOMETOR construction model for X(804) = ODD (- 2, 2) INFINITY POINT."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00804(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(804) = ODD (- 2, 2) INFINITY POINT on reference triangle ABC."""
    X_804 = eval_trilinear_point(model, A, B, C, 'a **(-3)*(b**(2) - c**(2)) + a**(1)*(b **(-2) - c **(-2))', ID="X(804)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_351 = point_from_barycentrics(model, A, B, C, -1.104798, 0.16783217, 1.9369658, ID="X(351)", classes=["center", "incident"])
    central_line(model, X_2, X_351, 2, 351, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X(511)", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    X_670 = eval_trilinear_point(model, A, B, C, '1/(a**(3)*(b**(2) - c**(2)))', ID="X(670)", classes=["center", "incident"])
    central_line(model, X_99, X_670, 99, 670, incident=True)
    return promote_point_to_top(model, X_804)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(804) on the given reference triangle."""
    model = create_model('X(804) = ODD (- 2, 2) INFINITY POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00804(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00804.json"))
    write_center_svg(
        model_acute,
        here / "x-00804.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
