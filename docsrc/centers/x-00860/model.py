"""GEOMETOR construction model for X(860) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(92)."""

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
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00860(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(860) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(92) on reference triangle ABC."""
    X_860 = eval_trilinear_point(model, A, B, C, '(tan(A) + tan(B))*sin(2*B)*sin(C - A) + (tan(A) + tan(C))*sin(2*C)*sin(B - A)', ID="X(860)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    X_201 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 + cos(B - C))', ID="X(201)", classes=["center", "incident"])
    central_line(model, X_10, X_201, 10, 201, incident=True)
    X_240 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(A + omega )', ID="X(240)", classes=["center", "incident"])
    X_522 = eval_trilinear_point(model, A, B, C, '(cos(B) - cos(C))*(csc(A))', ID="X(522)", classes=["center", "incident"])
    central_line(model, X_240, X_522, 240, 522, incident=True)
    return promote_point_to_top(model, X_860)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(860) on the given reference triangle."""
    model = create_model('X(860) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(92)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00860(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00860.json"))
    write_center_svg(
        model_acute,
        here / "x-00860.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
