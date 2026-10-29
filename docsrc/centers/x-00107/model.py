"""GEOMETOR construction model for X(107) = Ψ(SYMMEDIAN POINT, ORTHOCENTER)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00107(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(107) = Ψ(SYMMEDIAN POINT, ORTHOCENTER) on reference triangle ABC."""
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X(107)", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X(74)", classes=["center", "incident"])
    central_line(model, X_4, X_74, 4, 74, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X(25)", classes=["center", "incident"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A + omega )', ID="X(98)", classes=["center", "incident"])
    central_line(model, X_25, X_98, 25, 98, incident=True)
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X(27)", classes=["center", "incident"])
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X(103)", classes=["center", "incident"])
    central_line(model, X_27, X_103, 27, 103, incident=True)
    return promote_point_to_top(model, X_107)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(107) on the given reference triangle."""
    model = create_model('X(107) = Ψ(SYMMEDIAN POINT, ORTHOCENTER)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00107(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00107.json"))
    write_center_svg(
        model_acute,
        here / "x-00107.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
