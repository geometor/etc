"""GEOMETOR construction model for X_3125 = DANNEELS PERSPECTOR FOR X_81."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    cevapoint,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03125(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3125 = DANNEELS PERSPECTOR FOR X_81 on reference triangle ABC."""
    X_2643 = eval_trilinear_point(model, A, B, C, '1/(cot(C) - cot(A)) - 1/(cot(B) - cot(A))', ID="X_2643", classes=["center"])
    X_3124 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))**(2)', ID="X_3124", classes=["center"])
    X_3125 = cevapoint(model, A, B, C, X_2643, X_3124, ID="X_3125", classes=["selected", "target"])
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center", "incident"])
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X_125", classes=["center", "incident"])
    central_line(model, X_115, X_125, 115, 125, incident=True)
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    X_213 = eval_trilinear_point(model, A, B, C, '(b + c)*a**(2)', ID="X_213", classes=["center", "incident"])
    central_line(model, X_65, X_213, 65, 213, incident=True)
    X_257 = eval_trilinear_point(model, A, B, C, '1/(a**(3) + a*b*c)', ID="X_257", classes=["center", "incident"])
    X_274 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c)', ID="X_274", classes=["center", "incident"])
    central_line(model, X_257, X_274, 257, 274, incident=True)
    return promote_point_to_top(model, X_3125)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3125 on the given reference triangle."""
    model = create_model('X_3125 = DANNEELS PERSPECTOR FOR X_81')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03125(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03125.json"))
    write_center_svg(
        model_acute,
        here / "x-03125.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
