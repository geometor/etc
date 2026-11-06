"""GEOMETOR construction model for X_3983 = X_3523com(EXTOUCH TRIANGLE)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03983(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3983 = X_3523com(EXTOUCH TRIANGLE) on reference triangle ABC."""
    X_3983 = eval_barycentric_point(model, A, B, C, '(a*(b + c)*(b**(2) + c**(2) - a**(2) + 6*b*c))', ID="X_3983", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    central_line(model, X_10, X_12, 10, 12, incident=True)
    X_354 = eval_trilinear_point(model, A, B, C, '(b - c)**(2) - a*b - a*c', ID="X_354", classes=["center", "incident"])
    X_1698 = eval_trilinear_point(model, A, B, C, '2*cos(B - C) + cos(A) - cos(B) - cos(C) + 1', ID="X_1698", classes=["center", "incident"])
    central_line(model, X_354, X_1698, 354, 1698, incident=True)
    X_936 = eval_trilinear_point(model, A, B, C, 'a**(3) - a**(2)*(b + c) - a*(b - c)**(2) + (b + c)**(3)', ID="X_936", classes=["center", "incident"])
    X_1319 = eval_trilinear_point(model, A, B, C, '(b + c - 2*a)/ (b + c - a)', ID="X_1319", classes=["center", "incident"])
    central_line(model, X_936, X_1319, 936, 1319, incident=True)
    return promote_point_to_top(model, X_3983)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3983 on the given reference triangle."""
    model = create_model('X_3983 = X_3523com(EXTOUCH TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03983(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03983.json"))
    write_center_svg(
        model_acute,
        here / "x-03983.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
