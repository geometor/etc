"""GEOMETOR construction model for X(442) = COMPLEMENT OF SCHIFFLER POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    midpoint,
    mittenpunkt_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00442(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(442) = COMPLEMENT OF SCHIFFLER POINT on reference triangle ABC."""
    X_79 = eval_trilinear_point(model, A, B, C, '1/(1 + 2*cos(A))', ID="X(79)", classes=["center"])
    X_191 = eval_trilinear_point(model, A, B, C, '(b + c - a)*(b*c + c*a + a*b) + b**(3) + c**(3) - a**(3)', ID="X(191)", classes=["center"])
    X_442 = midpoint(model, X_79, X_191, ID="X(442)", classes=["selected", "target"], guide=False)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X(12)", classes=["center", "incident"])
    central_line(model, X_10, X_12, 10, 12, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X(46)", classes=["center", "incident"])
    central_line(model, X_9, X_46, 9, 46, incident=True)
    return promote_point_to_top(model, X_442)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(442) on the given reference triangle."""
    model = create_model('X(442) = COMPLEMENT OF SCHIFFLER POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00442(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00442.json"))
    write_center_svg(
        model_acute,
        here / "x-00442.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
