"""GEOMETOR construction model for X_3985 = X_3290com[INVERSE(n(INCENTRAL TRIANGLE))]."""

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
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03985(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3985 = X_3290com[INVERSE(n(INCENTRAL TRIANGLE))] on reference triangle ABC."""
    X_3985 = eval_barycentric_point(model, A, B, C, '((b + c)*(b + c - a)*(b*c - a**(2)))', ID="X_3985", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_312 = eval_trilinear_point(model, A, B, C, '(b + c - a)*b**(2)*c**(2)', ID="X_312", classes=["center", "incident"])
    central_line(model, X_9, X_312, 9, 312, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_714 = eval_trilinear_point(model, A, B, C, '(a **(-4)*(b **(-1) + c **(-1)) - a **(-2)*(b **(-3) + c **(-3)))', ID="X_714", classes=["center", "incident"])
    central_line(model, X_37, X_714, 37, 714, incident=True)
    X_522 = eval_trilinear_point(model, A, B, C, '(cos(B) - cos(C))*(csc(A))', ID="X_522", classes=["center", "incident"])
    X_650 = eval_trilinear_point(model, A, B, C, 'cos(B) - cos(C)', ID="X_650", classes=["center", "incident"])
    central_line(model, X_522, X_650, 522, 650, incident=True)
    return promote_point_to_top(model, X_3985)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3985 on the given reference triangle."""
    model = create_model('X_3985 = X_3290com[INVERSE(n(INCENTRAL TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03985(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03985.json"))
    write_center_svg(
        model_acute,
        here / "x-03985.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
