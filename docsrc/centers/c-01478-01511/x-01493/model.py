"""GEOMETOR construction model for X_1493 = NAPOLEON CROSSSUM."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01493(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1493 = NAPOLEON CROSSSUM on reference triangle ABC."""
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center"])
    X_195 = eval_trilinear_point(model, A, B, C, 'a*(a**(8) + b**(8) + c**(8) - 4*a**(6)*(b**(2) + c**(2)) + a**(4)*(6*b**(4) + 6*c**(4) + 5*b**(2)*c**(2)) - a**(2)*(4*b**(6) + 4*c**(6) - b**(4)*c**(2) - b**(2)*c**(4)) - 2*b**(2)*c**(2)*(b**(4) + c**(4) - b**(2)*c**(2)))', ID="X_195", classes=["center"])
    X_1493 = midpoint(model, X_54, X_195, ID="X_1493", classes=["selected", "target"], guide=False)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    central_line(model, X_3, X_54, 3, 54, incident=True)
    X_49 = eval_trilinear_point(model, A, B, C, 'cos(3*A)', ID="X_49", classes=["center", "incident"])
    X_143 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cos(2*C - 2*A) + cos(2*A - 2*B))', ID="X_143", classes=["center", "incident"])
    central_line(model, X_49, X_143, 49, 143, incident=True)
    X_113 = eval_trilinear_point(model, A, B, C, 'sin(B)*sin(C)*((sin(C))/(cos(C) - 2*cos(A)*cos(B)) + (sin(B))/(cos(B) - 2*cos(A)*cos(C)))', ID="X_113", classes=["center", "incident"])
    X_137 = point_from_barycentrics(model, A, B, C, 0.1354431, 0.64976082, 0.21479608, ID="X_137", classes=["center", "incident"])
    central_line(model, X_113, X_137, 113, 137, incident=True)
    return promote_point_to_top(model, X_1493)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1493 on the given reference triangle."""
    model = create_model('X_1493 = NAPOLEON CROSSSUM')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01493(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01493.json"))
    write_center_svg(
        model_acute,
        here / "x-01493.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
