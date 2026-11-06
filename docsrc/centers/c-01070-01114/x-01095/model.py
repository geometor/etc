"""GEOMETOR construction model for X_1095 = TRILINEAR SQUARE OF X_16."""

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


def construct_x_01095(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1095 = TRILINEAR SQUARE OF X_16 on reference triangle ABC."""
    X_1095 = eval_trilinear_point(model, A, B, C, '((sin(A -  pi  /3))**(2))', ID="X_1095", classes=["selected", "target"])
    X_16 = eval_trilinear_point(model, A, B, C, 'sin(A-  pi  /3)', ID="X_16", classes=["center", "incident"])
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    central_line(model, X_16, X_36, 16, 36, incident=True)
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    X_163 = eval_trilinear_point(model, A, B, C, '(sin(2*A))/(sin(2*B) - sin(2*C))', ID="X_163", classes=["center", "incident"])
    central_line(model, X_48, X_163, 48, 163, incident=True)
    return promote_point_to_top(model, X_1095)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1095 on the given reference triangle."""
    model = create_model('X_1095 = TRILINEAR SQUARE OF X_16')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01095(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01095.json"))
    write_center_svg(
        model_acute,
        here / "x-01095.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
