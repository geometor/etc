"""GEOMETOR construction model for X_771 = ISOGONAL CONJUGATE OF X_770."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00771(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_771 = ISOGONAL CONJUGATE OF X_770 on reference triangle ABC."""
    X_770 = point_from_barycentrics(model, A, B, C, -2.8386427, 0.81274255, 3.0259002, ID="X_770", classes=["center"])
    X_771 = isogonal_conjugate(model, A, B, C, X_770, ID="X_771", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    return promote_point_to_top(model, X_771)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_771 on the given reference triangle."""
    model = create_model('X_771 = ISOGONAL CONJUGATE OF X_770')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00771(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00771.json"))
    write_center_svg(
        model_acute,
        here / "x-00771.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
