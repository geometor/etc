"""GEOMETOR construction model for X_1461 = X_651-BETH CONJUGATE OF X_651."""

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


def construct_x_01461(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1461 = X_651-BETH CONJUGATE OF X_651 on reference triangle ABC."""
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X_77", classes=["center"])
    X_572 = eval_trilinear_point(model, A, B, C, '(cos(A - U))', ID="X_572", classes=["center"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center"])
    X_651 = eval_trilinear_point(model, A, B, C, '1/(cos(B) - cos(C))', ID="X_651", classes=["center"])
    central_line(model, X_77, X_572, 77, 572)
    central_line(model, X_101, X_651, 101, 651)
    X_1461 = intersect_lines(model, X_77, X_572, X_101, X_651, ID="X_1461", classes=["selected", "target"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    X_692 = eval_trilinear_point(model, A, B, C, 'a**(2)/(b - c)', ID="X_692", classes=["center", "incident"])
    central_line(model, X_109, X_692, 109, 692, incident=True)
    return promote_point_to_top(model, X_1461)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1461 on the given reference triangle."""
    model = create_model('X_1461 = X_651-BETH CONJUGATE OF X_651')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01461(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01461.json"))
    write_center_svg(
        model_acute,
        here / "x-01461.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
