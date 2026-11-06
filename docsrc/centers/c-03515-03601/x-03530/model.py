"""GEOMETOR construction model for X_3530 = EULER LINE INTERCEPT OF LINE X_15X_3411."""

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


def construct_x_03530(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3530 = EULER LINE INTERCEPT OF LINE X_15X_3411 on reference triangle ABC."""
    X_546 = eval_trilinear_point(model, A, B, C, '3*cos(B - C) - 2*cos(A)', ID="X_546", classes=["center"])
    X_3530 = complement(model, A, B, C, X_546, ID="X_3530", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_15 = eval_trilinear_point(model, A, B, C, 'sin(A +  pi  /3)', ID="X_15", classes=["center", "incident"])
    X_3411 = eval_trilinear_point(model, A, B, C, '(cos(A) - 2*sin(B)*sin(C) - 3*cos(A + pi  /3))', ID="X_3411", classes=["center", "incident"])
    central_line(model, X_15, X_3411, 15, 3411, incident=True)
    X_16 = eval_trilinear_point(model, A, B, C, 'sin(A-  pi  /3)', ID="X_16", classes=["center", "incident"])
    X_3412 = eval_trilinear_point(model, A, B, C, '(cos(A) - 2*sin(B)*sin(C) - 3*cos(A - pi  /3))', ID="X_3412", classes=["center", "incident"])
    central_line(model, X_16, X_3412, 16, 3412, incident=True)
    return promote_point_to_top(model, X_3530)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3530 on the given reference triangle."""
    model = create_model('X_3530 = EULER LINE INTERCEPT OF LINE X_15X_3411')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03530(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03530.json"))
    write_center_svg(
        model_acute,
        here / "x-03530.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
