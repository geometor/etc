"""GEOMETOR construction model for X_3413 = 1st KIEPERT INFINITY POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03413(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3413 = 1st KIEPERT INFINITY POINT on reference triangle ABC."""
    X_1379 = point_from_barycentrics(model, A, B, C, -0.11245297, 0.21461865, 0.89783432, ID="X_1379", classes=["center"])
    X_3413 = isogonal_conjugate(model, A, B, C, X_1379, ID="X_3413", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_1341 = point_from_barycentrics(model, A, B, C, 0.30653192, 0.35355532, 0.33991277, ID="X_1341", classes=["center", "incident"])
    central_line(model, X_2, X_1341, 2, 1341, incident=True)
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center", "incident"])
    X_1380 = eval_trilinear_point(model, A, B, C, 'e*cos(A) + cos(A +  omega  )', ID="X_1380", classes=["center", "incident"])
    central_line(model, X_98, X_1380, 98, 1380, incident=True)
    return promote_point_to_top(model, X_3413)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3413 on the given reference triangle."""
    model = create_model('X_3413 = 1st KIEPERT INFINITY POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03413(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03413.json"))
    write_center_svg(
        model_acute,
        here / "x-03413.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
