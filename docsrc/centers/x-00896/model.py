"""GEOMETOR construction model for X(896) = INTERSECTION OF LINES X(1)X(21) AND X(9)X(750)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00896(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(896) = INTERSECTION OF LINES X(1)X(21) AND X(9)X(750) on reference triangle ABC."""
    X_896 = eval_trilinear_point(model, A, B, C, '2*a**(2) - b**(2) - c**(2)', ID="X(896)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X(21)", classes=["center", "incident"])
    central_line(model, X_1, X_21, 1, 21, incident=True)
    X_162 = eval_trilinear_point(model, A, B, C, '1/(sin(2*B) - sin(2*C))', ID="X(162)", classes=["center", "incident"])
    X_240 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(A + omega )', ID="X(240)", classes=["center", "incident"])
    central_line(model, X_162, X_240, 162, 240, incident=True)
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X(238)", classes=["center", "incident"])
    X_244 = eval_trilinear_point(model, A, B, C, '(b - c)**(2)', ID="X(244)", classes=["center", "incident"])
    central_line(model, X_238, X_244, 238, 244, incident=True)
    return promote_point_to_top(model, X_896)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(896) on the given reference triangle."""
    model = create_model('X(896) = INTERSECTION OF LINES X(1)X(21) AND X(9)X(750)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00896(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00896.json"))
    write_center_svg(
        model_acute,
        here / "x-00896.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
