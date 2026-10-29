"""GEOMETOR construction model for X(47) = X(110)-BETH CONJUGATE OF X(34)."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00047(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(47) = X(110)-BETH CONJUGATE OF X(34) on reference triangle ABC."""
    X_47 = eval_trilinear_point(model, A, B, C, 'cos(2*A)', ID="X(47)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X(21)", classes=["center", "incident"])
    central_line(model, X_1, X_21, 1, 21, incident=True)
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X(34)", classes=["center", "incident"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X(46)", classes=["center", "incident"])
    central_line(model, X_34, X_46, 34, 46, incident=True)
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X(33)", classes=["center", "incident"])
    X_90 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C) - cos(A))', ID="X(90)", classes=["center", "incident"])
    central_line(model, X_33, X_90, 33, 90, incident=True)
    return promote_point_to_top(model, X_47)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(47) on the given reference triangle."""
    model = create_model('X(47) = X(110)-BETH CONJUGATE OF X(34)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00047(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00047.json"))
    write_center_svg(
        model_acute,
        here / "x-00047.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
