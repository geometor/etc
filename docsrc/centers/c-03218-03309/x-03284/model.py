"""GEOMETOR construction model for X_3284 = INTERSECTION OF LINES X_2X_340 AND X_3X_6."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03284(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3284 = INTERSECTION OF LINES X_2X_340 AND X_3X_6 on reference triangle ABC."""
    X_401 = eval_trilinear_point(model, A, B, C, '(sin(2*B)*sin(2*C) - (sin(2*A))**(2))*(csc(A))', ID="X_401", classes=["center"])
    X_648 = eval_trilinear_point(model, A, B, C, '1/(a*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2)))', ID="X_648", classes=["center"])
    X_3284 = midpoint(model, X_401, X_648, ID="X_3284", classes=["selected", "target"], guide=False)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_23 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X_23", classes=["center", "incident"])
    X_232 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(A +  omega  )', ID="X_232", classes=["center", "incident"])
    central_line(model, X_23, X_232, 23, 232, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_340 = eval_trilinear_point(model, A, B, C, 'sec(A)*sin(3*A)*(csc(A))**(3)', ID="X_340", classes=["center", "incident"])
    central_line(model, X_2, X_340, 2, 340, incident=True)
    return promote_point_to_top(model, X_3284)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3284 on the given reference triangle."""
    model = create_model('X_3284 = INTERSECTION OF LINES X_2X_340 AND X_3X_6')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03284(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03284.json"))
    write_center_svg(
        model_acute,
        here / "x-03284.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
