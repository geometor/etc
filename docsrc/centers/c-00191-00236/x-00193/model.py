"""GEOMETOR construction model for X_193 = X_4-CEVA CONJUGATE OF X_2."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00193(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_193 = X_4-CEVA CONJUGATE OF X_2 on reference triangle ABC."""
    X_193 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cot(B) + cot(C) - cot(A))', ID="X_193", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_23 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X_23", classes=["center", "incident"])
    X_159 = eval_trilinear_point(model, A, B, C, '(a*((a**(2) + b**(2) + c**(2))*sin(2*A) + (c**(2) - b**(2) - a**(2))*sin(2*B) + (b**(2) - c**(2) - a**(2))*sin(2*C)))', ID="X_159", classes=["center", "incident"])
    central_line(model, X_23, X_159, 23, 159, incident=True)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_185 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 - cos(A)*cos(B - C))', ID="X_185", classes=["center", "incident"])
    central_line(model, X_20, X_185, 20, 185, incident=True)
    return promote_point_to_top(model, X_193)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_193 on the given reference triangle."""
    model = create_model('X_193 = X_4-CEVA CONJUGATE OF X_2')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00193(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00193.json"))
    write_center_svg(
        model_acute,
        here / "x-00193.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
