"""GEOMETOR construction model for X_3588 = CENTER OF THE MYAKISHEV CONIC."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03588(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3588 = CENTER OF THE MYAKISHEV CONIC on reference triangle ABC."""
    X_3588 = eval_trilinear_point(model, A, B, C, '(a*(b + c)*(a**(4)*(b + c) - b**(4)*(c + a) - c**(4)*(a + b) + b**(2)*c**(2)*(b + c) + c**(2)*a**(2)*(a - c) + a**(2)*b**(2)*(a - b) - 2*a*b**(2)*c**(2)))', ID="X_3588", classes=["selected", "target"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    X_181 = eval_trilinear_point(model, A, B, C, 'a*(b + c)**(2)/(b + c - a)', ID="X_181", classes=["center", "incident"])
    central_line(model, X_42, X_181, 42, 181, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_573 = eval_trilinear_point(model, A, B, C, 'cos(A + U)', ID="X_573", classes=["center", "incident"])
    central_line(model, X_8, X_573, 8, 573, incident=True)
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center", "incident"])
    X_594 = eval_trilinear_point(model, A, B, C, '(b + c)**(2)/a', ID="X_594", classes=["center", "incident"])
    central_line(model, X_71, X_594, 71, 594, incident=True)
    return promote_point_to_top(model, X_3588)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3588 on the given reference triangle."""
    model = create_model('X_3588 = CENTER OF THE MYAKISHEV CONIC')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03588(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03588.json"))
    write_center_svg(
        model_acute,
        here / "x-03588.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
