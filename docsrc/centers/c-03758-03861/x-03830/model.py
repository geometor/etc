"""GEOMETOR construction model for X_3830 = X_3543com(EULER TRIANGLE)."""

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
    midpoint,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03830(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3830 = X_3543com(EULER TRIANGLE) on reference triangle ABC."""
    X_381 = eval_trilinear_point(model, A, B, C, '2*cos(B - C) - cos(A)', ID="X_381", classes=["center"])
    X_382 = eval_trilinear_point(model, A, B, C, 'cos(A) - 4*cos(B)*cos(C)', ID="X_382", classes=["center"])
    X_3830 = midpoint(model, X_381, X_382, ID="X_3830", classes=["selected", "target"], guide=False)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_265 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*csc(3*A)', ID="X_265", classes=["center", "incident"])
    X_541 = point_from_barycentrics(model, A, B, C, 0.11755139, 0.64096444, -0.75851583, ID="X_541", classes=["center", "incident"])
    central_line(model, X_265, X_541, 265, 541, incident=True)
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center", "incident"])
    X_1384 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) - 5*a**(2))', ID="X_1384", classes=["center", "incident"])
    central_line(model, X_115, X_1384, 115, 1384, incident=True)
    return promote_point_to_top(model, X_3830)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3830 on the given reference triangle."""
    model = create_model('X_3830 = X_3543com(EULER TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03830(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03830.json"))
    write_center_svg(
        model_acute,
        here / "x-03830.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
