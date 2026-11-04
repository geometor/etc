"""GEOMETOR construction model for X_1793 = INVERSE MIMOSA TRANSFORM OF X_30."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01793(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1793 = INVERSE MIMOSA TRANSFORM OF X_30 on reference triangle ABC."""
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X_125", classes=["center"])
    central_line(model, X_10, X_21, 10, 21)
    central_line(model, X_3, X_125, 3, 125)
    X_1793 = intersect_lines(model, X_10, X_21, X_3, X_125, ID="X_1793", classes=["selected", "target"])
    X_72 = eval_trilinear_point(model, A, B, C, '(b + c)*cot(A)', ID="X_72", classes=["center", "incident"])
    X_283 = eval_trilinear_point(model, A, B, C, '(cos(A))/(cos(B) + cos(C))', ID="X_283", classes=["center", "incident"])
    central_line(model, X_72, X_283, 72, 283, incident=True)
    return promote_point_to_top(model, X_1793)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1793 on the given reference triangle."""
    model = create_model('X_1793 = INVERSE MIMOSA TRANSFORM OF X_30')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01793(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01793.json"))
    write_center_svg(
        model_acute,
        here / "x-01793.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
