"""GEOMETOR construction model for X_3021 = 5th STEVANOVIC POINT."""

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
    feuerbach_point_of,
    gergonne_point_of,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03021(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3021 = 5th STEVANOVIC POINT on reference triangle ABC."""
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center"])
    X_3008 = eval_trilinear_point(model, A, B, C, '(b*c*((b - c)**(2) + 2*a**(2) - a*b - a*c))', ID="X_3008", classes=["center"])
    X_3021 = ceva_conjugate(model, A, B, C, X_7, X_3008, ID="X_3021", classes=["selected", "target"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    central_line(model, X_11, X_55, 11, 55, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_1292 = eval_trilinear_point(model, A, B, C, '1/((b - c)*(a**(2) + b**(2) + c**(2) - 2*a*b - 2*a*c))', ID="X_1292", classes=["center", "incident"])
    central_line(model, X_56, X_1292, 56, 1292, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_1358 = eval_trilinear_point(model, A, B, C, '(tan(A/2))**(2)*(sin(B/2 - C/2))**(2)', ID="X_1358", classes=["center", "incident"])
    central_line(model, X_1, X_1358, 1, 1358, incident=True)
    return promote_point_to_top(model, X_3021)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3021 on the given reference triangle."""
    model = create_model('X_3021 = 5th STEVANOVIC POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03021(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03021.json"))
    write_center_svg(
        model_acute,
        here / "x-03021.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
