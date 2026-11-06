"""GEOMETOR construction model for X_3982 = X_3683com(INTOUCH TRIANGLE)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    gergonne_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03982(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3982 = X_3683com(INTOUCH TRIANGLE) on reference triangle ABC."""
    X_3982 = eval_barycentric_point(model, A, B, C, '((a + b - c)*(a - b + c)*(2*a + 3*b + 3*c))', ID="X_3982", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_2, X_7, 2, 7, incident=True)
    X_382 = eval_trilinear_point(model, A, B, C, 'cos(A) - 4*cos(B)*cos(C)', ID="X_382", classes=["center", "incident"])
    X_950 = eval_trilinear_point(model, A, B, C, 'b*c*(b + c - a)*(2*a**(3) + (b + c)*(a**(2) + (b - c)**(2)))', ID="X_950", classes=["center", "incident"])
    central_line(model, X_382, X_950, 382, 950, incident=True)
    X_546 = eval_trilinear_point(model, A, B, C, '3*cos(B - C) - 2*cos(A)', ID="X_546", classes=["center", "incident"])
    X_942 = eval_trilinear_point(model, A, B, C, '2*a*b*c + (b + c)*(a - b + c)*(a + b -c)', ID="X_942", classes=["center", "incident"])
    central_line(model, X_546, X_942, 546, 942, incident=True)
    return promote_point_to_top(model, X_3982)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3982 on the given reference triangle."""
    model = create_model('X_3982 = X_3683com(INTOUCH TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03982(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03982.json"))
    write_center_svg(
        model_acute,
        here / "x-03982.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
