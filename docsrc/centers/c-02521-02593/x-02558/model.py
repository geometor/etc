"""GEOMETOR construction model for X_2558 = INSIMILICENTER(1st LEMOINE CIRCLE, 2nd BROCARD CIRCLE)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02558(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2558 = INSIMILICENTER(1st LEMOINE CIRCLE, 2nd BROCARD CIRCLE) on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_1672 = eval_trilinear_point(model, A, B, C, '1 + cos(A -  omega  )', ID="X_1672", classes=["center"])
    X_2565 = eval_trilinear_point(model, A, B, C, '(e - cos(A))', ID="X_2565", classes=["center"])
    central_line(model, X_3, X_6, 3, 6)
    central_line(model, X_1672, X_2565, 1672, 2565)
    X_2558 = intersect_lines(model, X_3, X_6, X_1672, X_2565, ID="X_2558", classes=["selected", "target"])
    X_1673 = eval_trilinear_point(model, A, B, C, '1 - cos(A -  omega  )', ID="X_1673", classes=["center", "incident"])
    X_2564 = eval_trilinear_point(model, A, B, C, '(e + cos(A))', ID="X_2564", classes=["center", "incident"])
    central_line(model, X_1673, X_2564, 1673, 2564, incident=True)
    return promote_point_to_top(model, X_2558)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2558 on the given reference triangle."""
    model = create_model('X_2558 = INSIMILICENTER(1st LEMOINE CIRCLE, 2nd BROCARD CIRCLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02558(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02558.json"))
    write_center_svg(
        model_acute,
        here / "x-02558.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
