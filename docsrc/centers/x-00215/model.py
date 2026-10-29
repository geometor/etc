"""GEOMETOR construction model for X(215) = X(1)-CEVA CONJUGATE OF X(50)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00215(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(215) = X(1)-CEVA CONJUGATE OF X(50) on reference triangle ABC."""
    X_215 = eval_trilinear_point(model, A, B, C, '(sin(3*A))*(sin(3*B) + sin(3*C) - sin(3*A))', ID="X(215)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_49 = eval_trilinear_point(model, A, B, C, 'cos(3*A)', ID="X(49)", classes=["center", "incident"])
    central_line(model, X_1, X_49, 1, 49, incident=True)
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X(12)", classes=["center", "incident"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X(54)", classes=["center", "incident"])
    central_line(model, X_12, X_54, 12, 54, incident=True)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X(11)", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    central_line(model, X_11, X_110, 11, 110, incident=True)
    return promote_point_to_top(model, X_215)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(215) on the given reference triangle."""
    model = create_model('X(215) = X(1)-CEVA CONJUGATE OF X(50)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00215(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00215.json"))
    write_center_svg(
        model_acute,
        here / "x-00215.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
