"""GEOMETOR construction model for X_1669 = INSIMILICENTER(BROCARD CIRCLE, 2nd LEMOINE CIRCLE)."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01669(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1669 = INSIMILICENTER(BROCARD CIRCLE, 2nd LEMOINE CIRCLE) on reference triangle ABC."""
    X_1669 = eval_trilinear_point(model, A, B, C, 'cos(A -  omega  ) + e*sin(A)', ID="X_1669", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_485 = eval_trilinear_point(model, A, B, C, 'sec(A -  pi  /4)', ID="X_485", classes=["center", "incident"])
    X_1349 = eval_trilinear_point(model, A, B, C, 'e*cos(B - C) - cos(A -  omega  )', ID="X_1349", classes=["center", "incident"])
    central_line(model, X_485, X_1349, 485, 1349, incident=True)
    X_486 = eval_trilinear_point(model, A, B, C, 'sec(A +  pi  /4)', ID="X_486", classes=["center", "incident"])
    X_1348 = eval_trilinear_point(model, A, B, C, 'e*cos(B - C) + cos(A -  omega  )', ID="X_1348", classes=["center", "incident"])
    central_line(model, X_486, X_1348, 486, 1348, incident=True)
    return promote_point_to_top(model, X_1669)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1669 on the given reference triangle."""
    model = create_model('X_1669 = INSIMILICENTER(BROCARD CIRCLE, 2nd LEMOINE CIRCLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01669(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01669.json"))
    write_center_svg(
        model_acute,
        here / "x-01669.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
