"""GEOMETOR construction model for X_1015 = EXSIMILICENTER OF MOSES CIRCLE AND INCIRCLE."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01015(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1015 = EXSIMILICENTER OF MOSES CIRCLE AND INCIRCLE on reference triangle ABC."""
    X_1015 = eval_trilinear_point(model, A, B, C, 'a*(b - c)**(2)', ID="X_1015", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    central_line(model, X_1, X_39, 1, 39, incident=True)
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    central_line(model, X_32, X_56, 32, 56, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    central_line(model, X_6, X_101, 6, 101, incident=True)
    return promote_point_to_top(model, X_1015)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1015 on the given reference triangle."""
    model = create_model('X_1015 = EXSIMILICENTER OF MOSES CIRCLE AND INCIRCLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01015(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01015.json"))
    write_center_svg(
        model_acute,
        here / "x-01015.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
