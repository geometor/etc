"""GEOMETOR construction model for X(928) = CROSSDIFFERENCE OF X(6) AND X(11)."""

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


def construct_x_00928(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(928) = CROSSDIFFERENCE OF X(6) AND X(11) on reference triangle ABC."""
    X_102 = eval_trilinear_point(model, A, B, C, '1/(sin(B)*(sec(A) - sec(B)) + sin(C)*(sec(A) - sec(C)))', ID="X(102)", classes=["center"])
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X(103)", classes=["center"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X(109)", classes=["center"])
    central_line(model, X_102, X_103, 102, 103)
    central_line(model, X_101, X_109, 101, 109)
    X_928 = intersect_lines(model, X_102, X_103, X_101, X_109, ID="X(928)", classes=["selected", "target"])
    X_117 = point_from_barycentrics(model, A, B, C, 0.19223485, -0.017045455, 0.82481061, ID="X(117)", classes=["center", "incident"])
    X_118 = point_from_barycentrics(model, A, B, C, 0.28918651, -0.056547619, 0.76736111, ID="X(118)", classes=["center", "incident"])
    central_line(model, X_117, X_118, 117, 118, incident=True)
    return promote_point_to_top(model, X_928)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(928) on the given reference triangle."""
    model = create_model('X(928) = CROSSDIFFERENCE OF X(6) AND X(11)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00928(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00928.json"))
    write_center_svg(
        model_acute,
        here / "x-00928.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
