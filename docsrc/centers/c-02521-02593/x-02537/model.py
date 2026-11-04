"""GEOMETOR construction model for X_2537 = EXSIMILICENTER(CIRCUMCIRCLE, SPIEKER RADICAL CIRCLE)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02537(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2537 = EXSIMILICENTER(CIRCUMCIRCLE, SPIEKER RADICAL CIRCLE) on reference triangle ABC."""
    X_573 = eval_trilinear_point(model, A, B, C, 'cos(A + U)', ID="X_573", classes=["center"])
    X_2536 = point_from_barycentrics(model, A, B, C, 0.40205108, 0.36842473, 0.22952419, ID="X_2536", classes=["center"])
    X_2537 = ceva_conjugate(model, A, B, C, X_573, X_2536, ID="X_2537", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    central_line(model, X_3, X_10, 3, 10, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_2534 = point_from_barycentrics(model, A, B, C, 0.29970374, 0.33333333, 0.36696293, ID="X_2534", classes=["center", "incident"])
    central_line(model, X_55, X_2534, 55, 2534, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_2535 = point_from_barycentrics(model, A, B, C, 0.2314987, 0.33333333, 0.43516797, ID="X_2535", classes=["center", "incident"])
    central_line(model, X_56, X_2535, 56, 2535, incident=True)
    return promote_point_to_top(model, X_2537)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2537 on the given reference triangle."""
    model = create_model('X_2537 = EXSIMILICENTER(CIRCUMCIRCLE, SPIEKER RADICAL CIRCLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02537(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02537.json"))
    write_center_svg(
        model_acute,
        here / "x-02537.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
