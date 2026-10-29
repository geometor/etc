"""GEOMETOR construction model for X(2) = CENTROID."""

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
    gergonne_point_of,
    incenter_of,
    mittenpunkt_of,
    nagel_point_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00002(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(2) = CENTROID on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center"])
    central_line(model, X_3, X_4, 3, 4)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center"])
    central_line(model, X_1, X_8, 1, 8)
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center"])
    central_line(model, X_7, X_9, 7, 9)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["selected", "target"], draw_medians=True)
    return promote_point_to_top(model, X_2)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = True,
) -> Model:
    """Build a `geometor.model.Model` for X(2) on the given reference triangle."""
    model = create_model('X(2) = CENTROID')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00002(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00002.json"))
    write_center_svg(
        model_acute,
        here / "x-00002.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
