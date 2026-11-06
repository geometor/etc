"""GEOMETOR construction model for X_3253 = INTERSECTION OF X_6X_190 AND X_238X_874."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03253(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3253 = INTERSECTION OF X_6X_190 AND X_238X_874 on reference triangle ABC."""
    X_3253 = eval_trilinear_point(model, A, B, C, '(b*c*(a**(2) - b*c)/(b**(2)*c - b**(2)*a + c**(2)*b - c**(2)*a))', ID="X_3253", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X_190", classes=["center", "incident"])
    central_line(model, X_6, X_190, 6, 190, incident=True)
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center", "incident"])
    X_874 = point_from_barycentrics(model, A, B, C, 4.4210526, 0.10835913, -3.5294118, ID="X_874", classes=["center", "incident"])
    central_line(model, X_238, X_874, 238, 874, incident=True)
    X_727 = eval_trilinear_point(model, A, B, C, '(1/(a **(-3)*(b **(-1) + c **(-1)) - a **(-2)*(b **(-2) + c **(-2))))', ID="X_727", classes=["center", "incident"])
    X_789 = eval_trilinear_point(model, A, B, C, 'a **(- 2)/(b**(3) - c**(3))', ID="X_789", classes=["center", "incident"])
    central_line(model, X_727, X_789, 727, 789, incident=True)
    return promote_point_to_top(model, X_3253)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3253 on the given reference triangle."""
    model = create_model('X_3253 = INTERSECTION OF X_6X_190 AND X_238X_874')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03253(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03253.json"))
    write_center_svg(
        model_acute,
        here / "x-03253.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
