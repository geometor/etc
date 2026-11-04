"""GEOMETOR construction model for X_2130 = EIGENTRANSFORM OF X_20."""

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


def construct_x_02130(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2130 = EIGENTRANSFORM OF X_20 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_1073 = eval_trilinear_point(model, A, B, C, '((cot(A))/(cos(A) - cos(B)*cos(C)))', ID="X_1073", classes=["center"])
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center"])
    X_2131 = point_from_barycentrics(model, A, B, C, 0.36616655, 0.37250097, 0.26133249, ID="X_2131", classes=["center"])
    central_line(model, X_4, X_1073, 4, 1073)
    central_line(model, X_20, X_2131, 20, 2131)
    X_2130 = intersect_lines(model, X_4, X_1073, X_20, X_2131, ID="X_2130", classes=["selected", "target"])
    return promote_point_to_top(model, X_2130)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2130 on the given reference triangle."""
    model = create_model('X_2130 = EIGENTRANSFORM OF X_20')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02130(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02130.json"))
    write_center_svg(
        model_acute,
        here / "x-02130.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
