"""GEOMETOR construction model for X(150) = REFLECTION OF X(20) IN X(103)."""

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
    gergonne_point_of,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00150(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(150) = REFLECTION OF X(20) IN X(103) on reference triangle ABC."""
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center"])
    X_80 = eval_trilinear_point(model, A, B, C, '1/(1 - 2*cos(A))', ID="X(80)", classes=["center"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center"])
    central_line(model, X_7, X_80, 7, 80)
    central_line(model, X_2, X_101, 2, 101)
    X_150 = intersect_lines(model, X_7, X_80, X_2, X_101, ID="X(150)", classes=["selected", "target"])
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X(20)", classes=["center", "incident"])
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X(103)", classes=["center", "incident"])
    central_line(model, X_20, X_103, 20, 103, incident=True)
    return promote_point_to_top(model, X_150)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(150) on the given reference triangle."""
    model = create_model('X(150) = REFLECTION OF X(20) IN X(103)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00150(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00150.json"))
    write_center_svg(
        model_acute,
        here / "x-00150.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
