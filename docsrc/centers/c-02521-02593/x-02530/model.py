"""GEOMETOR construction model for X_2530 = RADICAL CENTER OF {BROCARD, BEVAN, (X_4,2R)} CIRCLES."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02530(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2530 = RADICAL CENTER OF {BROCARD, BEVAN, (X_4,2R)} CIRCLES on reference triangle ABC."""
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center"])
    X_693 = eval_trilinear_point(model, A, B, C, '(b - c)/a**(2)', ID="X_693", classes=["center"])
    X_2530 = crosspoint(model, A, B, C, X_513, X_693, ID="X_2530", classes=["selected", "target"])
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center", "incident"])
    central_line(model, X_36, X_238, 36, 238, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center", "incident"])
    central_line(model, X_10, X_514, 10, 514, incident=True)
    X_661 = eval_trilinear_point(model, A, B, C, 'cot(B) - cot(C)', ID="X_661", classes=["center", "incident"])
    X_665 = eval_trilinear_point(model, A, B, C, 'a*((a - b)**(2)*(a + b - c) - (c - a)**(2)*(c + a - b))', ID="X_665", classes=["center", "incident"])
    central_line(model, X_661, X_665, 661, 665, incident=True)
    return promote_point_to_top(model, X_2530)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2530 on the given reference triangle."""
    model = create_model('X_2530 = RADICAL CENTER OF {BROCARD, BEVAN, (X_4,2R)} CIRCLES')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02530(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02530.json"))
    write_center_svg(
        model_acute,
        here / "x-02530.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
