"""GEOMETOR construction model for X_3521 = ISOGONAL CONJUGATE OF X_3520."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03521(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3521 = ISOGONAL CONJUGATE OF X_3520 on reference triangle ABC."""
    X_3521 = eval_trilinear_point(model, A, B, C, '1/(4*cos(A) + sec(A))', ID="X_3521", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center", "incident"])
    central_line(model, X_5, X_74, 5, 74, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    central_line(model, X_30, X_54, 30, 54, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_382 = eval_trilinear_point(model, A, B, C, 'cos(A) - 4*cos(B)*cos(C)', ID="X_382", classes=["center", "incident"])
    central_line(model, X_6, X_382, 6, 382, incident=True)
    return promote_point_to_top(model, X_3521)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3521 on the given reference triangle."""
    model = create_model('X_3521 = ISOGONAL CONJUGATE OF X_3520')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03521(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03521.json"))
    write_center_svg(
        model_acute,
        here / "x-03521.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
