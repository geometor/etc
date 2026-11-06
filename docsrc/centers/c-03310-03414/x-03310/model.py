"""GEOMETOR construction model for X_3310 = BARYCENTRIC PRODUCT X_513*X_517."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03310(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3310 = BARYCENTRIC PRODUCT X_513*X_517 on reference triangle ABC."""
    X_3310 = eval_trilinear_point(model, A, B, C, '(a*(b - c)*( -1 + cos(B) + cos(C)))', ID="X_3310", classes=["selected", "target"])
    X_230 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*(2*a**(2) - b**(2) - c**(2)) + (b**(2) - c**(2))**(2))', ID="X_230", classes=["center", "incident"])
    X_231 = eval_trilinear_point(model, A, B, C, '(cos(B))*(4*(sin(C))**(2) - 1)*(cos(A)*sin(B) - sin(A)*cos(B)) - (cos(C))*(4*(sin(B))**(2) - 1)*(cos(C)*sin(A) - sin(C)*cos(A))', ID="X_231", classes=["center", "incident"])
    central_line(model, X_230, X_231, 230, 231, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_654 = eval_trilinear_point(model, A, B, C, 'cos(A - B) - cos(C - A)', ID="X_654", classes=["center", "incident"])
    central_line(model, X_6, X_654, 6, 654, incident=True)
    X_244 = eval_trilinear_point(model, A, B, C, '(b - c)**(2)', ID="X_244", classes=["center", "incident"])
    X_665 = eval_trilinear_point(model, A, B, C, 'a*((a - b)**(2)*(a + b - c) - (c - a)**(2)*(c + a - b))', ID="X_665", classes=["center", "incident"])
    central_line(model, X_244, X_665, 244, 665, incident=True)
    return promote_point_to_top(model, X_3310)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3310 on the given reference triangle."""
    model = create_model('X_3310 = BARYCENTRIC PRODUCT X_513*X_517')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03310(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03310.json"))
    write_center_svg(
        model_acute,
        here / "x-03310.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
