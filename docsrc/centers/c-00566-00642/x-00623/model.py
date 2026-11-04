"""GEOMETOR construction model for X_623 = COMPLEMENT OF X_15."""

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
    intersect_lines,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00623(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_623 = COMPLEMENT OF X_15 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_14 = eval_trilinear_point(model, A, B, C, 'csc(A - pi /3)', ID="X_14", classes=["center"])
    X_18 = eval_trilinear_point(model, A, B, C, 'csc(A - pi /6)', ID="X_18", classes=["center"])
    X_83 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) + c**(2))', ID="X_83", classes=["center"])
    central_line(model, X_2, X_14, 2, 14)
    central_line(model, X_18, X_83, 18, 83)
    X_623 = intersect_lines(model, X_2, X_14, X_18, X_83, ID="X_623", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X_141", classes=["center", "incident"])
    central_line(model, X_5, X_141, 5, 141, incident=True)
    return promote_point_to_top(model, X_623)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_623 on the given reference triangle."""
    model = create_model('X_623 = COMPLEMENT OF X_15')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00623(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00623.json"))
    write_center_svg(
        model_acute,
        here / "x-00623.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
