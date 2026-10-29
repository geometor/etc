"""GEOMETOR construction model for X(191) = X(10)-CEVA CONJUGATE OF X(1)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00191(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(191) = X(10)-CEVA CONJUGATE OF X(1) on reference triangle ABC."""
    X_191 = eval_trilinear_point(model, A, B, C, '(b + c - a)*(b*c + c*a + a*b) + b**(3) + c**(3) - a**(3)', ID="X(191)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X(21)", classes=["center", "incident"])
    central_line(model, X_1, X_21, 1, 21, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X(46)", classes=["center", "incident"])
    central_line(model, X_9, X_46, 9, 46, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center", "incident"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X(40)", classes=["center", "incident"])
    central_line(model, X_30, X_40, 30, 40, incident=True)
    return promote_point_to_top(model, X_191)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(191) on the given reference triangle."""
    model = create_model('X(191) = X(10)-CEVA CONJUGATE OF X(1)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00191(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00191.json"))
    write_center_svg(
        model_acute,
        here / "x-00191.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
