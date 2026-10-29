"""GEOMETOR construction model for X(229) = X(7)-CEVA CONJUGATE OF X(81)."""

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


def construct_x_00229(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(229) = X(7)-CEVA CONJUGATE OF X(81) on reference triangle ABC."""
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X(21)", classes=["center"])
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X(36)", classes=["center"])
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X(28)", classes=["center"])
    X_60 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(B - C))', ID="X(60)", classes=["center"])
    central_line(model, X_21, X_36, 21, 36)
    central_line(model, X_28, X_60, 28, 60)
    X_229 = intersect_lines(model, X_21, X_36, X_28, X_60, ID="X(229)", classes=["selected", "target"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X(65)", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    central_line(model, X_65, X_110, 65, 110, incident=True)
    return promote_point_to_top(model, X_229)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(229) on the given reference triangle."""
    model = create_model('X(229) = X(7)-CEVA CONJUGATE OF X(81)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00229(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00229.json"))
    write_center_svg(
        model_acute,
        here / "x-00229.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
