"""GEOMETOR construction model for X(812) = ODD (- 1, 1) INFINITY POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00812(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(812) = ODD (- 1, 1) INFINITY POINT on reference triangle ABC."""
    X_812 = eval_trilinear_point(model, A, B, C, 'a **(-2)*(b**(1) - c**(1)) + a**(0)*(b **(-1) - c **(-1))', ID="X(812)", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X(511)", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X(190)", classes=["center", "incident"])
    X_646 = eval_trilinear_point(model, A, B, C, '(b + c - a)/(a**(2)*(b - c))', ID="X(646)", classes=["center", "incident"])
    central_line(model, X_190, X_646, 190, 646, incident=True)
    X_649 = eval_trilinear_point(model, A, B, C, 'a*(b - c)', ID="X(649)", classes=["center", "incident"])
    X_693 = eval_trilinear_point(model, A, B, C, '(b - c)/a**(2)', ID="X(693)", classes=["center", "incident"])
    central_line(model, X_649, X_693, 649, 693, incident=True)
    return promote_point_to_top(model, X_812)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(812) on the given reference triangle."""
    model = create_model('X(812) = ODD (- 1, 1) INFINITY POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00812(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00812.json"))
    write_center_svg(
        model_acute,
        here / "x-00812.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
