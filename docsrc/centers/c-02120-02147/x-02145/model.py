"""GEOMETOR construction model for X_2145 = X_2-ISOCONJUGATE OF X_2144."""

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


def construct_x_02145(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2145 = X_2-ISOCONJUGATE OF X_2144 on reference triangle ABC."""
    X_2145 = point_from_barycentrics(model, A, B, C, -2.0212277, -0.14360275, 3.1648305, ID="X_2145", classes=["selected", "target"])
    return promote_point_to_top(model, X_2145)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2145 on the given reference triangle."""
    model = create_model('X_2145 = X_2-ISOCONJUGATE OF X_2144')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02145(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02145.json"))
    write_center_svg(
        model_acute,
        here / "x-02145.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
