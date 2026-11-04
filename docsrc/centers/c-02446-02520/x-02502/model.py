"""GEOMETOR construction model for X_2502 = RADICAL CENTER OF {CIRCUMCIRCLE, BROCARD CIRCLE, PARRY CIRCLE}."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02502(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2502 = RADICAL CENTER OF {CIRCUMCIRCLE, BROCARD CIRCLE, PARRY CIRCLE} on reference triangle ABC."""
    X_583 = eval_trilinear_point(model, A, B, C, '(a*(a**(2)*b + a**(2)*c + 2*a*b*c - b**(3) - c**(3)))', ID="X_583", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_2502 = ceva_conjugate(model, A, B, C, X_583, X_6, ID="X_2502", classes=["selected", "target"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_6, X_110, 6, 110, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_353 = eval_trilinear_point(model, A, B, C, '(a*(4*a**(4) - 2*b**(4) - 2*c**(4) - b**(2)*c**(2) - 4*a**(2)*b**(2) -4*a**(2)*c**(2)))', ID="X_353", classes=["center", "incident"])
    central_line(model, X_2, X_353, 2, 353, incident=True)
    X_23 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X_23", classes=["center", "incident"])
    X_352 = eval_trilinear_point(model, A, B, C, '(a*(-a**(4) - b**(4) - c**(4) - 5*b**(2)*c**(2) + 4*a**(2)*b**(2) + 4*a**(2)*c**(2)))', ID="X_352", classes=["center", "incident"])
    central_line(model, X_23, X_352, 23, 352, incident=True)
    return promote_point_to_top(model, X_2502)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2502 on the given reference triangle."""
    model = create_model('X_2502 = RADICAL CENTER OF {CIRCUMCIRCLE, BROCARD CIRCLE, PARRY CIRCLE}')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02502(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02502.json"))
    write_center_svg(
        model_acute,
        here / "x-02502.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
