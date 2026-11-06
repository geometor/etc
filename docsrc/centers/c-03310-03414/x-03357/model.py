"""GEOMETOR construction model for X_3357 = MIDPOINT OF X_3 AND X_64."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    midpoint,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03357(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3357 = MIDPOINT OF X_3 AND X_64 on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X_64", classes=["center"])
    X_3357 = midpoint(model, X_3, X_64, ID="X_3357", classes=["selected", "target"], guide=False)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center", "incident"])
    central_line(model, X_4, X_74, 4, 74, incident=True)
    X_185 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 - cos(A)*cos(B - C))', ID="X_185", classes=["center", "incident"])
    X_378 = eval_trilinear_point(model, A, B, C, 'sec(A) + 2*cos(A)', ID="X_378", classes=["center", "incident"])
    central_line(model, X_185, X_378, 185, 378, incident=True)
    X_389 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(2*A)*cos(B - C)', ID="X_389", classes=["center", "incident"])
    X_1593 = eval_trilinear_point(model, A, B, C, 'cos(A) + sec(A)', ID="X_1593", classes=["center", "incident"])
    central_line(model, X_389, X_1593, 389, 1593, incident=True)
    return promote_point_to_top(model, X_3357)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3357 on the given reference triangle."""
    model = create_model('X_3357 = MIDPOINT OF X_3 AND X_64')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03357(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03357.json"))
    write_center_svg(
        model_acute,
        here / "x-03357.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
