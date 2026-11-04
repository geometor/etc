"""GEOMETOR construction model for X_2155 = X_2-ISOCONJUGATE OF X_20."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_02155(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2155 = X_2-ISOCONJUGATE OF X_20 on reference triangle ABC."""
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X_64", classes=["center"])
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center"])
    X_610 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C) - tan(A)', ID="X_610", classes=["center"])
    central_line(model, X_64, X_71, 64, 71)
    central_line(model, X_63, X_610, 63, 610)
    X_2155 = intersect_lines(model, X_64, X_71, X_63, X_610, ID="X_2155", classes=["selected", "target"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_774 = eval_trilinear_point(model, A, B, C, '(cos(B))**(2) + (cos(C))**(2)', ID="X_774", classes=["center", "incident"])
    central_line(model, X_19, X_774, 19, 774, incident=True)
    return promote_point_to_top(model, X_2155)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2155 on the given reference triangle."""
    model = create_model('X_2155 = X_2-ISOCONJUGATE OF X_20')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02155(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02155.json"))
    write_center_svg(
        model_acute,
        here / "x-02155.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
