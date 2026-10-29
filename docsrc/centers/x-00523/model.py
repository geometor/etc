"""GEOMETOR construction model for X(523) = ISOGONAL CONJUGATE OF X(110)."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00523(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(523) = ISOGONAL CONJUGATE OF X(110) on reference triangle ABC."""
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center"])
    X_523 = isogonal_conjugate(model, A, B, C, X_110, ID="X(523)", classes=["selected", "target"])
    X_23 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X(23)", classes=["center", "incident"])
    X_385 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(4) - b**(2)*c**(2))', ID="X(385)", classes=["center", "incident"])
    central_line(model, X_23, X_385, 23, 385, incident=True)
    X_230 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*(2*a**(2) - b**(2) - c**(2)) + (b**(2) - c**(2))**(2))', ID="X(230)", classes=["center", "incident"])
    X_231 = eval_barycentric_point(model, A, B, C, '2*a**(8) - 4*a**(6)*b**(2) + 3*a**(4)*b**(4) - 2*a**(2)*b**(6) + b**(8) - 4*a**(6)*c**(2) + 2*a**(2)*b**(4)*c**(2) - 4*b**(6)*c**(2) + 3*a**(4)*c**(4) + 2*a**(2)*b**(2)*c**(4) + 6*b**(4)*c**(4) - 2*a**(2)*c**(6) - 4*b**(2)*c**(6) + c**(8)', ID="X(231)", classes=["center", "incident"])
    central_line(model, X_230, X_231, 230, 231, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X(511)", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    return promote_point_to_top(model, X_523)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(523) on the given reference triangle."""
    model = create_model('X(523) = ISOGONAL CONJUGATE OF X(110)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00523(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00523.json"))
    write_center_svg(
        model_acute,
        here / "x-00523.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
