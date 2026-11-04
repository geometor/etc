"""GEOMETOR construction model for X_2978 = RADICAL CENTER OF {CIRCUMCIRCLE, BROCARD CIRCLE, CONWAY CIRCLE}."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02978(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2978 = RADICAL CENTER OF {CIRCUMCIRCLE, BROCARD CIRCLE, CONWAY CIRCLE} on reference triangle ABC."""
    X_785 = eval_trilinear_point(model, A, B, C, '(1/(a **(-4)*(b **(-2) - c **(-2)) + a **(-3)*(b **(-3) - c **(-3))))', ID="X_785", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_2978 = ceva_conjugate(model, A, B, C, X_785, X_6, ID="X_2978", classes=["selected", "target"])
    X_187 = eval_trilinear_point(model, A, B, C, 'a*(2*a**(2) - b**(2) - c**(2))', ID="X_187", classes=["center", "incident"])
    X_237 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A +  omega  )', ID="X_237", classes=["center", "incident"])
    central_line(model, X_187, X_237, 187, 237, incident=True)
    X_320 = eval_trilinear_point(model, A, B, C, '(1 - 2*cos(A))/a**(2)', ID="X_320", classes=["center", "incident"])
    X_350 = eval_trilinear_point(model, A, B, C, '(a**(2) - b*c)*b**(2)*c**(2)', ID="X_350", classes=["center", "incident"])
    central_line(model, X_320, X_350, 320, 350, incident=True)
    X_661 = eval_trilinear_point(model, A, B, C, 'cot(B) - cot(C)', ID="X_661", classes=["center", "incident"])
    X_788 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b**(3) - c**(3))', ID="X_788", classes=["center", "incident"])
    central_line(model, X_661, X_788, 661, 788, incident=True)
    return promote_point_to_top(model, X_2978)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2978 on the given reference triangle."""
    model = create_model('X_2978 = RADICAL CENTER OF {CIRCUMCIRCLE, BROCARD CIRCLE, CONWAY CIRCLE}')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02978(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02978.json"))
    write_center_svg(
        model_acute,
        here / "x-02978.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
