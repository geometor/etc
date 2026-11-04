"""GEOMETOR construction model for X_2402 = GIBERT-SIMSON TRANSFORM OF X_105."""

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
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02402(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2402 = GIBERT-SIMSON TRANSFORM OF X_105 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_650 = eval_trilinear_point(model, A, B, C, 'cos(B) - cos(C)', ID="X_650", classes=["center"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center"])
    X_885 = eval_barycentric_point(model, A, B, C, '(b - c)*(a - b - c)/(b**(2) + c**(2) - a*b - a*c)', ID="X_885", classes=["center"])
    central_line(model, X_2, X_650, 2, 650)
    central_line(model, X_523, X_885, 523, 885)
    X_2402 = intersect_lines(model, X_2, X_650, X_523, X_885, ID="X_2402", classes=["selected", "target"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center", "incident"])
    X_1024 = eval_trilinear_point(model, A, B, C, '((b - c)*(b + c - a)/(b**(2) + c**(2) - a*(b + c)))', ID="X_1024", classes=["center", "incident"])
    central_line(model, X_514, X_1024, 514, 1024, incident=True)
    return promote_point_to_top(model, X_2402)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2402 on the given reference triangle."""
    model = create_model('X_2402 = GIBERT-SIMSON TRANSFORM OF X_105')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02402(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02402.json"))
    write_center_svg(
        model_acute,
        here / "x-02402.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
