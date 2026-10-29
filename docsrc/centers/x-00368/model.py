"""GEOMETOR construction model for X(368) = EQUI-BROCARD CENTER."""

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


def construct_x_00368(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(368) = EQUI-BROCARD CENTER on reference triangle ABC."""
    X_368 = point_from_barycentrics(model, A, B, C, 0.3279321, 0.34259259, 0.32947531, ID="X(368)", classes=["selected", "target"])
    return promote_point_to_top(model, X_368)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(368) on the given reference triangle."""
    model = create_model('X(368) = EQUI-BROCARD CENTER')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00368(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00368.json"))
    write_center_svg(
        model_acute,
        here / "x-00368.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
