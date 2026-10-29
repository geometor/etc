"""GEOMETOR construction model for X(927) = ISOGONAL CONJUGATE OF X(926)."""

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


def construct_x_00927(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(927) = ISOGONAL CONJUGATE OF X(926) on reference triangle ABC."""
    X_926 = eval_trilinear_point(model, A, B, C, 'a*(a - b - c)*(b - c)*(a*b + a*c - b**(2) - c**(2))', ID="X(926)", classes=["center"])
    X_927 = isogonal_conjugate(model, A, B, C, X_926, ID="X(927)", classes=["selected", "target"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center", "incident"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X(514)", classes=["center", "incident"])
    central_line(model, X_101, X_514, 101, 514, incident=True)
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X(103)", classes=["center", "incident"])
    X_516 = eval_trilinear_point(model, A, B, C, 'b*c*((a - b)*cot(C) + (a - c)*cot(B))', ID="X(516)", classes=["center", "incident"])
    central_line(model, X_103, X_516, 103, 516, incident=True)
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X(109)", classes=["center", "incident"])
    X_658 = eval_trilinear_point(model, A, B, C, '1/((1 + cos(A))*(cos(B) - cos(C)))', ID="X(658)", classes=["center", "incident"])
    central_line(model, X_109, X_658, 109, 658, incident=True)
    return promote_point_to_top(model, X_927)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(927) on the given reference triangle."""
    model = create_model('X(927) = ISOGONAL CONJUGATE OF X(926)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00927(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00927.json"))
    write_center_svg(
        model_acute,
        here / "x-00927.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
