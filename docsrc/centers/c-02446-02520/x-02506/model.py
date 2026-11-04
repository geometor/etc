"""GEOMETOR construction model for X_2506 = RADICAL CENTER OF {NINE-POINT CIRCLE, 1st LEMOINE CIRCLE, 2nd LEMOINE CIRCLE}."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02506(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2506 = RADICAL CENTER OF {NINE-POINT CIRCLE, 1st LEMOINE CIRCLE, 2nd LEMOINE CIRCLE} on reference triangle ABC."""
    X_2506 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) - c**(2))*(a**(6) + (b**(2) + c**(2))*(a**(4) - b**(4) + 4*b**(2)*c**(2) - c**(4)) - a**(2)*(b**(4) + 4*b**(2)*c**(2) + c**(4))))', ID="X_2506", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center", "incident"])
    central_line(model, X_6, X_512, 6, 512, incident=True)
    X_525 = eval_trilinear_point(model, A, B, C, '(b*cos(B) - c*cos(C))/a', ID="X_525", classes=["center", "incident"])
    X_2485 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) - c**(2))*(b**(4) + c**(4) - a**(4)))', ID="X_2485", classes=["center", "incident"])
    central_line(model, X_525, X_2485, 525, 2485, incident=True)
    X_2489 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) - c**(2))/(b**(2) + c**(2) - a**(2)))', ID="X_2489", classes=["center", "incident"])
    X_2519 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))*(a**(4) + b**(4) + c**(4) + 2*a**(2)*b**(2) + 2*a**(2)*c**(2) - 6*b**(2)*c**(2)))', ID="X_2519", classes=["center", "incident"])
    central_line(model, X_2489, X_2519, 2489, 2519, incident=True)
    return promote_point_to_top(model, X_2506)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2506 on the given reference triangle."""
    model = create_model('X_2506 = RADICAL CENTER OF {NINE-POINT CIRCLE, 1st LEMOINE CIRCLE, 2nd LEMOINE CIRCLE}')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02506(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02506.json"))
    write_center_svg(
        model_acute,
        here / "x-02506.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
