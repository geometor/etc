"""GEOMETOR construction model for X_1963 = CROSSSUM OF PU(32)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01963(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1963 = CROSSSUM OF PU(32) on reference triangle ABC."""
    X_1929 = point_from_barycentrics(model, A, B, C, 0.02276867, 1.010929, -0.033697632, ID="X_1929", classes=["center"])
    X_1931 = eval_trilinear_point(model, A, B, C, '(((b + c)**(2) - (a + b)*(a + c))/(b + c))', ID="X_1931", classes=["center"])
    X_1963 = ceva_conjugate(model, A, B, C, X_1929, X_1931, ID="X_1963", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_757 = eval_trilinear_point(model, A, B, C, '(b + c) **(-2)', ID="X_757", classes=["center", "incident"])
    central_line(model, X_37, X_757, 37, 757, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_1326 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) + c**(2) - a**(2) + b*c - a*b - a*c)/(b + c))', ID="X_1326", classes=["center", "incident"])
    central_line(model, X_1, X_1326, 1, 1326, incident=True)
    return promote_point_to_top(model, X_1963)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1963 on the given reference triangle."""
    model = create_model('X_1963 = CROSSSUM OF PU(32)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01963(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01963.json"))
    write_center_svg(
        model_acute,
        here / "x-01963.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
