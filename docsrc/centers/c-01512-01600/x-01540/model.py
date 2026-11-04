"""GEOMETOR construction model for X_1540 = ORTHOJOIN OF X_54."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01540(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1540 = ORTHOJOIN OF X_54 on reference triangle ABC."""
    X_1540 = point_from_barycentrics(model, A, B, C, -1.3885574, -1.6887696, 4.077327, ID="X_1540", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_4, X_6, 4, 6, incident=True)
    return promote_point_to_top(model, X_1540)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1540 on the given reference triangle."""
    model = create_model('X_1540 = ORTHOJOIN OF X_54')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01540(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01540.json"))
    write_center_svg(
        model_acute,
        here / "x-01540.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
