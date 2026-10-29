"""GEOMETOR construction model for X(655) = TRILINEAR POLE OF LINE X(1)X(5)."""

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


def construct_x_00655(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(655) = TRILINEAR POLE OF LINE X(1)X(5) on reference triangle ABC."""
    X_654 = eval_trilinear_point(model, A, B, C, 'cos(A - B) - cos(C - A)', ID="X(654)", classes=["center"])
    X_655 = isogonal_conjugate(model, A, B, C, X_654, ID="X(655)", classes=["selected", "target"])
    X_59 = eval_trilinear_point(model, A, B, C, '1/(1 - cos(B - C))', ID="X(59)", classes=["center", "incident"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X(523)", classes=["center", "incident"])
    central_line(model, X_59, X_523, 59, 523, incident=True)
    X_80 = eval_trilinear_point(model, A, B, C, '1/(1 - 2*cos(A))', ID="X(80)", classes=["center", "incident"])
    X_516 = eval_trilinear_point(model, A, B, C, 'b*c*((a - b)*cot(C) + (a - c)*cot(B))', ID="X(516)", classes=["center", "incident"])
    central_line(model, X_80, X_516, 80, 516, incident=True)
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X(100)", classes=["center", "incident"])
    X_522 = eval_trilinear_point(model, A, B, C, '(cos(B) - cos(C))*(csc(A))', ID="X(522)", classes=["center", "incident"])
    central_line(model, X_100, X_522, 100, 522, incident=True)
    return promote_point_to_top(model, X_655)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(655) on the given reference triangle."""
    model = create_model('X(655) = TRILINEAR POLE OF LINE X(1)X(5)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00655(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00655.json"))
    write_center_svg(
        model_acute,
        here / "x-00655.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
