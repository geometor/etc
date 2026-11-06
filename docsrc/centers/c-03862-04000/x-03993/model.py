"""GEOMETOR construction model for X_3993 = X_984com[INVERSE(n(INCENTRAL TRIANGLE))]."""

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
    incenter_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03993(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3993 = X_984com[INVERSE(n(INCENTRAL TRIANGLE))] on reference triangle ABC."""
    X_3993 = eval_barycentric_point(model, A, B, C, '((b + c)*(2*a**(2) + a*b + a*c - b*c))', ID="X_3993", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    central_line(model, X_10, X_37, 10, 37, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_87 = eval_trilinear_point(model, A, B, C, '1/(a*b + a*c - b*c)', ID="X_87", classes=["center", "incident"])
    central_line(model, X_1, X_87, 1, 87, incident=True)
    X_536 = eval_barycentric_point(model, A, B, C, '2*b*c - c*a - a*b', ID="X_536", classes=["center", "incident"])
    X_551 = eval_trilinear_point(model, A, B, C, '(4*a + b + c)/a', ID="X_551", classes=["center", "incident"])
    central_line(model, X_536, X_551, 536, 551, incident=True)
    return promote_point_to_top(model, X_3993)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3993 on the given reference triangle."""
    model = create_model('X_3993 = X_984com[INVERSE(n(INCENTRAL TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03993(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03993.json"))
    write_center_svg(
        model_acute,
        here / "x-03993.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
