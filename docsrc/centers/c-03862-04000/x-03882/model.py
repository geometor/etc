"""GEOMETOR construction model for X_3882 = X_2486com[INVERSE(n(3rd EULER TRIANGLE))]."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03882(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3882 = X_2486com[INVERSE(n(3rd EULER TRIANGLE))] on reference triangle ABC."""
    X_3882 = eval_barycentric_point(model, A, B, C, '(a*(a - b)*(a - c)*(b**(2) + c**(2) + a*b + a*c))', ID="X_3882", classes=["selected", "target"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    central_line(model, X_100, X_109, 100, 109, incident=True)
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    X_573 = eval_trilinear_point(model, A, B, C, 'cos(A + U)', ID="X_573", classes=["center", "incident"])
    central_line(model, X_69, X_573, 69, 573, incident=True)
    X_193 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cot(B) + cot(C) - cot(A))', ID="X_193", classes=["center", "incident"])
    X_579 = eval_trilinear_point(model, A, B, C, '(a*(a**(2)*b + a**(2)*c + a*b*c - b**(3) - c**(3)))', ID="X_579", classes=["center", "incident"])
    central_line(model, X_193, X_579, 193, 579, incident=True)
    return promote_point_to_top(model, X_3882)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3882 on the given reference triangle."""
    model = create_model('X_3882 = X_2486com[INVERSE(n(3rd EULER TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03882(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03882.json"))
    write_center_svg(
        model_acute,
        here / "x-03882.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
