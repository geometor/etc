"""GEOMETOR construction model for X_1283 = 7th SHARYGIN POINT."""

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
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01283(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1283 = 7th SHARYGIN POINT on reference triangle ABC."""
    X_1283 = eval_trilinear_point(model, A, B, C, '(a*(a**(4) - (b + c)*a**(3) + (b**(3) + c**(3))*a + b**(2)*c**(2) - b**(4) - c**(4)))', ID="X_1283", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    central_line(model, X_10, X_21, 10, 21, incident=True)
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_244 = eval_trilinear_point(model, A, B, C, '(b - c)**(2)', ID="X_244", classes=["center", "incident"])
    central_line(model, X_36, X_244, 36, 244, incident=True)
    X_242 = eval_trilinear_point(model, A, B, C, '((sec(A))*((sin(A))**(2) - sin(B)*sin(C)))', ID="X_242", classes=["center", "incident"])
    X_243 = eval_trilinear_point(model, A, B, C, '(sec(A))*((cos(A))**(2) - cos(B)*cos(C))', ID="X_243", classes=["center", "incident"])
    central_line(model, X_242, X_243, 242, 243, incident=True)
    return promote_point_to_top(model, X_1283)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1283 on the given reference triangle."""
    model = create_model('X_1283 = 7th SHARYGIN POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01283(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01283.json"))
    write_center_svg(
        model_acute,
        here / "x-01283.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
