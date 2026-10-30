"""GEOMETOR construction model for X(423) = X(4)-HIRST INVERSE OF X(27)."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_00423(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(423) = X(4)-HIRST INVERSE OF X(27) on reference triangle ABC."""
    X_423 = point_from_barycentrics(model, A, B, C, 0.38368056, 0.36458333, 0.25173611, ID="X(423)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    return promote_point_to_top(model, X_423)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(423) on the given reference triangle."""
    model = create_model('X(423) = X(4)-HIRST INVERSE OF X(27)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00423(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00423.json"))
    write_center_svg(
        model_acute,
        here / "x-00423.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
