"""GEOMETOR construction model for X_3411 = 1st BROCARD-KIEPERT-FERMAT CUSP."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03411(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3411 = 1st BROCARD-KIEPERT-FERMAT CUSP on reference triangle ABC."""
    X_3411 = eval_trilinear_point(model, A, B, C, '(cos(A) - 2*sin(B)*sin(C) - 3*cos(A + pi  /3))', ID="X_3411", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A +  pi  /3)', ID="X_13", classes=["center", "incident"])
    central_line(model, X_5, X_13, 5, 13, incident=True)
    X_16 = eval_trilinear_point(model, A, B, C, 'sin(A-  pi  /3)', ID="X_16", classes=["center", "incident"])
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    central_line(model, X_16, X_20, 16, 20, incident=True)
    X_14 = eval_trilinear_point(model, A, B, C, 'csc(A -  pi  /3)', ID="X_14", classes=["center", "incident"])
    X_382 = eval_trilinear_point(model, A, B, C, 'cos(A) - 4*cos(B)*cos(C)', ID="X_382", classes=["center", "incident"])
    central_line(model, X_14, X_382, 14, 382, incident=True)
    return promote_point_to_top(model, X_3411)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3411 on the given reference triangle."""
    model = create_model('X_3411 = 1st BROCARD-KIEPERT-FERMAT CUSP')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03411(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03411.json"))
    write_center_svg(
        model_acute,
        here / "x-03411.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
