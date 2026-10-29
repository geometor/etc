"""GEOMETOR construction model for X(864) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(32)."""

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


def construct_x_00864(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(864) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(32) on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_669 = eval_trilinear_point(model, A, B, C, 'a**(3)*(b**(2) - c**(2))', ID="X(669)", classes=["center"])
    X_688 = eval_trilinear_point(model, A, B, C, 'a**(3)*(b**(4)- c**(4))', ID="X(688)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    central_line(model, X_669, X_688, 669, 688)
    X_864 = intersect_lines(model, X_2, X_3, X_669, X_688, ID="X(864)", classes=["selected", "target"])
    return promote_point_to_top(model, X_864)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(864) on the given reference triangle."""
    model = create_model('X(864) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(32)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00864(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00864.json"))
    write_center_svg(
        model_acute,
        here / "x-00864.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
