"""GEOMETOR construction model for X_2603 = TRILINEAR POLE OF PU(69)."""

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
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02603(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2603 = TRILINEAR POLE OF PU(69) on reference triangle ABC."""
    X_2602 = eval_trilinear_point(model, A, B, C, 'sec(A - B)*sec(A - C) - (sec(B - C))**(2)', ID="X_2602", classes=["center"])
    X_2603 = isogonal_conjugate(model, A, B, C, X_2602, ID="X_2603", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2597 = eval_trilinear_point(model, A, B, C, '(1/(cos(A - B)*cos(A - C) - (cos(B - C))**(2)))', ID="X_2597", classes=["center", "incident"])
    central_line(model, X_1, X_2597, 1, 2597, incident=True)
    X_2594 = eval_trilinear_point(model, A, B, C, '(cos(C- A) + cos(B - A))', ID="X_2594", classes=["center", "incident"])
    X_2601 = eval_trilinear_point(model, A, B, C, 'sec(A - B)*sec(A - C) + (sec(B - C))**(2)', ID="X_2601", classes=["center", "incident"])
    central_line(model, X_2594, X_2601, 2594, 2601, incident=True)
    return promote_point_to_top(model, X_2603)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2603 on the given reference triangle."""
    model = create_model('X_2603 = TRILINEAR POLE OF PU(69)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02603(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02603.json"))
    write_center_svg(
        model_acute,
        here / "x-02603.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
