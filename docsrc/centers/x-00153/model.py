"""GEOMETOR construction model for X(153) = REFLECTION OF X(20) IN X(100)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    gergonne_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00153(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(153) = REFLECTION OF X(20) IN X(100) on reference triangle ABC."""
    X_153 = eval_barycentric_point(model, A, B, C, 'a**(7) - a**(6)*(b + c) - a**(5)*(b**(2) - 7*b*c + c**(2)) + a**(4)*(b + c)*(b**(2) - 6*b*c + c**(2)) - a**(3)*(b**(4) + 2*b**(3)*c - 10*b**(2)*c**(2) + 2*b*c**(3) + c**(4)) + a**(2)*(b - c)**(2)*(b + c)*(b**(2) + 6*b*c + c**(2)) + a*(b**(2) - c**(2))**(2)*(b**(2) - 5*b*c + c**(2)) - (b - c)**(4)*(b + c)**(3)', ID="X(153)", classes=["selected", "target"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    X_80 = eval_trilinear_point(model, A, B, C, '1/(1 - 2*cos(A))', ID="X(80)", classes=["center", "incident"])
    central_line(model, X_7, X_80, 7, 80, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X(104)", classes=["center", "incident"])
    central_line(model, X_2, X_104, 2, 104, incident=True)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X(20)", classes=["center", "incident"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X(100)", classes=["center", "incident"])
    central_line(model, X_20, X_100, 20, 100, incident=True)
    return promote_point_to_top(model, X_153)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(153) on the given reference triangle."""
    model = create_model('X(153) = REFLECTION OF X(20) IN X(100)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00153(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00153.json"))
    write_center_svg(
        model_acute,
        here / "x-00153.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
