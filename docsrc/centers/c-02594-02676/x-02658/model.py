"""GEOMETOR construction model for X_2658 = SUM OF PU(83)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02658(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2658 = SUM OF PU(83) on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_2654 = eval_trilinear_point(model, A, B, C, '2*sec(A) + sec(B) + sec(C)', ID="X_2654", classes=["center"])
    X_2658 = ceva_conjugate(model, A, B, C, X_1, X_2654, ID="X_2658", classes=["selected", "target"])
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X_29", classes=["center", "incident"])
    central_line(model, X_1, X_29, 1, 29, incident=True)
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    central_line(model, X_42, X_65, 42, 65, incident=True)
    X_1108 = point_from_barycentrics(model, A, B, C, 0.16604303, 0.31992516, 0.51403181, ID="X_1108", classes=["center", "incident"])
    X_1201 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) + c**(2) - 2*b*c + a*b + a*c))', ID="X_1201", classes=["center", "incident"])
    central_line(model, X_1108, X_1201, 1108, 1201, incident=True)
    return promote_point_to_top(model, X_2658)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2658 on the given reference triangle."""
    model = create_model('X_2658 = SUM OF PU(83)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02658(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02658.json"))
    write_center_svg(
        model_acute,
        here / "x-02658.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
