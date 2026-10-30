"""GEOMETOR construction model for X(930) = ANTICOMPLEMENT OF X(137)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    anticomplement,
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00930(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(930) = ANTICOMPLEMENT OF X(137) on reference triangle ABC."""
    X_137 = point_from_barycentrics(model, A, B, C, 0.1354431, 0.64976082, 0.21479608, ID="X(137)", classes=["center"])
    X_930 = anticomplement(model, A, B, C, X_137, ID="X(930)", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_128 = point_from_barycentrics(model, A, B, C, 0.43052912, -0.045594157, 0.61506504, ID="X(128)", classes=["center", "incident"])
    central_line(model, X_4, X_128, 4, 128, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    central_line(model, X_2, X_137, 2, 137, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_252 = point_from_barycentrics(model, A, B, C, 0.46254977, 0.32862274, 0.20882749, ID="X(252)", classes=["center", "incident"])
    central_line(model, X_3, X_252, 3, 252, incident=True)
    return promote_point_to_top(model, X_930)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(930) on the given reference triangle."""
    model = create_model('X(930) = ANTICOMPLEMENT OF X(137)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00930(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00930.json"))
    write_center_svg(
        model_acute,
        here / "x-00930.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
