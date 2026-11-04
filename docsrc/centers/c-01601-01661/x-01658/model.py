"""GEOMETOR construction model for X_1658 = CIRCUMCENTER OF KOSNITA TRIANGLE."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    midpoint,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01658(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1658 = CIRCUMCENTER OF KOSNITA TRIANGLE on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_26 = eval_trilinear_point(model, A, B, C, 'a*(b**(2)*cos(2*B) + c**(2)*cos(2*C) - a**(2)*cos(2*A))', ID="X_26", classes=["center"])
    X_1658 = midpoint(model, X_3, X_26, ID="X_1658", classes=["selected", "target"], guide=False)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    X_568 = eval_trilinear_point(model, A, B, C, 'a*(3*R**(2)*(b**(2) + c**(2) - a**(2)) + a**(2)*b**(2) + a**(2)*c**(2) - b**(4) - c**(4))', ID="X_568", classes=["center", "incident"])
    central_line(model, X_54, X_568, 54, 568, incident=True)
    X_143 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cos(2*C - 2*A) + cos(2*A - 2*B))', ID="X_143", classes=["center", "incident"])
    X_578 = eval_trilinear_point(model, A, B, C, 'cos(A) + sin(A)*(tan(A) + tan(B) + tan(C))', ID="X_578", classes=["center", "incident"])
    central_line(model, X_143, X_578, 143, 578, incident=True)
    return promote_point_to_top(model, X_1658)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1658 on the given reference triangle."""
    model = create_model('X_1658 = CIRCUMCENTER OF KOSNITA TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01658(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01658.json"))
    write_center_svg(
        model_acute,
        here / "x-01658.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
