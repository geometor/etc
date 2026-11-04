"""GEOMETOR construction model for X_1112 = CROSSPOINT OF X_4 AND X_250."""

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
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_01112(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1112 = CROSSPOINT OF X_4 AND X_250 on reference triangle ABC."""
    X_974 = eval_trilinear_point(model, A, B, C, '(s*a**(10) - a**(8)*(3*b**(4) - 2*b**(2)*c**(2) + 3*c**(4)) + a**(6)*s*(2*b**(4) - 3*b**(2)*c**(2) + 2*c**(4)) + a**(4)*(b**(2) - c**(2))**(2)*(2*b**(4) - 7*b**(2)*c**(2) + 2*c**(4)) - 3*a**(2)*s*(b**(2) - c**(2))**(2)*(b**(4) - 3*b**(2)*c**(2) + c**(4)) + (b**(2) - c**(2))**(4)*(b**(4) + b**(2)*c**(2) + c**(4)))*cos(A)', ID="X_974", classes=["center"])
    X_389 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(2*A)*cos(B - C)', ID="X_389", classes=["center"])
    X_1112 = reflection_in_point(model, X_974, X_389, ID="X_1112", classes=["selected", "target"], guide=False)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_94 = eval_trilinear_point(model, A, B, C, 'csc(3*A)', ID="X_94", classes=["center", "incident"])
    central_line(model, X_4, X_94, 4, 94, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_25, X_110, 25, 110, incident=True)
    X_52 = eval_trilinear_point(model, A, B, C, 'cos(2*A)*cos(B - C)', ID="X_52", classes=["center", "incident"])
    X_113 = eval_trilinear_point(model, A, B, C, 'sin(B)*sin(C)*((sin(C))/(cos(C) - 2*cos(A)*cos(B)) + (sin(B))/(cos(B) - 2*cos(A)*cos(C)))', ID="X_113", classes=["center", "incident"])
    central_line(model, X_52, X_113, 52, 113, incident=True)
    return promote_point_to_top(model, X_1112)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1112 on the given reference triangle."""
    model = create_model('X_1112 = CROSSPOINT OF X_4 AND X_250')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01112(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01112.json"))
    write_center_svg(
        model_acute,
        here / "x-01112.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
