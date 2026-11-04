"""GEOMETOR construction model for X_1656 = INTERSECTION OF EULER LINE AND LINEX(17)X_18."""

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
    feuerbach_point_of,
    midpoint,
    nine_point_center_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01656(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1656 = INTERSECTION OF EULER LINE AND LINEX(17)X_18 on reference triangle ABC."""
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center"])
    X_632 = eval_trilinear_point(model, A, B, C, '7*cos(A) + 6*cos(B)*cos(C)', ID="X_632", classes=["center"])
    X_1656 = midpoint(model, X_5, X_632, ID="X_1656", classes=["selected", "target"], guide=False)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_17 = eval_trilinear_point(model, A, B, C, 'csc(A +  pi  /6)', ID="X_17", classes=["center", "incident"])
    central_line(model, X_6, X_17, 6, 17, incident=True)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_498 = eval_trilinear_point(model, A, B, C, '1 + 2*sin(B)*sin(C)', ID="X_498", classes=["center", "incident"])
    central_line(model, X_11, X_498, 11, 498, incident=True)
    return promote_point_to_top(model, X_1656)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1656 on the given reference triangle."""
    model = create_model('X_1656 = INTERSECTION OF EULER LINE AND LINEX(17)X_18')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01656(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01656.json"))
    write_center_svg(
        model_acute,
        here / "x-01656.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
