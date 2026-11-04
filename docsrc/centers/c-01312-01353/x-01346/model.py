"""GEOMETOR construction model for X_1346 = INSIMILICENTER(NINE-POINT CIRCLE, ORTHOCENTROIDAL CIRCLE)."""

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


def construct_x_01346(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1346 = INSIMILICENTER(NINE-POINT CIRCLE, ORTHOCENTROIDAL CIRCLE) on reference triangle ABC."""
    X_1346 = eval_trilinear_point(model, A, B, C, '(R*cos(A) +  OH*cos(B - C) + 4*R*cos(B)*cos(C))', ID="X_1346", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_2464 = eval_trilinear_point(model, A, B, C, '(J - cos(A) - 4*cos(B)*cos(C))', ID="X_2464", classes=["center", "incident"])
    central_line(model, X_56, X_2464, 56, 2464, incident=True)
    return promote_point_to_top(model, X_1346)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1346 on the given reference triangle."""
    model = create_model('X_1346 = INSIMILICENTER(NINE-POINT CIRCLE, ORTHOCENTROIDAL CIRCLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01346(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01346.json"))
    write_center_svg(
        model_acute,
        here / "x-01346.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
