"""GEOMETOR construction model for X_2038 = 2nd BROCARD-AXIS-APOLLONIUS-CIRCLE INTERSECTION."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
    spieker_center_of,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02038(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2038 = 2nd BROCARD-AXIS-APOLLONIUS-CIRCLE INTERSECTION on reference triangle ABC."""
    X_2037 = point_from_barycentrics(model, A, B, C, -1.0381449, -0.09234361, 2.1304885, ID="X_2037", classes=["center"])
    X_970 = eval_trilinear_point(model, A, B, C, 'a*(a**(3)*(b + c)**(2) + a*(a*b + a*c - 2*b*c)*(b**(2) + c**(2)) - b*c*(b**(3) + c**(3)) - a*(b**(4) + c**(4)) - (b**(5) + c**(5)))', ID="X_970", classes=["center"])
    X_2038 = reflection_in_point(model, X_2037, X_970, ID="X_2038", classes=["selected", "target"], guide=False)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_2040 = eval_trilinear_point(model, A, B, C, 'e*cos(A) + 2*e*cos(B)*cos(C) - cos(A +  omega  )', ID="X_2040", classes=["center", "incident"])
    central_line(model, X_10, X_2040, 10, 2040, incident=True)
    X_2039 = eval_trilinear_point(model, A, B, C, 'e*cos(A) + 2*e*cos(B)*cos(C) + cos(A +  omega  )', ID="X_2039", classes=["center", "incident"])
    X_2051 = eval_trilinear_point(model, A, B, C, 'sec(A - U)', ID="X_2051", classes=["center", "incident"])
    central_line(model, X_2039, X_2051, 2039, 2051, incident=True)
    return promote_point_to_top(model, X_2038)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2038 on the given reference triangle."""
    model = create_model('X_2038 = 2nd BROCARD-AXIS-APOLLONIUS-CIRCLE INTERSECTION')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02038(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02038.json"))
    write_center_svg(
        model_acute,
        here / "x-02038.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
