"""GEOMETOR construction model for X_2526 = RADICAL CENTER OF {NINE-POINT, APOLLONIUS, (X_4,2R)} CIRCLES."""

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
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_02526(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2526 = RADICAL CENTER OF {NINE-POINT, APOLLONIUS, (X_4,2R)} CIRCLES on reference triangle ABC."""
    X_650 = eval_trilinear_point(model, A, B, C, 'cos(B) - cos(C)', ID="X_650", classes=["center"])
    X_1491 = eval_trilinear_point(model, A, B, C, 'b**(3) - c**(3)', ID="X_1491", classes=["center"])
    X_2526 = reflection_in_point(model, X_650, X_1491, ID="X_2526", classes=["selected", "target"], guide=False)
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    central_line(model, X_44, X_513, 44, 513, incident=True)
    X_830 = eval_trilinear_point(model, A, B, C, '(a**(0)*(b**(3) - c**(3)) + a**(2)*(b**(1) - c**(1)))', ID="X_830", classes=["center", "incident"])
    X_905 = eval_trilinear_point(model, A, B, C, '(b - c)*cot(A)', ID="X_905", classes=["center", "incident"])
    central_line(model, X_830, X_905, 830, 905, incident=True)
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center", "incident"])
    X_2525 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(4) - c**(4))*(b**(2) + c**(2) - a**(2)))', ID="X_2525", classes=["center", "incident"])
    central_line(model, X_523, X_2525, 523, 2525, incident=True)
    return promote_point_to_top(model, X_2526)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2526 on the given reference triangle."""
    model = create_model('X_2526 = RADICAL CENTER OF {NINE-POINT, APOLLONIUS, (X_4,2R)} CIRCLES')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02526(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02526.json"))
    write_center_svg(
        model_acute,
        here / "x-02526.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
