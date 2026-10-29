"""GEOMETOR construction model for X(867) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(514)."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00867(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(867) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(514) on reference triangle ABC."""
    X_867 = eval_trilinear_point(model, A, B, C, 'sin(C)*sin(2*B)*sin(A - C)/(sin(A) - sin(B)) - sin(B)*sin(2*C)*sin(A - B)/(sin(A) - sin(C))', ID="X(867)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X(11)", classes=["center", "incident"])
    X_244 = eval_trilinear_point(model, A, B, C, '(b - c)**(2)', ID="X(244)", classes=["center", "incident"])
    central_line(model, X_11, X_244, 11, 244, incident=True)
    return promote_point_to_top(model, X_867)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(867) on the given reference triangle."""
    model = create_model('X(867) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(514)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00867(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00867.json"))
    write_center_svg(
        model_acute,
        here / "x-00867.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
