"""GEOMETOR construction model for X_1288 = COLLINGS TRANSFORM OF X_24."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01288(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1288 = COLLINGS TRANSFORM OF X_24 on reference triangle ABC."""
    X_1288 = point_from_barycentrics(model, A, B, C, -0.081215203, 0.1407786, 0.9404366, ID="X_1288", classes=["selected", "target"])
    X_70 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2)*cos(2*B) + c**(2)*cos(2*C) - a**(2)*cos(2*A))', ID="X_70", classes=["center", "incident"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center", "incident"])
    central_line(model, X_70, X_74, 70, 74, incident=True)
    return promote_point_to_top(model, X_1288)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1288 on the given reference triangle."""
    model = create_model('X_1288 = COLLINGS TRANSFORM OF X_24')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01288(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01288.json"))
    write_center_svg(
        model_acute,
        here / "x-01288.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
