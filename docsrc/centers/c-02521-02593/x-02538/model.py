"""GEOMETOR construction model for X_2538 = INSIMILICENTER(APOLLONIUS CIRCLE, SPIEKER RADICAL CIRCLE)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nine_point_center_of,
    point_from_barycentrics,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02538(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2538 = INSIMILICENTER(APOLLONIUS CIRCLE, SPIEKER RADICAL CIRCLE) on reference triangle ABC."""
    X_2538 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c)*r*(r**(2) + s**(2))**(1/2) - a*(4*( area )**(2) + b*c*(r**(2) - s**(2))*cos(A)))', ID="X_2538", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    central_line(model, X_5, X_10, 5, 10, incident=True)
    X_181 = eval_trilinear_point(model, A, B, C, 'a*(b + c)**(2)/(b + c - a)', ID="X_181", classes=["center", "incident"])
    X_2534 = point_from_barycentrics(model, A, B, C, 0.29970374, 0.33333333, 0.36696293, ID="X_2534", classes=["center", "incident"])
    central_line(model, X_181, X_2534, 181, 2534, incident=True)
    X_386 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) + b*c + c*a + a*b)', ID="X_386", classes=["center", "incident"])
    X_2536 = point_from_barycentrics(model, A, B, C, 0.40205108, 0.36842473, 0.22952419, ID="X_2536", classes=["center", "incident"])
    central_line(model, X_386, X_2536, 386, 2536, incident=True)
    return promote_point_to_top(model, X_2538)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2538 on the given reference triangle."""
    model = create_model('X_2538 = INSIMILICENTER(APOLLONIUS CIRCLE, SPIEKER RADICAL CIRCLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02538(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02538.json"))
    write_center_svg(
        model_acute,
        here / "x-02538.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
