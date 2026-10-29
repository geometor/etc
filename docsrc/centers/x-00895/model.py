"""GEOMETOR construction model for X(895) = ISOGONAL CONJUGATE OF X(468)."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00895(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(895) = ISOGONAL CONJUGATE OF X(468) on reference triangle ABC."""
    X_468 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cot(B) + cot(C) - 2*cot(A))', ID="X(468)", classes=["center"])
    X_895 = isogonal_conjugate(model, A, B, C, X_468, ID="X(895)", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    central_line(model, X_6, X_110, 6, 110, incident=True)
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X(69)", classes=["center", "incident"])
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X(125)", classes=["center", "incident"])
    central_line(model, X_69, X_125, 69, 125, incident=True)
    X_66 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(4) + c**(4) - a**(4))', ID="X(66)", classes=["center", "incident"])
    X_193 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cot(B) + cot(C) - cot(A))', ID="X(193)", classes=["center", "incident"])
    central_line(model, X_66, X_193, 66, 193, incident=True)
    return promote_point_to_top(model, X_895)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(895) on the given reference triangle."""
    model = create_model('X(895) = ISOGONAL CONJUGATE OF X(468)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00895(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00895.json"))
    write_center_svg(
        model_acute,
        here / "x-00895.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
