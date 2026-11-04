"""GEOMETOR construction model for X_2642 = SUM OF PU(79)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02642(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2642 = SUM OF PU(79) on reference triangle ABC."""
    X_2642 = eval_trilinear_point(model, A, B, C, '1/(cot(C) - cot(A)) + 1/(cot(B) - cot(A))', ID="X_2642", classes=["selected", "target"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    central_line(model, X_44, X_513, 44, 513, incident=True)
    X_163 = eval_trilinear_point(model, A, B, C, '(sin(2*A))/(sin(2*B) - sin(2*C))', ID="X_163", classes=["center", "incident"])
    X_662 = eval_trilinear_point(model, A, B, C, '1/(cot(B) - cot(C))', ID="X_662", classes=["center", "incident"])
    central_line(model, X_163, X_662, 163, 662, incident=True)
    X_900 = eval_trilinear_point(model, A, B, C, '(b - c)*(b + c - 2*a)/a', ID="X_900", classes=["center", "incident"])
    X_1213 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c)*(2*a + b + c))', ID="X_1213", classes=["center", "incident"])
    central_line(model, X_900, X_1213, 900, 1213, incident=True)
    return promote_point_to_top(model, X_2642)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2642 on the given reference triangle."""
    model = create_model('X_2642 = SUM OF PU(79)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02642(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02642.json"))
    write_center_svg(
        model_acute,
        here / "x-02642.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
