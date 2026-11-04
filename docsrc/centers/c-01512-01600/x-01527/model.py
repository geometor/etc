"""GEOMETOR construction model for X_1527 = ORTHOJOIN OF X_18."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01527(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1527 = ORTHOJOIN OF X_18 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_15 = eval_trilinear_point(model, A, B, C, 'sin(A +  pi  /3)', ID="X_15", classes=["center"])
    X_128 = eval_trilinear_point(model, A, B, C, '((sec(A))*(cos(2*B) + cos(2*C))*(1 + 2*cos(2*A))*(cos(2*A) + 2*cos(2*B)*cos(2*C)))', ID="X_128", classes=["center"])
    X_1154 = eval_trilinear_point(model, A, B, C, '(1 - 4*(cos(A))**(2))*cos(B - C)', ID="X_1154", classes=["center"])
    central_line(model, X_4, X_15, 4, 15)
    central_line(model, X_128, X_1154, 128, 1154)
    X_1527 = intersect_lines(model, X_4, X_15, X_128, X_1154, ID="X_1527", classes=["selected", "target"])
    return promote_point_to_top(model, X_1527)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1527 on the given reference triangle."""
    model = create_model('X_1527 = ORTHOJOIN OF X_18')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01527(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01527.json"))
    write_center_svg(
        model_acute,
        here / "x-01527.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
