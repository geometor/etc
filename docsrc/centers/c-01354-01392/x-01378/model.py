"""GEOMETOR construction model for X_1378 = EXSIMILICENTER(2nd LEMOINE CIRCLE, SPIEKER CIRCLE)."""

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
    promote_point_to_top,
    spieker_center_of,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01378(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1378 = EXSIMILICENTER(2nd LEMOINE CIRCLE, SPIEKER CIRCLE) on reference triangle ABC."""
    X_1378 = eval_trilinear_point(model, A, B, C, 'b*c*(b + c - a*sin(A))', ID="X_1378", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    central_line(model, X_6, X_10, 6, 10, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_1124 = eval_trilinear_point(model, A, B, C, '1 + sin(A)', ID="X_1124", classes=["center", "incident"])
    central_line(model, X_2, X_1124, 2, 1124, incident=True)
    X_371 = eval_trilinear_point(model, A, B, C, 'cos(A -  pi  /4)', ID="X_371", classes=["center", "incident"])
    X_958 = eval_trilinear_point(model, A, B, C, '(b + c - a)*(a**(2) + a*b + a*c + 2*b*c)', ID="X_958", classes=["center", "incident"])
    central_line(model, X_371, X_958, 371, 958, incident=True)
    return promote_point_to_top(model, X_1378)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1378 on the given reference triangle."""
    model = create_model('X_1378 = EXSIMILICENTER(2nd LEMOINE CIRCLE, SPIEKER CIRCLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01378(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01378.json"))
    write_center_svg(
        model_acute,
        here / "x-01378.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
