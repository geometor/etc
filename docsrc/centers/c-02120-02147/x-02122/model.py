"""GEOMETOR construction model for X_2122 = EIGENTRANSFORM OF X_8."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02122(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2122 = EIGENTRANSFORM OF X_8 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_84 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C) - cos(A) - 1)', ID="X_84", classes=["center"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center"])
    X_1035 = point_from_barycentrics(model, A, B, C, 9.6083789, 14.775956, -23.384335, ID="X_1035", classes=["center"])
    central_line(model, X_1, X_84, 1, 84)
    central_line(model, X_109, X_1035, 109, 1035)
    X_2122 = intersect_lines(model, X_1, X_84, X_109, X_1035, ID="X_2122", classes=["selected", "target"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center", "incident"])
    X_1767 = point_from_barycentrics(model, A, B, C, -16.139785, -20.043011, 37.182796, ID="X_1767", classes=["center", "incident"])
    central_line(model, X_34, X_1767, 34, 1767, incident=True)
    return promote_point_to_top(model, X_2122)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2122 on the given reference triangle."""
    model = create_model('X_2122 = EIGENTRANSFORM OF X_8')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02122(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02122.json"))
    write_center_svg(
        model_acute,
        here / "x-02122.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
