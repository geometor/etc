"""GEOMETOR construction model for X_2593 = X_6-ISOCONJUGATE OF X_1823."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02593(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2593 = X_6-ISOCONJUGATE OF X_1823 on reference triangle ABC."""
    X_297 = eval_trilinear_point(model, A, B, C, 'csc(2*A)*cos(A +  omega  )', ID="X_297", classes=["center"])
    X_525 = eval_trilinear_point(model, A, B, C, '(b*cos(B) - c*cos(C))/a', ID="X_525", classes=["center"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center"])
    X_1113 = eval_trilinear_point(model, A, B, C, '(R - d)*cos(A) - 2*R*cos(B)*cos(C)', ID="X_1113", classes=["center"])
    central_line(model, X_297, X_525, 297, 525)
    central_line(model, X_98, X_1113, 98, 1113)
    X_2593 = intersect_lines(model, X_297, X_525, X_98, X_1113, ID="X_2593", classes=["selected", "target"])
    X_262 = eval_trilinear_point(model, A, B, C, 'sec(A -  omega  )', ID="X_262", classes=["center", "incident"])
    X_1347 = eval_trilinear_point(model, A, B, C, '(R*cos(A) -  OH*cos(B - C) + 4*R*cos(B)*cos(C))', ID="X_1347", classes=["center", "incident"])
    central_line(model, X_262, X_1347, 262, 1347, incident=True)
    return promote_point_to_top(model, X_2593)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2593 on the given reference triangle."""
    model = create_model('X_2593 = X_6-ISOCONJUGATE OF X_1823')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02593(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02593.json"))
    write_center_svg(
        model_acute,
        here / "x-02593.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
