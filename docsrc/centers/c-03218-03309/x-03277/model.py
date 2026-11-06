"""GEOMETOR construction model for X_3277 = CENTER OF 3rd MORLEY TRIANGLE."""

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


def construct_x_03277(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3277 = CENTER OF 3rd MORLEY TRIANGLE on reference triangle ABC."""
    X_3277 = eval_trilinear_point(model, A, B, C, 'cos(A/3 - 4*pi  /3) + 2*cos(B/3 - 4*pi  /3)*cos(C/3 - 4*pi  /3)', ID="X_3277", classes=["selected", "target"])
    X_356 = eval_trilinear_point(model, A, B, C, 'cos(A/3) + 2*cos(B/3)*cos(C/3)', ID="X_356", classes=["center", "incident"])
    X_1134 = eval_trilinear_point(model, A, B, C, '1/cos(A/3 + 2*pi  /3)', ID="X_1134", classes=["center", "incident"])
    central_line(model, X_356, X_1134, 356, 1134, incident=True)
    X_1136 = eval_trilinear_point(model, A, B, C, '1/cos(A/3 + 4*pi  /3)', ID="X_1136", classes=["center", "incident"])
    X_1137 = eval_trilinear_point(model, A, B, C, '(cos(A/3 + 4*pi  /3))', ID="X_1137", classes=["center", "incident"])
    central_line(model, X_1136, X_1137, 1136, 1137, incident=True)
    X_3272 = eval_trilinear_point(model, A, B, C, 'cos(B/3 - C/3)', ID="X_3272", classes=["center", "incident"])
    X_3275 = eval_trilinear_point(model, A, B, C, 'sin(A/3)', ID="X_3275", classes=["center", "incident"])
    central_line(model, X_3272, X_3275, 3272, 3275, incident=True)
    return promote_point_to_top(model, X_3277)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3277 on the given reference triangle."""
    model = create_model('X_3277 = CENTER OF 3rd MORLEY TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03277(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03277.json"))
    write_center_svg(
        model_acute,
        here / "x-03277.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
