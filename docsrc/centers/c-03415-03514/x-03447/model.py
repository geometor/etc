"""GEOMETOR construction model for X_3447 = X_523-VERTEX CONJUGATE OF X_523."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03447(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3447 = X_523-VERTEX CONJUGATE OF X_523 on reference triangle ABC."""
    X_50 = eval_trilinear_point(model, A, B, C, 'sin(3*A)', ID="X_50", classes=["center"])
    X_232 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(A +  omega  )', ID="X_232", classes=["center"])
    X_23 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X_23", classes=["center"])
    X_325 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)', ID="X_325", classes=["center"])
    central_line(model, X_50, X_232, 50, 232)
    central_line(model, X_23, X_325, 23, 325)
    X_3447 = intersect_lines(model, X_50, X_232, X_23, X_325, ID="X_3447", classes=["selected", "target"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    X_2070 = eval_trilinear_point(model, A, B, C, '(J**(2) - 2)*cos(A) + 4*cos(B)*cos(C)', ID="X_2070", classes=["center", "incident"])
    central_line(model, X_511, X_2070, 511, 2070, incident=True)
    return promote_point_to_top(model, X_3447)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3447 on the given reference triangle."""
    model = create_model('X_3447 = X_523-VERTEX CONJUGATE OF X_523')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03447(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03447.json"))
    write_center_svg(
        model_acute,
        here / "x-03447.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
