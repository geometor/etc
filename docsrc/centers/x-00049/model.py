"""GEOMETOR construction model for X(49) = CENTER OF SINE-TRIPLE-ANGLE CIRCLE."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    nine_point_center_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00049(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(49) = CENTER OF SINE-TRIPLE-ANGLE CIRCLE on reference triangle ABC."""
    X_49 = eval_trilinear_point(model, A, B, C, 'cos(3*A)', ID="X(49)", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center", "incident"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X(54)", classes=["center", "incident"])
    central_line(model, X_5, X_54, 5, 54, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_155 = eval_barycentric_point(model, A, B, C, 'a**(2)*(a**(2) - b**(2) - c**(2))*(a**(6) - 3*a**(4)*(b**(2) + c**(2)) + a**(2)*(3*b**(4) - 2*b**(2)*c**(2) + 3*c**(4)) - (b**(2) - c**(2))**(2)*(b**(2) + c**(2)))', ID="X(155)", classes=["center", "incident"])
    central_line(model, X_3, X_155, 3, 155, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_156 = eval_barycentric_point(model, A, B, C, 'a**(2)*(a**(8) - 3*a**(6)*(b**(2) + c**(2)) + a**(4)*(3*b**(4) + 2*b**(2)*c**(2) + 3*c**(4)) - a**(2)*(b**(6) + c**(6)) + b**(2)*c**(2)*(b**(2) - c**(2))**(2))', ID="X(156)", classes=["center", "incident"])
    central_line(model, X_4, X_156, 4, 156, incident=True)
    return promote_point_to_top(model, X_49)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(49) on the given reference triangle."""
    model = create_model('X(49) = CENTER OF SINE-TRIPLE-ANGLE CIRCLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00049(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00049.json"))
    write_center_svg(
        model_acute,
        here / "x-00049.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
