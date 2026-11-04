"""GEOMETOR construction model for X_1521 = ORTHOJOIN OF X_11."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_01521(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1521 = ORTHOJOIN OF X_11 on reference triangle ABC."""
    X_117 = point_from_barycentrics(model, A, B, C, 0.19223485, -0.017045455, 0.82481061, ID="X_117", classes=["center"])
    X_515 = eval_trilinear_point(model, A, B, C, '(b + c)*sec(A) - b*sec(B) - c*sec(C)', ID="X_515", classes=["center"])
    X_118 = point_from_barycentrics(model, A, B, C, 0.28918651, -0.056547619, 0.76736111, ID="X_118", classes=["center"])
    X_516 = eval_trilinear_point(model, A, B, C, 'b*c*((a - b)*cot(C) + (a - c)*cot(B))', ID="X_516", classes=["center"])
    central_line(model, X_117, X_515, 117, 515)
    central_line(model, X_118, X_516, 118, 516)
    X_1521 = intersect_lines(model, X_117, X_515, X_118, X_516, ID="X_1521", classes=["selected", "target"])
    return promote_point_to_top(model, X_1521)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1521 on the given reference triangle."""
    model = create_model('X_1521 = ORTHOJOIN OF X_11')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01521(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01521.json"))
    write_center_svg(
        model_acute,
        here / "x-01521.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
