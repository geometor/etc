"""GEOMETOR construction model for X_3829 = X_3158com(3rd EULER TRIANGLE)."""

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
    feuerbach_point_of,
    nine_point_center_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03829(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3829 = X_3158com(3rd EULER TRIANGLE) on reference triangle ABC."""
    X_3829 = eval_barycentric_point(model, A, B, C, '(3*b**(3) + 3*c**(3) - 3*a*b**(2) - 3*a*c**(2) + 4*a*b*c - 3*b**(2)*c - 3*b*c**(2))', ID="X_3829", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    central_line(model, X_2, X_11, 2, 11, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_519 = eval_trilinear_point(model, A, B, C, '(2*a - b - c)/a', ID="X_519", classes=["center", "incident"])
    central_line(model, X_5, X_519, 5, 519, incident=True)
    X_381 = eval_trilinear_point(model, A, B, C, '2*cos(B - C) - cos(A)', ID="X_381", classes=["center", "incident"])
    X_529 = point_from_barycentrics(model, A, B, C, -0.60626071, -0.17051082, 0.77677153, ID="X_529", classes=["center", "incident"])
    central_line(model, X_381, X_529, 381, 529, incident=True)
    return promote_point_to_top(model, X_3829)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3829 on the given reference triangle."""
    model = create_model('X_3829 = X_3158com(3rd EULER TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03829(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03829.json"))
    write_center_svg(
        model_acute,
        here / "x-03829.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
