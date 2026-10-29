"""GEOMETOR construction model for X(513) = ISOGONAL CONJUGATE OF X(100)."""

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


def construct_x_00513(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(513) = ISOGONAL CONJUGATE OF X(100) on reference triangle ABC."""
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X(100)", classes=["center"])
    X_513 = isogonal_conjugate(model, A, B, C, X_100, ID="X(513)", classes=["selected", "target"])
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X(36)", classes=["center", "incident"])
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X(238)", classes=["center", "incident"])
    central_line(model, X_36, X_238, 36, 238, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X(511)", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    X_320 = eval_trilinear_point(model, A, B, C, '(1 - 2*cos(A))/a**(2)', ID="X(320)", classes=["center", "incident"])
    X_350 = eval_trilinear_point(model, A, B, C, '(a**(2) - b*c)*b**(2)*c**(2)', ID="X(350)", classes=["center", "incident"])
    central_line(model, X_320, X_350, 320, 350, incident=True)
    return promote_point_to_top(model, X_513)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(513) on the given reference triangle."""
    model = create_model('X(513) = ISOGONAL CONJUGATE OF X(100)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00513(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00513.json"))
    write_center_svg(
        model_acute,
        here / "x-00513.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
