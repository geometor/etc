"""GEOMETOR construction model for X_3652 = KS(CARNOT TRIANGLE)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03652(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3652 = KS(CARNOT TRIANGLE) on reference triangle ABC."""
    X_3652 = eval_trilinear_point(model, A, B, C, '(a**(6) + a**(4)*(b*c - 3*b**(2) - 3*c**(2)) + a**(3)*b*c*(b + c) + 3*a**(2)*(b**(4) + c**(4)) - a*b*c*(b + c)*(b - c)**(2) - (b**(2) - c**(2))**(2)*(b**(2) + b*c + c**(2)))', ID="X_3652", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    central_line(model, X_30, X_40, 30, 40, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_79 = eval_trilinear_point(model, A, B, C, '1/(1 + 2*cos(A))', ID="X_79", classes=["center", "incident"])
    central_line(model, X_5, X_79, 5, 79, incident=True)
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center", "incident"])
    central_line(model, X_21, X_104, 21, 104, incident=True)
    return promote_point_to_top(model, X_3652)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3652 on the given reference triangle."""
    model = create_model('X_3652 = KS(CARNOT TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03652(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03652.json"))
    write_center_svg(
        model_acute,
        here / "x-03652.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
