"""GEOMETOR construction model for X(396) = MIDPOINT OF X(13) AND X(15)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nine_point_center_of,
    promote_point_to_top,
    reflection_in_point,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00396(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(396) = MIDPOINT OF X(13) AND X(15) on reference triangle ABC."""
    X_395 = eval_trilinear_point(model, A, B, C, 'cos(B - C) + 2*cos(A + pi /3)', ID="X(395)", classes=["center"])
    X_230 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*(2*a**(2) - b**(2) - c**(2)) + (b**(2) - c**(2))**(2))', ID="X(230)", classes=["center"])
    X_396 = reflection_in_point(model, X_395, X_230, ID="X(396)", classes=["selected", "target"], guide=False)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center", "incident"])
    X_14 = eval_trilinear_point(model, A, B, C, 'csc(A - pi /3)', ID="X(14)", classes=["center", "incident"])
    central_line(model, X_5, X_14, 5, 14, incident=True)
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A + pi /3)', ID="X(13)", classes=["center", "incident"])
    X_15 = eval_trilinear_point(model, A, B, C, 'sin(A + pi /3)', ID="X(15)", classes=["center", "incident"])
    central_line(model, X_13, X_15, 13, 15, incident=True)
    return promote_point_to_top(model, X_396)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(396) on the given reference triangle."""
    model = create_model('X(396) = MIDPOINT OF X(13) AND X(15)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00396(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00396.json"))
    write_center_svg(
        model_acute,
        here / "x-00396.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
