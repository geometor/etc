"""GEOMETOR construction model for X_3081 = DANNEELS POINT OF X_30."""

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
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_03081(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3081 = DANNEELS POINT OF X_30 on reference triangle ABC."""
    X_1650 = point_from_barycentrics(model, A, B, C, 0.55489887, 0.47085677, -0.025755641, ID="X_1650", classes=["center"])
    X_1651 = point_from_barycentrics(model, A, B, C, 0.1117678, 0.1958099, 0.69242231, ID="X_1651", classes=["center"])
    X_3081 = reflection_in_point(model, X_1650, X_1651, ID="X_3081", classes=["selected", "target"], guide=False)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    return promote_point_to_top(model, X_3081)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3081 on the given reference triangle."""
    model = create_model('X_3081 = DANNEELS POINT OF X_30')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03081(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03081.json"))
    write_center_svg(
        model_acute,
        here / "x-03081.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
