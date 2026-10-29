"""GEOMETOR construction model for X(550) = MIDPOINT OF X(3) AND X(20)."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00550(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(550) = MIDPOINT OF X(3) AND X(20) on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X(20)", classes=["center"])
    X_550 = midpoint(model, X_3, X_20, ID="X(550)", classes=["selected", "target"], guide=False)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_15 = eval_trilinear_point(model, A, B, C, 'sin(A + pi /3)', ID="X(15)", classes=["center", "incident"])
    X_397 = eval_trilinear_point(model, A, B, C, 'cos(B - C) - 2*cos(A + pi /3)', ID="X(397)", classes=["center", "incident"])
    central_line(model, X_15, X_397, 15, 397, incident=True)
    X_16 = eval_trilinear_point(model, A, B, C, 'sin(A- pi /3)', ID="X(16)", classes=["center", "incident"])
    X_398 = eval_trilinear_point(model, A, B, C, 'cos(B - C) - 2*cos(A - pi /3)', ID="X(398)", classes=["center", "incident"])
    central_line(model, X_16, X_398, 16, 398, incident=True)
    return promote_point_to_top(model, X_550)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(550) on the given reference triangle."""
    model = create_model('X(550) = MIDPOINT OF X(3) AND X(20)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00550(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00550.json"))
    write_center_svg(
        model_acute,
        here / "x-00550.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
