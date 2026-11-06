"""GEOMETOR construction model for X_3611 = 2nd AYME-MOSES PERSPECTOR."""

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


def construct_x_03611(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3611 = 2nd AYME-MOSES PERSPECTOR on reference triangle ABC."""
    X_3611 = eval_trilinear_point(model, A, B, C, '(a*(b + c)*(b**(2) + c**(2) - a**(2))*(a**(3)*(b + c) + (b - c)**(2)*(b**(2) + c**(2) - a**(2) - a*b - a*c + 2*b*c)))', ID="X_3611", classes=["selected", "target"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X_51", classes=["center", "incident"])
    central_line(model, X_19, X_51, 19, 51, incident=True)
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    X_185 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 - cos(A)*cos(B - C))', ID="X_185", classes=["center", "incident"])
    central_line(model, X_40, X_185, 40, 185, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    central_line(model, X_55, X_184, 55, 184, incident=True)
    return promote_point_to_top(model, X_3611)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3611 on the given reference triangle."""
    model = create_model('X_3611 = 2nd AYME-MOSES PERSPECTOR')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03611(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03611.json"))
    write_center_svg(
        model_acute,
        here / "x-03611.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
