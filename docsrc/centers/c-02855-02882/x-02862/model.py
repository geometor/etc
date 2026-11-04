"""GEOMETOR construction model for X_2862 = SM(X_100, X_105)."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02862(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2862 = SM(X_100, X_105) on reference triangle ABC."""
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center"])
    X_693 = eval_trilinear_point(model, A, B, C, '(b - c)/a**(2)', ID="X_693", classes=["center"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center"])
    X_813 = eval_trilinear_point(model, A, B, C, '1/(a**(-2)*(b**(1) - c**(1)) + a**(0)*(b**(-1) - c **(-1)))', ID="X_813", classes=["center"])
    central_line(model, X_105, X_693, 105, 693)
    central_line(model, X_63, X_813, 63, 813)
    X_2862 = intersect_lines(model, X_105, X_693, X_63, X_813, ID="X_2862", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_919 = point_from_barycentrics(model, A, B, C, -0.11560694, 0.83236994, 0.28323699, ID="X_919", classes=["center", "incident"])
    central_line(model, X_2, X_919, 2, 919, incident=True)
    return promote_point_to_top(model, X_2862)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2862 on the given reference triangle."""
    model = create_model('X_2862 = SM(X_100, X_105)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02862(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02862.json"))
    write_center_svg(
        model_acute,
        here / "x-02862.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
