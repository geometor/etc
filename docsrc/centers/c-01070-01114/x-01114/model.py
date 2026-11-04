"""GEOMETOR construction model for X_1114 = 2nd EULER-LINE-CIRCUMCIRCLE INTERSECTION."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01114(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1114 = 2nd EULER-LINE-CIRCUMCIRCLE INTERSECTION on reference triangle ABC."""
    X_1114 = eval_trilinear_point(model, A, B, C, '(R + d)*cos(A) - 2*R*cos(B)*cos(C)', ID="X_1114", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    X_1823 = point_from_barycentrics(model, A, B, C, 0.72123578, 0.4152025, -0.13643829, ID="X_1823", classes=["center", "incident"])
    central_line(model, X_109, X_1823, 109, 1823, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2101 = point_from_barycentrics(model, A, B, C, 1.5708923, 1.0669906, -1.637883, ID="X_2101", classes=["center", "incident"])
    central_line(model, X_1, X_2101, 1, 2101, incident=True)
    return promote_point_to_top(model, X_1114)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1114 on the given reference triangle."""
    model = create_model('X_1114 = 2nd EULER-LINE-CIRCUMCIRCLE INTERSECTION')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01114(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01114.json"))
    write_center_svg(
        model_acute,
        here / "x-01114.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
