"""GEOMETOR construction model for X(534) = DIRECTION OF VECTOR AX + BX + CX, where X = X(19)."""

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
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00534(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(534) = DIRECTION OF VECTOR AX + BX + CX, where X = X(19) on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X(19)", classes=["center"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X(511)", classes=["center"])
    central_line(model, X_2, X_19, 2, 19)
    central_line(model, X_30, X_511, 30, 511)
    X_534 = intersect_lines(model, X_2, X_19, X_30, X_511, ID="X(534)", classes=["selected", "target"])
    return promote_point_to_top(model, X_534)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(534) on the given reference triangle."""
    model = create_model('X(534) = DIRECTION OF VECTOR AX + BX + CX, where X = X(19)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00534(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00534.json"))
    write_center_svg(
        model_acute,
        here / "x-00534.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
