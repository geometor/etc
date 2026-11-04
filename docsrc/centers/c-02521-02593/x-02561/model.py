"""GEOMETOR construction model for X_2561 = EXSIMILICENTER(2nd LEMOINE CIRCLE, 2nd BROCARD CIRCLE)."""

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


def construct_x_02561(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2561 = EXSIMILICENTER(2nd LEMOINE CIRCLE, 2nd BROCARD CIRCLE) on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_485 = eval_trilinear_point(model, A, B, C, 'sec(A -  pi  /4)', ID="X_485", classes=["center"])
    X_2566 = eval_trilinear_point(model, A, B, C, '(cos(A) + e*cos(B - C))', ID="X_2566", classes=["center"])
    central_line(model, X_3, X_6, 3, 6)
    central_line(model, X_485, X_2566, 485, 2566)
    X_2561 = intersect_lines(model, X_3, X_6, X_485, X_2566, ID="X_2561", classes=["selected", "target"])
    X_486 = eval_trilinear_point(model, A, B, C, 'sec(A +  pi  /4)', ID="X_486", classes=["center", "incident"])
    X_2567 = eval_trilinear_point(model, A, B, C, '(cos(A) - e*cos(B - C))', ID="X_2567", classes=["center", "incident"])
    central_line(model, X_486, X_2567, 486, 2567, incident=True)
    return promote_point_to_top(model, X_2561)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2561 on the given reference triangle."""
    model = create_model('X_2561 = EXSIMILICENTER(2nd LEMOINE CIRCLE, 2nd BROCARD CIRCLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02561(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02561.json"))
    write_center_svg(
        model_acute,
        here / "x-02561.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
