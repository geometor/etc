"""GEOMETOR construction model for X_1188 = 2nd SARAGOSSA POINT OF X_41."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01188(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1188 = 2nd SARAGOSSA POINT OF X_41 on reference triangle ABC."""
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_279 = eval_trilinear_point(model, A, B, C, 'csc(A)*(tan(A/2))**(2)', ID="X_279", classes=["center"])
    central_line(model, X_31, X_32, 31, 32)
    central_line(model, X_6, X_279, 6, 279)
    X_1188 = intersect_lines(model, X_31, X_32, X_6, X_279, ID="X_1188", classes=["selected", "target"])
    return promote_point_to_top(model, X_1188)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1188 on the given reference triangle."""
    model = create_model('X_1188 = 2nd SARAGOSSA POINT OF X_41')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01188(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01188.json"))
    write_center_svg(
        model_acute,
        here / "x-01188.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
