"""GEOMETOR construction model for X(642) = COMPLEMENT OF X(486)."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00642(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(642) = COMPLEMENT OF X(486) on reference triangle ABC."""
    X_486 = eval_trilinear_point(model, A, B, C, 'sec(A + pi /4)', ID="X(486)", classes=["center"])
    X_487 = point_from_barycentrics(model, A, B, C, -1.1839423, 1.1273575, 1.0565848, ID="X(487)", classes=["center"])
    X_642 = midpoint(model, X_486, X_487, ID="X(642)", classes=["selected", "target"], guide=False)
    X_140 = eval_trilinear_point(model, A, B, C, '2*cos(A) + cos(B - C)', ID="X(140)", classes=["center", "incident"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X(141)", classes=["center", "incident"])
    central_line(model, X_140, X_141, 140, 141, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_371 = eval_trilinear_point(model, A, B, C, 'cos(A - pi /4)', ID="X(371)", classes=["center", "incident"])
    central_line(model, X_2, X_371, 2, 371, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_640 = point_from_barycentrics(model, A, B, C, 0.50503315, 0.37571481, 0.11925204, ID="X(640)", classes=["center", "incident"])
    central_line(model, X_3, X_640, 3, 640, incident=True)
    return promote_point_to_top(model, X_642)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(642) on the given reference triangle."""
    model = create_model('X(642) = COMPLEMENT OF X(486)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00642(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00642.json"))
    write_center_svg(
        model_acute,
        here / "x-00642.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
