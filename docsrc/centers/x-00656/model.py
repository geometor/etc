"""GEOMETOR construction model for X(656) = CROSSDIFFERENCE OF X(1) AND X(19)."""

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


def construct_x_00656(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(656) = CROSSDIFFERENCE OF X(1) AND X(19) on reference triangle ABC."""
    X_162 = eval_trilinear_point(model, A, B, C, '1/(sin(2*B) - sin(2*C))', ID="X(162)", classes=["center"])
    X_656 = isogonal_conjugate(model, A, B, C, X_162, ID="X(656)", classes=["selected", "target"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X(44)", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X(513)", classes=["center", "incident"])
    central_line(model, X_44, X_513, 44, 513, incident=True)
    X_240 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(A + omega )', ID="X(240)", classes=["center", "incident"])
    X_522 = eval_trilinear_point(model, A, B, C, '(cos(B) - cos(C))*(csc(A))', ID="X(522)", classes=["center", "incident"])
    central_line(model, X_240, X_522, 240, 522, incident=True)
    X_521 = eval_trilinear_point(model, A, B, C, '(sec(B) - sec(C))*(csc(A))', ID="X(521)", classes=["center", "incident"])
    X_810 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))', ID="X(810)", classes=["center", "incident"])
    central_line(model, X_521, X_810, 521, 810, incident=True)
    return promote_point_to_top(model, X_656)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(656) on the given reference triangle."""
    model = create_model('X(656) = CROSSDIFFERENCE OF X(1) AND X(19)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00656(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00656.json"))
    write_center_svg(
        model_acute,
        here / "x-00656.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
