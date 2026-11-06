"""GEOMETOR construction model for X_3415 = X_1-VERTEX CONJUGATE OF X_2."""

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


def construct_x_03415(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3415 = X_1-VERTEX CONJUGATE OF X_2 on reference triangle ABC."""
    X_3415 = eval_barycentric_point(model, A, B, C, '(a**(2)/(a**(3) - (b + c)*(b**(2) + c**(2))))', ID="X_3415", classes=["selected", "target"])
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X_22", classes=["center", "incident"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    central_line(model, X_22, X_55, 22, 55, incident=True)
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center", "incident"])
    X_386 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) + b*c + c*a + a*b)', ID="X_386", classes=["center", "incident"])
    central_line(model, X_41, X_386, 41, 386, incident=True)
    return promote_point_to_top(model, X_3415)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3415 on the given reference triangle."""
    model = create_model('X_3415 = X_1-VERTEX CONJUGATE OF X_2')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03415(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03415.json"))
    write_center_svg(
        model_acute,
        here / "x-03415.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
