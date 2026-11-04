"""GEOMETOR construction model for X_2466 = EXSIMILICENTER(ORTHOCENTROIDAL CIRCLE, 2nd LEMOINE CIRCLE)."""

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


def construct_x_02466(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2466 = EXSIMILICENTER(ORTHOCENTROIDAL CIRCLE, 2nd LEMOINE CIRCLE) on reference triangle ABC."""
    X_2466 = eval_trilinear_point(model, A, B, C, '(cos(A) + 4*cos(B)*cos(C) - J*sin(A))', ID="X_2466", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A +  pi  /3)', ID="X_13", classes=["center", "incident"])
    central_line(model, X_6, X_13, 6, 13, incident=True)
    X_1124 = eval_trilinear_point(model, A, B, C, '1 + sin(A)', ID="X_1124", classes=["center", "incident"])
    X_2463 = eval_trilinear_point(model, A, B, C, '(J + cos(A) + 4*cos(B)*cos(C))', ID="X_2463", classes=["center", "incident"])
    central_line(model, X_1124, X_2463, 1124, 2463, incident=True)
    X_1335 = eval_trilinear_point(model, A, B, C, '(1 - sin(A))', ID="X_1335", classes=["center", "incident"])
    X_2464 = eval_trilinear_point(model, A, B, C, '(J - cos(A) - 4*cos(B)*cos(C))', ID="X_2464", classes=["center", "incident"])
    central_line(model, X_1335, X_2464, 1335, 2464, incident=True)
    return promote_point_to_top(model, X_2466)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2466 on the given reference triangle."""
    model = create_model('X_2466 = EXSIMILICENTER(ORTHOCENTROIDAL CIRCLE, 2nd LEMOINE CIRCLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02466(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02466.json"))
    write_center_svg(
        model_acute,
        here / "x-02466.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
