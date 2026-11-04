"""GEOMETOR construction model for X_2597 = TRILINEAR POLE OF PU(68)."""

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


def construct_x_02597(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2597 = TRILINEAR POLE OF PU(68) on reference triangle ABC."""
    X_2596 = eval_trilinear_point(model, A, B, C, 'cos(A - B)*cos(A - C) - (cos(B - C))**(2)', ID="X_2596", classes=["center"])
    X_2597 = isogonal_conjugate(model, A, B, C, X_2596, ID="X_2597", classes=["selected", "target"])
    X_655 = eval_trilinear_point(model, A, B, C, '1/(cos(A - B) - cos(C- A))', ID="X_655", classes=["center", "incident"])
    X_2595 = eval_trilinear_point(model, A, B, C, '(cos(A - B)*cos(A - C) + (cos(B - C))**(2))', ID="X_2595", classes=["center", "incident"])
    central_line(model, X_655, X_2595, 655, 2595, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2603 = eval_trilinear_point(model, A, B, C, '(1/(sec(A - B)*sec(A - C) - (sec(B - C))**(2)))', ID="X_2603", classes=["center", "incident"])
    central_line(model, X_1, X_2603, 1, 2603, incident=True)
    return promote_point_to_top(model, X_2597)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2597 on the given reference triangle."""
    model = create_model('X_2597 = TRILINEAR POLE OF PU(68)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02597(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02597.json"))
    write_center_svg(
        model_acute,
        here / "x-02597.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
