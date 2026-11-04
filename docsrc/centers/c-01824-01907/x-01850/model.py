"""GEOMETOR construction model for X_1850 = ZOSMA TRANSFORM OF X_176."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    gergonne_point_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01850(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1850 = ZOSMA TRANSFORM OF X_176 on reference triangle ABC."""
    X_1850 = point_from_barycentrics(model, A, B, C, 0.14008901, 0.21652192, 0.64338907, ID="X_1850", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_4, X_7, 4, 7, incident=True)
    return promote_point_to_top(model, X_1850)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1850 on the given reference triangle."""
    model = create_model('X_1850 = ZOSMA TRANSFORM OF X_176')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01850(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01850.json"))
    write_center_svg(
        model_acute,
        here / "x-01850.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
