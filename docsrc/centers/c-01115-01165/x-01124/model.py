"""GEOMETOR construction model for X_1124 = ISOGONAL CONJUGATE OF X_1123."""

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
    isogonal_conjugate,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01124(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1124 = ISOGONAL CONJUGATE OF X_1123 on reference triangle ABC."""
    X_1123 = eval_trilinear_point(model, A, B, C, '1/(1 +sin(A))', ID="X_1123", classes=["center"])
    X_1124 = isogonal_conjugate(model, A, B, C, X_1123, ID="X_1124", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_372 = eval_trilinear_point(model, A, B, C, 'cos(A + pi /4)', ID="X_372", classes=["center", "incident"])
    central_line(model, X_55, X_372, 55, 372, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_371 = eval_trilinear_point(model, A, B, C, 'cos(A - pi /4)', ID="X_371", classes=["center", "incident"])
    central_line(model, X_56, X_371, 56, 371, incident=True)
    return promote_point_to_top(model, X_1124)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1124 on the given reference triangle."""
    model = create_model('X_1124 = ISOGONAL CONJUGATE OF X_1123')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01124(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01124.json"))
    write_center_svg(
        model_acute,
        here / "x-01124.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
