"""GEOMETOR construction model for X_3290 = INTERSECTION OF LINES X_2X_37 AND X_230X_231."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    midpoint,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03290(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3290 = INTERSECTION OF LINES X_2X_37 AND X_230X_231 on reference triangle ABC."""
    X_3125 = eval_trilinear_point(model, A, B, C, '((b + c)*(b - c)**(2))', ID="X_3125", classes=["center"])
    X_3230 = eval_trilinear_point(model, A, B, C, '(a*(2*b*c - a*b - a*c))', ID="X_3230", classes=["center"])
    X_3290 = midpoint(model, X_3125, X_3230, ID="X_3290", classes=["selected", "target"], guide=False)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    central_line(model, X_2, X_37, 2, 37, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_354 = eval_trilinear_point(model, A, B, C, '(b - c)**(2) - a*b - a*c', ID="X_354", classes=["center", "incident"])
    central_line(model, X_6, X_354, 6, 354, incident=True)
    X_230 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*(2*a**(2) - b**(2) - c**(2)) + (b**(2) - c**(2))**(2))', ID="X_230", classes=["center", "incident"])
    X_231 = eval_trilinear_point(model, A, B, C, '(cos(B))*(4*(sin(C))**(2) - 1)*(cos(A)*sin(B) - sin(A)*cos(B)) - (cos(C))*(4*(sin(B))**(2) - 1)*(cos(C)*sin(A) - sin(C)*cos(A))', ID="X_231", classes=["center", "incident"])
    central_line(model, X_230, X_231, 230, 231, incident=True)
    return promote_point_to_top(model, X_3290)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3290 on the given reference triangle."""
    model = create_model('X_3290 = INTERSECTION OF LINES X_2X_37 AND X_230X_231')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03290(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03290.json"))
    write_center_svg(
        model_acute,
        here / "x-03290.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
