"""GEOMETOR construction model for X_2592 = X_6-ISOCONJUGATE OF X_1822."""

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


def construct_x_02592(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2592 = X_6-ISOCONJUGATE OF X_1822 on reference triangle ABC."""
    X_297 = eval_trilinear_point(model, A, B, C, 'csc(2*A)*cos(A +  omega  )', ID="X_297", classes=["center"])
    X_525 = eval_trilinear_point(model, A, B, C, '(b*cos(B) - c*cos(C))/a', ID="X_525", classes=["center"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center"])
    X_1114 = eval_trilinear_point(model, A, B, C, '(R + d)*cos(A) - 2*R*cos(B)*cos(C)', ID="X_1114", classes=["center"])
    central_line(model, X_297, X_525, 297, 525)
    central_line(model, X_98, X_1114, 98, 1114)
    X_2592 = intersect_lines(model, X_297, X_525, X_98, X_1114, ID="X_2592", classes=["selected", "target"])
    X_262 = eval_trilinear_point(model, A, B, C, 'sec(A -  omega  )', ID="X_262", classes=["center", "incident"])
    X_1346 = eval_trilinear_point(model, A, B, C, '(R*cos(A) +  OH*cos(B - C) + 4*R*cos(B)*cos(C))', ID="X_1346", classes=["center", "incident"])
    central_line(model, X_262, X_1346, 262, 1346, incident=True)
    return promote_point_to_top(model, X_2592)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2592 on the given reference triangle."""
    model = create_model('X_2592 = X_6-ISOCONJUGATE OF X_1822')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02592(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02592.json"))
    write_center_svg(
        model_acute,
        here / "x-02592.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
