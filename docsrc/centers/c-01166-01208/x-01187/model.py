"""GEOMETOR construction model for X_1187 = 2nd SARAGOSSA POINT OF X_37."""

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
    spieker_center_of,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01187(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1187 = 2nd SARAGOSSA POINT OF X_37 on reference triangle ABC."""
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_60 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(B - C))', ID="X_60", classes=["center"])
    central_line(model, X_10, X_37, 10, 37)
    central_line(model, X_6, X_60, 6, 60)
    X_1187 = intersect_lines(model, X_10, X_37, X_6, X_60, ID="X_1187", classes=["selected", "target"])
    return promote_point_to_top(model, X_1187)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1187 on the given reference triangle."""
    model = create_model('X_1187 = 2nd SARAGOSSA POINT OF X_37')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01187(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01187.json"))
    write_center_svg(
        model_acute,
        here / "x-01187.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
