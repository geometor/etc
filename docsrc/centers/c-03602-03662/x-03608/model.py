"""GEOMETOR construction model for X_3608 = 1st MORLEY-GIBERT PERSPECTOR."""

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


def construct_x_03608(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3608 = 1st MORLEY-GIBERT PERSPECTOR on reference triangle ABC."""
    X_3608 = eval_trilinear_point(model, A, B, C, '(cos(A) + 2*cos(B)*cos(C) + 3*cos(A/3) + 6*cos(B/3)*cos(C/3))', ID="X_3608", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_356 = eval_trilinear_point(model, A, B, C, 'cos(A/3) + 2*cos(B/3)*cos(C/3)', ID="X_356", classes=["center", "incident"])
    central_line(model, X_5, X_356, 5, 356, incident=True)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_3278 = eval_trilinear_point(model, A, B, C, '(cos(A/3)*cos(2*A/3) + cos(B/3)*cos(C/3))', ID="X_3278", classes=["center", "incident"])
    central_line(model, X_20, X_3278, 20, 3278, incident=True)
    X_631 = eval_trilinear_point(model, A, B, C, '2*cos(A) + cos(B)*cos(C)', ID="X_631", classes=["center", "incident"])
    X_3279 = eval_trilinear_point(model, A, B, C, '(cos(B/3)*cos(C/3) + sin(A/3)*sin(2*A/3))', ID="X_3279", classes=["center", "incident"])
    central_line(model, X_631, X_3279, 631, 3279, incident=True)
    return promote_point_to_top(model, X_3608)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3608 on the given reference triangle."""
    model = create_model('X_3608 = 1st MORLEY-GIBERT PERSPECTOR')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03608(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03608.json"))
    write_center_svg(
        model_acute,
        here / "x-03608.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
