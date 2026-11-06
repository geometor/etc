"""GEOMETOR construction model for X_3467 = ISOGONAL CONJUGATE OF X_3336."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    incenter_of,
    isogonal_conjugate,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03467(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3467 = ISOGONAL CONJUGATE OF X_3336 on reference triangle ABC."""
    X_3336 = eval_trilinear_point(model, A, B, C, '(a - b + c)*(a + b - c)*(a + b + c) - a*b*c', ID="X_3336", classes=["center"])
    X_3467 = isogonal_conjugate(model, A, B, C, X_3336, ID="X_3467", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_79 = eval_trilinear_point(model, A, B, C, '1/(1 + 2*cos(A))', ID="X_79", classes=["center", "incident"])
    central_line(model, X_5, X_79, 5, 79, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_195 = eval_trilinear_point(model, A, B, C, 'a*(a**(8) + b**(8) + c**(8) - 4*a**(6)*(b**(2) + c**(2)) + a**(4)*(6*b**(4) + 6*c**(4) + 5*b**(2)*c**(2)) - a**(2)*(4*b**(6) + 4*c**(6) - b**(4)*c**(2) - b**(2)*c**(4)) - 2*b**(2)*c**(2)*(b**(4) + c**(4) - b**(2)*c**(2)))', ID="X_195", classes=["center", "incident"])
    central_line(model, X_1, X_195, 1, 195, incident=True)
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_499 = eval_trilinear_point(model, A, B, C, '1 - 2*sin(B)*sin(C)', ID="X_499", classes=["center", "incident"])
    central_line(model, X_7, X_499, 7, 499, incident=True)
    return promote_point_to_top(model, X_3467)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3467 on the given reference triangle."""
    model = create_model('X_3467 = ISOGONAL CONJUGATE OF X_3336')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03467(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03467.json"))
    write_center_svg(
        model_acute,
        here / "x-03467.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
