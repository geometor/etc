"""GEOMETOR construction model for X(487) = ANTICOMPLEMENT OF X(486)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00487(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(487) = ANTICOMPLEMENT OF X(486) on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X(69)", classes=["center"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_371 = eval_trilinear_point(model, A, B, C, 'cos(A - pi /4)', ID="X(371)", classes=["center"])
    central_line(model, X_3, X_69, 3, 69)
    central_line(model, X_2, X_371, 2, 371)
    X_487 = intersect_lines(model, X_3, X_69, X_2, X_371, ID="X(487)", classes=["selected", "target"])
    X_193 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cot(B) + cot(C) - cot(A))', ID="X(193)", classes=["center", "incident"])
    X_372 = eval_trilinear_point(model, A, B, C, 'cos(A + pi /4)', ID="X(372)", classes=["center", "incident"])
    central_line(model, X_193, X_372, 193, 372, incident=True)
    return promote_point_to_top(model, X_487)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(487) on the given reference triangle."""
    model = create_model('X(487) = ANTICOMPLEMENT OF X(486)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00487(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00487.json"))
    write_center_svg(
        model_acute,
        here / "x-00487.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
