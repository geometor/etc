"""GEOMETOR construction model for X(355) = FUHRMANN CENTER."""

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
    midpoint,
    nagel_point_of,
    nine_point_center_of,
    orthocenter_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00355(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(355) = FUHRMANN CENTER on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center"])
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center"])
    X_355 = midpoint(model, X_4, X_8, ID="X(355)", classes=["selected", "target"], guide=False)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center", "incident"])
    central_line(model, X_1, X_5, 1, 5, incident=True)
    central_line(model, X_4, X_8, 4, 8, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    central_line(model, X_3, X_10, 3, 10, incident=True)
    return promote_point_to_top(model, X_355)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(355) on the given reference triangle."""
    model = create_model('X(355) = FUHRMANN CENTER')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00355(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00355.json"))
    write_center_svg(
        model_acute,
        here / "x-00355.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
