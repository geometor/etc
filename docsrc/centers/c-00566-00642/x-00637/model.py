"""GEOMETOR construction model for X_637 = ANTICOMPLEMENT OF X_371."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    anticomplement,
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00637(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_637 = ANTICOMPLEMENT OF X_371 on reference triangle ABC."""
    X_371 = eval_trilinear_point(model, A, B, C, 'cos(A - pi /4)', ID="X_371", classes=["center"])
    X_637 = anticomplement(model, A, B, C, X_371, ID="X_637", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    central_line(model, X_4, X_69, 4, 69, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_2, X_371, 2, 371, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_489 = eval_trilinear_point(model, A, B, C, '((cos(A))*(1 - csc(A)*sin(B)*sin(C)) - cos(B)*cos(C))', ID="X_489", classes=["center", "incident"])
    central_line(model, X_3, X_489, 3, 489, incident=True)
    return promote_point_to_top(model, X_637)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_637 on the given reference triangle."""
    model = create_model('X_637 = ANTICOMPLEMENT OF X_371')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00637(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00637.json"))
    write_center_svg(
        model_acute,
        here / "x-00637.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
