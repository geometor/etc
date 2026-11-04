"""GEOMETOR construction model for X_1285 = LEMOINE HOMOTHETIC CENTER."""

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
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01285(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1285 = LEMOINE HOMOTHETIC CENTER on reference triangle ABC."""
    X_1285 = eval_trilinear_point(model, A, B, C, '(b*c*(3*a**(2) + b**(2) - c**(2))*(3*a**(2) - b**(2) + c**(2)))', ID="X_1285", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    central_line(model, X_4, X_32, 4, 32, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_376 = eval_trilinear_point(model, A, B, C, '5*cos(A) - cos(B - C)', ID="X_376", classes=["center", "incident"])
    central_line(model, X_6, X_376, 6, 376, incident=True)
    X_497 = eval_trilinear_point(model, A, B, C, '1 - cos(B)*cos(C)', ID="X_497", classes=["center", "incident"])
    X_609 = eval_barycentric_point(model, A, B, C, 'a*( area + a**(2)*sin(A))', ID="X_609", classes=["center", "incident"])
    central_line(model, X_497, X_609, 497, 609, incident=True)
    return promote_point_to_top(model, X_1285)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1285 on the given reference triangle."""
    model = create_model('X_1285 = LEMOINE HOMOTHETIC CENTER')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01285(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01285.json"))
    write_center_svg(
        model_acute,
        here / "x-01285.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
