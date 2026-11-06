"""GEOMETOR construction model for X_3321 = INCIRCLE TRANSFORM T(X_663)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    feuerbach_point_of,
    gergonne_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03321(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3321 = INCIRCLE TRANSFORM T(X_663) on reference triangle ABC."""
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center"])
    X_1323 = eval_trilinear_point(model, A, B, C, '(((sec(A/2))**(2))*(2*(cos(A/2))**(2) - (cos(B/2))**(2) - (cos(C/2))**(2)))', ID="X_1323", classes=["center"])
    X_3321 = crosspoint(model, A, B, C, X_7, X_1323, ID="X_3321", classes=["selected", "target"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    central_line(model, X_7, X_11, 7, 11, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_934 = eval_trilinear_point(model, A, B, C, '1/((b - c)*(b + c - a)**(2))', ID="X_934", classes=["center", "incident"])
    central_line(model, X_55, X_934, 55, 934, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_1358 = eval_trilinear_point(model, A, B, C, '(tan(A/2))**(2)*(sin(B/2 - C/2))**(2)', ID="X_1358", classes=["center", "incident"])
    central_line(model, X_57, X_1358, 57, 1358, incident=True)
    return promote_point_to_top(model, X_3321)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3321 on the given reference triangle."""
    model = create_model('X_3321 = INCIRCLE TRANSFORM T(X_663)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03321(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03321.json"))
    write_center_svg(
        model_acute,
        here / "x-03321.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
