"""GEOMETOR construction model for X_2590 = X_2-ISOCONJUGATE OF X_1381."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02590(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2590 = X_2-ISOCONJUGATE OF X_1381 on reference triangle ABC."""
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    X_1381 = eval_trilinear_point(model, A, B, C, '(r + ( OI  - R)*cos(A))', ID="X_1381", classes=["center"])
    X_2590 = crosspoint(model, A, B, C, X_57, X_1381, ID="X_2590", classes=["selected", "target"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    central_line(model, X_44, X_513, 44, 513, incident=True)
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    central_line(model, X_101, X_1381, 101, 1381, incident=True)
    X_1382 = eval_trilinear_point(model, A, B, C, '(r - ( OI  + R)*cos(A))', ID="X_1382", classes=["center", "incident"])
    X_2291 = eval_trilinear_point(model, A, B, C, 'a/(a*(2*a - b - c) - (b - c)**(2))', ID="X_2291", classes=["center", "incident"])
    central_line(model, X_1382, X_2291, 1382, 2291, incident=True)
    return promote_point_to_top(model, X_2590)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2590 on the given reference triangle."""
    model = create_model('X_2590 = X_2-ISOCONJUGATE OF X_1381')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02590(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02590.json"))
    write_center_svg(
        model_acute,
        here / "x-02590.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
