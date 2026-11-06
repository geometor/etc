"""GEOMETOR construction model for X_3560 = SS(sin A → cos A) OF X_940."""

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
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03560(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3560 = SS(sin A → cos A) OF X_940 on reference triangle ABC."""
    X_3560 = eval_trilinear_point(model, A, B, C, '((cos(A))**(2) + 2*cos(B)*cos(C) + cos(C)*cos(A) + cos(A)*cos(B))', ID="X_3560", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_90 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C) - cos(A))', ID="X_90", classes=["center", "incident"])
    central_line(model, X_1, X_90, 1, 90, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_355 = eval_trilinear_point(model, A, B, C, 'a*cos(A) - (b + c)*cos(B - C)', ID="X_355", classes=["center", "incident"])
    central_line(model, X_55, X_355, 55, 355, incident=True)
    return promote_point_to_top(model, X_3560)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3560 on the given reference triangle."""
    model = create_model('X_3560 = SS(sin A → cos A) OF X_940')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03560(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03560.json"))
    write_center_svg(
        model_acute,
        here / "x-03560.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
