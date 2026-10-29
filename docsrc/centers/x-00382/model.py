"""GEOMETOR construction model for X(382) = REFLECTION OF CIRCUMCENTER IN ORTHOCENTER."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00382(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(382) = REFLECTION OF CIRCUMCENTER IN ORTHOCENTER on reference triangle ABC."""
    X_382 = eval_trilinear_point(model, A, B, C, 'cos(A) - 4*cos(B)*cos(C)', ID="X(382)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X(64)", classes=["center", "incident"])
    X_265 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*csc(3*A)', ID="X(265)", classes=["center", "incident"])
    central_line(model, X_64, X_265, 64, 265, incident=True)
    X_155 = eval_barycentric_point(model, A, B, C, 'a**(2)*SA*(a**(2)*(SA**(2) - SB*SC) - SA*(SB**(2) + SC**(2)))', ID="X(155)", classes=["center", "incident"])
    X_399 = point_from_barycentrics(model, A, B, C, 0.35450269, -1.0108871, 1.6563844, ID="X(399)", classes=["center", "incident"])
    central_line(model, X_155, X_399, 155, 399, incident=True)
    return promote_point_to_top(model, X_382)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(382) on the given reference triangle."""
    model = create_model('X(382) = REFLECTION OF CIRCUMCENTER IN ORTHOCENTER')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00382(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00382.json"))
    write_center_svg(
        model_acute,
        here / "x-00382.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
