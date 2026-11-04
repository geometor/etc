"""GEOMETOR construction model for X_2138 = EIGENTRANSFORM OF X_69."""

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
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02138(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2138 = EIGENTRANSFORM OF X_69 on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X_64", classes=["center"])
    X_1249 = eval_trilinear_point(model, A, B, C, '(tan(A))*(cos(A) - cos(B)*cos(C))', ID="X_1249", classes=["center"])
    X_1941 = eval_trilinear_point(model, A, B, C, '(cos(B)*cos(C)*((cos(A))**(4) + (cos(B))**(2)*(cos(C))**(2)))', ID="X_1941", classes=["center"])
    central_line(model, X_6, X_64, 6, 64)
    central_line(model, X_1249, X_1941, 1249, 1941)
    X_2138 = intersect_lines(model, X_6, X_64, X_1249, X_1941, ID="X_2138", classes=["selected", "target"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    X_2139 = point_from_barycentrics(model, A, B, C, 0.67949204, 0.47837797, -0.15787001, ID="X_2139", classes=["center", "incident"])
    central_line(model, X_69, X_2139, 69, 2139, incident=True)
    return promote_point_to_top(model, X_2138)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2138 on the given reference triangle."""
    model = create_model('X_2138 = EIGENTRANSFORM OF X_69')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02138(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02138.json"))
    write_center_svg(
        model_acute,
        here / "x-02138.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
