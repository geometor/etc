"""GEOMETOR construction model for X(520) = ISOGONAL CONJUGATE OF X(107)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00520(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(520) = ISOGONAL CONJUGATE OF X(107) on reference triangle ABC."""
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X(107)", classes=["center"])
    X_520 = isogonal_conjugate(model, A, B, C, X_107, ID="X(520)", classes=["selected", "target"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    X_250 = eval_trilinear_point(model, A, B, C, '(sec(A))*(csc(B - C))**(2)', ID="X(250)", classes=["center", "incident"])
    central_line(model, X_110, X_250, 110, 250, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X(511)", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X(69)", classes=["center", "incident"])
    X_879 = eval_barycentric_point(model, A, B, C, '(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))/(b**(4) + c**(4) - a**(2)*b**(2) - a**(2)*c**(2))', ID="X(879)", classes=["center", "incident"])
    central_line(model, X_69, X_879, 69, 879, incident=True)
    return promote_point_to_top(model, X_520)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(520) on the given reference triangle."""
    model = create_model('X(520) = ISOGONAL CONJUGATE OF X(107)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00520(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00520.json"))
    write_center_svg(
        model_acute,
        here / "x-00520.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
