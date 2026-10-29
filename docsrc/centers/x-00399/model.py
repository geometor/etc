"""GEOMETOR construction model for X(399) = PARRY REFLECTION POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00399(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(399) = PARRY REFLECTION POINT on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A + pi /3)', ID="X(13)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X(74)", classes=["center"])
    central_line(model, X_6, X_13, 6, 13)
    central_line(model, X_3, X_74, 3, 74)
    X_399 = intersect_lines(model, X_6, X_13, X_3, X_74, ID="X(399)", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center", "incident"])
    X_146 = eval_barycentric_point(model, A, B, C, 'a**(10) + a**(8)*(b**(2) + c**(2)) - a**(6)*(8*b**(4) - 9*b**(2)*c**(2) + 8*c**(4)) + 2*a**(4)*(b**(2) + c**(2))*(4*b**(4) - 7*b**(2)*c**(2) + 4*c**(4)) - a**(2)*(b**(2) - c**(2))**(2)*(b**(4) + 9*b**(2)*c**(2) + c**(4)) - (b**(2) - c**(2))**(4)*(b**(2) + c**(2))', ID="X(146)", classes=["center", "incident"])
    central_line(model, X_30, X_146, 30, 146, incident=True)
    return promote_point_to_top(model, X_399)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(399) on the given reference triangle."""
    model = create_model('X(399) = PARRY REFLECTION POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00399(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00399.json"))
    write_center_svg(
        model_acute,
        here / "x-00399.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
