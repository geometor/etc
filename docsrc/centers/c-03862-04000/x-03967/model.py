"""GEOMETOR construction model for X_3967 = X_3752com[INVERSE(n(INCENTRAL TRIANGLE))]."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03967(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3967 = X_3752com[INVERSE(n(INCENTRAL TRIANGLE))] on reference triangle ABC."""
    X_3967 = eval_barycentric_point(model, A, B, C, '((b + c)*(a**(2) - a*b - a*c + 2*b*c))', ID="X_3967", classes=["selected", "target"])
    X_210 = eval_trilinear_point(model, A, B, C, '(b + c)*(b + c - a)', ID="X_210", classes=["center", "incident"])
    X_321 = eval_trilinear_point(model, A, B, C, '(b + c)*b**(2)*c**(2)', ID="X_321", classes=["center", "incident"])
    central_line(model, X_210, X_321, 210, 321, incident=True)
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center", "incident"])
    X_536 = eval_barycentric_point(model, A, B, C, '2*b*c - c*a - a*b', ID="X_536", classes=["center", "incident"])
    central_line(model, X_43, X_536, 43, 536, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_714 = eval_trilinear_point(model, A, B, C, '(a **(-4)*(b **(-1) + c **(-1)) - a **(-2)*(b **(-3) + c **(-3)))', ID="X_714", classes=["center", "incident"])
    central_line(model, X_37, X_714, 37, 714, incident=True)
    return promote_point_to_top(model, X_3967)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3967 on the given reference triangle."""
    model = create_model('X_3967 = X_3752com[INVERSE(n(INCENTRAL TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03967(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03967.json"))
    write_center_svg(
        model_acute,
        here / "x-03967.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
