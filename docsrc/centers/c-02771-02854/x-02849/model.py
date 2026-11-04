"""GEOMETOR construction model for X_2849 = ISOGONAL CONJUGATE OF X_2765."""

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


def construct_x_02849(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2849 = ISOGONAL CONJUGATE OF X_2765 on reference triangle ABC."""
    X_2765 = point_from_barycentrics(model, A, B, C, -0.078369906, 0.13479624, 0.94357367, ID="X_2765", classes=["center"])
    X_2849 = isogonal_conjugate(model, A, B, C, X_2765, ID="X_2849", classes=["selected", "target"])
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center", "incident"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    central_line(model, X_108, X_109, 108, 109, incident=True)
    X_123 = eval_trilinear_point(model, A, B, C, '(csc(A))*(sec(B) - sec(C))*((sec(A))*((sin(B))**(2) - (sin(C))**(2)) + sin(C)*tan(C) - sin(B)*tan(B))', ID="X_123", classes=["center", "incident"])
    X_124 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c - a)*(b - c)**(2)*((b + c)*(b**(2) + c**(2) - a**(2) - b*c) + a*b*c))', ID="X_124", classes=["center", "incident"])
    central_line(model, X_123, X_124, 123, 124, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    return promote_point_to_top(model, X_2849)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2849 on the given reference triangle."""
    model = create_model('X_2849 = ISOGONAL CONJUGATE OF X_2765')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02849(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02849.json"))
    write_center_svg(
        model_acute,
        here / "x-02849.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
