"""GEOMETOR construction model for X(526) = ISOGONAL CONJUGATE OF X(476)."""

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


def construct_x_00526(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(526) = ISOGONAL CONJUGATE OF X(476) on reference triangle ABC."""
    X_476 = eval_trilinear_point(model, A, B, C, '1/((1 + 2*cos(2*A))*sin(B - C))', ID="X(476)", classes=["center"])
    X_526 = isogonal_conjugate(model, A, B, C, X_476, ID="X(526)", classes=["selected", "target"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    X_351 = point_from_barycentrics(model, A, B, C, -1.104798, 0.16783217, 1.9369658, ID="X(351)", classes=["center", "incident"])
    central_line(model, X_110, X_351, 110, 351, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X(511)", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    X_67 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X(67)", classes=["center", "incident"])
    X_879 = eval_barycentric_point(model, A, B, C, '(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))/(b**(4) + c**(4) - a**(2)*b**(2) - a**(2)*c**(2))', ID="X(879)", classes=["center", "incident"])
    central_line(model, X_67, X_879, 67, 879, incident=True)
    return promote_point_to_top(model, X_526)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(526) on the given reference triangle."""
    model = create_model('X(526) = ISOGONAL CONJUGATE OF X(476)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00526(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00526.json"))
    write_center_svg(
        model_acute,
        here / "x-00526.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
