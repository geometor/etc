"""GEOMETOR construction model for X_2653 = MIDPOINT OF PU(81)."""

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


def construct_x_02653(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2653 = MIDPOINT OF PU(81) on reference triangle ABC."""
    X_2653 = eval_trilinear_point(model, A, B, C, '((a/(cos(B) + cos(A)) + b/(cos(C) + cos(B)) + c/(cos(A) + cos(C)))/(cos(C) + cos(A)) + (a/(cos(C) + cos(A)) + b/(cos(A) + cos(B)) + c/(cos(B) + cos(C)))/(cos(B) + cos(A)))', ID="X_2653", classes=["selected", "target"])
    X_661 = eval_trilinear_point(model, A, B, C, 'cot(B) - cot(C)', ID="X_661", classes=["center", "incident"])
    X_2650 = eval_trilinear_point(model, A, B, C, '1/(cos(A) + cos(B)) + 1/(cos(A) + cos(C))', ID="X_2650", classes=["center", "incident"])
    central_line(model, X_661, X_2650, 661, 2650, incident=True)
    X_2092 = eval_trilinear_point(model, A, B, C, '(a**(2)*(b + c)**(2) + a*(b + c)*(b**(2) + c**(2)))', ID="X_2092", classes=["center", "incident"])
    X_2183 = eval_trilinear_point(model, A, B, C, '(a - c)*cos(B) + (a - b)*cos(C)', ID="X_2183", classes=["center", "incident"])
    central_line(model, X_2092, X_2183, 2092, 2183, incident=True)
    return promote_point_to_top(model, X_2653)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2653 on the given reference triangle."""
    model = create_model('X_2653 = MIDPOINT OF PU(81)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02653(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02653.json"))
    write_center_svg(
        model_acute,
        here / "x-02653.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
