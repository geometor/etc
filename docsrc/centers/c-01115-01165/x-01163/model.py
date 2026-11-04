"""GEOMETOR construction model for X_1163 = INNER GREBE-ORTHIC PERSPECTOR."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01163(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1163 = INNER GREBE-ORTHIC PERSPECTOR on reference triangle ABC."""
    X_1163 = eval_trilinear_point(model, A, B, C, '(( area - a**(2))*(2*area - b**(2) - c**(2))/(a*(b**(2) + c**(2) - a**(2))))', ID="X_1163", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_1161 = eval_trilinear_point(model, A, B, C, '(1 - 2*cot(A) - 2*cot(B) - 2*cot(C))*cos(A) + 2*sin(A)', ID="X_1161", classes=["center", "incident"])
    central_line(model, X_4, X_1161, 4, 1161, incident=True)
    X_428 = eval_trilinear_point(model, A, B, C, '3*sec(A) - csc(A)*tan(omega)', ID="X_428", classes=["center", "incident"])
    X_1162 = eval_trilinear_point(model, A, B, C, '( area + a**(2))*(2*area + b**(2) + c**(2))/(a*(b**(2) + c**(2) - a**(2)))', ID="X_1162", classes=["center", "incident"])
    central_line(model, X_428, X_1162, 428, 1162, incident=True)
    return promote_point_to_top(model, X_1163)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1163 on the given reference triangle."""
    model = create_model('X_1163 = INNER GREBE-ORTHIC PERSPECTOR')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01163(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01163.json"))
    write_center_svg(
        model_acute,
        here / "x-01163.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
