"""GEOMETOR construction model for X_3913 = X_10com[INVERSE(n(INTOUCH TRIANGLE))]."""

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
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03913(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3913 = X_10com[INVERSE(n(INTOUCH TRIANGLE))] on reference triangle ABC."""
    X_3913 = eval_barycentric_point(model, A, B, C, '(a*(b + c - a)*(a**(2) + a*b + a*c - 2*b*c))', ID="X_3913", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    central_line(model, X_8, X_21, 8, 21, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    central_line(model, X_56, X_100, 56, 100, incident=True)
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    X_224 = eval_trilinear_point(model, A, B, C, '(cot(B)*(cos(B/2))**(2) + cot(C)*(cos(C/2))**(2) - cot(A)*(cos(A/2))**(2))*cot(A)', ID="X_224", classes=["center", "incident"])
    central_line(model, X_65, X_224, 65, 224, incident=True)
    return promote_point_to_top(model, X_3913)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3913 on the given reference triangle."""
    model = create_model('X_3913 = X_10com[INVERSE(n(INTOUCH TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03913(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03913.json"))
    write_center_svg(
        model_acute,
        here / "x-03913.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
