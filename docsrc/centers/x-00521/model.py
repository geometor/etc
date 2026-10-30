"""GEOMETOR construction model for X(521) = ISOGONAL CONJUGATE OF X(108)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00521(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(521) = ISOGONAL CONJUGATE OF X(108) on reference triangle ABC."""
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X(108)", classes=["center"])
    X_521 = isogonal_conjugate(model, A, B, C, X_108, ID="X(521)", classes=["selected", "target"])
    X_59 = eval_trilinear_point(model, A, B, C, '1/(1 - cos(B - C))', ID="X(59)", classes=["center", "incident"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X(100)", classes=["center", "incident"])
    central_line(model, X_59, X_100, 59, 100, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X(511)", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    X_651 = eval_trilinear_point(model, A, B, C, '1/(cos(B) - cos(C))', ID="X(651)", classes=["center", "incident"])
    X_677 = point_from_barycentrics(model, A, B, C, -0.62962963, 0.83111111, 0.79851852, ID="X(677)", classes=["center", "incident"])
    central_line(model, X_651, X_677, 651, 677, incident=True)
    return promote_point_to_top(model, X_521)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(521) on the given reference triangle."""
    model = create_model('X(521) = ISOGONAL CONJUGATE OF X(108)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00521(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00521.json"))
    write_center_svg(
        model_acute,
        here / "x-00521.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
