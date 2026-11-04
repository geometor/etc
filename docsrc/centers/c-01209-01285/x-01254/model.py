"""GEOMETOR construction model for X_1254 = ISOGONAL CONJUGATE OF X_1098."""

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


def construct_x_01254(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1254 = ISOGONAL CONJUGATE OF X_1098 on reference triangle ABC."""
    X_1098 = eval_trilinear_point(model, A, B, C, '(1/(cos(B) + cos(C))**(2))', ID="X_1098", classes=["center"])
    X_1254 = isogonal_conjugate(model, A, B, C, X_1098, ID="X_1254", classes=["selected", "target"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center", "incident"])
    central_line(model, X_31, X_34, 31, 34, incident=True)
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    central_line(model, X_42, X_65, 42, 65, incident=True)
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    X_201 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 + cos(B - C))', ID="X_201", classes=["center", "incident"])
    central_line(model, X_12, X_201, 12, 201, incident=True)
    return promote_point_to_top(model, X_1254)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1254 on the given reference triangle."""
    model = create_model('X_1254 = ISOGONAL CONJUGATE OF X_1098')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01254(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01254.json"))
    write_center_svg(
        model_acute,
        here / "x-01254.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
