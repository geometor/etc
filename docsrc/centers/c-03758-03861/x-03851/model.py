"""GEOMETOR construction model for X_3851 = X_3523com(EULER TRIANGLE)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    complement,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03851(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3851 = X_3523com(EULER TRIANGLE) on reference triangle ABC."""
    X_3528 = eval_trilinear_point(model, A, B, C, '(5*cos(A) - sin(B)*sin(C))', ID="X_3528", classes=["center"])
    X_3851 = complement(model, A, B, C, X_3528, ID="X_3851", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_355 = eval_trilinear_point(model, A, B, C, 'a*cos(A) - (b + c)*cos(B - C)', ID="X_355", classes=["center", "incident"])
    X_3244 = eval_trilinear_point(model, A, B, C, 'b*c*(4*a - b - c)', ID="X_3244", classes=["center", "incident"])
    central_line(model, X_355, X_3244, 355, 3244, incident=True)
    X_946 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(3)*(b + c) + (b - c)**(2)*(a**(2) - a*b - a*c - b**(2) - c**(2) - 2*b*c))', ID="X_946", classes=["center", "incident"])
    X_3626 = eval_trilinear_point(model, A, B, C, 'b*c*(2*a - 3*b - 3*c)', ID="X_3626", classes=["center", "incident"])
    central_line(model, X_946, X_3626, 946, 3626, incident=True)
    return promote_point_to_top(model, X_3851)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3851 on the given reference triangle."""
    model = create_model('X_3851 = X_3523com(EULER TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03851(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03851.json"))
    write_center_svg(
        model_acute,
        here / "x-03851.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
