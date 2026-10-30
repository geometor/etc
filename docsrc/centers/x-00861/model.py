"""GEOMETOR construction model for X(861) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(9)."""

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
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00861(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(861) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(9) on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_650 = eval_trilinear_point(model, A, B, C, 'cos(B) - cos(C)', ID="X(650)", classes=["center"])
    X_663 = eval_trilinear_point(model, A, B, C, 'a*(b - c)*(b + c - a)', ID="X(663)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    central_line(model, X_650, X_663, 650, 663)
    X_861 = intersect_lines(model, X_2, X_3, X_650, X_663, ID="X(861)", classes=["selected", "target"])
    return promote_point_to_top(model, X_861)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(861) on the given reference triangle."""
    model = create_model('X(861) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(9)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00861(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00861.json"))
    write_center_svg(
        model_acute,
        here / "x-00861.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
