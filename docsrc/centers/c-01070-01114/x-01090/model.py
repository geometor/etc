"""GEOMETOR construction model for X_1090 = TRILINEAR SQUARE OF X_11."""

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
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01090(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1090 = TRILINEAR SQUARE OF X_11 on reference triangle ABC."""
    X_1090 = eval_trilinear_point(model, A, B, C, '((1 - cos(B - C))**(2))', ID="X_1090", classes=["selected", "target"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center", "incident"])
    central_line(model, X_11, X_523, 11, 523, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_1091 = eval_trilinear_point(model, A, B, C, '((1 + cos(B - C))**(2))', ID="X_1091", classes=["center", "incident"])
    central_line(model, X_5, X_1091, 5, 1091, incident=True)
    return promote_point_to_top(model, X_1090)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1090 on the given reference triangle."""
    model = create_model('X_1090 = TRILINEAR SQUARE OF X_11')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01090(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01090.json"))
    write_center_svg(
        model_acute,
        here / "x-01090.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
