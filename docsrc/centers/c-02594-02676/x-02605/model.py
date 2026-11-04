"""GEOMETOR construction model for X_2605 = DIFFERENCE OF PU(71)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    midpoint,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02605(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2605 = DIFFERENCE OF PU(71) on reference triangle ABC."""
    X_663 = eval_trilinear_point(model, A, B, C, 'a*(b - c)*(b + c - a)', ID="X_663", classes=["center"])
    X_1459 = eval_trilinear_point(model, A, B, C, '(b - c)*cos(A)', ID="X_1459", classes=["center"])
    X_2605 = midpoint(model, X_663, X_1459, ID="X_2605", classes=["selected", "target"], guide=False)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center", "incident"])
    central_line(model, X_1, X_523, 1, 523, incident=True)
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    central_line(model, X_513, X_663, 513, 663, incident=True)
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    X_1101 = eval_trilinear_point(model, A, B, C, '((csc(B - C))**(2))', ID="X_1101", classes=["center", "incident"])
    central_line(model, X_110, X_1101, 110, 1101, incident=True)
    return promote_point_to_top(model, X_2605)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2605 on the given reference triangle."""
    model = create_model('X_2605 = DIFFERENCE OF PU(71)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02605(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02605.json"))
    write_center_svg(
        model_acute,
        here / "x-02605.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
