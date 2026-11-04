"""GEOMETOR construction model for X_1776 = MIMOSA TRANSFORM OF X_1156."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01776(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1776 = MIMOSA TRANSFORM OF X_1156 on reference triangle ABC."""
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center"])
    X_1156 = eval_trilinear_point(model, A, B, C, '(1/((b - c)**(2) + a*(b + c - 2*a)))', ID="X_1156", classes=["center"])
    X_1776 = crosspoint(model, A, B, C, X_21, X_1156, ID="X_1776", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center", "incident"])
    central_line(model, X_4, X_46, 4, 46, incident=True)
    X_60 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(B - C))', ID="X_60", classes=["center", "incident"])
    central_line(model, X_21, X_60, 21, 60, incident=True)
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    X_497 = eval_trilinear_point(model, A, B, C, '1 - cos(B)*cos(C)', ID="X_497", classes=["center", "incident"])
    central_line(model, X_63, X_497, 63, 497, incident=True)
    return promote_point_to_top(model, X_1776)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1776 on the given reference triangle."""
    model = create_model('X_1776 = MIMOSA TRANSFORM OF X_1156')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01776(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01776.json"))
    write_center_svg(
        model_acute,
        here / "x-01776.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
