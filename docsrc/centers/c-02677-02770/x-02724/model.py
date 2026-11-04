"""GEOMETOR construction model for X_2724 = SR(X_101, X_103)."""

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


def construct_x_02724(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2724 = SR(X_101, X_103) on reference triangle ABC."""
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center"])
    X_516 = eval_trilinear_point(model, A, B, C, 'b*c*((a - b)*cot(C) + (a - c)*cot(B))', ID="X_516", classes=["center"])
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X_103", classes=["center"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center"])
    central_line(model, X_101, X_516, 101, 516)
    central_line(model, X_103, X_514, 103, 514)
    X_2724 = intersect_lines(model, X_101, X_516, X_103, X_514, ID="X_2724", classes=["selected", "target"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    X_813 = eval_trilinear_point(model, A, B, C, '1/(a**(-2)*(b**(1) - c**(1)) + a**(0)*(b**(-1) - c **(-1)))', ID="X_813", classes=["center", "incident"])
    central_line(model, X_40, X_813, 40, 813, incident=True)
    return promote_point_to_top(model, X_2724)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2724 on the given reference triangle."""
    model = create_model('X_2724 = SR(X_101, X_103)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02724(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02724.json"))
    write_center_svg(
        model_acute,
        here / "x-02724.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
