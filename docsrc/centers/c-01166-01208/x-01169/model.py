"""GEOMETOR construction model for X_1169 = 1st SARAGOSSA POINT OF X_37."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01169(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1169 = 1st SARAGOSSA POINT OF X_37 on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_60 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(B - C))', ID="X_60", classes=["center"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center"])
    X_172 = eval_trilinear_point(model, A, B, C, 'a**(3) + a*b*c', ID="X_172", classes=["center"])
    central_line(model, X_6, X_60, 6, 60)
    central_line(model, X_21, X_172, 21, 172)
    X_1169 = intersect_lines(model, X_6, X_60, X_21, X_172, ID="X_1169", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_261 = eval_trilinear_point(model, A, B, C, '(((csc(A))*(sec(B/2 - C/2)))**(2))', ID="X_261", classes=["center", "incident"])
    central_line(model, X_2, X_261, 2, 261, incident=True)
    return promote_point_to_top(model, X_1169)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1169 on the given reference triangle."""
    model = create_model('X_1169 = 1st SARAGOSSA POINT OF X_37')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01169(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01169.json"))
    write_center_svg(
        model_acute,
        here / "x-01169.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
