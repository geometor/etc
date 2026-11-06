"""GEOMETOR construction model for X_3958 = X_2294com[INVERSE(n(EXTANGENTS TRIANGLE))]."""

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


def construct_x_03958(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3958 = X_2294com[INVERSE(n(EXTANGENTS TRIANGLE))] on reference triangle ABC."""
    X_3958 = eval_barycentric_point(model, A, B, C, '(a*(b + c)*(2*a + b + c)*(b**(2) + c**(2) - a**(2)))', ID="X_3958", classes=["selected", "target"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    central_line(model, X_48, X_63, 48, 63, incident=True)
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center", "incident"])
    X_72 = eval_trilinear_point(model, A, B, C, '(b + c)*cot(A)', ID="X_72", classes=["center", "incident"])
    central_line(model, X_71, X_72, 71, 72, incident=True)
    X_191 = eval_trilinear_point(model, A, B, C, '(b + c - a)*(b*c + c*a + a*b) + b**(3) + c**(3) - a**(3)', ID="X_191", classes=["center", "incident"])
    X_284 = eval_trilinear_point(model, A, B, C, '(sin(A))/(cos(B) + cos(C))', ID="X_284", classes=["center", "incident"])
    central_line(model, X_191, X_284, 191, 284, incident=True)
    return promote_point_to_top(model, X_3958)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3958 on the given reference triangle."""
    model = create_model('X_3958 = X_2294com[INVERSE(n(EXTANGENTS TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03958(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03958.json"))
    write_center_svg(
        model_acute,
        here / "x-03958.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
