"""GEOMETOR construction model for X_3355 = REFLECTION OF X_2131 IN X_3."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    incenter_of,
    intersect_lines,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03355(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3355 = REFLECTION OF X_2131 IN X_3 on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_2130 = point_from_barycentrics(model, A, B, C, 0.19373197, 0.27423005, 0.53203798, ID="X_2130", classes=["center"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_3348 = point_from_barycentrics(model, A, B, C, 0.67432359, 0.51743661, -0.1917602, ID="X_3348", classes=["center"])
    central_line(model, X_3, X_2130, 3, 2130)
    central_line(model, X_4, X_3348, 4, 3348)
    X_3355 = intersect_lines(model, X_3, X_2130, X_4, X_3348, ID="X_3355", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_3354 = point_from_barycentrics(model, A, B, C, 0.52487682, 0.4279698, 0.047153374, ID="X_3354", classes=["center", "incident"])
    central_line(model, X_1, X_3354, 1, 3354, incident=True)
    return promote_point_to_top(model, X_3355)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3355 on the given reference triangle."""
    model = create_model('X_3355 = REFLECTION OF X_2131 IN X_3')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03355(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03355.json"))
    write_center_svg(
        model_acute,
        here / "x-03355.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
