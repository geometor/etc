"""GEOMETOR construction model for X_3609 = 2nd MORLEY-GIBERT PERSPECTOR."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03609(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3609 = 2nd MORLEY-GIBERT PERSPECTOR on reference triangle ABC."""
    X_3609 = eval_trilinear_point(model, A, B, C, '(cos(A) + 2*cos(B)*cos(C) + 3*sin(A/3+ pi  /6) + 6*sin(B/3)*sin(C/3))', ID="X_3609", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_3272 = eval_trilinear_point(model, A, B, C, 'cos(B/3 - C/3)', ID="X_3272", classes=["center", "incident"])
    central_line(model, X_5, X_3272, 5, 3272, incident=True)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_3334 = eval_trilinear_point(model, A, B, C, 'cos(A) + 2*sin(B/3)*sin(C/3) + sin(A/3 + pi  /6)', ID="X_3334", classes=["center", "incident"])
    central_line(model, X_20, X_3334, 20, 3334, incident=True)
    X_631 = eval_trilinear_point(model, A, B, C, '2*cos(A) + cos(B)*cos(C)', ID="X_631", classes=["center", "incident"])
    X_3335 = eval_trilinear_point(model, A, B, C, '(cos(A) - 2*sin(B/3)*sin(C/3) - sin(A/3 + pi  /6))', ID="X_3335", classes=["center", "incident"])
    central_line(model, X_631, X_3335, 631, 3335, incident=True)
    return promote_point_to_top(model, X_3609)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3609 on the given reference triangle."""
    model = create_model('X_3609 = 2nd MORLEY-GIBERT PERSPECTOR')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03609(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03609.json"))
    write_center_svg(
        model_acute,
        here / "x-03609.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
