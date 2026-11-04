"""GEOMETOR construction model for X_1166 = 1st SARAGOSSA POINT OF X_5."""

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
    intersect_lines,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01166(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1166 = 1st SARAGOSSA POINT OF X_5 on reference triangle ABC."""
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center"])
    X_96 = eval_trilinear_point(model, A, B, C, 'sec(2*A)*sec(B - C)', ID="X_96", classes=["center"])
    X_52 = eval_trilinear_point(model, A, B, C, 'cos(2*A)*cos(B - C)', ID="X_52", classes=["center"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center"])
    central_line(model, X_5, X_96, 5, 96)
    central_line(model, X_52, X_54, 52, 54)
    X_1166 = intersect_lines(model, X_5, X_96, X_52, X_54, ID="X_1166", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_252 = eval_trilinear_point(model, A, B, C, '(sec(B - C)/(1 - 2*cos(2*A)))', ID="X_252", classes=["center", "incident"])
    central_line(model, X_2, X_252, 2, 252, incident=True)
    return promote_point_to_top(model, X_1166)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1166 on the given reference triangle."""
    model = create_model('X_1166 = 1st SARAGOSSA POINT OF X_5')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01166(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01166.json"))
    write_center_svg(
        model_acute,
        here / "x-01166.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
