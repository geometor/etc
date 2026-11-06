"""GEOMETOR construction model for X_3909 = X_3120com[INVERSE(n(3rd EULER TRIANGLE))]."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03909(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3909 = X_3120com[INVERSE(n(3rd EULER TRIANGLE))] on reference triangle ABC."""
    X_3909 = eval_barycentric_point(model, A, B, C, '(a*(a - b)*(a - c)*(b**(3) + c**(3) + a*b**(2) + a*c**(2)))', ID="X_3909", classes=["selected", "target"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    central_line(model, X_100, X_109, 100, 109, incident=True)
    X_2836 = point_from_barycentrics(model, A, B, C, -0.17277369, 0.77748158, -0.6047079, ID="X_2836", classes=["center", "incident"])
    X_2895 = point_from_barycentrics(model, A, B, C, 0.49425287, 0.34252874, 0.16321839, ID="X_2895", classes=["center", "incident"])
    central_line(model, X_2836, X_2895, 2836, 2895, incident=True)
    return promote_point_to_top(model, X_3909)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3909 on the given reference triangle."""
    model = create_model('X_3909 = X_3120com[INVERSE(n(3rd EULER TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03909(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03909.json"))
    write_center_svg(
        model_acute,
        here / "x-03909.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
