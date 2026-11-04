"""GEOMETOR construction model for X_1328 = ARCTAN(-3) KIEPERT POINT."""

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


def construct_x_01328(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1328 = ARCTAN(-3) KIEPERT POINT on reference triangle ABC."""
    X_1328 = eval_trilinear_point(model, A, B, C, '1/(sin(A) - 3*cos(A))', ID="X_1328", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_486 = eval_trilinear_point(model, A, B, C, 'sec(A + pi /4)', ID="X_486", classes=["center", "incident"])
    central_line(model, X_30, X_486, 30, 486, incident=True)
    X_381 = eval_trilinear_point(model, A, B, C, '2*cos(B - C) - cos(A)', ID="X_381", classes=["center", "incident"])
    X_485 = eval_trilinear_point(model, A, B, C, 'sec(A - pi /4)', ID="X_485", classes=["center", "incident"])
    central_line(model, X_381, X_485, 381, 485, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_1327 = eval_trilinear_point(model, A, B, C, '(1/(sin(A) + 3*cos(A)))', ID="X_1327", classes=["center", "incident"])
    central_line(model, X_6, X_1327, 6, 1327, incident=True)
    return promote_point_to_top(model, X_1328)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1328 on the given reference triangle."""
    model = create_model('X_1328 = ARCTAN(-3) KIEPERT POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01328(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01328.json"))
    write_center_svg(
        model_acute,
        here / "x-01328.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
