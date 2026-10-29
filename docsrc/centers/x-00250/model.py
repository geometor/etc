"""GEOMETOR construction model for X(250) = ISOGONAL CONJUGATE OF X(125)."""

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


def construct_x_00250(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(250) = ISOGONAL CONJUGATE OF X(125) on reference triangle ABC."""
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X(125)", classes=["center"])
    X_250 = isogonal_conjugate(model, A, B, C, X_125, ID="X(250)", classes=["selected", "target"])
    X_23 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X(23)", classes=["center", "incident"])
    X_232 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(A + omega )', ID="X(232)", classes=["center", "incident"])
    central_line(model, X_23, X_232, 23, 232, incident=True)
    X_186 = eval_trilinear_point(model, A, B, C, '4*cos(A) - sec(A)', ID="X(186)", classes=["center", "incident"])
    X_249 = eval_trilinear_point(model, A, B, C, '(csc(A))*(csc(B - C))**(2)', ID="X(249)", classes=["center", "incident"])
    central_line(model, X_186, X_249, 186, 249, incident=True)
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    X_520 = eval_trilinear_point(model, A, B, C, '(cos(A))*(sin(2*B) - sin(2*C))', ID="X(520)", classes=["center", "incident"])
    central_line(model, X_110, X_520, 110, 520, incident=True)
    return promote_point_to_top(model, X_250)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(250) on the given reference triangle."""
    model = create_model('X(250) = ISOGONAL CONJUGATE OF X(125)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00250(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00250.json"))
    write_center_svg(
        model_acute,
        here / "x-00250.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
