"""GEOMETOR construction model for X(227) = X(10)-CEVA CONJUGATE OF X(65)."""

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


def construct_x_00227(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(227) = X(10)-CEVA CONJUGATE OF X(65) on reference triangle ABC."""
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X(12)", classes=["center"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X(34)", classes=["center"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X(55)", classes=["center"])
    central_line(model, X_12, X_37, 12, 37)
    central_line(model, X_34, X_55, 34, 55)
    X_227 = intersect_lines(model, X_12, X_37, X_34, X_55, ID="X(227)", classes=["selected", "target"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X(42)", classes=["center", "incident"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X(65)", classes=["center", "incident"])
    central_line(model, X_42, X_65, 42, 65, incident=True)
    return promote_point_to_top(model, X_227)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(227) on the given reference triangle."""
    model = create_model('X(227) = X(10)-CEVA CONJUGATE OF X(65)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00227(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00227.json"))
    write_center_svg(
        model_acute,
        here / "x-00227.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
