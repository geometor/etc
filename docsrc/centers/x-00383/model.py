"""GEOMETOR construction model for X(383) = EULER LINE INTERCEPT OF LINE X(14)X(98)."""

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


def construct_x_00383(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(383) = EULER LINE INTERCEPT OF LINE X(14)X(98) on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_14 = eval_trilinear_point(model, A, B, C, 'csc(A - pi /3)', ID="X(14)", classes=["center"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A + omega )', ID="X(98)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    central_line(model, X_14, X_98, 14, 98)
    X_383 = intersect_lines(model, X_2, X_3, X_14, X_98, ID="X(383)", classes=["selected", "target"])
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A + pi /3)', ID="X(13)", classes=["center", "incident"])
    X_262 = eval_trilinear_point(model, A, B, C, 'sec(A - omega )', ID="X(262)", classes=["center", "incident"])
    central_line(model, X_13, X_262, 13, 262, incident=True)
    return promote_point_to_top(model, X_383)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(383) on the given reference triangle."""
    model = create_model('X(383) = EULER LINE INTERCEPT OF LINE X(14)X(98)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00383(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00383.json"))
    write_center_svg(
        model_acute,
        here / "x-00383.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
