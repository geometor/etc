"""GEOMETOR construction model for X_3124 = DANNEELS PERSPECTOR FOR X_76."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03124(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3124 = DANNEELS PERSPECTOR FOR X_76 on reference triangle ABC."""
    X_3124 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))**(2)', ID="X_3124", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_6, X_110, 6, 110, incident=True)
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center", "incident"])
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X_125", classes=["center", "incident"])
    central_line(model, X_115, X_125, 115, 125, incident=True)
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    X_373 = eval_trilinear_point(model, A, B, C, '(2*b*c + a*c*cos(C) + a*b*cos(B))', ID="X_373", classes=["center", "incident"])
    central_line(model, X_39, X_373, 39, 373, incident=True)
    return promote_point_to_top(model, X_3124)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3124 on the given reference triangle."""
    model = create_model('X_3124 = DANNEELS PERSPECTOR FOR X_76')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03124(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03124.json"))
    write_center_svg(
        model_acute,
        here / "x-03124.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
