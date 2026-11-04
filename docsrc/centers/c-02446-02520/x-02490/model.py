"""GEOMETOR construction model for X_2490 = RADICAL CENTER OF {CIRCUMCIRCLE,NINE-POINT-CIRCLE, SPIEKER CIRCLE}."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_02490(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2490 = RADICAL CENTER OF {CIRCUMCIRCLE,NINE-POINT-CIRCLE, SPIEKER CIRCLE} on reference triangle ABC."""
    X_2490 = eval_trilinear_point(model, A, B, C, '(b*c*(b - c)*(4*a**(2) - 3*a*b - 3*a*c + (b + c)**(2)))', ID="X_2490", classes=["selected", "target"])
    X_230 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*(2*a**(2) - b**(2) - c**(2)) + (b**(2) - c**(2))**(2))', ID="X_230", classes=["center", "incident"])
    X_231 = eval_trilinear_point(model, A, B, C, '(cos(B))*(4*(sin(C))**(2) - 1)*(cos(A)*sin(B) - sin(A)*cos(B)) - (cos(C))*(4*(sin(B))**(2) - 1)*(cos(C)*sin(A) - sin(C)*cos(A))', ID="X_231", classes=["center", "incident"])
    central_line(model, X_230, X_231, 230, 231, incident=True)
    X_661 = eval_trilinear_point(model, A, B, C, 'cot(B) - cot(C)', ID="X_661", classes=["center", "incident"])
    X_1213 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c)*(2*a + b + c))', ID="X_1213", classes=["center", "incident"])
    central_line(model, X_661, X_1213, 661, 1213, incident=True)
    X_649 = eval_trilinear_point(model, A, B, C, 'a*(b - c)', ID="X_649", classes=["center", "incident"])
    X_1639 = eval_trilinear_point(model, A, B, C, '(b*c*(b - c)*(b + c - a)*(b + c - 2*a))', ID="X_1639", classes=["center", "incident"])
    central_line(model, X_649, X_1639, 649, 1639, incident=True)
    return promote_point_to_top(model, X_2490)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2490 on the given reference triangle."""
    model = create_model('X_2490 = RADICAL CENTER OF {CIRCUMCIRCLE,NINE-POINT-CIRCLE, SPIEKER CIRCLE}')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02490(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02490.json"))
    write_center_svg(
        model_acute,
        here / "x-02490.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
