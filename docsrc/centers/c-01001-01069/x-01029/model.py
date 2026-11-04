"""GEOMETOR construction model for X_1029 = CYCLOCEVIAN CONJUGATE OF X_1."""

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
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01029(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1029 = CYCLOCEVIAN CONJUGATE OF X_1 on reference triangle ABC."""
    X_1029 = eval_trilinear_point(model, A, B, C, '(1/(a + 2*(a + b + c)*cos(A)))', ID="X_1029", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_191 = eval_trilinear_point(model, A, B, C, '(b + c - a)*(b*c + c*a + a*b) + b**(3) + c**(3) - a**(3)', ID="X_191", classes=["center", "incident"])
    central_line(model, X_10, X_191, 10, 191, incident=True)
    X_319 = eval_trilinear_point(model, A, B, C, '(1 + 2*cos(A))/a**(2)', ID="X_319", classes=["center", "incident"])
    X_321 = eval_trilinear_point(model, A, B, C, '(b + c)*b**(2)*c**(2)', ID="X_321", classes=["center", "incident"])
    central_line(model, X_319, X_321, 319, 321, incident=True)
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center", "incident"])
    X_593 = eval_trilinear_point(model, A, B, C, 'a/(b + c)**(2)', ID="X_593", classes=["center", "incident"])
    central_line(model, X_115, X_593, 115, 593, incident=True)
    return promote_point_to_top(model, X_1029)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1029 on the given reference triangle."""
    model = create_model('X_1029 = CYCLOCEVIAN CONJUGATE OF X_1')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01029(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01029.json"))
    write_center_svg(
        model_acute,
        here / "x-01029.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
