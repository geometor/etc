"""GEOMETOR construction model for X(373) = CENTROID OF THE PEDAL TRIANGLE OF THE CENTROID."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    intersect_lines,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00373(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(373) = CENTROID OF THE PEDAL TRIANGLE OF THE CENTROID on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X(51)", classes=["center"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center"])
    X_113 = eval_trilinear_point(model, A, B, C, 'sin(B)*sin(C)*((sin(C))/(cos(C) - 2*cos(A)*cos(B)) + (sin(B))/(cos(B) - 2*cos(A)*cos(C)))', ID="X(113)", classes=["center"])
    central_line(model, X_2, X_51, 2, 51)
    central_line(model, X_5, X_113, 5, 113)
    X_373 = intersect_lines(model, X_2, X_51, X_5, X_113, ID="X(373)", classes=["selected", "target"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    X_575 = eval_barycentric_point(model, A, B, C, 'a**(2)*(2*a**(4) + b**(4) + c**(4) - 3*a**(2)*b**(2) - 3*a**(2)*c**(2) - 4*b**(2)*c**(2))', ID="X(575)", classes=["center", "incident"])
    central_line(model, X_110, X_575, 110, 575, incident=True)
    return promote_point_to_top(model, X_373)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(373) on the given reference triangle."""
    model = create_model('X(373) = CENTROID OF THE PEDAL TRIANGLE OF THE CENTROID')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00373(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00373.json"))
    write_center_svg(
        model_acute,
        here / "x-00373.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
