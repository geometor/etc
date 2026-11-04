"""GEOMETOR construction model for X_1695 = INSIMILICENTER(BEVAN CIRCLE, APOLLONIUS CIRCLE)."""

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
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01695(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1695 = INSIMILICENTER(BEVAN CIRCLE, APOLLONIUS CIRCLE) on reference triangle ABC."""
    X_939 = eval_trilinear_point(model, A, B, C, '(a/(a**(4) - 2*a**(3)*(b + c) - 4*a**(2)*b*c + (b - c)*(b**(2) - c**(2))*(2*a - b - c)))', ID="X_939", classes=["center"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center"])
    X_1695 = ceva_conjugate(model, A, B, C, X_939, X_55, ID="X_1695", classes=["selected", "target"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center", "incident"])
    central_line(model, X_40, X_43, 40, 43, incident=True)
    X_165 = eval_trilinear_point(model, A, B, C, 'tan(B/2) + tan(C/2) - tan(A/2)', ID="X_165", classes=["center", "incident"])
    X_386 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) + b*c + c*a + a*b)', ID="X_386", classes=["center", "incident"])
    central_line(model, X_165, X_386, 165, 386, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_573 = eval_trilinear_point(model, A, B, C, 'cos(A + U)', ID="X_573", classes=["center", "incident"])
    central_line(model, X_1, X_573, 1, 573, incident=True)
    return promote_point_to_top(model, X_1695)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1695 on the given reference triangle."""
    model = create_model('X_1695 = INSIMILICENTER(BEVAN CIRCLE, APOLLONIUS CIRCLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01695(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01695.json"))
    write_center_svg(
        model_acute,
        here / "x-01695.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
