"""GEOMETOR construction model for X_3888 = X_1086com[INVERSE(n(3rd EULER TRIANGLE))]."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03888(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3888 = X_1086com[INVERSE(n(3rd EULER TRIANGLE))] on reference triangle ABC."""
    X_3888 = eval_barycentric_point(model, A, B, C, '(a*(a - b)*(a - c)*(b**(2) + c**(2) - b*c))', ID="X_3888", classes=["selected", "target"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    central_line(model, X_100, X_109, 100, 109, incident=True)
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X_190", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    central_line(model, X_190, X_513, 190, 513, incident=True)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    X_815 = eval_trilinear_point(model, A, B, C, '(1/(a **(-2)*(b**(2) - c**(2)) + a**(1)*(b **(-1) - c **(-1))))', ID="X_815", classes=["center", "incident"])
    central_line(model, X_99, X_815, 99, 815, incident=True)
    return promote_point_to_top(model, X_3888)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3888 on the given reference triangle."""
    model = create_model('X_3888 = X_1086com[INVERSE(n(3rd EULER TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03888(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03888.json"))
    write_center_svg(
        model_acute,
        here / "x-03888.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
