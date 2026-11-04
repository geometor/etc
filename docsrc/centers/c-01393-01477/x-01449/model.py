"""GEOMETOR construction model for X_1449 = {X_1,X_6}-HARMONIC CONJUGATE OF X_9."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01449(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1449 = {X_1,X_6}-HARMONIC CONJUGATE OF X_9 on reference triangle ABC."""
    X_1449 = eval_trilinear_point(model, A, B, C, '3*a + b + c', ID="X_1449", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X_77", classes=["center", "incident"])
    central_line(model, X_57, X_77, 57, 77, incident=True)
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    X_380 = eval_trilinear_point(model, A, B, C, '((b + c - a)*(3*a**(3) + (b + c)*(3*a**(2) + (b - c)**(2) + a*(b + c))))', ID="X_380", classes=["center", "incident"])
    central_line(model, X_65, X_380, 65, 380, incident=True)
    return promote_point_to_top(model, X_1449)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1449 on the given reference triangle."""
    model = create_model('X_1449 = {X_1,X_6}-HARMONIC CONJUGATE OF X_9')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01449(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01449.json"))
    write_center_svg(
        model_acute,
        here / "x-01449.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
