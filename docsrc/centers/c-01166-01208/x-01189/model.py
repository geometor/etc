"""GEOMETOR construction model for X_1189 = 2nd SARAGOSSA POINT OF X_43."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    incenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01189(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1189 = 2nd SARAGOSSA POINT OF X_43 on reference triangle ABC."""
    X_1189 = point_from_barycentrics(model, A, B, C, 0.20138395, 0.33333333, 0.46528272, ID="X_1189", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)
    return promote_point_to_top(model, X_1189)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1189 on the given reference triangle."""
    model = create_model('X_1189 = 2nd SARAGOSSA POINT OF X_43')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01189(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01189.json"))
    write_center_svg(
        model_acute,
        here / "x-01189.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
