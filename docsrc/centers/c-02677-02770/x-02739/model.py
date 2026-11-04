"""GEOMETOR construction model for X_2739 = SR(X_103, X_108)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_02739(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2739 = SR(X_103, X_108) on reference triangle ABC."""
    X_2728 = point_from_barycentrics(model, A, B, C, -0.15565134, 0.36494253, 0.79070881, ID="X_2728", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_2739 = reflection_in_point(model, X_2728, X_3, ID="X_2739", classes=["selected", "target"], guide=False)
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X_103", classes=["center", "incident"])
    X_521 = eval_trilinear_point(model, A, B, C, '(sec(B) - sec(C))*(csc(A))', ID="X_521", classes=["center", "incident"])
    central_line(model, X_103, X_521, 103, 521, incident=True)
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center", "incident"])
    X_516 = eval_trilinear_point(model, A, B, C, 'b*c*((a - b)*cot(C) + (a - c)*cot(B))', ID="X_516", classes=["center", "incident"])
    central_line(model, X_108, X_516, 108, 516, incident=True)
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center", "incident"])
    X_1295 = point_from_barycentrics(model, A, B, C, 0.79525862, 0.88362069, -0.67887931, ID="X_1295", classes=["center", "incident"])
    central_line(model, X_514, X_1295, 514, 1295, incident=True)
    return promote_point_to_top(model, X_2739)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2739 on the given reference triangle."""
    model = create_model('X_2739 = SR(X_103, X_108)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02739(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02739.json"))
    write_center_svg(
        model_acute,
        here / "x-02739.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
