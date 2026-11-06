"""GEOMETOR construction model for X_3373 = SEC(A - 3π/8) POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03373(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3373 = SEC(A - 3π/8) POINT on reference triangle ABC."""
    X_3371 = eval_trilinear_point(model, A, B, C, 'cos(A - 3*pi  /8)', ID="X_3371", classes=["center"])
    X_3373 = isogonal_conjugate(model, A, B, C, X_3371, ID="X_3373", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_371 = eval_trilinear_point(model, A, B, C, 'cos(A -  pi  /4)', ID="X_371", classes=["center", "incident"])
    central_line(model, X_5, X_371, 5, 371, incident=True)
    return promote_point_to_top(model, X_3373)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3373 on the given reference triangle."""
    model = create_model('X_3373 = SEC(A - 3π/8) POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03373(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03373.json"))
    write_center_svg(
        model_acute,
        here / "x-03373.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
