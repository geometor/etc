"""GEOMETOR construction model for X_3326 = INCIRCLE TRANSFORM T(X_909)."""

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
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_03326(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3326 = INCIRCLE TRANSFORM T(X_909) on reference triangle ABC."""
    X_3319 = eval_barycentric_point(model, A, B, C, '((2*a**(4) - 2*a**(3)*(b + c) - a**(2)*(b**(2) - 4*b*c + c**(2)) + 2*a*(b + c)*(b - c)**(2) - (b**(2) - c**(2))**(2))**(2)/(b + c - a))', ID="X_3319", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_3326 = reflection_in_point(model, X_3319, X_1, ID="X_3326", classes=["selected", "target"], guide=False)
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_1354 = point_from_barycentrics(model, A, B, C, 0.14777719, 0.075909331, 0.77631348, ID="X_1354", classes=["center", "incident"])
    central_line(model, X_36, X_1354, 36, 1354, incident=True)
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    X_1364 = eval_trilinear_point(model, A, B, C, 'csc(A)*tan(A/2) / (sec(B) - sec(C))', ID="X_1364", classes=["center", "incident"])
    central_line(model, X_513, X_1364, 513, 1364, incident=True)
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X_517", classes=["center", "incident"])
    X_1361 = point_from_barycentrics(model, A, B, C, 0.19480519, 0.041558442, 0.76363636, ID="X_1361", classes=["center", "incident"])
    central_line(model, X_517, X_1361, 517, 1361, incident=True)
    return promote_point_to_top(model, X_3326)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3326 on the given reference triangle."""
    model = create_model('X_3326 = INCIRCLE TRANSFORM T(X_909)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03326(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03326.json"))
    write_center_svg(
        model_acute,
        here / "x-03326.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
