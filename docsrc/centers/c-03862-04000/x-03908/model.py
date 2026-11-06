"""GEOMETOR construction model for X_3908 = X_120com[INVERSE(n(5th EULER TRIANGLE))]."""

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


def construct_x_03908(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3908 = X_120com[INVERSE(n(5th EULER TRIANGLE))] on reference triangle ABC."""
    X_3908 = eval_barycentric_point(model, A, B, C, '(a*(a - b)*(a - c)*(2*b**(2) + 2*c**(2) - a**(2)))', ID="X_3908", classes=["selected", "target"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_100, X_110, 100, 110, incident=True)
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    X_644 = eval_trilinear_point(model, A, B, C, '((b + c - a)/(b - c))', ID="X_644", classes=["center", "incident"])
    central_line(model, X_513, X_644, 513, 644, incident=True)
    X_668 = eval_trilinear_point(model, A, B, C, '1/(a**(2)*(b - c))', ID="X_668", classes=["center", "incident"])
    X_892 = point_from_barycentrics(model, A, B, C, -0.10419811, 0.98771128, 0.11648683, ID="X_892", classes=["center", "incident"])
    central_line(model, X_668, X_892, 668, 892, incident=True)
    return promote_point_to_top(model, X_3908)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3908 on the given reference triangle."""
    model = create_model('X_3908 = X_120com[INVERSE(n(5th EULER TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03908(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03908.json"))
    write_center_svg(
        model_acute,
        here / "x-03908.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
