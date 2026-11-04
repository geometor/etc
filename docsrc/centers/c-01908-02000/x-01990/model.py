"""GEOMETOR construction model for X_1990 = ORTHIC-AXIS INTERCEPT OF LINE X_4X_6."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    midpoint,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01990(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1990 = ORTHIC-AXIS INTERCEPT OF LINE X_4X_6 on reference triangle ABC."""
    X_297 = eval_trilinear_point(model, A, B, C, 'csc(2*A)*cos(A + omega )', ID="X_297", classes=["center"])
    X_648 = eval_trilinear_point(model, A, B, C, '1/(a*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2)))', ID="X_648", classes=["center"])
    X_1990 = midpoint(model, X_297, X_648, ID="X_1990", classes=["selected", "target"], guide=False)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_4, X_6, 4, 6, incident=True)
    X_50 = eval_trilinear_point(model, A, B, C, 'sin(3*A)', ID="X_50", classes=["center", "incident"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center", "incident"])
    central_line(model, X_50, X_112, 50, 112, incident=True)
    X_140 = eval_trilinear_point(model, A, B, C, '2*cos(A) + cos(B - C)', ID="X_140", classes=["center", "incident"])
    X_216 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*cos(B - C)', ID="X_216", classes=["center", "incident"])
    central_line(model, X_140, X_216, 140, 216, incident=True)
    return promote_point_to_top(model, X_1990)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1990 on the given reference triangle."""
    model = create_model('X_1990 = ORTHIC-AXIS INTERCEPT OF LINE X_4X_6')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01990(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01990.json"))
    write_center_svg(
        model_acute,
        here / "x-01990.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
