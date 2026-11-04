"""GEOMETOR construction model for X_2001 = ORTHOCORRESPONDENT OF X_32."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02001(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2001 = ORTHOCORRESPONDENT OF X_32 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center"])
    X_1915 = eval_trilinear_point(model, A, B, C, '(a*(a**(4) + b**(2)*c**(2)))', ID="X_1915", classes=["center"])
    X_1995 = eval_trilinear_point(model, A, B, C, '(a*(b**(4) + c**(4) - a**(4) - 4*b**(2)*c**(2)))', ID="X_1995", classes=["center"])
    central_line(model, X_2, X_98, 2, 98)
    central_line(model, X_1915, X_1995, 1915, 1995)
    X_2001 = intersect_lines(model, X_2, X_98, X_1915, X_1995, ID="X_2001", classes=["selected", "target"])
    return promote_point_to_top(model, X_2001)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2001 on the given reference triangle."""
    model = create_model('X_2001 = ORTHOCORRESPONDENT OF X_32')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02001(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02001.json"))
    write_center_svg(
        model_acute,
        here / "x-02001.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
