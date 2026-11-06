"""GEOMETOR construction model for X_3202 = X_54-CEVA CONJUGATE OF X_32."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03202(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3202 = X_54-CEVA CONJUGATE OF X_32 on reference triangle ABC."""
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center"])
    X_3202 = ceva_conjugate(model, A, B, C, X_54, X_32, ID="X_3202", classes=["selected", "target"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_76, X_110, 76, 110, incident=True)
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    central_line(model, X_39, X_184, 39, 184, incident=True)
    X_26 = eval_trilinear_point(model, A, B, C, 'a*(b**(2)*cos(2*B) + c**(2)*cos(2*C) - a**(2)*cos(2*A))', ID="X_26", classes=["center", "incident"])
    X_206 = eval_trilinear_point(model, A, B, C, 'a**(3)*(b**(4) + c**(4) - a**(4))', ID="X_206", classes=["center", "incident"])
    central_line(model, X_26, X_206, 26, 206, incident=True)
    return promote_point_to_top(model, X_3202)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3202 on the given reference triangle."""
    model = create_model('X_3202 = X_54-CEVA CONJUGATE OF X_32')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03202(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03202.json"))
    write_center_svg(
        model_acute,
        here / "x-03202.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
