"""GEOMETOR construction model for X_2648 = TRILINEAR POLE OF PU(80)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02648(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2648 = TRILINEAR POLE OF PU(80) on reference triangle ABC."""
    X_1758 = eval_trilinear_point(model, A, B, C, '(a**(3) + b**(3) + c**(3) - 2*a**(2)*b - 2*a**(2)*c + a*b*c)/(b + c - a)', ID="X_1758", classes=["center"])
    X_2648 = isogonal_conjugate(model, A, B, C, X_1758, ID="X_2648", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_1046 = point_from_barycentrics(model, A, B, C, 0.13236391, 0.3064877, 0.5611484, ID="X_1046", classes=["center", "incident"])
    central_line(model, X_4, X_1046, 4, 1046, incident=True)
    X_80 = eval_trilinear_point(model, A, B, C, '1/(1 - 2*cos(A))', ID="X_80", classes=["center", "incident"])
    X_1757 = eval_trilinear_point(model, A, B, C, '((b + c)**(2) - (a + b)*(a + c))', ID="X_1757", classes=["center", "incident"])
    central_line(model, X_80, X_1757, 80, 1757, incident=True)
    X_896 = eval_trilinear_point(model, A, B, C, '2*a**(2) - b**(2) - c**(2)', ID="X_896", classes=["center", "incident"])
    X_1156 = eval_trilinear_point(model, A, B, C, '(1/((b - c)**(2) + a*(b + c - 2*a)))', ID="X_1156", classes=["center", "incident"])
    central_line(model, X_896, X_1156, 896, 1156, incident=True)
    return promote_point_to_top(model, X_2648)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2648 on the given reference triangle."""
    model = create_model('X_2648 = TRILINEAR POLE OF PU(80)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02648(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02648.json"))
    write_center_svg(
        model_acute,
        here / "x-02648.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
