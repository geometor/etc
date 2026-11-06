"""GEOMETOR construction model for X_3025 = 9th STEVANOVIC POINT."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03025(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3025 = 9th STEVANOVIC POINT on reference triangle ABC."""
    X_3025 = eval_trilinear_point(model, A, B, C, '(a*(b + c - a)*(b - c)**(2)*(b**(2) + c**(2) - a**(2) - b*c)**(2))', ID="X_3025", classes=["selected", "target"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    central_line(model, X_11, X_513, 11, 513, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_953 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(4) - 2*a**(3)*(b + c) - a**(2)*(b**(2) - 4*b*c + c**(2)) + (2*a - b - c)*(b - c)*(b**(2) - c**(2)))', ID="X_953", classes=["center", "incident"])
    central_line(model, X_56, X_953, 56, 953, incident=True)
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_1464 = eval_trilinear_point(model, A, B, C, '(1 - cos(A))*(b + c)*(b**(2) + c**(2) - a**(2) - b*c)', ID="X_1464", classes=["center", "incident"])
    central_line(model, X_36, X_1464, 36, 1464, incident=True)
    return promote_point_to_top(model, X_3025)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3025 on the given reference triangle."""
    model = create_model('X_3025 = 9th STEVANOVIC POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03025(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03025.json"))
    write_center_svg(
        model_acute,
        here / "x-03025.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
