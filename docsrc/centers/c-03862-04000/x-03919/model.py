"""GEOMETOR construction model for X_3919 = X_381com[INVERSE(n(HEXYL TRIANGLE))]."""

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
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03919(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3919 = X_381com[INVERSE(n(HEXYL TRIANGLE))] on reference triangle ABC."""
    X_3919 = eval_barycentric_point(model, A, B, C, '(a*(b + c)*(2*b**(2) + 2*c**(2) - 2*a**(2) - 5*b*c))', ID="X_3919", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    central_line(model, X_10, X_12, 10, 12, incident=True)
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X_517", classes=["center", "incident"])
    X_549 = eval_trilinear_point(model, A, B, C, 'cos(B - C) + 4*cos(A)', ID="X_549", classes=["center", "incident"])
    central_line(model, X_517, X_549, 517, 549, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_1392 = eval_trilinear_point(model, A, B, C, '((a - b -c)/(3*a - 2*b - 2*c))', ID="X_1392", classes=["center", "incident"])
    central_line(model, X_1, X_1392, 1, 1392, incident=True)
    return promote_point_to_top(model, X_3919)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3919 on the given reference triangle."""
    model = create_model('X_3919 = X_381com[INVERSE(n(HEXYL TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03919(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03919.json"))
    write_center_svg(
        model_acute,
        here / "x-03919.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
