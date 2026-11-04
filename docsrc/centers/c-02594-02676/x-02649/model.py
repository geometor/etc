"""GEOMETOR construction model for X_2649 = MIDPOINT OF PU(80)."""

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


def construct_x_02649(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2649 = MIDPOINT OF PU(80) on reference triangle ABC."""
    X_2649 = eval_trilinear_point(model, A, B, C, '((a*(cos(B) + cos(A)) + b*(cos(C) + cos(B)) + c*(cos(A) + cos(C)))*(cos(C) + cos(A)) + (a*(cos(C) + cos(A)) + b*(cos(A) + cos(B)) + c*(cos(B) + cos(C)))*(cos(B) + cos(A)))', ID="X_2649", classes=["selected", "target"])
    X_650 = eval_trilinear_point(model, A, B, C, 'cos(B) - cos(C)', ID="X_650", classes=["center", "incident"])
    X_2646 = eval_trilinear_point(model, A, B, C, '2*cos(A) + cos(B) + cos(C)', ID="X_2646", classes=["center", "incident"])
    central_line(model, X_650, X_2646, 650, 2646, incident=True)
    return promote_point_to_top(model, X_2649)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2649 on the given reference triangle."""
    model = create_model('X_2649 = MIDPOINT OF PU(80)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02649(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02649.json"))
    write_center_svg(
        model_acute,
        here / "x-02649.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
