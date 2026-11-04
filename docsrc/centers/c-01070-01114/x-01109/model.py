"""GEOMETOR construction model for X_1109 = TRILINEAR SQUARE OF X_523."""

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
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01109(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1109 = TRILINEAR SQUARE OF X_523 on reference triangle ABC."""
    X_1101 = eval_trilinear_point(model, A, B, C, '((csc(B - C))**(2))', ID="X_1101", classes=["center"])
    X_1109 = isogonal_conjugate(model, A, B, C, X_1101, ID="X_1109", classes=["selected", "target"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X_92", classes=["center", "incident"])
    central_line(model, X_31, X_92, 31, 92, incident=True)
    X_91 = eval_trilinear_point(model, A, B, C, 'sec(2*A)', ID="X_91", classes=["center", "incident"])
    X_255 = eval_trilinear_point(model, A, B, C, '(cos(A))**(2)', ID="X_255", classes=["center", "incident"])
    central_line(model, X_91, X_255, 91, 255, incident=True)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center", "incident"])
    central_line(model, X_11, X_523, 11, 523, incident=True)
    return promote_point_to_top(model, X_1109)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1109 on the given reference triangle."""
    model = create_model('X_1109 = TRILINEAR SQUARE OF X_523')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01109(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01109.json"))
    write_center_svg(
        model_acute,
        here / "x-01109.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
