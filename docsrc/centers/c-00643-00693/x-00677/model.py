"""GEOMETOR construction model for X_677 = TRILINEAR POLE OF LINE X_3X_101."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00677(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_677 = TRILINEAR POLE OF LINE X_3X_101 on reference triangle ABC."""
    X_676 = eval_trilinear_point(model, A, B, C, '(b*c*(b - c)*(b**(3) + c**(3) - 2*a**(3) + (b + c)*(a**(2) - b*c)))', ID="X_676", classes=["center"])
    X_677 = isogonal_conjugate(model, A, B, C, X_676, ID="X_677", classes=["selected", "target"])
    X_521 = eval_trilinear_point(model, A, B, C, '(sec(B) - sec(C))*(csc(A))', ID="X_521", classes=["center", "incident"])
    X_651 = eval_trilinear_point(model, A, B, C, '1/(cos(B) - cos(C))', ID="X_651", classes=["center", "incident"])
    central_line(model, X_521, X_651, 521, 651, incident=True)
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X_103", classes=["center", "incident"])
    X_901 = eval_trilinear_point(model, A, B, C, 'a/((b - c)*(b + c - 2*a))', ID="X_901", classes=["center", "incident"])
    central_line(model, X_103, X_901, 103, 901, incident=True)
    X_59 = eval_trilinear_point(model, A, B, C, '1/(1 - cos(B - C))', ID="X_59", classes=["center", "incident"])
    X_1813 = eval_trilinear_point(model, A, B, C, '(cos(A))/(cos(B) - cos(C))', ID="X_1813", classes=["center", "incident"])
    central_line(model, X_59, X_1813, 59, 1813, incident=True)
    return promote_point_to_top(model, X_677)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_677 on the given reference triangle."""
    model = create_model('X_677 = TRILINEAR POLE OF LINE X_3X_101')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00677(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00677.json"))
    write_center_svg(
        model_acute,
        here / "x-00677.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
