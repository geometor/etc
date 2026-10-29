"""GEOMETOR construction model for X(124) = X(109)-OF-MEDIAL-TRIANGLE."""

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
    midpoint,
    nine_point_center_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00124(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(124) = X(109)-OF-MEDIAL-TRIANGLE on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center"])
    X_102 = eval_trilinear_point(model, A, B, C, '1/(sin(B)*(sec(A) - sec(B)) + sin(C)*(sec(A) - sec(C)))', ID="X(102)", classes=["center"])
    X_124 = midpoint(model, X_4, X_102, ID="X(124)", classes=["selected", "target"], guide=False)
    central_line(model, X_4, X_102, 4, 102, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X(109)", classes=["center", "incident"])
    central_line(model, X_2, X_109, 2, 109, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center", "incident"])
    X_117 = point_from_barycentrics(model, A, B, C, 0.19223485, -0.017045455, 0.82481061, ID="X(117)", classes=["center", "incident"])
    central_line(model, X_5, X_117, 5, 117, incident=True)
    return promote_point_to_top(model, X_124)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(124) on the given reference triangle."""
    model = create_model('X(124) = X(109)-OF-MEDIAL-TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00124(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00124.json"))
    write_center_svg(
        model_acute,
        here / "x-00124.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
