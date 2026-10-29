"""GEOMETOR construction model for X(918) = ISOTOMIC CONJUGATE OF X(666)."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00918(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(918) = ISOTOMIC CONJUGATE OF X(666) on reference triangle ABC."""
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X(511)", classes=["center"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X(63)", classes=["center"])
    X_654 = eval_trilinear_point(model, A, B, C, 'cos(A - B) - cos(C - A)', ID="X(654)", classes=["center"])
    central_line(model, X_30, X_511, 30, 511)
    central_line(model, X_63, X_654, 63, 654)
    X_918 = intersect_lines(model, X_30, X_511, X_63, X_654, ID="X(918)", classes=["selected", "target"])
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X(190)", classes=["center", "incident"])
    X_644 = eval_trilinear_point(model, A, B, C, '(b + c - a)/(b - c)', ID="X(644)", classes=["center", "incident"])
    central_line(model, X_190, X_644, 190, 644, incident=True)
    return promote_point_to_top(model, X_918)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(918) on the given reference triangle."""
    model = create_model('X(918) = ISOTOMIC CONJUGATE OF X(666)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00918(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00918.json"))
    write_center_svg(
        model_acute,
        here / "x-00918.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
