"""GEOMETOR construction model for X(891) = ISOTOMIC CONJUGATE OF X(889)."""

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


def construct_x_00891(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(891) = ISOTOMIC CONJUGATE OF X(889) on reference triangle ABC."""
    X_891 = eval_trilinear_point(model, A, B, C, '(b - c)*(a*b + a*c - 2*b*c)', ID="X(891)", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X(511)", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_659 = eval_trilinear_point(model, A, B, C, '(a**(2) - b*c)*(b - c)', ID="X(659)", classes=["center", "incident"])
    central_line(model, X_1, X_659, 1, 659, incident=True)
    X_244 = eval_trilinear_point(model, A, B, C, '(b - c)**(2)', ID="X(244)", classes=["center", "incident"])
    X_665 = eval_trilinear_point(model, A, B, C, 'a*((a - b)**(2)*(a + b - c) - (c - a)**(2)*(c + a - b))', ID="X(665)", classes=["center", "incident"])
    central_line(model, X_244, X_665, 244, 665, incident=True)
    return promote_point_to_top(model, X_891)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(891) on the given reference triangle."""
    model = create_model('X(891) = ISOTOMIC CONJUGATE OF X(889)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00891(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00891.json"))
    write_center_svg(
        model_acute,
        here / "x-00891.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
