"""GEOMETOR construction model for X_1032 = CYCLOCEVIAN CONJUGATE OF X_20."""

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


def construct_x_01032(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1032 = CYCLOCEVIAN CONJUGATE OF X_20 on reference triangle ABC."""
    X_1032 = point_from_barycentrics(model, A, B, C, 0.68146836, 0.48642354, -0.1678919, ID="X_1032", classes=["selected", "target"])
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_394 = eval_trilinear_point(model, A, B, C, 'cos(A)*cot(A)', ID="X_394", classes=["center", "incident"])
    central_line(model, X_20, X_394, 20, 394, incident=True)
    return promote_point_to_top(model, X_1032)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1032 on the given reference triangle."""
    model = create_model('X_1032 = CYCLOCEVIAN CONJUGATE OF X_20')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01032(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01032.json"))
    write_center_svg(
        model_acute,
        here / "x-01032.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
