"""GEOMETOR construction model for X(146) = REFLECTION OF X(20) IN X(110)."""

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
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00146(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(146) = REFLECTION OF X(20) IN X(110) on reference triangle ABC."""
    X_146 = eval_barycentric_point(model, A, B, C, 'a**(10) + a**(8)*(b**(2) + c**(2)) - a**(6)*(8*b**(4) - 9*b**(2)*c**(2) + 8*c**(4)) + 2*a**(4)*(b**(2) + c**(2))*(4*b**(4) - 7*b**(2)*c**(2) + 4*c**(4)) - a**(2)*(b**(2) - c**(2))**(2)*(b**(4) + 9*b**(2)*c**(2) + c**(4)) - (b**(2) - c**(2))**(4)*(b**(2) + c**(2))', ID="X(146)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X(74)", classes=["center", "incident"])
    central_line(model, X_2, X_74, 2, 74, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_94 = eval_trilinear_point(model, A, B, C, 'csc(3*A)', ID="X(94)", classes=["center", "incident"])
    central_line(model, X_4, X_94, 4, 94, incident=True)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X(20)", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    central_line(model, X_20, X_110, 20, 110, incident=True)
    return promote_point_to_top(model, X_146)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(146) on the given reference triangle."""
    model = create_model('X(146) = REFLECTION OF X(20) IN X(110)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00146(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00146.json"))
    write_center_svg(
        model_acute,
        here / "x-00146.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
