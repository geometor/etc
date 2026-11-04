"""GEOMETOR construction model for X_2645 = MIDPOINT OF PU(79)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02645(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2645 = MIDPOINT OF PU(79) on reference triangle ABC."""
    X_2645 = eval_trilinear_point(model, A, B, C, '((a/(cot(B) - cot(A)) + b/(cot(C) - cot(B)) + c/(cot(A) - cot(C)))/(cot(C) - cot(A)) + (a/(cot(C) - cot(A)) + b/(cot(A) - cot(B)) + c/(cot(B) - cot(C)))/(cot(B) - cot(A)))', ID="X_2645", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_2640 = eval_trilinear_point(model, A, B, C, '(cot(A) - cot(B))*(cot(A) - cot(C)) - (cot(B) - cot(C))**(2)', ID="X_2640", classes=["center", "incident"])
    central_line(model, X_9, X_2640, 9, 2640, incident=True)
    X_2642 = eval_trilinear_point(model, A, B, C, '1/(cot(C) - cot(A)) + 1/(cot(B) - cot(A))', ID="X_2642", classes=["center", "incident"])
    X_2643 = eval_trilinear_point(model, A, B, C, '1/(cot(C) - cot(A)) - 1/(cot(B) - cot(A))', ID="X_2643", classes=["center", "incident"])
    central_line(model, X_2642, X_2643, 2642, 2643, incident=True)
    return promote_point_to_top(model, X_2645)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2645 on the given reference triangle."""
    model = create_model('X_2645 = MIDPOINT OF PU(79)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02645(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02645.json"))
    write_center_svg(
        model_acute,
        here / "x-02645.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
