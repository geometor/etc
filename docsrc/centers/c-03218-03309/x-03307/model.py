"""GEOMETOR construction model for X_3307 = ISOGONAL CONJUGATE OF X_1381."""

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


def construct_x_03307(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3307 = ISOGONAL CONJUGATE OF X_1381 on reference triangle ABC."""
    X_1381 = eval_trilinear_point(model, A, B, C, '(r + ( OI  - R)*cos(A))', ID="X_1381", classes=["center"])
    X_3307 = isogonal_conjugate(model, A, B, C, X_1381, ID="X_3307", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    central_line(model, X_100, X_1381, 100, 1381, incident=True)
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center", "incident"])
    X_1382 = eval_trilinear_point(model, A, B, C, '(r - ( OI  + R)*cos(A))', ID="X_1382", classes=["center", "incident"])
    central_line(model, X_104, X_1382, 104, 1382, incident=True)
    return promote_point_to_top(model, X_3307)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3307 on the given reference triangle."""
    model = create_model('X_3307 = ISOGONAL CONJUGATE OF X_1381')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03307(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03307.json"))
    write_center_svg(
        model_acute,
        here / "x-03307.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
