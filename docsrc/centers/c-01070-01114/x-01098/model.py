"""GEOMETOR construction model for X_1098 = TRILINEAR SQUARE OF X_21."""

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


def construct_x_01098(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1098 = TRILINEAR SQUARE OF X_21 on reference triangle ABC."""
    X_1098 = eval_trilinear_point(model, A, B, C, '(1/(cos(B) + cos(C))**(2))', ID="X_1098", classes=["selected", "target"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    X_60 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(B - C))', ID="X_60", classes=["center", "incident"])
    central_line(model, X_21, X_60, 21, 60, incident=True)
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X_86", classes=["center", "incident"])
    central_line(model, X_58, X_86, 58, 86, incident=True)
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X_29", classes=["center", "incident"])
    X_270 = eval_trilinear_point(model, A, B, C, '(sec(A))/(1 + cos(B - C))', ID="X_270", classes=["center", "incident"])
    central_line(model, X_29, X_270, 29, 270, incident=True)
    return promote_point_to_top(model, X_1098)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1098 on the given reference triangle."""
    model = create_model('X_1098 = TRILINEAR SQUARE OF X_21')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01098(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01098.json"))
    write_center_svg(
        model_acute,
        here / "x-01098.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
