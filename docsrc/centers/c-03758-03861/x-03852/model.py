"""GEOMETOR construction model for X_3852 = X_732com(2nd EULER TRIANGLE)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03852(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3852 = X_732com(2nd EULER TRIANGLE) on reference triangle ABC."""
    X_3852 = eval_barycentric_point(model, A, B, C, '(a**(4)*(b**(8) + c**(8) - a**(4)*b**(4) - a**(4)*c**(4)))', ID="X_3852", classes=["selected", "target"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    X_206 = eval_trilinear_point(model, A, B, C, 'a**(3)*(b**(4) + c**(4) - a**(4))', ID="X_206", classes=["center", "incident"])
    central_line(model, X_32, X_206, 32, 206, incident=True)
    X_66 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(4) + c**(4) - a**(4))', ID="X_66", classes=["center", "incident"])
    X_315 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(4) + c**(4) - a**(4))', ID="X_315", classes=["center", "incident"])
    central_line(model, X_66, X_315, 66, 315, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    return promote_point_to_top(model, X_3852)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3852 on the given reference triangle."""
    model = create_model('X_3852 = X_732com(2nd EULER TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03852(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03852.json"))
    write_center_svg(
        model_acute,
        here / "x-03852.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
