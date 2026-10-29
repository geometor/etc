"""GEOMETOR construction model for X(512) = ISOGONAL CONJUGATE OF X(99)."""

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


def construct_x_00512(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(512) = ISOGONAL CONJUGATE OF X(99) on reference triangle ABC."""
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center"])
    X_512 = isogonal_conjugate(model, A, B, C, X_99, ID="X(512)", classes=["selected", "target"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    X_249 = eval_trilinear_point(model, A, B, C, '(csc(A))*(csc(B - C))**(2)', ID="X(249)", classes=["center", "incident"])
    central_line(model, X_110, X_249, 110, 249, incident=True)
    X_187 = eval_trilinear_point(model, A, B, C, 'a*(2*a**(2) - b**(2) - c**(2))', ID="X(187)", classes=["center", "incident"])
    X_237 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A + omega )', ID="X(237)", classes=["center", "incident"])
    central_line(model, X_187, X_237, 187, 237, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X(511)", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    return promote_point_to_top(model, X_512)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(512) on the given reference triangle."""
    model = create_model('X(512) = ISOGONAL CONJUGATE OF X(99)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00512(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00512.json"))
    write_center_svg(
        model_acute,
        here / "x-00512.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
