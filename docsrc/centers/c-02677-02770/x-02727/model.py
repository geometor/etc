"""GEOMETOR construction model for X_2727 = SR(X_101, X_107)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02727(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2727 = SR(X_101, X_107) on reference triangle ABC."""
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center"])
    X_520 = eval_trilinear_point(model, A, B, C, '(cos(A))*(sin(2*B) - sin(2*C))', ID="X_520", classes=["center"])
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X_107", classes=["center"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center"])
    central_line(model, X_101, X_520, 101, 520)
    central_line(model, X_107, X_514, 107, 514)
    X_2727 = intersect_lines(model, X_101, X_520, X_107, X_514, ID="X_2727", classes=["selected", "target"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center", "incident"])
    X_1459 = eval_trilinear_point(model, A, B, C, '(b - c)*cos(A)', ID="X_1459", classes=["center", "incident"])
    central_line(model, X_112, X_1459, 112, 1459, incident=True)
    return promote_point_to_top(model, X_2727)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2727 on the given reference triangle."""
    model = create_model('X_2727 = SR(X_101, X_107)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02727(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02727.json"))
    write_center_svg(
        model_acute,
        here / "x-02727.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
