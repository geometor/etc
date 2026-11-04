"""GEOMETOR construction model for X_1777 = MIMOSA TRANSFORM OF X_1167."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01777(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1777 = MIMOSA TRANSFORM OF X_1167 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_84 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C) - cos(A) - 1)', ID="X_84", classes=["center"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center"])
    central_line(model, X_1, X_84, 1, 84)
    central_line(model, X_4, X_109, 4, 109)
    X_1777 = intersect_lines(model, X_1, X_84, X_4, X_109, ID="X_1777", classes=["selected", "target"])
    X_255 = eval_trilinear_point(model, A, B, C, '(cos(A))**(2)', ID="X_255", classes=["center", "incident"])
    X_516 = eval_trilinear_point(model, A, B, C, 'b*c*((a - b)*cot(C) + (a - c)*cot(B))', ID="X_516", classes=["center", "incident"])
    central_line(model, X_255, X_516, 255, 516, incident=True)
    return promote_point_to_top(model, X_1777)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1777 on the given reference triangle."""
    model = create_model('X_1777 = MIMOSA TRANSFORM OF X_1167')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01777(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01777.json"))
    write_center_svg(
        model_acute,
        here / "x-01777.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
