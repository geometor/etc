"""GEOMETOR construction model for X_2776 = ISOGONAL CONJUGATE OF X_2692."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02776(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2776 = ISOGONAL CONJUGATE OF X_2692 on reference triangle ABC."""
    X_2692 = point_from_barycentrics(model, A, B, C, 0.15981192, 1.0991935, -0.25900546, ID="X_2692", classes=["center"])
    X_2776 = isogonal_conjugate(model, A, B, C, X_2692, ID="X_2776", classes=["selected", "target"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center", "incident"])
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X_106", classes=["center", "incident"])
    central_line(model, X_74, X_106, 74, 106, incident=True)
    X_113 = eval_trilinear_point(model, A, B, C, 'sin(B)*sin(C)*((sin(C))/(cos(C) - 2*cos(A)*cos(B)) + (sin(B))/(cos(B) - 2*cos(A)*cos(C)))', ID="X_113", classes=["center", "incident"])
    X_121 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c - 2*a)*(b**(3) + c**(3) + a*(b**(2) + c**(2)) - 2*b*c*(b + c)))', ID="X_121", classes=["center", "incident"])
    central_line(model, X_113, X_121, 113, 121, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    return promote_point_to_top(model, X_2776)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2776 on the given reference triangle."""
    model = create_model('X_2776 = ISOGONAL CONJUGATE OF X_2692')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02776(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02776.json"))
    write_center_svg(
        model_acute,
        here / "x-02776.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
