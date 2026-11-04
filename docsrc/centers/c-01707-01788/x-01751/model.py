"""GEOMETOR construction model for X_1751 = MIMOSA TRANSFORM OF X_272."""

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
    isogonal_conjugate,
    promote_point_to_top,
    spieker_center_of,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01751(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1751 = MIMOSA TRANSFORM OF X_272 on reference triangle ABC."""
    X_579 = eval_trilinear_point(model, A, B, C, '(a*(a**(2)*b + a**(2)*c + a*b*c - b**(3) - c**(3)))', ID="X_579", classes=["center"])
    X_1751 = isogonal_conjugate(model, A, B, C, X_579, ID="X_1751", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    central_line(model, X_10, X_55, 10, 55, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X_226", classes=["center", "incident"])
    central_line(model, X_6, X_226, 6, 226, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_272 = eval_trilinear_point(model, A, B, C, '(1/((sin(A) + sin(A - B) + sin(A - C))*(sin(B) + sin(C))))', ID="X_272", classes=["center", "incident"])
    central_line(model, X_2, X_272, 2, 272, incident=True)
    return promote_point_to_top(model, X_1751)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1751 on the given reference triangle."""
    model = create_model('X_1751 = MIMOSA TRANSFORM OF X_272')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01751(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01751.json"))
    write_center_svg(
        model_acute,
        here / "x-01751.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
