"""GEOMETOR construction model for X(525) = ISOGONAL CONJUGATE OF X(112)."""

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


def construct_x_00525(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(525) = ISOGONAL CONJUGATE OF X(112) on reference triangle ABC."""
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X(112)", classes=["center"])
    X_525 = isogonal_conjugate(model, A, B, C, X_112, ID="X(525)", classes=["selected", "target"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    X_249 = eval_trilinear_point(model, A, B, C, '(csc(A))*(csc(B - C))**(2)', ID="X(249)", classes=["center", "incident"])
    central_line(model, X_99, X_249, 99, 249, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X(511)", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    X_323 = eval_trilinear_point(model, A, B, C, '4*sin(A) - 3*csc(A)', ID="X(323)", classes=["center", "incident"])
    X_401 = eval_trilinear_point(model, A, B, C, '(sin(2*B)*sin(2*C) - (sin(2*A))**(2))*(csc(A))', ID="X(401)", classes=["center", "incident"])
    central_line(model, X_323, X_401, 323, 401, incident=True)
    return promote_point_to_top(model, X_525)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(525) on the given reference triangle."""
    model = create_model('X(525) = ISOGONAL CONJUGATE OF X(112)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00525(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00525.json"))
    write_center_svg(
        model_acute,
        here / "x-00525.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
