"""GEOMETOR construction model for X(856) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(63)."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_00856(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(856) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(63) on reference triangle ABC."""
    X_856 = eval_trilinear_point(model, A, B, C, 'tan(C)*sin(2*B)*sin(C - A) + tan(B)*sin(2*C)*sin(B - A)', ID="X(856)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_521 = eval_trilinear_point(model, A, B, C, '(sec(B) - sec(C))*(csc(A))', ID="X(521)", classes=["center", "incident"])
    X_656 = eval_trilinear_point(model, A, B, C, 'tan(B) - tan(C)', ID="X(656)", classes=["center", "incident"])
    central_line(model, X_521, X_656, 521, 656, incident=True)
    return promote_point_to_top(model, X_856)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(856) on the given reference triangle."""
    model = create_model('X(856) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(63)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00856(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00856.json"))
    write_center_svg(
        model_acute,
        here / "x-00856.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
