"""GEOMETOR construction model for X(522) = ISOGONAL CONJUGATE OF X(109)."""

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
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00522(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(522) = ISOGONAL CONJUGATE OF X(109) on reference triangle ABC."""
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X(109)", classes=["center"])
    X_522 = isogonal_conjugate(model, A, B, C, X_109, ID="X(522)", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X(511)", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    X_657 = eval_trilinear_point(model, A, B, C, '(1 + cos(A))*(cos(B) - cos(C))', ID="X(657)", classes=["center", "incident"])
    central_line(model, X_9, X_657, 9, 657, incident=True)
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X(100)", classes=["center", "incident"])
    X_655 = eval_trilinear_point(model, A, B, C, '1/(cos(A - B) - cos(C- A))', ID="X(655)", classes=["center", "incident"])
    central_line(model, X_100, X_655, 100, 655, incident=True)
    return promote_point_to_top(model, X_522)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(522) on the given reference triangle."""
    model = create_model('X(522) = ISOGONAL CONJUGATE OF X(109)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00522(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00522.json"))
    write_center_svg(
        model_acute,
        here / "x-00522.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
