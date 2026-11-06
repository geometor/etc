"""GEOMETOR construction model for X_3590 = 1st DIXIT POINT."""

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


def construct_x_03590(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3590 = 1st DIXIT POINT on reference triangle ABC."""
    X_3590 = eval_trilinear_point(model, A, B, C, '(b*c/(b**(2) + c**(2) - a**(2) + 6*area ))', ID="X_3590", classes=["selected", "target"])
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_1327 = eval_trilinear_point(model, A, B, C, '(1/(sin(A) + 3*cos(A)))', ID="X_1327", classes=["center", "incident"])
    central_line(model, X_20, X_1327, 20, 1327, incident=True)
    X_590 = eval_trilinear_point(model, A, B, C, '(a**(2) + 4*area )/a', ID="X_590", classes=["center", "incident"])
    X_1131 = eval_trilinear_point(model, A, B, C, '1/(sin(A) + 2*cos(A))', ID="X_1131", classes=["center", "incident"])
    central_line(model, X_590, X_1131, 590, 1131, incident=True)
    X_140 = eval_trilinear_point(model, A, B, C, '2*cos(A) + cos(B - C)', ID="X_140", classes=["center", "incident"])
    X_3316 = eval_trilinear_point(model, A, B, C, '1/(cos(A) + 2*sin(A))', ID="X_3316", classes=["center", "incident"])
    central_line(model, X_140, X_3316, 140, 3316, incident=True)
    return promote_point_to_top(model, X_3590)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3590 on the given reference triangle."""
    model = create_model('X_3590 = 1st DIXIT POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03590(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03590.json"))
    write_center_svg(
        model_acute,
        here / "x-03590.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
