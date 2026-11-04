"""GEOMETOR construction model for X_2865 = SM(X_104, X_105)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02865(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2865 = SM(X_104, X_105) on reference triangle ABC."""
    X_919 = point_from_barycentrics(model, A, B, C, -0.11560694, 0.83236994, 0.28323699, ID="X_919", classes=["center"])
    X_2397 = point_from_barycentrics(model, A, B, C, -6, 1, 6, ID="X_2397", classes=["center"])
    X_883 = point_from_barycentrics(model, A, B, C, -1.5, 0.1, 2.4, ID="X_883", classes=["center"])
    X_2720 = point_from_barycentrics(model, A, B, C, -0.17241379, 0.49655172, 0.67586207, ID="X_2720", classes=["center"])
    central_line(model, X_919, X_2397, 919, 2397)
    central_line(model, X_883, X_2720, 883, 2720)
    X_2865 = intersect_lines(model, X_919, X_2397, X_883, X_2720, ID="X_2865", classes=["selected", "target"])
    return promote_point_to_top(model, X_2865)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2865 on the given reference triangle."""
    model = create_model('X_2865 = SM(X_104, X_105)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02865(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02865.json"))
    write_center_svg(
        model_acute,
        here / "x-02865.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
