"""GEOMETOR construction model for X_3843 = X_3091com(EULER TRIANGLE)."""

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


def construct_x_03843(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3843 = X_3091com(EULER TRIANGLE) on reference triangle ABC."""
    X_3843 = eval_barycentric_point(model, A, B, C, '3*a**(4) - 4*b**(4) - 4*c**(4) + a**(2)*b**(2) + a**(2)*c**(2) + 8*b**(2)*c**(2)', ID="X_3843", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_1159 = eval_trilinear_point(model, A, B, C, '(cos(A) + 4*cos(B) + 4*cos(C))', ID="X_1159", classes=["center", "incident"])
    X_1837 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - 2*cos(B)*cos(C)', ID="X_1837", classes=["center", "incident"])
    central_line(model, X_1159, X_1837, 1159, 1837, incident=True)
    X_1482 = point_from_barycentrics(model, A, B, C, 0.12152778, 0.27083333, 0.60763889, ID="X_1482", classes=["center", "incident"])
    X_1699 = eval_trilinear_point(model, A, B, C, '2*cos(B - C) - cos(A) + cos(B) + cos(C) - 1', ID="X_1699", classes=["center", "incident"])
    central_line(model, X_1482, X_1699, 1482, 1699, incident=True)
    return promote_point_to_top(model, X_3843)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3843 on the given reference triangle."""
    model = create_model('X_3843 = X_3091com(EULER TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03843(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03843.json"))
    write_center_svg(
        model_acute,
        here / "x-03843.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
