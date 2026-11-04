"""GEOMETOR construction model for X_2478 = INVERSE-IN-ORTHOCENTROIDAL-CIRCLE OF X_377."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    anticomplement,
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02478(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2478 = INVERSE-IN-ORTHOCENTROIDAL-CIRCLE OF X_377 on reference triangle ABC."""
    X_474 = eval_trilinear_point(model, A, B, C, 'cos(A) - (a + b + c)/a', ID="X_474", classes=["center"])
    X_2478 = anticomplement(model, A, B, C, X_474, ID="X_2478", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_210 = eval_trilinear_point(model, A, B, C, '(b + c)*(b + c - a)', ID="X_210", classes=["center", "incident"])
    central_line(model, X_8, X_210, 8, 210, incident=True)
    X_355 = eval_trilinear_point(model, A, B, C, 'a*cos(A) - (b + c)*cos(B - C)', ID="X_355", classes=["center", "incident"])
    X_392 = eval_trilinear_point(model, A, B, C, '(b + c)*(b**(2) + c**(2) - a**(2)) + 4*a*b*c', ID="X_392", classes=["center", "incident"])
    central_line(model, X_355, X_392, 355, 392, incident=True)
    return promote_point_to_top(model, X_2478)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2478 on the given reference triangle."""
    model = create_model('X_2478 = INVERSE-IN-ORTHOCENTROIDAL-CIRCLE OF X_377')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02478(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02478.json"))
    write_center_svg(
        model_acute,
        here / "x-02478.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
