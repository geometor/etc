"""GEOMETOR construction model for X_3076 = INTERSECTION OF X_1X_606 AND X_47X_605."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03076(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3076 = INTERSECTION OF X_1X_606 AND X_47X_605 on reference triangle ABC."""
    X_3076 = eval_trilinear_point(model, A, B, C, '(cos(A))**(2) + sin(A)', ID="X_3076", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_255 = eval_trilinear_point(model, A, B, C, '(cos(A))**(2)', ID="X_255", classes=["center", "incident"])
    central_line(model, X_6, X_255, 6, 255, incident=True)
    X_212 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 + cos(A))', ID="X_212", classes=["center", "incident"])
    X_372 = eval_trilinear_point(model, A, B, C, 'cos(A +  pi  /4)', ID="X_372", classes=["center", "incident"])
    central_line(model, X_212, X_372, 212, 372, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_606 = eval_trilinear_point(model, A, B, C, 'a*(1 - sin(A))', ID="X_606", classes=["center", "incident"])
    central_line(model, X_1, X_606, 1, 606, incident=True)
    return promote_point_to_top(model, X_3076)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3076 on the given reference triangle."""
    model = create_model('X_3076 = INTERSECTION OF X_1X_606 AND X_47X_605')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03076(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03076.json"))
    write_center_svg(
        model_acute,
        here / "x-03076.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
