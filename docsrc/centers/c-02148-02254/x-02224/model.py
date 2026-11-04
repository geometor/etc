"""GEOMETOR construction model for X_2224 = X_2-ISOCONJUGATE OF X_674."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_02224(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2224 = X_2-ISOCONJUGATE OF X_674 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center"])
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X_81", classes=["center"])
    X_163 = eval_trilinear_point(model, A, B, C, '(sin(2*A))/(sin(2*B) - sin(2*C))', ID="X_163", classes=["center"])
    central_line(model, X_2, X_101, 2, 101)
    central_line(model, X_81, X_163, 81, 163)
    X_2224 = intersect_lines(model, X_2, X_101, X_81, X_163, ID="X_2224", classes=["selected", "target"])
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_291 = eval_trilinear_point(model, A, B, C, '1/(a**(2) - b*c)', ID="X_291", classes=["center", "incident"])
    central_line(model, X_36, X_291, 36, 291, incident=True)
    return promote_point_to_top(model, X_2224)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2224 on the given reference triangle."""
    model = create_model('X_2224 = X_2-ISOCONJUGATE OF X_674')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02224(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02224.json"))
    write_center_svg(
        model_acute,
        here / "x-02224.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
