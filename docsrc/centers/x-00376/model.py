"""GEOMETOR construction model for X(376) = CENTROID OF THE ANTIPEDAL TRIANGLE OF X(2)."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00376(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(376) = CENTROID OF THE ANTIPEDAL TRIANGLE OF X(2) on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X(20)", classes=["center"])
    X_376 = midpoint(model, X_2, X_20, ID="X(376)", classes=["selected", "target"], guide=False)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X(69)", classes=["center", "incident"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X(74)", classes=["center", "incident"])
    central_line(model, X_69, X_74, 69, 74, incident=True)
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X(35)", classes=["center", "incident"])
    X_388 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) + (b + c)**(2))/(b + c - a)', ID="X(388)", classes=["center", "incident"])
    central_line(model, X_35, X_388, 35, 388, incident=True)
    return promote_point_to_top(model, X_376)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(376) on the given reference triangle."""
    model = create_model('X(376) = CENTROID OF THE ANTIPEDAL TRIANGLE OF X(2)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00376(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00376.json"))
    write_center_svg(
        model_acute,
        here / "x-00376.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
