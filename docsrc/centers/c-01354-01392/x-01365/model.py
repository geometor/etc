"""GEOMETOR construction model for X_1365 = BRISSE TRANSFORM OF X_110."""

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


def construct_x_01365(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1365 = BRISSE TRANSFORM OF X_110 on reference triangle ABC."""
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center"])
    X_759 = eval_trilinear_point(model, A, B, C, '(1/(a**(0)*(b**(3) + c**(3)) - a**(2)*(b**(1) + c**(1))))', ID="X_759", classes=["center"])
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X_125", classes=["center"])
    X_1109 = eval_trilinear_point(model, A, B, C, '(sin(B - C))**(2)', ID="X_1109", classes=["center"])
    central_line(model, X_56, X_759, 56, 759)
    central_line(model, X_125, X_1109, 125, 1109)
    X_1365 = intersect_lines(model, X_56, X_759, X_125, X_1109, ID="X_1365", classes=["selected", "target"])
    X_1086 = eval_trilinear_point(model, A, B, C, '(b*c*(b - c)**(2))', ID="X_1086", classes=["center", "incident"])
    X_1357 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)*(b - c)**(2)*(a**(2) - (b - c)**(2))**(2)', ID="X_1357", classes=["center", "incident"])
    central_line(model, X_1086, X_1357, 1086, 1357, incident=True)
    return promote_point_to_top(model, X_1365)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1365 on the given reference triangle."""
    model = create_model('X_1365 = BRISSE TRANSFORM OF X_110')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01365(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01365.json"))
    write_center_svg(
        model_acute,
        here / "x-01365.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
