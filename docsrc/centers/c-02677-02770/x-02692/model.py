"""GEOMETOR construction model for X_2692 = SR(X_74, X_106)."""

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


def construct_x_02692(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2692 = SR(X_74, X_106) on reference triangle ABC."""
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center"])
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X_106", classes=["center"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center"])
    X_519 = eval_trilinear_point(model, A, B, C, '(2*a - b - c)/a', ID="X_519", classes=["center"])
    central_line(model, X_30, X_106, 30, 106)
    central_line(model, X_74, X_519, 74, 519)
    X_2692 = intersect_lines(model, X_30, X_106, X_74, X_519, ID="X_2692", classes=["selected", "target"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center", "incident"])
    X_1293 = eval_trilinear_point(model, A, B, C, '(a/((b - c)*(3*a - b - c)))', ID="X_1293", classes=["center", "incident"])
    central_line(model, X_523, X_1293, 523, 1293, incident=True)
    return promote_point_to_top(model, X_2692)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2692 on the given reference triangle."""
    model = create_model('X_2692 = SR(X_74, X_106)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02692(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02692.json"))
    write_center_svg(
        model_acute,
        here / "x-02692.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
