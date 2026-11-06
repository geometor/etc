"""GEOMETOR construction model for X_3904 = X_3716com[INVERSE(n(4th EULER TRIANGLE))]."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isotomic_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03904(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3904 = X_3716com[INVERSE(n(4th EULER TRIANGLE))] on reference triangle ABC."""
    X_655 = eval_trilinear_point(model, A, B, C, '1/(cos(A - B) - cos(C- A))', ID="X_655", classes=["center"])
    X_3904 = isotomic_conjugate(model, A, B, C, X_655, ID="X_3904", classes=["selected", "target"])
    X_323 = eval_trilinear_point(model, A, B, C, 'sin(3*A)*(csc(A))**(2)', ID="X_323", classes=["center", "incident"])
    X_401 = eval_trilinear_point(model, A, B, C, '(sin(2*B)*sin(2*C) - (sin(2*A))**(2))*(csc(A))', ID="X_401", classes=["center", "incident"])
    central_line(model, X_323, X_401, 323, 401, incident=True)
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X_190", classes=["center", "incident"])
    X_644 = eval_trilinear_point(model, A, B, C, '((b + c - a)/(b - c))', ID="X_644", classes=["center", "incident"])
    central_line(model, X_190, X_644, 190, 644, incident=True)
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center", "incident"])
    X_661 = eval_trilinear_point(model, A, B, C, 'cot(B) - cot(C)', ID="X_661", classes=["center", "incident"])
    central_line(model, X_514, X_661, 514, 661, incident=True)
    return promote_point_to_top(model, X_3904)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3904 on the given reference triangle."""
    model = create_model('X_3904 = X_3716com[INVERSE(n(4th EULER TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03904(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03904.json"))
    write_center_svg(
        model_acute,
        here / "x-03904.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
