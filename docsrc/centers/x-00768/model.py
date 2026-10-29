"""GEOMETOR construction model for X(768) = ODD (- 4, - 3) INFINITY POINT."""

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


def construct_x_00768(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(768) = ODD (- 4, - 3) INFINITY POINT on reference triangle ABC."""
    X_768 = eval_trilinear_point(model, A, B, C, 'a**(-5)*(b**(-3)- c**(-3)) + a**(-4)*(b**(-4)- c**(-4))', ID="X(768)", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X(511)", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    return promote_point_to_top(model, X_768)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(768) on the given reference triangle."""
    model = create_model('X(768) = ODD (- 4, - 3) INFINITY POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00768(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00768.json"))
    write_center_svg(
        model_acute,
        here / "x-00768.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
