"""GEOMETOR construction model for X_2628 = MIDPOINT OF PU(73)."""

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


def construct_x_02628(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2628 = MIDPOINT OF PU(73) on reference triangle ABC."""
    X_2628 = eval_trilinear_point(model, A, B, C, '((a*cot(B - A) + b*cot(C - B) + c*cot(A - C))*cot(C - A) + (a*cot(C - A) + b*cot(A - B) + c*cot(B - C))*cot(B - A))', ID="X_2628", classes=["selected", "target"])
    X_1109 = eval_trilinear_point(model, A, B, C, '(sin(B - C))**(2)', ID="X_1109", classes=["center", "incident"])
    X_2624 = eval_trilinear_point(model, A, B, C, 'cot(A - B) + cot(A - C)', ID="X_2624", classes=["center", "incident"])
    central_line(model, X_1109, X_2624, 1109, 2624, incident=True)
    return promote_point_to_top(model, X_2628)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2628 on the given reference triangle."""
    model = create_model('X_2628 = MIDPOINT OF PU(73)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02628(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02628.json"))
    write_center_svg(
        model_acute,
        here / "x-02628.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
