"""GEOMETOR construction model for X_1302 = COLLINGS TRANSFORM OF X_381."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    cevapoint,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01302(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1302 = COLLINGS TRANSFORM OF X_381 on reference triangle ABC."""
    X_381 = eval_trilinear_point(model, A, B, C, '2*cos(B - C) - cos(A)', ID="X_381", classes=["center"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center"])
    X_1302 = cevapoint(model, A, B, C, X_381, X_523, ID="X_1302", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center", "incident"])
    central_line(model, X_2, X_74, 2, 74, incident=True)
    X_23 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X_23", classes=["center", "incident"])
    X_477 = eval_trilinear_point(model, A, B, C, '1/(4*cos(A) + cos(A - 2*B) + cos(A - 2*C) - 3*cos(B - C))', ID="X_477", classes=["center", "incident"])
    central_line(model, X_23, X_477, 23, 477, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_841 = point_from_barycentrics(model, A, B, C, 1.0412972, 0.27499895, -0.31629615, ID="X_841", classes=["center", "incident"])
    central_line(model, X_30, X_841, 30, 841, incident=True)
    return promote_point_to_top(model, X_1302)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1302 on the given reference triangle."""
    model = create_model('X_1302 = COLLINGS TRANSFORM OF X_381')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01302(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01302.json"))
    write_center_svg(
        model_acute,
        here / "x-01302.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
