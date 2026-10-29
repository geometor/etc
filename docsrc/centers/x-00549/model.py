"""GEOMETOR construction model for X(549) = MIDPOINT OF X(2) AND X(3)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    complement,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00549(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(549) = MIDPOINT OF X(2) AND X(3) on reference triangle ABC."""
    X_381 = eval_trilinear_point(model, A, B, C, '2*cos(B - C) - cos(A)', ID="X(381)", classes=["center"])
    X_549 = complement(model, A, B, C, X_381, ID="X(549)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_15 = eval_trilinear_point(model, A, B, C, 'sin(A + pi /3)', ID="X(15)", classes=["center", "incident"])
    X_395 = eval_trilinear_point(model, A, B, C, 'cos(B - C) + 2*cos(A + pi /3)', ID="X(395)", classes=["center", "incident"])
    central_line(model, X_15, X_395, 15, 395, incident=True)
    return promote_point_to_top(model, X_549)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(549) on the given reference triangle."""
    model = create_model('X(549) = MIDPOINT OF X(2) AND X(3)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00549(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00549.json"))
    write_center_svg(
        model_acute,
        here / "x-00549.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
