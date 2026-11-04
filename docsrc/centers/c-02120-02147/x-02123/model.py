"""GEOMETOR construction model for X_2123 = ISOGONAL CONJUGATE OF X_2122."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    isogonal_conjugate,
    nagel_point_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02123(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2123 = ISOGONAL CONJUGATE OF X_2122 on reference triangle ABC."""
    X_2122 = point_from_barycentrics(model, A, B, C, 2.008547, 2.5764103, -3.5849573, ID="X_2122", classes=["center"])
    X_2123 = isogonal_conjugate(model, A, B, C, X_2122, ID="X_2123", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    central_line(model, X_8, X_2122, 8, 2122, incident=True)
    return promote_point_to_top(model, X_2123)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2123 on the given reference triangle."""
    model = create_model('X_2123 = ISOGONAL CONJUGATE OF X_2122')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02123(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02123.json"))
    write_center_svg(
        model_acute,
        here / "x-02123.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
