"""GEOMETOR construction model for X_1533 = ORTHOJOIN OF X_39."""

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


def construct_x_01533(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1533 = ORTHOJOIN OF X_39 on reference triangle ABC."""
    X_1531 = eval_trilinear_point(model, A, B, C, '(2*a**(4) - a**(2)*(b**(2) + c**(2)) - b**(4) - c**(4) + 2*b**(2)*c**(2))*(a**(5) - a*(b**(2) - c**(2))**(2) - 4*b*c*(b**(3)*cos(B) + c**(3)*cos(C)))', ID="X_1531", classes=["center"])
    X_1514 = point_from_barycentrics(model, A, B, C, -0.40927419, -0.46693548, 1.8762097, ID="X_1514", classes=["center"])
    X_1533 = reflection_in_point(model, X_1531, X_1514, ID="X_1533", classes=["selected", "target"], guide=False)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_83 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) + c**(2))', ID="X_83", classes=["center", "incident"])
    central_line(model, X_4, X_83, 4, 83, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_113 = eval_trilinear_point(model, A, B, C, 'sin(B)*sin(C)*((sin(C))/(cos(C) - 2*cos(A)*cos(B)) + (sin(B))/(cos(B) - 2*cos(A)*cos(C)))', ID="X_113", classes=["center", "incident"])
    central_line(model, X_30, X_113, 30, 113, incident=True)
    X_297 = eval_trilinear_point(model, A, B, C, 'csc(2*A)*cos(A + omega )', ID="X_297", classes=["center", "incident"])
    X_1515 = point_from_barycentrics(model, A, B, C, 0.44128126, 0.59428735, -0.035568613, ID="X_1515", classes=["center", "incident"])
    central_line(model, X_297, X_1515, 297, 1515, incident=True)
    return promote_point_to_top(model, X_1533)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1533 on the given reference triangle."""
    model = create_model('X_1533 = ORTHOJOIN OF X_39')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01533(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01533.json"))
    write_center_svg(
        model_acute,
        here / "x-01533.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
