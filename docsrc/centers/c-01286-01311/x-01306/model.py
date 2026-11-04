"""GEOMETOR construction model for X_1306 = COLLINGS TRANSFORM OF X_639."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01306(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1306 = COLLINGS TRANSFORM OF X_639 on reference triangle ABC."""
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X_111", classes=["center"])
    X_493 = eval_trilinear_point(model, A, B, C, '1/(sin(A) + sin(B)*sin(C))', ID="X_493", classes=["center"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center"])
    X_637 = point_from_barycentrics(model, A, B, C, 0.40143148, 0.29769606, 0.30087247, ID="X_637", classes=["center"])
    central_line(model, X_111, X_493, 111, 493)
    central_line(model, X_98, X_637, 98, 637)
    X_1306 = intersect_lines(model, X_111, X_493, X_98, X_637, ID="X_1306", classes=["selected", "target"])
    return promote_point_to_top(model, X_1306)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1306 on the given reference triangle."""
    model = create_model('X_1306 = COLLINGS TRANSFORM OF X_639')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01306(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01306.json"))
    write_center_svg(
        model_acute,
        here / "x-01306.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
