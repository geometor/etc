"""GEOMETOR construction model for X_2615 = MIDPOINT OF PU(71)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02615(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2615 = MIDPOINT OF PU(71) on reference triangle ABC."""
    X_2615 = eval_trilinear_point(model, A, B, C, '((a*csc(B - A) + b*csc(C - B) + c*csc(A - C))*csc(C - A) + (a*csc(C - A) + b*csc(A - B) + c*csc(B - C))*csc(B - A))', ID="X_2615", classes=["selected", "target"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center", "incident"])
    central_line(model, X_11, X_115, 11, 115, incident=True)
    X_2610 = point_from_barycentrics(model, A, B, C, -2.9137931, 0.99310345, 2.9206897, ID="X_2610", classes=["center", "incident"])
    X_2611 = point_from_barycentrics(model, A, B, C, 0.21464646, 0.68065268, 0.10470085, ID="X_2611", classes=["center", "incident"])
    central_line(model, X_2610, X_2611, 2610, 2611, incident=True)
    return promote_point_to_top(model, X_2615)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2615 on the given reference triangle."""
    model = create_model('X_2615 = MIDPOINT OF PU(71)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02615(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02615.json"))
    write_center_svg(
        model_acute,
        here / "x-02615.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
