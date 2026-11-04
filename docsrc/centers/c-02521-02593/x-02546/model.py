"""GEOMETOR construction model for X_2546 = INSIMILICENTER(1st LEMOINE CIRCLE, (X_4,2R))."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02546(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2546 = INSIMILICENTER(1st LEMOINE CIRCLE, (X_4,2R)) on reference triangle ABC."""
    X_2546 = eval_trilinear_point(model, A, B, C, '(cos(B)*cos(C) + cos(A -  omega  ))', ID="X_2546", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_83 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) + c**(2))', ID="X_83", classes=["center", "incident"])
    central_line(model, X_4, X_83, 4, 83, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_1343 = eval_trilinear_point(model, A, B, C, 'sin(A) - cos(A)*tan( omega  /2)', ID="X_1343", classes=["center", "incident"])
    central_line(model, X_2, X_1343, 2, 1343, incident=True)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_1342 = eval_trilinear_point(model, A, B, C, 'sin(A) + cos(A)*cot( omega  /2)', ID="X_1342", classes=["center", "incident"])
    central_line(model, X_20, X_1342, 20, 1342, incident=True)
    return promote_point_to_top(model, X_2546)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2546 on the given reference triangle."""
    model = create_model('X_2546 = INSIMILICENTER(1st LEMOINE CIRCLE, (X_4,2R))')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02546(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02546.json"))
    write_center_svg(
        model_acute,
        here / "x-02546.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
