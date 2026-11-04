"""GEOMETOR construction model for X_2670 = MIDPOINT OF PU(85)."""

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


def construct_x_02670(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2670 = MIDPOINT OF PU(85) on reference triangle ABC."""
    X_2670 = eval_trilinear_point(model, A, B, C, '((b*a**(2)/(b + a) + c*b**(2)/(c + b) + a*c**(2)/(a + c))*c*a/(c + a) + (c*a**(2)/(c + a) + a*b**(2)/(a + b) + b*c**(2)/(b + c))*b*a/(b + a))', ID="X_2670", classes=["selected", "target"])
    X_1084 = eval_trilinear_point(model, A, B, C, 'a**(3)*(b**(2) - c**(2))**(2)', ID="X_1084", classes=["center", "incident"])
    X_1100 = eval_trilinear_point(model, A, B, C, '2*a + b + c', ID="X_1100", classes=["center", "incident"])
    central_line(model, X_1084, X_1100, 1084, 1100, incident=True)
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    X_2653 = eval_trilinear_point(model, A, B, C, '((a/(cos(B) + cos(A)) + b/(cos(C) + cos(B)) + c/(cos(A) + cos(C)))/(cos(C) + cos(A)) + (a/(cos(C) + cos(A)) + b/(cos(A) + cos(B)) + c/(cos(B) + cos(C)))/(cos(B) + cos(A)))', ID="X_2653", classes=["center", "incident"])
    central_line(model, X_511, X_2653, 511, 2653, incident=True)
    X_798 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b**(2) - c**(2))', ID="X_798", classes=["center", "incident"])
    X_2667 = eval_trilinear_point(model, A, B, C, 'c*a/(c + a) + b*a/(b + a)', ID="X_2667", classes=["center", "incident"])
    central_line(model, X_798, X_2667, 798, 2667, incident=True)
    return promote_point_to_top(model, X_2670)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2670 on the given reference triangle."""
    model = create_model('X_2670 = MIDPOINT OF PU(85)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02670(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02670.json"))
    write_center_svg(
        model_acute,
        here / "x-02670.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
