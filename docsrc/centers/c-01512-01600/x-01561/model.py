"""GEOMETOR construction model for X_1561 = ORTHOJOIN OF X_511."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_01561(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1561 = ORTHOJOIN OF X_511 on reference triangle ABC."""
    X_1555 = point_from_barycentrics(model, A, B, C, -0.89912757, -0.7709824, 2.67011, ID="X_1555", classes=["center"])
    X_1514 = point_from_barycentrics(model, A, B, C, -0.40927419, -0.46693548, 1.8762097, ID="X_1514", classes=["center"])
    X_1561 = reflection_in_point(model, X_1555, X_1514, ID="X_1561", classes=["selected", "target"], guide=False)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    central_line(model, X_4, X_32, 4, 32, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_113 = eval_trilinear_point(model, A, B, C, 'sin(B)*sin(C)*((sin(C))/(cos(C) - 2*cos(A)*cos(B)) + (sin(B))/(cos(B) - 2*cos(A)*cos(C)))', ID="X_113", classes=["center", "incident"])
    central_line(model, X_30, X_113, 30, 113, incident=True)
    return promote_point_to_top(model, X_1561)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1561 on the given reference triangle."""
    model = create_model('X_1561 = ORTHOJOIN OF X_511')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01561(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01561.json"))
    write_center_svg(
        model_acute,
        here / "x-01561.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
