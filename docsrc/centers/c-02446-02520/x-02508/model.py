"""GEOMETOR construction model for X_2508 = RADICAL CENTER OF {NINE-POINT CIRCLE, 1st LEMOINE CIRCLE, MOSES CIRCLE}."""

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


def construct_x_02508(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2508 = RADICAL CENTER OF {NINE-POINT CIRCLE, 1st LEMOINE CIRCLE, MOSES CIRCLE} on reference triangle ABC."""
    X_2508 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) - c**(2))*(a**(8) - b**(8) - c**(8) + b**(2)*c**(2)*(b**(4) + c**(4) - a**(4))))', ID="X_2508", classes=["selected", "target"])
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center", "incident"])
    X_804 = eval_trilinear_point(model, A, B, C, 'a **(-3)*(b**(2) - c**(2)) + a**(1)*(b **(-2) - c **(-2))', ID="X_804", classes=["center", "incident"])
    central_line(model, X_115, X_804, 115, 804, incident=True)
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center", "incident"])
    X_2032 = eval_trilinear_point(model, A, B, C, '((3 + 5*cos(4*omega)  )*sin(A) + (2*sin(2*omega)  - 3*sin(4*omega)  )*cos(A))', ID="X_2032", classes=["center", "incident"])
    central_line(model, X_512, X_2032, 512, 2032, incident=True)
    X_525 = eval_trilinear_point(model, A, B, C, '(b*cos(B) - c*cos(C))/a', ID="X_525", classes=["center", "incident"])
    X_2485 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) - c**(2))*(b**(4) + c**(4) - a**(4)))', ID="X_2485", classes=["center", "incident"])
    central_line(model, X_525, X_2485, 525, 2485, incident=True)
    return promote_point_to_top(model, X_2508)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2508 on the given reference triangle."""
    model = create_model('X_2508 = RADICAL CENTER OF {NINE-POINT CIRCLE, 1st LEMOINE CIRCLE, MOSES CIRCLE}')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02508(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02508.json"))
    write_center_svg(
        model_acute,
        here / "x-02508.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
