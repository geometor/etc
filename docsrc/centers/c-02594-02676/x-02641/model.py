"""GEOMETOR construction model for X_2641 = MIDPOINT OF PU(78)."""

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


def construct_x_02641(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2641 = MIDPOINT OF PU(78) on reference triangle ABC."""
    X_2641 = eval_trilinear_point(model, A, B, C, '((a*(cot(B) - cot(A)) + b*(cot(C) - cot(B)) + c*(cot(A) - cot(C)))*(cot(C) - cot(A)) + (a*(cot(C) - cot(A)) + b*(cot(A) - cot(B)) + c*(cot(B) - cot(C)))*(cot(B) - cot(A)))', ID="X_2641", classes=["selected", "target"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    central_line(model, X_44, X_513, 44, 513, incident=True)
    X_1914 = eval_trilinear_point(model, A, B, C, '1 - a**(2)/(b*c)', ID="X_1914", classes=["center", "incident"])
    X_2651 = eval_trilinear_point(model, A, B, C, '(1/((cos(A) + cos(B))*(cos(A) + cos(C))) - 1/(cos(B) + cos(C))**(2))', ID="X_2651", classes=["center", "incident"])
    central_line(model, X_1914, X_2651, 1914, 2651, incident=True)
    X_1931 = eval_trilinear_point(model, A, B, C, '(((b + c)**(2) - (a + b)*(a + c))/(b + c))', ID="X_1931", classes=["center", "incident"])
    X_2642 = eval_trilinear_point(model, A, B, C, '1/(cot(C) - cot(A)) + 1/(cot(B) - cot(A))', ID="X_2642", classes=["center", "incident"])
    central_line(model, X_1931, X_2642, 1931, 2642, incident=True)
    return promote_point_to_top(model, X_2641)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2641 on the given reference triangle."""
    model = create_model('X_2641 = MIDPOINT OF PU(78)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02641(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02641.json"))
    write_center_svg(
        model_acute,
        here / "x-02641.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
