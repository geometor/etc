"""GEOMETOR construction model for X_2840 = ISOGONAL CONJUGATE OF X_2756."""

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


def construct_x_02840(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2840 = ISOGONAL CONJUGATE OF X_2756 on reference triangle ABC."""
    X_2756 = point_from_barycentrics(model, A, B, C, 0.87719275, -7.0090178e-08, 0.12280732, ID="X_2756", classes=["center"])
    X_2840 = isogonal_conjugate(model, A, B, C, X_2756, ID="X_2840", classes=["selected", "target"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center", "incident"])
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X_106", classes=["center", "incident"])
    central_line(model, X_34, X_106, 34, 106, incident=True)
    X_121 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c - 2*a)*(b**(3) + c**(3) + a*(b**(2) + c**(2)) - 2*b*c*(b + c)))', ID="X_121", classes=["center", "incident"])
    X_123 = eval_trilinear_point(model, A, B, C, '(csc(A))*(sec(B) - sec(C))*((sec(A))*((sin(B))**(2) - (sin(C))**(2)) + sin(C)*tan(C) - sin(B)*tan(B))', ID="X_123", classes=["center", "incident"])
    central_line(model, X_121, X_123, 121, 123, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    return promote_point_to_top(model, X_2840)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2840 on the given reference triangle."""
    model = create_model('X_2840 = ISOGONAL CONJUGATE OF X_2756')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02840(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02840.json"))
    write_center_svg(
        model_acute,
        here / "x-02840.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
