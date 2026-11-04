"""GEOMETOR construction model for X_2609 = MIDPOINT OF PU(70)."""

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


def construct_x_02609(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2609 = MIDPOINT OF PU(70) on reference triangle ABC."""
    X_2609 = eval_trilinear_point(model, A, B, C, '((a*sin(B - A) + b*sin(C - B) + c*sin(A - C))*sin(C - A) + (a*sin(C - A) + b*sin(A - B) + c*sin(B - C))*sin(B - A))', ID="X_2609", classes=["selected", "target"])
    X_2245 = eval_trilinear_point(model, A, B, C, '(sin(A) + sin(B) + sin(C))*cos(A) - (cos(A) + cos(B) + cos(C))*sin(A)', ID="X_2245", classes=["center", "incident"])
    X_2605 = eval_trilinear_point(model, A, B, C, '(sin(C- A) - sin(B - A))', ID="X_2605", classes=["center", "incident"])
    central_line(model, X_2245, X_2605, 2245, 2605, incident=True)
    return promote_point_to_top(model, X_2609)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2609 on the given reference triangle."""
    model = create_model('X_2609 = MIDPOINT OF PU(70)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02609(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02609.json"))
    write_center_svg(
        model_acute,
        here / "x-02609.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
