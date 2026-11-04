"""GEOMETOR construction model for X_1929 = ISOGONAL CONJUGATE OF X_1757."""

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


def construct_x_01929(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1929 = ISOGONAL CONJUGATE OF X_1757 on reference triangle ABC."""
    X_1757 = eval_trilinear_point(model, A, B, C, '((b + c)**(2) - (a + b)*(a + c))', ID="X_1757", classes=["center"])
    X_1929 = isogonal_conjugate(model, A, B, C, X_1757, ID="X_1929", classes=["selected", "target"])
    return promote_point_to_top(model, X_1929)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1929 on the given reference triangle."""
    model = create_model('X_1929 = ISOGONAL CONJUGATE OF X_1757')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01929(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01929.json"))
    write_center_svg(
        model_acute,
        here / "x-01929.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
