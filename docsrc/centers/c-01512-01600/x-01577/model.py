"""GEOMETOR construction model for X_1577 = ISOGONAL CONJUGATE OF X_163."""

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


def construct_x_01577(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1577 = ISOGONAL CONJUGATE OF X_163 on reference triangle ABC."""
    X_163 = eval_trilinear_point(model, A, B, C, '(sin(2*A))/(sin(2*B) - sin(2*C))', ID="X_163", classes=["center"])
    X_1577 = isogonal_conjugate(model, A, B, C, X_163, ID="X_1577", classes=["selected", "target"])
    X_240 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(A +  omega  )', ID="X_240", classes=["center", "incident"])
    X_522 = eval_trilinear_point(model, A, B, C, '(cos(B) - cos(C))*(csc(A))', ID="X_522", classes=["center", "incident"])
    central_line(model, X_240, X_522, 240, 522, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_810 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*((cos(B))**(2) - (cos(C))**(2))', ID="X_810", classes=["center", "incident"])
    central_line(model, X_1, X_810, 1, 810, incident=True)
    X_784 = eval_trilinear_point(model, A, B, C, '(a **(-4)*(b **(-2) - c **(-2)) + a **(-3)*(b **(-3) - c **(-3)))', ID="X_784", classes=["center", "incident"])
    X_149 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(3) + c**(3) - a**(3) + (a**(2) - b*c)*(b + c) + a*(b*c - b**(2) - c**(2))))', ID="X_149", classes=["center", "incident"])
    central_line(model, X_784, X_149, 784, 149, incident=True)
    return promote_point_to_top(model, X_1577)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1577 on the given reference triangle."""
    model = create_model('X_1577 = ISOGONAL CONJUGATE OF X_163')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01577(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01577.json"))
    write_center_svg(
        model_acute,
        here / "x-01577.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
