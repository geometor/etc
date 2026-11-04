"""GEOMETOR construction model for X_2979 = CENTROID OF DUAL OF THE ORTHIC TRIANGLE."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_02979(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2979 = CENTROID OF DUAL OF THE ORTHIC TRIANGLE on reference triangle ABC."""
    X_568 = eval_trilinear_point(model, A, B, C, 'a*(3*R**(2)*(b**(2) + c**(2) - a**(2)) + a**(2)*b**(2) + a**(2)*c**(2) - b**(4) - c**(4))', ID="X_568", classes=["center"])
    X_549 = eval_trilinear_point(model, A, B, C, 'cos(B - C) + 4*cos(A)', ID="X_549", classes=["center"])
    X_2979 = reflection_in_point(model, X_568, X_549, ID="X_2979", classes=["selected", "target"], guide=False)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X_51", classes=["center", "incident"])
    central_line(model, X_2, X_51, 2, 51, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    central_line(model, X_3, X_54, 3, 54, incident=True)
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X_22", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_22, X_110, 22, 110, incident=True)
    return promote_point_to_top(model, X_2979)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2979 on the given reference triangle."""
    model = create_model('X_2979 = CENTROID OF DUAL OF THE ORTHIC TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02979(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02979.json"))
    write_center_svg(
        model_acute,
        here / "x-02979.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
