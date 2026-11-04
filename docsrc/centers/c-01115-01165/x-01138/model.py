"""GEOMETOR construction model for X_1138 = ISOGONAL CONJUGATE OF X_399."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01138(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1138 = ISOGONAL CONJUGATE OF X_399 on reference triangle ABC."""
    X_399 = eval_trilinear_point(model, A, B, C, '5*cos(A) - 4*cos(B)*cos(C) - 8*sin(B)*sin(C)*(cos(A))**(2)', ID="X_399", classes=["center"])
    X_1138 = isogonal_conjugate(model, A, B, C, X_399, ID="X_1138", classes=["selected", "target"])
    return promote_point_to_top(model, X_1138)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1138 on the given reference triangle."""
    model = create_model('X_1138 = ISOGONAL CONJUGATE OF X_399')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01138(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01138.json"))
    write_center_svg(
        model_acute,
        here / "x-01138.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
