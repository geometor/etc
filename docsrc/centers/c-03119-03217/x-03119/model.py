"""GEOMETOR construction model for X_3119 = DANNEELS PERSPECTOR FOR X_9."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03119(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3119 = DANNEELS PERSPECTOR FOR X_9 on reference triangle ABC."""
    X_3119 = eval_trilinear_point(model, A, B, C, '((b - c)**(2)*(b + c - a)**(3))', ID="X_3119", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    central_line(model, X_9, X_100, 9, 100, incident=True)
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X_125", classes=["center", "incident"])
    X_661 = eval_trilinear_point(model, A, B, C, 'cot(B) - cot(C)', ID="X_661", classes=["center", "incident"])
    central_line(model, X_125, X_661, 125, 661, incident=True)
    X_282 = eval_trilinear_point(model, A, B, C, '(cot(A/2))/(-1 - cos(A) + cos(B) + cos(C))', ID="X_282", classes=["center", "incident"])
    X_604 = eval_trilinear_point(model, A, B, C, 'a*(1 - cos(A))', ID="X_604", classes=["center", "incident"])
    central_line(model, X_282, X_604, 282, 604, incident=True)
    return promote_point_to_top(model, X_3119)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3119 on the given reference triangle."""
    model = create_model('X_3119 = DANNEELS PERSPECTOR FOR X_9')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03119(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03119.json"))
    write_center_svg(
        model_acute,
        here / "x-03119.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
