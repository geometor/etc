"""GEOMETOR construction model for X_3270 = X_1-CEVA CONJUGATE OF X_647."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03270(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3270 = X_1-CEVA CONJUGATE OF X_647 on reference triangle ABC."""
    X_3270 = eval_trilinear_point(model, A, B, C, '(a*(b - c)**(2)*(b + c - a)**(2)*(b**(2) + c**(2) - a**(2)))', ID="X_3270", classes=["selected", "target"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center", "incident"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X_51", classes=["center", "incident"])
    central_line(model, X_33, X_51, 33, 51, incident=True)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X_125", classes=["center", "incident"])
    central_line(model, X_11, X_125, 11, 125, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_185 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 - cos(A)*cos(B - C))', ID="X_185", classes=["center", "incident"])
    central_line(model, X_1, X_185, 1, 185, incident=True)
    return promote_point_to_top(model, X_3270)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3270 on the given reference triangle."""
    model = create_model('X_3270 = X_1-CEVA CONJUGATE OF X_647')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03270(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03270.json"))
    write_center_svg(
        model_acute,
        here / "x-03270.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
