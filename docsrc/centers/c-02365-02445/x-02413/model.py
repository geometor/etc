"""GEOMETOR construction model for X_2413 = GIBERT-SIMSON TRANSFORM OF X_1141."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    construct_baseline_triangle,
    create_model,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02413(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2413 = GIBERT-SIMSON TRANSFORM OF X_1141 on reference triangle ABC."""
    X_2413 = point_from_barycentrics(model, A, B, C, 0.91919317, -0.017879982, 0.098686809, ID="X_2413", classes=["selected", "target"])
    return promote_point_to_top(model, X_2413)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2413 on the given reference triangle."""
    model = create_model('X_2413 = GIBERT-SIMSON TRANSFORM OF X_1141')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02413(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02413.json"))
    write_center_svg(
        model_acute,
        here / "x-02413.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
