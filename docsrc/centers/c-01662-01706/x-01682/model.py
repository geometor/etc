"""GEOMETOR construction model for X_1682 = INSIMILICENTER(INCIRCLE, APOLLONIUS CIRCLE)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    incenter_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01682(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1682 = INSIMILICENTER(INCIRCLE, APOLLONIUS CIRCLE) on reference triangle ABC."""
    X_1682 = eval_trilinear_point(model, A, B, C, '(s*cos(A/2) - r*sin(A/2))**(2)', ID="X_1682", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    central_line(model, X_10, X_11, 10, 11, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_181 = eval_trilinear_point(model, A, B, C, 'a*(b + c)**(2)/(b + c - a)', ID="X_181", classes=["center", "incident"])
    central_line(model, X_1, X_181, 1, 181, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_386 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) + b*c + c*a + a*b)', ID="X_386", classes=["center", "incident"])
    central_line(model, X_55, X_386, 55, 386, incident=True)
    return promote_point_to_top(model, X_1682)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1682 on the given reference triangle."""
    model = create_model('X_1682 = INSIMILICENTER(INCIRCLE, APOLLONIUS CIRCLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01682(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01682.json"))
    write_center_svg(
        model_acute,
        here / "x-01682.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
