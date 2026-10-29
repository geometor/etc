"""GEOMETOR construction model for X(859) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(81)."""

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


def construct_x_00859(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(859) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(81) on reference triangle ABC."""
    X_851 = eval_trilinear_point(model, A, B, C, 'sin(2*B)*sin(C - A) + sin(2*C)*sin(B - A)', ID="X(851)", classes=["center"])
    X_855 = eval_trilinear_point(model, A, B, C, 'cot(C/2)*sin(2*B)*sin(C - A) + cot(B/2)*sin(2*C)*sin(B - A)', ID="X(855)", classes=["center"])
    X_859 = midpoint(model, X_851, X_855, ID="X(859)", classes=["selected", "target"], guide=False)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X(56)", classes=["center", "incident"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X(58)", classes=["center", "incident"])
    central_line(model, X_56, X_58, 56, 58, incident=True)
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X(36)", classes=["center", "incident"])
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X(238)", classes=["center", "incident"])
    central_line(model, X_36, X_238, 36, 238, incident=True)
    return promote_point_to_top(model, X_859)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(859) on the given reference triangle."""
    model = create_model('X(859) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(81)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00859(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00859.json"))
    write_center_svg(
        model_acute,
        here / "x-00859.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
