"""GEOMETOR construction model for X_3185 = X_21-CEVA CONJUGATE OF X_6."""

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


def construct_x_03185(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3185 = X_21-CEVA CONJUGATE OF X_6 on reference triangle ABC."""
    X_2995 = point_from_barycentrics(model, A, B, C, 0.034563044, 0.051985067, 0.91345189, ID="X_2995", classes=["center"])
    X_3185 = isogonal_conjugate(model, A, B, C, X_2995, ID="X_3185", classes=["selected", "target"])
    return promote_point_to_top(model, X_3185)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3185 on the given reference triangle."""
    model = create_model('X_3185 = X_21-CEVA CONJUGATE OF X_6')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03185(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03185.json"))
    write_center_svg(
        model_acute,
        here / "x-03185.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
