"""GEOMETOR construction model for X_2856 = SM(X_98, X_100)."""

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


def construct_x_02856(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2856 = SM(X_98, X_100) on reference triangle ABC."""
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center"])
    X_325 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)', ID="X_325", classes=["center"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center"])
    X_693 = eval_trilinear_point(model, A, B, C, '(b - c)/a**(2)', ID="X_693", classes=["center"])
    central_line(model, X_100, X_325, 100, 325)
    central_line(model, X_98, X_693, 98, 693)
    X_2856 = intersect_lines(model, X_100, X_325, X_98, X_693, ID="X_2856", classes=["selected", "target"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    X_1959 = eval_trilinear_point(model, A, B, C, '(cot(A))**(2) - cot(B)*cot(C)', ID="X_1959", classes=["center", "incident"])
    central_line(model, X_101, X_1959, 101, 1959, incident=True)
    return promote_point_to_top(model, X_2856)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2856 on the given reference triangle."""
    model = create_model('X_2856 = SM(X_98, X_100)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02856(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02856.json"))
    write_center_svg(
        model_acute,
        here / "x-02856.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
