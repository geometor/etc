"""GEOMETOR construction model for X_1553 = ORTHOJOIN OF X_115."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    intersect_lines,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01553(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1553 = ORTHOJOIN OF X_115 on reference triangle ABC."""
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center"])
    X_113 = eval_trilinear_point(model, A, B, C, 'sin(B)*sin(C)*((sin(C))/(cos(C) - 2*cos(A)*cos(B)) + (sin(B))/(cos(B) - 2*cos(A)*cos(C)))', ID="X_113", classes=["center"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_250 = eval_trilinear_point(model, A, B, C, '(sec(A))*(csc(B - C))**(2)', ID="X_250", classes=["center"])
    central_line(model, X_30, X_113, 30, 113)
    central_line(model, X_4, X_250, 4, 250)
    X_1553 = intersect_lines(model, X_30, X_113, X_4, X_250, ID="X_1553", classes=["selected", "target"])
    X_146 = eval_barycentric_point(model, A, B, C, 'a**(10) + a**(8)*(b**(2) + c**(2)) - a**(6)*(8*b**(4) - 9*b**(2)*c**(2) + 8*c**(4)) + 2*a**(4)*(b**(2) + c**(2))*(4*b**(4) - 7*b**(2)*c**(2) + 4*c**(4)) - a**(2)*(b**(2) - c**(2))**(2)*(b**(4) + 9*b**(2)*c**(2) + c**(4)) - (b**(2) - c**(2))**(4)*(b**(2) + c**(2))', ID="X_146", classes=["center", "incident"])
    X_476 = eval_trilinear_point(model, A, B, C, '1/((1 + 2*cos(2*A))*sin(B - C))', ID="X_476", classes=["center", "incident"])
    central_line(model, X_146, X_476, 146, 476, incident=True)
    return promote_point_to_top(model, X_1553)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1553 on the given reference triangle."""
    model = create_model('X_1553 = ORTHOJOIN OF X_115')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01553(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01553.json"))
    write_center_svg(
        model_acute,
        here / "x-01553.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
