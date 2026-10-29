"""GEOMETOR construction model for X(853) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(55)."""

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


def construct_x_00853(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(853) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(55) on reference triangle ABC."""
    X_853 = eval_trilinear_point(model, A, B, C, '(sec(C/2))**(2)*sin(2*B)*sin(C - A) + (sec(B/2))**(2)*sin(2*C)*sin(B - A)', ID="X(853)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_657 = eval_trilinear_point(model, A, B, C, '(1 + cos(A))*(cos(B) - cos(C))', ID="X(657)", classes=["center", "incident"])
    X_663 = eval_trilinear_point(model, A, B, C, 'a*(b - c)*(b + c - a)', ID="X(663)", classes=["center", "incident"])
    central_line(model, X_657, X_663, 657, 663, incident=True)
    return promote_point_to_top(model, X_853)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(853) on the given reference triangle."""
    model = create_model('X(853) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(55)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00853(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00853.json"))
    write_center_svg(
        model_acute,
        here / "x-00853.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
