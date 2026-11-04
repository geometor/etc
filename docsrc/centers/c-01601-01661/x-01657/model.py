"""GEOMETOR construction model for X_1657 = {X_3,X_4}-HARMONIC CONJUGATE OF X_1656."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01657(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1657 = {X_3,X_4}-HARMONIC CONJUGATE OF X_1656 on reference triangle ABC."""
    X_1657 = eval_trilinear_point(model, A, B, C, '3*cos(A) - 4*cos(B)*cos(C)', ID="X_1657", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_195 = eval_trilinear_point(model, A, B, C, 'a*(a**(8) + b**(8) + c**(8) - 4*a**(6)*(b**(2) + c**(2)) + a**(4)*(6*b**(4) + 6*c**(4) + 5*b**(2)*c**(2)) - a**(2)*(4*b**(6) + 4*c**(6) - b**(4)*c**(2) - b**(2)*c**(4)) - 2*b**(2)*c**(2)*(b**(4) + c**(4) - b**(2)*c**(2)))', ID="X_195", classes=["center", "incident"])
    X_1181 = eval_trilinear_point(model, A, B, C, '((1 - cos(A)*sin(B)*sin(C))*cos(A))', ID="X_1181", classes=["center", "incident"])
    central_line(model, X_195, X_1181, 195, 1181, incident=True)
    X_399 = eval_trilinear_point(model, A, B, C, '5*cos(A) - 4*cos(B)*cos(C) - 8*sin(B)*sin(C)*(cos(A))**(2)', ID="X_399", classes=["center", "incident"])
    X_1498 = eval_trilinear_point(model, A, B, C, '(sin(A))*((tan(B))**(2) + (tan(C))**(2) - (tan(A))**(2))', ID="X_1498", classes=["center", "incident"])
    central_line(model, X_399, X_1498, 399, 1498, incident=True)
    return promote_point_to_top(model, X_1657)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1657 on the given reference triangle."""
    model = create_model('X_1657 = {X_3,X_4}-HARMONIC CONJUGATE OF X_1656')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01657(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01657.json"))
    write_center_svg(
        model_acute,
        here / "x-01657.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
