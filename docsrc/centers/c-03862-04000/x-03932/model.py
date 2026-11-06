"""GEOMETOR construction model for X_3932 = X_1279com[INVERSE(n(INCENTRAL TRIANGLE))]."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03932(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3932 = X_1279com[INVERSE(n(INCENTRAL TRIANGLE))] on reference triangle ABC."""
    X_3932 = eval_barycentric_point(model, A, B, C, '((b + c)*(b**(2) + c**(2) - a*b - a*c))', ID="X_3932", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    central_line(model, X_10, X_37, 10, 37, incident=True)
    X_23 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X_23", classes=["center", "incident"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    central_line(model, X_23, X_100, 23, 100, incident=True)
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    X_313 = eval_trilinear_point(model, A, B, C, '(b + c)*b**(3)*c**(3)', ID="X_313", classes=["center", "incident"])
    central_line(model, X_12, X_313, 12, 313, incident=True)
    return promote_point_to_top(model, X_3932)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3932 on the given reference triangle."""
    model = create_model('X_3932 = X_1279com[INVERSE(n(INCENTRAL TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03932(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03932.json"))
    write_center_svg(
        model_acute,
        here / "x-03932.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
