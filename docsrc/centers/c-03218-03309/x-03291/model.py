"""GEOMETOR construction model for X_3291 = INTERSECTION OF LINES X_2X_39 AND X_230X_231."""

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
    midpoint,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03291(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3291 = INTERSECTION OF LINES X_2X_39 AND X_230X_231 on reference triangle ABC."""
    X_3124 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))**(2)', ID="X_3124", classes=["center"])
    X_3231 = eval_trilinear_point(model, A, B, C, '(a*(2*b**(2)*c**(2) - a**(2)*b**(2) - a**(2)*c**(2)))', ID="X_3231", classes=["center"])
    X_3291 = midpoint(model, X_3124, X_3231, ID="X_3291", classes=["selected", "target"], guide=False)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    central_line(model, X_2, X_39, 2, 39, incident=True)
    X_23 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X_23", classes=["center", "incident"])
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X_111", classes=["center", "incident"])
    central_line(model, X_23, X_111, 23, 111, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_373 = eval_trilinear_point(model, A, B, C, '(2*b*c + a*c*cos(C) + a*b*cos(B))', ID="X_373", classes=["center", "incident"])
    central_line(model, X_6, X_373, 6, 373, incident=True)
    return promote_point_to_top(model, X_3291)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3291 on the given reference triangle."""
    model = create_model('X_3291 = INTERSECTION OF LINES X_2X_39 AND X_230X_231')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03291(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03291.json"))
    write_center_svg(
        model_acute,
        here / "x-03291.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
