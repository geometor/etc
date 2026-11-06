"""GEOMETOR construction model for X_3922 = X_3090com[INVERSE(n(HEXYL TRIANGLE))]."""

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
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03922(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3922 = X_3090com[INVERSE(n(HEXYL TRIANGLE))] on reference triangle ABC."""
    X_3922 = eval_barycentric_point(model, A, B, C, '(a*(b + c)*(3*b**(2) + 3*c**(2) - 3*a**(2) - 10*b*c))', ID="X_3922", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    central_line(model, X_10, X_12, 10, 12, incident=True)
    X_145 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a - b - c)', ID="X_145", classes=["center", "incident"])
    X_354 = eval_trilinear_point(model, A, B, C, '(b - c)**(2) - a*b - a*c', ID="X_354", classes=["center", "incident"])
    central_line(model, X_145, X_354, 145, 354, incident=True)
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X_517", classes=["center", "incident"])
    X_3526 = eval_trilinear_point(model, A, B, C, '(5*cos(A) + 4*cos(B)*cos(C))', ID="X_3526", classes=["center", "incident"])
    central_line(model, X_517, X_3526, 517, 3526, incident=True)
    return promote_point_to_top(model, X_3922)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3922 on the given reference triangle."""
    model = create_model('X_3922 = X_3090com[INVERSE(n(HEXYL TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03922(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03922.json"))
    write_center_svg(
        model_acute,
        here / "x-03922.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
