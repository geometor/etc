"""GEOMETOR construction model for X(59) = ISOGONAL CONJUGATE OF X(11)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00059(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(59) = ISOGONAL CONJUGATE OF X(11) on reference triangle ABC."""
    X_11 = feuerbach_point_of(model, A, B, C, ID="X(11)", classes=["center"])
    X_59 = isogonal_conjugate(model, A, B, C, X_11, ID="X(59)", classes=["selected", "target"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X(100)", classes=["center", "incident"])
    X_521 = eval_trilinear_point(model, A, B, C, '(sec(B) - sec(C))*(csc(A))', ID="X(521)", classes=["center", "incident"])
    central_line(model, X_100, X_521, 100, 521, incident=True)
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center", "incident"])
    X_657 = eval_trilinear_point(model, A, B, C, '(1 + cos(A))*(cos(B) - cos(C))', ID="X(657)", classes=["center", "incident"])
    central_line(model, X_101, X_657, 101, 657, incident=True)
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X(109)", classes=["center", "incident"])
    X_901 = eval_trilinear_point(model, A, B, C, 'a/((b - c)*(b + c - 2*a))', ID="X(901)", classes=["center", "incident"])
    central_line(model, X_109, X_901, 109, 901, incident=True)
    return promote_point_to_top(model, X_59)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(59) on the given reference triangle."""
    model = create_model('X(59) = ISOGONAL CONJUGATE OF X(11)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00059(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00059.json"))
    write_center_svg(
        model_acute,
        here / "x-00059.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
