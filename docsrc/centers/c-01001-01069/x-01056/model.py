"""GEOMETOR construction model for X_1056 = POINT ALCYONE."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01056(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1056 = POINT ALCYONE on reference triangle ABC."""
    X_1056 = eval_trilinear_point(model, A, B, C, '(2 + cos(B)*cos(C))', ID="X_1056", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    central_line(model, X_1, X_4, 1, 4, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_390 = eval_trilinear_point(model, A, B, C, 'b*c*(b + c - a)*(3*a**(2) + (b - c)**(2))', ID="X_390", classes=["center", "incident"])
    central_line(model, X_30, X_390, 30, 390, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_376 = eval_trilinear_point(model, A, B, C, '5*cos(A) - cos(B - C)', ID="X_376", classes=["center", "incident"])
    central_line(model, X_55, X_376, 55, 376, incident=True)
    return promote_point_to_top(model, X_1056)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1056 on the given reference triangle."""
    model = create_model('X_1056 = POINT ALCYONE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01056(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01056.json"))
    write_center_svg(
        model_acute,
        here / "x-01056.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
