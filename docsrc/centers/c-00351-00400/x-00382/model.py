"""GEOMETOR construction model for X_382 = REFLECTION OF CIRCUMCENTER IN ORTHOCENTER."""

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
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00382(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_382 = REFLECTION OF CIRCUMCENTER IN ORTHOCENTER on reference triangle ABC."""
    X_382 = eval_trilinear_point(model, A, B, C, 'cos(A) - 4*cos(B)*cos(C)', ID="X_382", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X_64", classes=["center", "incident"])
    X_265 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*csc(3*A)', ID="X_265", classes=["center", "incident"])
    central_line(model, X_64, X_265, 64, 265, incident=True)
    X_155 = eval_trilinear_point(model, A, B, C, '(cos(A))*((cos(B))**(2) + (cos(C))**(2) - (cos(A))**(2))', ID="X_155", classes=["center", "incident"])
    X_399 = eval_trilinear_point(model, A, B, C, '5*cos(A) - 4*cos(B)*cos(C) - 8*sin(B)*sin(C)*(cos(A))**(2)', ID="X_399", classes=["center", "incident"])
    central_line(model, X_155, X_399, 155, 399, incident=True)
    return promote_point_to_top(model, X_382)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_382 on the given reference triangle."""
    model = create_model('X_382 = REFLECTION OF CIRCUMCENTER IN ORTHOCENTER')
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
