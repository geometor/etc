"""GEOMETOR construction model for X_3667 = X_513com(INTOUCH TRIANGLE)."""

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
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03667(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3667 = X_513com(INTOUCH TRIANGLE) on reference triangle ABC."""
    X_1293 = eval_trilinear_point(model, A, B, C, '(a/((b - c)*(3*a - b - c)))', ID="X_1293", classes=["center"])
    X_3667 = isogonal_conjugate(model, A, B, C, X_1293, ID="X_3667", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_2457 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(2) - c**(2))*(2*a**(3) + a**(2)*(b + c) - (b + c)*(b - c)**(2) - 2*a*(b**(2) - b*c + c**(2))))', ID="X_2457", classes=["center", "incident"])
    central_line(model, X_4, X_2457, 4, 2457, incident=True)
    X_572 = eval_trilinear_point(model, A, B, C, '(cos(A - U))', ID="X_572", classes=["center", "incident"])
    X_1919 = eval_trilinear_point(model, A, B, C, '(a**(3)*(b - c))', ID="X_1919", classes=["center", "incident"])
    central_line(model, X_572, X_1919, 572, 1919, incident=True)
    return promote_point_to_top(model, X_3667)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3667 on the given reference triangle."""
    model = create_model('X_3667 = X_513com(INTOUCH TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03667(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03667.json"))
    write_center_svg(
        model_acute,
        here / "x-03667.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
