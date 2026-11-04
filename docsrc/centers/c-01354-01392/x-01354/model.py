"""GEOMETOR construction model for X_1354 = BRISSE TRANSFORM OF X_74."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01354(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1354 = BRISSE TRANSFORM OF X_74 on reference triangle ABC."""
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center"])
    X_759 = eval_trilinear_point(model, A, B, C, '(1/(a**(0)*(b**(3) + c**(3)) - a**(2)*(b**(1) + c**(1))))', ID="X_759", classes=["center"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center"])
    X_1367 = point_from_barycentrics(model, A, B, C, 0.34721271, 0.6328996, 0.019887687, ID="X_1367", classes=["center"])
    central_line(model, X_56, X_759, 56, 759)
    central_line(model, X_7, X_1367, 7, 1367)
    X_1354 = intersect_lines(model, X_56, X_759, X_7, X_1367, ID="X_1354", classes=["selected", "target"])
    X_942 = eval_trilinear_point(model, A, B, C, '2*a*b*c + (b + c)*(a - b + c)*(a + b -c)', ID="X_942", classes=["center", "incident"])
    X_1364 = eval_trilinear_point(model, A, B, C, 'csc(A)*tan(A/2) / (sec(B) - sec(C))', ID="X_1364", classes=["center", "incident"])
    central_line(model, X_942, X_1364, 942, 1364, incident=True)
    return promote_point_to_top(model, X_1354)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1354 on the given reference triangle."""
    model = create_model('X_1354 = BRISSE TRANSFORM OF X_74')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01354(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01354.json"))
    write_center_svg(
        model_acute,
        here / "x-01354.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
