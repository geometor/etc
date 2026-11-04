"""GEOMETOR construction model for X_2756 = SR(X_106, X_108)."""

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


def construct_x_02756(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2756 = SR(X_106, X_108) on reference triangle ABC."""
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X_106", classes=["center"])
    X_521 = eval_trilinear_point(model, A, B, C, '(sec(B) - sec(C))*(csc(A))', ID="X_521", classes=["center"])
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center"])
    X_519 = eval_trilinear_point(model, A, B, C, '(2*a - b - c)/a', ID="X_519", classes=["center"])
    central_line(model, X_106, X_521, 106, 521)
    central_line(model, X_108, X_519, 108, 519)
    X_2756 = intersect_lines(model, X_106, X_521, X_108, X_519, ID="X_2756", classes=["selected", "target"])
    X_78 = eval_trilinear_point(model, A, B, C, '1/(1 - sec(A))', ID="X_78", classes=["center", "incident"])
    X_901 = eval_trilinear_point(model, A, B, C, 'a/((b - c)*(b + c - 2*a))', ID="X_901", classes=["center", "incident"])
    central_line(model, X_78, X_901, 78, 901, incident=True)
    return promote_point_to_top(model, X_2756)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2756 on the given reference triangle."""
    model = create_model('X_2756 = SR(X_106, X_108)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02756(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02756.json"))
    write_center_svg(
        model_acute,
        here / "x-02756.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
