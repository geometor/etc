"""GEOMETOR construction model for X_3792 = X_190com[INVERSE(nT(bc, c²))]."""

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
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03792(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3792 = X_190com[INVERSE(nT(bc, c²))] on reference triangle ABC."""
    X_3792 = eval_barycentric_point(model, A, B, C, '(a**(2)*(a**(2) - b**(2) - c**(2) + b*c)*(b**(2) + c**(2) + b*c))', ID="X_3792", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_674 = eval_trilinear_point(model, A, B, C, '(a*(b**(3) + c**(3) - a*(b**(2) + c**(2))))', ID="X_674", classes=["center", "incident"])
    central_line(model, X_1, X_674, 1, 674, incident=True)
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_238, X_511, 238, 511, incident=True)
    X_320 = eval_trilinear_point(model, A, B, C, '(1 - 2*cos(A))/a**(2)', ID="X_320", classes=["center", "incident"])
    X_758 = eval_trilinear_point(model, A, B, C, 'a**(0)*(b**(3) + c**(3)) - a**(2)*(b**(1) + c**(1))', ID="X_758", classes=["center", "incident"])
    central_line(model, X_320, X_758, 320, 758, incident=True)
    return promote_point_to_top(model, X_3792)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3792 on the given reference triangle."""
    model = create_model('X_3792 = X_190com[INVERSE(nT(bc, c²))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03792(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03792.json"))
    write_center_svg(
        model_acute,
        here / "x-03792.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
