"""GEOMETOR construction model for X_2610 = SUM OF PU(71)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02610(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2610 = SUM OF PU(71) on reference triangle ABC."""
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center"])
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X_125", classes=["center"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center"])
    central_line(model, X_115, X_125, 115, 125)
    central_line(model, X_44, X_513, 44, 513)
    X_2610 = intersect_lines(model, X_115, X_125, X_44, X_513, ID="X_2610", classes=["selected", "target"])
    X_918 = eval_barycentric_point(model, A, B, C, '((b - c)*(b**(2) + c**(2) -a*b - a*c))', ID="X_918", classes=["center", "incident"])
    X_1211 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c)*(b**(2) + c**(2) + a*b + a*c))', ID="X_1211", classes=["center", "incident"])
    central_line(model, X_918, X_1211, 918, 1211, incident=True)
    return promote_point_to_top(model, X_2610)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2610 on the given reference triangle."""
    model = create_model('X_2610 = SUM OF PU(71)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02610(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02610.json"))
    write_center_svg(
        model_acute,
        here / "x-02610.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
