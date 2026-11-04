"""GEOMETOR construction model for X_540 = DIRECTION OF VECTOR AX + BX + CX, where X = X_58."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00540(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_540 = DIRECTION OF VECTOR AX + BX + CX, where X = X_58 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X_511", classes=["center"])
    central_line(model, X_2, X_58, 2, 58)
    central_line(model, X_30, X_511, 30, 511)
    X_540 = intersect_lines(model, X_2, X_58, X_30, X_511, ID="X_540", classes=["selected", "target"])
    X_340 = eval_trilinear_point(model, A, B, C, 'sec(A)*sin(3*A)*(csc(A))**(3)', ID="X_340", classes=["center", "incident"])
    X_447 = point_from_barycentrics(model, A, B, C, -0.43131573, -0.14127643, 1.5725922, ID="X_447", classes=["center", "incident"])
    central_line(model, X_340, X_447, 340, 447, incident=True)
    return promote_point_to_top(model, X_540)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_540 on the given reference triangle."""
    model = create_model('X_540 = DIRECTION OF VECTOR AX + BX + CX, where X = X_58')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00540(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00540.json"))
    write_center_svg(
        model_acute,
        here / "x-00540.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
