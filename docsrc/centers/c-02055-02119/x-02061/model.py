"""GEOMETOR construction model for X_2061 = ORION TRANSFORM OF X_40."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02061(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2061 = ORION TRANSFORM OF X_40 on reference triangle ABC."""
    X_2061 = point_from_barycentrics(model, A, B, C, 0.5210125, 0.43062722, 0.048360284, ID="X_2061", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    central_line(model, X_1, X_3, 1, 3, incident=True)
    return promote_point_to_top(model, X_2061)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2061 on the given reference triangle."""
    model = create_model('X_2061 = ORION TRANSFORM OF X_40')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02061(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02061.json"))
    write_center_svg(
        model_acute,
        here / "x-02061.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
