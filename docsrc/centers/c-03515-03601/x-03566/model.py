"""GEOMETOR construction model for X_3566 = 2nd MOSES INFINITY POINT."""

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
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03566(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3566 = 2nd MOSES INFINITY POINT on reference triangle ABC."""
    X_3565 = eval_trilinear_point(model, A, B, C, '(a/((3*a**(2) - b**(2) - c**(2))*(b**(2) - c**(2))))', ID="X_3565", classes=["center"])
    X_3566 = isogonal_conjugate(model, A, B, C, X_3565, ID="X_3566", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X_64", classes=["center", "incident"])
    X_879 = eval_barycentric_point(model, A, B, C, '(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))/(b**(4) + c**(4) - a**(2)*b**(2) - a**(2)*c**(2))', ID="X_879", classes=["center", "incident"])
    central_line(model, X_64, X_879, 64, 879, incident=True)
    X_1640 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))*(2*a**(6) - b**(6) - c**(6) - 2*a**(4)*b**(2) - 2*a**(4)*c**(2) + a**(2)*b**(4) + a**(2)*c**(4) + b**(4)*c**(2) + b**(2)*c**(4))', ID="X_1640", classes=["center", "incident"])
    X_1853 = point_from_barycentrics(model, A, B, C, -0.10818713, -0.21754386, 1.325731, ID="X_1853", classes=["center", "incident"])
    central_line(model, X_1640, X_1853, 1640, 1853, incident=True)
    return promote_point_to_top(model, X_3566)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3566 on the given reference triangle."""
    model = create_model('X_3566 = 2nd MOSES INFINITY POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03566(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03566.json"))
    write_center_svg(
        model_acute,
        here / "x-03566.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
