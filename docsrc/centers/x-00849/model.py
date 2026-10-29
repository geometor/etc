"""GEOMETOR construction model for X(849) = 4th HATZIPOLAKIS-YIU POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00849(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(849) = 4th HATZIPOLAKIS-YIU POINT on reference triangle ABC."""
    X_249 = eval_trilinear_point(model, A, B, C, '(csc(A))*(csc(B - C))**(2)', ID="X(249)", classes=["center"])
    X_163 = eval_trilinear_point(model, A, B, C, '(sin(2*A))/(sin(2*B) - sin(2*C))', ID="X(163)", classes=["center"])
    X_849 = ceva_conjugate(model, A, B, C, X_249, X_163, ID="X(849)", classes=["selected", "target"])
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X(36)", classes=["center", "incident"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X(58)", classes=["center", "incident"])
    central_line(model, X_36, X_58, 36, 58, incident=True)
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X(32)", classes=["center", "incident"])
    central_line(model, X_32, X_163, 32, 163, incident=True)
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    X_595 = eval_trilinear_point(model, A, B, C, 'r + R*(cos(2*A) - 1)', ID="X(595)", classes=["center", "incident"])
    central_line(model, X_110, X_595, 110, 595, incident=True)
    return promote_point_to_top(model, X_849)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(849) on the given reference triangle."""
    model = create_model('X(849) = 4th HATZIPOLAKIS-YIU POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00849(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00849.json"))
    write_center_svg(
        model_acute,
        here / "x-00849.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
