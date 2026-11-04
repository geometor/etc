"""GEOMETOR construction model for X_2438 = ISOGONAL CONJUGATE OF X_2412."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    construct_baseline_triangle,
    create_model,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02438(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2438 = ISOGONAL CONJUGATE OF X_2412 on reference triangle ABC."""
    X_2412 = point_from_barycentrics(model, A, B, C, -0.081310586, 0.9509715, 0.13033909, ID="X_2412", classes=["center"])
    X_2438 = isogonal_conjugate(model, A, B, C, X_2412, ID="X_2438", classes=["selected", "target"])
    return promote_point_to_top(model, X_2438)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2438 on the given reference triangle."""
    model = create_model('X_2438 = ISOGONAL CONJUGATE OF X_2412')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02438(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02438.json"))
    write_center_svg(
        model_acute,
        here / "x-02438.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
