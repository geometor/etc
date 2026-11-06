"""GEOMETOR construction model for X_3591 = 2nd DIXIT POINT."""

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


def construct_x_03591(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3591 = 2nd DIXIT POINT on reference triangle ABC."""
    X_3591 = eval_trilinear_point(model, A, B, C, '(b*c/(b**(2) + c**(2) - a**(2) - 6*area ))', ID="X_3591", classes=["selected", "target"])
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_1328 = eval_trilinear_point(model, A, B, C, '1/(sin(A) - 3*cos(A))', ID="X_1328", classes=["center", "incident"])
    central_line(model, X_20, X_1328, 20, 1328, incident=True)
    X_615 = eval_trilinear_point(model, A, B, C, '(a**(2) - 4*area )/a', ID="X_615", classes=["center", "incident"])
    X_1132 = eval_trilinear_point(model, A, B, C, '1/(sin(A) - 2*cos(A))', ID="X_1132", classes=["center", "incident"])
    central_line(model, X_615, X_1132, 615, 1132, incident=True)
    X_140 = eval_trilinear_point(model, A, B, C, '2*cos(A) + cos(B - C)', ID="X_140", classes=["center", "incident"])
    X_3317 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*sin(A))', ID="X_3317", classes=["center", "incident"])
    central_line(model, X_140, X_3317, 140, 3317, incident=True)
    return promote_point_to_top(model, X_3591)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3591 on the given reference triangle."""
    model = create_model('X_3591 = 2nd DIXIT POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03591(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03591.json"))
    write_center_svg(
        model_acute,
        here / "x-03591.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
