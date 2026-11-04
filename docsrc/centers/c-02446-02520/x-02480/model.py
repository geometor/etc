"""GEOMETOR construction model for X_2480 = 2nd INTERSECTION(EULER LINE, STEINERCIRCUMELLIPSE)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    anticomplement,
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02480(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2480 = 2nd INTERSECTION(EULER LINE, STEINERCIRCUMELLIPSE) on reference triangle ABC."""
    X_2454 = eval_trilinear_point(model, A, B, C, '(b*c*(3*a**(2)*b*c*cos(B)*cos(C) - 4*( area )**(2) - 2*K))', ID="X_2454", classes=["center"])
    X_2480 = anticomplement(model, A, B, C, X_2454, ID="X_2480", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    return promote_point_to_top(model, X_2480)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2480 on the given reference triangle."""
    model = create_model('X_2480 = 2nd INTERSECTION(EULER LINE, STEINERCIRCUMELLIPSE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02480(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02480.json"))
    write_center_svg(
        model_acute,
        here / "x-02480.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
