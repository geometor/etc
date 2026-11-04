"""GEOMETOR construction model for X_2694 = SR(X_74, X_108)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02694(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2694 = SR(X_74, X_108) on reference triangle ABC."""
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center"])
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center"])
    X_521 = eval_trilinear_point(model, A, B, C, '(sec(B) - sec(C))*(csc(A))', ID="X_521", classes=["center"])
    central_line(model, X_30, X_108, 30, 108)
    central_line(model, X_74, X_521, 74, 521)
    X_2694 = intersect_lines(model, X_30, X_108, X_74, X_521, ID="X_2694", classes=["selected", "target"])
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_1290 = point_from_barycentrics(model, A, B, C, -0.096774194, 0.87096774, 0.22580645, ID="X_1290", classes=["center", "incident"])
    central_line(model, X_20, X_1290, 20, 1290, incident=True)
    return promote_point_to_top(model, X_2694)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2694 on the given reference triangle."""
    model = create_model('X_2694 = SR(X_74, X_108)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02694(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02694.json"))
    write_center_svg(
        model_acute,
        here / "x-02694.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
