"""GEOMETOR construction model for X_2842 = ISOGONAL CONJUGATE OF X_2758."""

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


def construct_x_02842(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2842 = ISOGONAL CONJUGATE OF X_2758 on reference triangle ABC."""
    X_2758 = point_from_barycentrics(model, A, B, C, 0.70824463, -0.30752942, 0.59928479, ID="X_2758", classes=["center"])
    X_2842 = isogonal_conjugate(model, A, B, C, X_2758, ID="X_2842", classes=["selected", "target"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X_106", classes=["center", "incident"])
    central_line(model, X_58, X_106, 58, 106, incident=True)
    X_121 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c - 2*a)*(b**(3) + c**(3) + a*(b**(2) + c**(2)) - 2*b*c*(b + c)))', ID="X_121", classes=["center", "incident"])
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X_125", classes=["center", "incident"])
    central_line(model, X_121, X_125, 121, 125, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    return promote_point_to_top(model, X_2842)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2842 on the given reference triangle."""
    model = create_model('X_2842 = ISOGONAL CONJUGATE OF X_2758')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02842(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02842.json"))
    write_center_svg(
        model_acute,
        here / "x-02842.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
