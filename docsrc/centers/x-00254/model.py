"""GEOMETOR construction model for X(254) = X(3)-CROSS CONJUGATE OF X(4)."""

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
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00254(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(254) = X(3)-CROSS CONJUGATE OF X(4) on reference triangle ABC."""
    X_155 = eval_barycentric_point(model, A, B, C, 'a**(2)*(a**(2) - b**(2) - c**(2))*(a**(6) - 3*a**(4)*(b**(2) + c**(2)) + a**(2)*(3*b**(4) - 2*b**(2)*c**(2) + 3*c**(4)) - (b**(2) - c**(2))**(2)*(b**(2) + c**(2)))', ID="X(155)", classes=["center"])
    X_254 = isogonal_conjugate(model, A, B, C, X_155, ID="X(254)", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    central_line(model, X_4, X_155, 4, 155, incident=True)
    X_68 = eval_trilinear_point(model, A, B, C, 'cos(A)*sec(2*A)', ID="X(68)", classes=["center", "incident"])
    X_136 = eval_barycentric_point(model, A, B, C, '(b**(2) - c**(2))**(2)*(a**(4) + b**(4) + c**(4) - 2*a**(2)*b**(2) - 2*a**(2)*c**(2))/(a**(2) - b**(2) - c**(2))', ID="X(136)", classes=["center", "incident"])
    central_line(model, X_68, X_136, 68, 136, incident=True)
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X(46)", classes=["center", "incident"])
    X_225 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cos(B) + cos(C))', ID="X(225)", classes=["center", "incident"])
    central_line(model, X_46, X_225, 46, 225, incident=True)
    return promote_point_to_top(model, X_254)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(254) on the given reference triangle."""
    model = create_model('X(254) = X(3)-CROSS CONJUGATE OF X(4)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00254(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00254.json"))
    write_center_svg(
        model_acute,
        here / "x-00254.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
