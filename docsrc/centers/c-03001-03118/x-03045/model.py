"""GEOMETOR construction model for X_3045 = INTERSECTION X_54X_119∩X_100X_184."""

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


def construct_x_03045(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3045 = INTERSECTION X_54X_119∩X_100X_184 on reference triangle ABC."""
    X_3045 = eval_trilinear_point(model, A, B, C, '(a**(2)*(a**(3) + b**(3) - a**(2)*b - a*b**(2) - a*c**(2) + a*b*c)*(a**(3) + c**(3) - a**(2)*c - a*c**(2) - a*b**(2) + a*b*c))', ID="X_3045", classes=["selected", "target"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_11, X_110, 11, 110, incident=True)
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    X_119 = eval_trilinear_point(model, A, B, C, '(csc(A))*(-1 + cos(B) + cos(C))*(sin(2*B) + sin(2*C) + 2*(-1 + cos(A))*(sin(B) + sin(C)))', ID="X_119", classes=["center", "incident"])
    central_line(model, X_54, X_119, 54, 119, incident=True)
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    central_line(model, X_100, X_184, 100, 184, incident=True)
    return promote_point_to_top(model, X_3045)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3045 on the given reference triangle."""
    model = create_model('X_3045 = INTERSECTION X_54X_119∩X_100X_184')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03045(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03045.json"))
    write_center_svg(
        model_acute,
        here / "x-03045.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
