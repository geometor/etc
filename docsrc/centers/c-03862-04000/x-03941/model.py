"""GEOMETOR construction model for X_3941 = X_3694com(TANGENTIAL TRIANGLE)."""

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


def construct_x_03941(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3941 = X_3694com(TANGENTIAL TRIANGLE) on reference triangle ABC."""
    X_3941 = eval_barycentric_point(model, A, B, C, '(a**(3)*(b**(2) + c**(2) - b*c - c*a - a*b))', ID="X_3941", classes=["selected", "target"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    central_line(model, X_31, X_48, 31, 48, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_1100 = eval_trilinear_point(model, A, B, C, '2*a + b + c', ID="X_1100", classes=["center", "incident"])
    central_line(model, X_55, X_1100, 55, 1100, incident=True)
    X_579 = eval_trilinear_point(model, A, B, C, '(a*(a**(2)*b + a**(2)*c + a*b*c - b**(3) - c**(3)))', ID="X_579", classes=["center", "incident"])
    X_674 = eval_trilinear_point(model, A, B, C, '(a*(b**(3) + c**(3) - a*(b**(2) + c**(2))))', ID="X_674", classes=["center", "incident"])
    central_line(model, X_579, X_674, 579, 674, incident=True)
    return promote_point_to_top(model, X_3941)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3941 on the given reference triangle."""
    model = create_model('X_3941 = X_3694com(TANGENTIAL TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03941(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03941.json"))
    write_center_svg(
        model_acute,
        here / "x-03941.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
