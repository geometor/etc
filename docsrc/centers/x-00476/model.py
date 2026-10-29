"""GEOMETOR construction model for X(476) = TIXIER POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00476(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(476) = TIXIER POINT on reference triangle ABC."""
    X_476 = eval_trilinear_point(model, A, B, C, '1/((1 + 2*cos(2*A))*sin(B - C))', ID="X(476)", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center", "incident"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X(74)", classes=["center", "incident"])
    central_line(model, X_30, X_74, 30, 74, incident=True)
    X_23 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X(23)", classes=["center", "incident"])
    X_94 = eval_trilinear_point(model, A, B, C, 'csc(3*A)', ID="X(94)", classes=["center", "incident"])
    central_line(model, X_23, X_94, 23, 94, incident=True)
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X(111)", classes=["center", "incident"])
    X_230 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*(2*a**(2) - b**(2) - c**(2)) + (b**(2) - c**(2))**(2))', ID="X(230)", classes=["center", "incident"])
    central_line(model, X_111, X_230, 111, 230, incident=True)
    return promote_point_to_top(model, X_476)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(476) on the given reference triangle."""
    model = create_model('X(476) = TIXIER POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00476(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00476.json"))
    write_center_svg(
        model_acute,
        here / "x-00476.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
