"""GEOMETOR construction model for X_1568 = ORTHOJOIN OF X_800."""

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
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01568(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1568 = ORTHOJOIN OF X_800 on reference triangle ABC."""
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X_51", classes=["center"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center"])
    X_113 = eval_trilinear_point(model, A, B, C, 'sin(B)*sin(C)*((sin(C))/(cos(C) - 2*cos(A)*cos(B)) + (sin(B))/(cos(B) - 2*cos(A)*cos(C)))', ID="X_113", classes=["center"])
    central_line(model, X_5, X_51, 5, 51)
    central_line(model, X_30, X_113, 30, 113)
    X_1568 = intersect_lines(model, X_5, X_51, X_30, X_113, ID="X_1568", classes=["selected", "target"])
    X_381 = eval_trilinear_point(model, A, B, C, '2*cos(B - C) - cos(A)', ID="X_381", classes=["center", "incident"])
    X_394 = eval_trilinear_point(model, A, B, C, 'cos(A)*cot(A)', ID="X_394", classes=["center", "incident"])
    central_line(model, X_381, X_394, 381, 394, incident=True)
    return promote_point_to_top(model, X_1568)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1568 on the given reference triangle."""
    model = create_model('X_1568 = ORTHOJOIN OF X_800')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01568(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01568.json"))
    write_center_svg(
        model_acute,
        here / "x-01568.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
