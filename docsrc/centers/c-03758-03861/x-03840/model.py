"""GEOMETOR construction model for X_3840 = X_3210com(3rd EULER TRIANGLE)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    complement,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03840(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3840 = X_3210com(3rd EULER TRIANGLE) on reference triangle ABC."""
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center"])
    X_3840 = complement(model, A, B, C, X_43, ID="X_3840", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)
    X_244 = eval_trilinear_point(model, A, B, C, '(b - c)**(2)', ID="X_244", classes=["center", "incident"])
    X_321 = eval_trilinear_point(model, A, B, C, '(b + c)*b**(2)*c**(2)', ID="X_321", classes=["center", "incident"])
    central_line(model, X_244, X_321, 244, 321, incident=True)
    X_312 = eval_trilinear_point(model, A, B, C, '(b + c - a)*b**(2)*c**(2)', ID="X_312", classes=["center", "incident"])
    X_726 = eval_trilinear_point(model, A, B, C, '(a **(-3)*(b **(-1) + c **(-1)) - a **(-2)*(b **(-2) + c **(-2)))', ID="X_726", classes=["center", "incident"])
    central_line(model, X_312, X_726, 312, 726, incident=True)
    return promote_point_to_top(model, X_3840)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3840 on the given reference triangle."""
    model = create_model('X_3840 = X_3210com(3rd EULER TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03840(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03840.json"))
    write_center_svg(
        model_acute,
        here / "x-03840.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
