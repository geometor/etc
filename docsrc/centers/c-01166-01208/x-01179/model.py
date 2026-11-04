"""GEOMETOR construction model for X_1179 = 1st SARAGOSSA POINT OF X_96."""

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
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01179(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1179 = 1st SARAGOSSA POINT OF X_96 on reference triangle ABC."""
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X_24", classes=["center"])
    X_264 = eval_trilinear_point(model, A, B, C, 'csc(A)*csc(2*A)', ID="X_264", classes=["center"])
    X_93 = eval_trilinear_point(model, A, B, C, 'sec(3*A)', ID="X_93", classes=["center"])
    X_324 = eval_trilinear_point(model, A, B, C, 'b*c*sec(A)*cos(B - C)', ID="X_324", classes=["center"])
    central_line(model, X_24, X_264, 24, 264)
    central_line(model, X_93, X_324, 93, 324)
    X_1179 = intersect_lines(model, X_24, X_264, X_93, X_324, ID="X_1179", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_569 = point_from_barycentrics(model, A, B, C, 0.2994203, 0.35119708, 0.34938262, ID="X_569", classes=["center", "incident"])
    central_line(model, X_4, X_569, 4, 569, incident=True)
    return promote_point_to_top(model, X_1179)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1179 on the given reference triangle."""
    model = create_model('X_1179 = 1st SARAGOSSA POINT OF X_96')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01179(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01179.json"))
    write_center_svg(
        model_acute,
        here / "x-01179.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
