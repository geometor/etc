"""GEOMETOR construction model for X_3047 = INTERSECTION X_54X_113∩X_2X_98."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_03047(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3047 = INTERSECTION X_54X_113∩X_2X_98 on reference triangle ABC."""
    X_3043 = eval_trilinear_point(model, A, B, C, '((1 - 4*(cos(A))**(2))**(2)*sec(A))', ID="X_3043", classes=["center"])
    X_49 = eval_trilinear_point(model, A, B, C, 'cos(3*A)', ID="X_49", classes=["center"])
    X_3047 = reflection_in_point(model, X_3043, X_49, ID="X_3047", classes=["selected", "target"], guide=False)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center", "incident"])
    central_line(model, X_2, X_98, 2, 98, incident=True)
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    X_113 = eval_trilinear_point(model, A, B, C, 'sin(B)*sin(C)*((sin(C))/(cos(C) - 2*cos(A)*cos(B)) + (sin(B))/(cos(B) - 2*cos(A)*cos(C)))', ID="X_113", classes=["center", "incident"])
    central_line(model, X_54, X_113, 54, 113, incident=True)
    X_156 = eval_barycentric_point(model, A, B, C, 'a**(2)*(a**(8) - 3*a**(6)*(b**(2) + c**(2)) + a**(4)*(3*b**(4) + 2*b**(2)*c**(2) + 3*c**(4)) - a**(2)*(b**(6) + c**(6)) + b**(2)*c**(2)*(b**(2) - c**(2))**(2))', ID="X_156", classes=["center", "incident"])
    X_265 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*csc(3*A)', ID="X_265", classes=["center", "incident"])
    central_line(model, X_156, X_265, 156, 265, incident=True)
    return promote_point_to_top(model, X_3047)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3047 on the given reference triangle."""
    model = create_model('X_3047 = INTERSECTION X_54X_113∩X_2X_98')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03047(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03047.json"))
    write_center_svg(
        model_acute,
        here / "x-03047.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
