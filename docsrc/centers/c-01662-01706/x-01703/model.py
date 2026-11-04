"""GEOMETOR construction model for X_1703 = EXSIMILICENTER(BEVAN CIRCLE, 2nd LEMOINE CIRCLE)."""

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


def construct_x_01703(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1703 = EXSIMILICENTER(BEVAN CIRCLE, 2nd LEMOINE CIRCLE) on reference triangle ABC."""
    X_1703 = eval_trilinear_point(model, A, B, C, '(2*sin(A) - cos(A) + cos(B) + cos(C) - 1)', ID="X_1703", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    central_line(model, X_6, X_40, 6, 40, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_372 = eval_trilinear_point(model, A, B, C, 'cos(A + pi /4)', ID="X_372", classes=["center", "incident"])
    central_line(model, X_1, X_372, 1, 372, incident=True)
    X_165 = eval_trilinear_point(model, A, B, C, 'tan(B/2) + tan(C/2) - tan(A/2)', ID="X_165", classes=["center", "incident"])
    X_371 = eval_trilinear_point(model, A, B, C, 'cos(A - pi /4)', ID="X_371", classes=["center", "incident"])
    central_line(model, X_165, X_371, 165, 371, incident=True)
    return promote_point_to_top(model, X_1703)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1703 on the given reference triangle."""
    model = create_model('X_1703 = EXSIMILICENTER(BEVAN CIRCLE, 2nd LEMOINE CIRCLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01703(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01703.json"))
    write_center_svg(
        model_acute,
        here / "x-01703.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
