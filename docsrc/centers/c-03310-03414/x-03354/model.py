"""GEOMETOR construction model for X_3354 = ISOGONAL CONJUGATE OF X_3353."""

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


def construct_x_03354(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3354 = ISOGONAL CONJUGATE OF X_3353 on reference triangle ABC."""
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center"])
    X_2130 = point_from_barycentrics(model, A, B, C, 0.19373197, 0.27423005, 0.53203798, ID="X_2130", classes=["center"])
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center"])
    X_3353 = point_from_barycentrics(model, A, B, C, 0.040677939, 0.071839896, 0.88748216, ID="X_3353", classes=["center"])
    central_line(model, X_40, X_2130, 40, 2130)
    central_line(model, X_20, X_3353, 20, 3353)
    X_3354 = intersect_lines(model, X_40, X_2130, X_20, X_3353, ID="X_3354", classes=["selected", "target"])
    X_1490 = eval_trilinear_point(model, A, B, C, '1 + sec(A) - sec(B) - sec(C)', ID="X_1490", classes=["center", "incident"])
    X_3183 = point_from_barycentrics(model, A, B, C, -0.24902136, -0.46731562, 1.716337, ID="X_3183", classes=["center", "incident"])
    central_line(model, X_1490, X_3183, 1490, 3183, incident=True)
    return promote_point_to_top(model, X_3354)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3354 on the given reference triangle."""
    model = create_model('X_3354 = ISOGONAL CONJUGATE OF X_3353')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03354(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03354.json"))
    write_center_svg(
        model_acute,
        here / "x-03354.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
