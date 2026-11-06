"""GEOMETOR construction model for X_3892 = X_547com[INVERSE(n(3rd EULER TRIANGLE))]."""

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
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03892(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3892 = X_547com[INVERSE(n(3rd EULER TRIANGLE))] on reference triangle ABC."""
    X_3892 = eval_barycentric_point(model, A, B, C, '(a*(b**(3) + c**(3) - a**(2)*b - a**(2)*c - 6*a*b*c))', ID="X_3892", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    central_line(model, X_1, X_21, 1, 21, incident=True)
    X_354 = eval_trilinear_point(model, A, B, C, '(b - c)**(2) - a*b - a*c', ID="X_354", classes=["center", "incident"])
    X_519 = eval_trilinear_point(model, A, B, C, '(2*a - b - c)/a', ID="X_519", classes=["center", "incident"])
    central_line(model, X_354, X_519, 354, 519, incident=True)
    X_518 = eval_trilinear_point(model, A, B, C, '(a*b + a*c - b**(2) - c**(2))', ID="X_518", classes=["center", "incident"])
    X_551 = eval_trilinear_point(model, A, B, C, '(4*a + b + c)/a', ID="X_551", classes=["center", "incident"])
    central_line(model, X_518, X_551, 518, 551, incident=True)
    return promote_point_to_top(model, X_3892)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3892 on the given reference triangle."""
    model = create_model('X_3892 = X_547com[INVERSE(n(3rd EULER TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03892(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03892.json"))
    write_center_svg(
        model_acute,
        here / "x-03892.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
