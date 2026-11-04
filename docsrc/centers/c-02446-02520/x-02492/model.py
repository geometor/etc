"""GEOMETOR construction model for X_2492 = RADICAL CENTER OF {CIRCUMCIRCLE,NINE-POINT-CIRCLE, MOSES CIRCLE}."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    midpoint,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02492(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2492 = RADICAL CENTER OF {CIRCUMCIRCLE,NINE-POINT-CIRCLE, MOSES CIRCLE} on reference triangle ABC."""
    X_2485 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) - c**(2))*(b**(4) + c**(4) - a**(4)))', ID="X_2485", classes=["center"])
    X_2489 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) - c**(2))/(b**(2) + c**(2) - a**(2)))', ID="X_2489", classes=["center"])
    X_2492 = midpoint(model, X_2485, X_2489, ID="X_2492", classes=["selected", "target"], guide=False)
    X_230 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*(2*a**(2) - b**(2) - c**(2)) + (b**(2) - c**(2))**(2))', ID="X_230", classes=["center", "incident"])
    X_231 = eval_trilinear_point(model, A, B, C, '(cos(B))*(4*(sin(C))**(2) - 1)*(cos(A)*sin(B) - sin(A)*cos(B)) - (cos(C))*(4*(sin(B))**(2) - 1)*(cos(C)*sin(A) - sin(C)*cos(A))', ID="X_231", classes=["center", "incident"])
    central_line(model, X_230, X_231, 230, 231, incident=True)
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X_111", classes=["center", "incident"])
    X_351 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) - c**(2))*(b**(2) + c**(2) - 2*a**(2)))', ID="X_351", classes=["center", "incident"])
    central_line(model, X_111, X_351, 111, 351, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_526 = eval_trilinear_point(model, A, B, C, '(1 + 2*cos(2*A))*sin(B - C)', ID="X_526", classes=["center", "incident"])
    central_line(model, X_6, X_526, 6, 526, incident=True)
    return promote_point_to_top(model, X_2492)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2492 on the given reference triangle."""
    model = create_model('X_2492 = RADICAL CENTER OF {CIRCUMCIRCLE,NINE-POINT-CIRCLE, MOSES CIRCLE}')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02492(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02492.json"))
    write_center_svg(
        model_acute,
        here / "x-02492.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
