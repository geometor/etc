"""GEOMETOR construction model for X_3026 = 10th STEVANOVIC POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03026(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3026 = 10th STEVANOVIC POINT on reference triangle ABC."""
    X_3026 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c - a)*(b - c)**(2)*(a**(2) + a*b + a*c + 2*b*c)**(2))', ID="X_3026", classes=["selected", "target"])
    X_150 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(4) + c**(4) - a**(4) + a*(b*c**(2) +c*b**(2) - b**(3) - c**(3)) - b*c*(a**(2) + b**(2) + c**(2)) + (b + c)*a**(3)))', ID="X_150", classes=["center", "incident"])
    X_388 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) + (b + c)**(2))/(b + c - a)', ID="X_388", classes=["center", "incident"])
    central_line(model, X_150, X_388, 150, 388, incident=True)
    X_274 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c)', ID="X_274", classes=["center", "incident"])
    X_1682 = eval_trilinear_point(model, A, B, C, '(s*cos(A/2) - r*sin(A/2))**(2)', ID="X_1682", classes=["center", "incident"])
    central_line(model, X_274, X_1682, 274, 1682, incident=True)
    X_1111 = eval_trilinear_point(model, A, B, C, '(((b - c)/a)**(2))', ID="X_1111", classes=["center", "incident"])
    X_1357 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)*(b - c)**(2)*(a**(2) - (b - c)**(2))**(2)', ID="X_1357", classes=["center", "incident"])
    central_line(model, X_1111, X_1357, 1111, 1357, incident=True)
    return promote_point_to_top(model, X_3026)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3026 on the given reference triangle."""
    model = create_model('X_3026 = 10th STEVANOVIC POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03026(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03026.json"))
    write_center_svg(
        model_acute,
        here / "x-03026.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
