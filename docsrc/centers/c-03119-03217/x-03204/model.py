"""GEOMETOR construction model for X_3204 = X_54-CEVA CONJUGATE OF X_55."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03204(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3204 = X_54-CEVA CONJUGATE OF X_55 on reference triangle ABC."""
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center"])
    X_3204 = ceva_conjugate(model, A, B, C, X_54, X_55, ID="X_3204", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    central_line(model, X_6, X_101, 6, 101, incident=True)
    X_45 = eval_trilinear_point(model, A, B, C, '2*b + 2*c - a', ID="X_45", classes=["center", "incident"])
    X_284 = eval_trilinear_point(model, A, B, C, '(sin(A))/(cos(B) + cos(C))', ID="X_284", classes=["center", "incident"])
    central_line(model, X_45, X_284, 45, 284, incident=True)
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center", "incident"])
    X_584 = eval_trilinear_point(model, A, B, C, '(a*(a*b**(2) + a*c**(2) + b*c**(2) + b**(2)*c + 2*a*b*c - a**(3)))', ID="X_584", classes=["center", "incident"])
    central_line(model, X_41, X_584, 41, 584, incident=True)
    return promote_point_to_top(model, X_3204)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3204 on the given reference triangle."""
    model = create_model('X_3204 = X_54-CEVA CONJUGATE OF X_55')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03204(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03204.json"))
    write_center_svg(
        model_acute,
        here / "x-03204.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
