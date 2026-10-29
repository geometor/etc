"""GEOMETOR construction model for X(441) = COMPLEMENT OF X(297)."""

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


def construct_x_00441(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(441) = COMPLEMENT OF X(297) on reference triangle ABC."""
    X_297 = eval_trilinear_point(model, A, B, C, 'csc(2*A)*cos(A + omega )', ID="X(297)", classes=["center"])
    X_401 = eval_trilinear_point(model, A, B, C, '(sin(2*B)*sin(2*C) - (sin(2*A))**(2))*(csc(A))', ID="X(401)", classes=["center"])
    X_441 = midpoint(model, X_297, X_401, ID="X(441)", classes=["selected", "target"], guide=False)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X(141)", classes=["center", "incident"])
    X_577 = eval_trilinear_point(model, A, B, C, 'cos(A)*(tan(A) + tan(B) + tan(C)) - sin(A)', ID="X(577)", classes=["center", "incident"])
    central_line(model, X_141, X_577, 141, 577, incident=True)
    X_525 = eval_trilinear_point(model, A, B, C, '(b*cos(B) - c*cos(C))/a', ID="X(525)", classes=["center", "incident"])
    X_647 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))', ID="X(647)", classes=["center", "incident"])
    central_line(model, X_525, X_647, 525, 647, incident=True)
    return promote_point_to_top(model, X_441)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(441) on the given reference triangle."""
    model = create_model('X(441) = COMPLEMENT OF X(297)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00441(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00441.json"))
    write_center_svg(
        model_acute,
        here / "x-00441.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
