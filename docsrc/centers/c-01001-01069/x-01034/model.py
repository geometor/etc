"""GEOMETOR construction model for X_1034 = X_4-CROSS CONJUGATE OF X_8."""

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


def construct_x_01034(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1034 = X_4-CROSS CONJUGATE OF X_8 on reference triangle ABC."""
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center"])
    X_78 = eval_trilinear_point(model, A, B, C, '1/(1 - sec(A))', ID="X_78", classes=["center"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_271 = eval_trilinear_point(model, A, B, C, '((cot(A)*cot(A/2))/(-1 - cos(A) + cos(B) + cos(C)))', ID="X_271", classes=["center"])
    central_line(model, X_20, X_78, 20, 78)
    central_line(model, X_2, X_271, 2, 271)
    X_1034 = intersect_lines(model, X_20, X_78, X_2, X_271, ID="X_1034", classes=["selected", "target"])
    return promote_point_to_top(model, X_1034)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1034 on the given reference triangle."""
    model = create_model('X_1034 = X_4-CROSS CONJUGATE OF X_8')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01034(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01034.json"))
    write_center_svg(
        model_acute,
        here / "x-01034.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
