"""GEOMETOR construction model for X_3046 = INTERSECTION X_54X_118∩X_101X_184."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03046(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3046 = INTERSECTION X_54X_118∩X_101X_184 on reference triangle ABC."""
    X_3046 = eval_trilinear_point(model, A, B, C, '(a**(3)*(a**(3) + b**(3) - c**(3) - a**(2)*b - a*b**(2) + b*c**(2))*(a**(3) - b**(3) + c**(3) - a**(2)*c - a*c**(2) + b**(2)*c))', ID="X_3046", classes=["selected", "target"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    X_118 = point_from_barycentrics(model, A, B, C, 0.28918651, -0.056547619, 0.76736111, ID="X_118", classes=["center", "incident"])
    central_line(model, X_54, X_118, 54, 118, incident=True)
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    central_line(model, X_101, X_184, 101, 184, incident=True)
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X_103", classes=["center", "incident"])
    X_1147 = eval_trilinear_point(model, A, B, C, '(sin(4*A))/sin(A)', ID="X_1147", classes=["center", "incident"])
    central_line(model, X_103, X_1147, 103, 1147, incident=True)
    return promote_point_to_top(model, X_3046)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3046 on the given reference triangle."""
    model = create_model('X_3046 = INTERSECTION X_54X_118∩X_101X_184')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03046(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03046.json"))
    write_center_svg(
        model_acute,
        here / "x-03046.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
