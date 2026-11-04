"""GEOMETOR construction model for X_1106 = TRILINEAR SQUARE OF X_56."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01106(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1106 = TRILINEAR SQUARE OF X_56 on reference triangle ABC."""
    X_341 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*(b + c - a)**(2)', ID="X_341", classes=["center"])
    X_1106 = isogonal_conjugate(model, A, B, C, X_341, ID="X_1106", classes=["selected", "target"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    central_line(model, X_31, X_56, 31, 56, incident=True)
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center", "incident"])
    X_244 = eval_trilinear_point(model, A, B, C, '(b - c)**(2)', ID="X_244", classes=["center", "incident"])
    central_line(model, X_34, X_244, 34, 244, incident=True)
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_255 = eval_trilinear_point(model, A, B, C, '(cos(A))**(2)', ID="X_255", classes=["center", "incident"])
    central_line(model, X_36, X_255, 36, 255, incident=True)
    return promote_point_to_top(model, X_1106)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1106 on the given reference triangle."""
    model = create_model('X_1106 = TRILINEAR SQUARE OF X_56')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01106(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01106.json"))
    write_center_svg(
        model_acute,
        here / "x-01106.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
