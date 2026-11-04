"""GEOMETOR construction model for X_1282 = 5th SHARYGIN POINT."""

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
    intersect_lines,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01282(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1282 = 5th SHARYGIN POINT on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center"])
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    central_line(model, X_1, X_41, 1, 41)
    central_line(model, X_43, X_57, 43, 57)
    X_1282 = intersect_lines(model, X_1, X_41, X_43, X_57, ID="X_1282", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_150 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(4) + c**(4) - a**(4) + a*(b*c**(2) +c*b**(2) - b**(3) - c**(3)) - b*c*(a**(2) + b**(2) + c**(2)) + (b + c)*a**(3)))', ID="X_150", classes=["center", "incident"])
    central_line(model, X_10, X_150, 10, 150, incident=True)
    return promote_point_to_top(model, X_1282)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1282 on the given reference triangle."""
    model = create_model('X_1282 = 5th SHARYGIN POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01282(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01282.json"))
    write_center_svg(
        model_acute,
        here / "x-01282.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
