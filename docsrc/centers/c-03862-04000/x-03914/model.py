"""GEOMETOR construction model for X_3914 = X_31com(ORTHIC TRIANGLE)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03914(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3914 = X_31com(ORTHIC TRIANGLE) on reference triangle ABC."""
    X_3914 = eval_barycentric_point(model, A, B, C, '(b + c)*(a**(2) + b**(2) + c**(2) - 2*b*c)', ID="X_3914", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_224 = eval_trilinear_point(model, A, B, C, '(cot(B)*(cos(B/2))**(2) + cot(C)*(cos(C/2))**(2) - cot(A)*(cos(A/2))**(2))*cot(A)', ID="X_224", classes=["center", "incident"])
    central_line(model, X_1, X_224, 1, 224, incident=True)
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X_226", classes=["center", "incident"])
    central_line(model, X_42, X_226, 42, 226, incident=True)
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    X_225 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cos(B) + cos(C))', ID="X_225", classes=["center", "incident"])
    central_line(model, X_65, X_225, 65, 225, incident=True)
    return promote_point_to_top(model, X_3914)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3914 on the given reference triangle."""
    model = create_model('X_3914 = X_31com(ORTHIC TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03914(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03914.json"))
    write_center_svg(
        model_acute,
        here / "x-03914.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
