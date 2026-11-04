"""GEOMETOR construction model for X_2774 = ISOGONAL CONJUGATE OF X_2690."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02774(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2774 = ISOGONAL CONJUGATE OF X_2690 on reference triangle ABC."""
    X_2690 = point_from_barycentrics(model, A, B, C, -0.14133385, 0.76367127, 0.37766257, ID="X_2690", classes=["center"])
    X_2774 = isogonal_conjugate(model, A, B, C, X_2690, ID="X_2774", classes=["selected", "target"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center", "incident"])
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X_103", classes=["center", "incident"])
    central_line(model, X_74, X_103, 74, 103, incident=True)
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_101, X_110, 101, 110, incident=True)
    X_113 = eval_trilinear_point(model, A, B, C, 'sin(B)*sin(C)*((sin(C))/(cos(C) - 2*cos(A)*cos(B)) + (sin(B))/(cos(B) - 2*cos(A)*cos(C)))', ID="X_113", classes=["center", "incident"])
    X_118 = point_from_barycentrics(model, A, B, C, 0.28918651, -0.056547619, 0.76736111, ID="X_118", classes=["center", "incident"])
    central_line(model, X_113, X_118, 113, 118, incident=True)
    return promote_point_to_top(model, X_2774)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2774 on the given reference triangle."""
    model = create_model('X_2774 = ISOGONAL CONJUGATE OF X_2690')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02774(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02774.json"))
    write_center_svg(
        model_acute,
        here / "x-02774.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
