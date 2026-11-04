"""GEOMETOR construction model for X_1541 = ORTHOJOIN OF X_55."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    intersect_lines,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01541(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1541 = ORTHOJOIN OF X_55 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_118 = point_from_barycentrics(model, A, B, C, 0.28918651, -0.056547619, 0.76736111, ID="X_118", classes=["center"])
    X_516 = eval_trilinear_point(model, A, B, C, 'b*c*((a - b)*cot(C) + (a - c)*cot(B))', ID="X_516", classes=["center"])
    central_line(model, X_1, X_4, 1, 4)
    central_line(model, X_118, X_516, 118, 516)
    X_1541 = intersect_lines(model, X_1, X_4, X_118, X_516, ID="X_1541", classes=["selected", "target"])
    return promote_point_to_top(model, X_1541)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1541 on the given reference triangle."""
    model = create_model('X_1541 = ORTHOJOIN OF X_55')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01541(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01541.json"))
    write_center_svg(
        model_acute,
        here / "x-01541.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
