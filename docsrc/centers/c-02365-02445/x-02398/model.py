"""GEOMETOR construction model for X_2398 = GIBERT-SIMSON TRANSFORM OF X_101."""

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
    incenter_of,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02398(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2398 = GIBERT-SIMSON TRANSFORM OF X_101 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center"])
    X_658 = eval_trilinear_point(model, A, B, C, '1/((1 + cos(A))*(cos(B) - cos(C)))', ID="X_658", classes=["center"])
    central_line(model, X_1, X_2, 1, 2)
    central_line(model, X_100, X_658, 100, 658)
    X_2398 = intersect_lines(model, X_1, X_2, X_100, X_658, ID="X_2398", classes=["selected", "target"])
    X_666 = eval_trilinear_point(model, A, B, C, 'b*c/((a - b)**(2)*(a + b - c) - (c - a)**(2)*(c + a - b))', ID="X_666", classes=["center", "incident"])
    X_885 = eval_barycentric_point(model, A, B, C, '(b - c)*(a - b - c)/(b**(2) + c**(2) - a*b - a*c)', ID="X_885", classes=["center", "incident"])
    central_line(model, X_666, X_885, 666, 885, incident=True)
    return promote_point_to_top(model, X_2398)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2398 on the given reference triangle."""
    model = create_model('X_2398 = GIBERT-SIMSON TRANSFORM OF X_101')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02398(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02398.json"))
    write_center_svg(
        model_acute,
        here / "x-02398.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
