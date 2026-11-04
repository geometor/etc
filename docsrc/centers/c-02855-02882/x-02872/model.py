"""GEOMETOR construction model for X_2872 = ISOGONAL CONJUGATE OF X_2858."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02872(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2872 = ISOGONAL CONJUGATE OF X_2858 on reference triangle ABC."""
    X_2858 = eval_trilinear_point(model, A, B, C, '(b*c/((b**(2) - c**(2))*(a**(4) + b**(4) + c**(4) - 3*b**(2)*c**(2))))', ID="X_2858", classes=["center"])
    X_2872 = isogonal_conjugate(model, A, B, C, X_2858, ID="X_2872", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    X_1976 = eval_trilinear_point(model, A, B, C, '(a**(2)/(a**(2)*cos(B)*cos(C) - b*c*(cos(A))**(2)))', ID="X_1976", classes=["center", "incident"])
    X_2422 = eval_barycentric_point(model, A, B, C, 'a**(2)*(b**(2) - c**(2))/(b**(4) + c**(4) - a**(2)*b**(2) - a**(2)*c**(2))', ID="X_2422", classes=["center", "incident"])
    central_line(model, X_1976, X_2422, 1976, 2422, incident=True)
    return promote_point_to_top(model, X_2872)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2872 on the given reference triangle."""
    model = create_model('X_2872 = ISOGONAL CONJUGATE OF X_2858')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02872(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02872.json"))
    write_center_svg(
        model_acute,
        here / "x-02872.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
