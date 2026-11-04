"""GEOMETOR construction model for X_2969 = 3rd MACBEATH POINT."""

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
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02969(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2969 = 3rd MACBEATH POINT on reference triangle ABC."""
    X_2969 = eval_trilinear_point(model, A, B, C, '((b - c)**(2)*cos(B)*cos(C))', ID="X_2969", classes=["selected", "target"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center", "incident"])
    central_line(model, X_25, X_105, 25, 105, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_145 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a - b - c)', ID="X_145", classes=["center", "incident"])
    central_line(model, X_4, X_145, 4, 145, incident=True)
    X_124 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c - a)*(b - c)**(2)*((b + c)*(b**(2) + c**(2) - a**(2) - b*c) + a*b*c))', ID="X_124", classes=["center", "incident"])
    X_136 = eval_barycentric_point(model, A, B, C, '(b**(2) - c**(2))**(2)*(a**(4) + b**(4) + c**(4) - 2*a**(2)*b**(2) - 2*a**(2)*c**(2))/(a**(2) - b**(2) - c**(2))', ID="X_136", classes=["center", "incident"])
    central_line(model, X_124, X_136, 124, 136, incident=True)
    return promote_point_to_top(model, X_2969)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2969 on the given reference triangle."""
    model = create_model('X_2969 = 3rd MACBEATH POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02969(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02969.json"))
    write_center_svg(
        model_acute,
        here / "x-02969.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
