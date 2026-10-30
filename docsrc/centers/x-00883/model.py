"""GEOMETOR construction model for X(883) = INTERSECTION OF LINES X(7)X(8) AND X(190)X(644)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    intersect_lines,
    nagel_point_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00883(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(883) = INTERSECTION OF LINES X(7)X(8) AND X(190)X(644) on reference triangle ABC."""
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center"])
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center"])
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X(190)", classes=["center"])
    X_644 = point_from_barycentrics(model, A, B, C, 0.8, -0.36, 0.56, ID="X(644)", classes=["center"])
    central_line(model, X_7, X_8, 7, 8)
    central_line(model, X_190, X_644, 190, 644)
    X_883 = intersect_lines(model, X_7, X_8, X_190, X_644, ID="X(883)", classes=["selected", "target"])
    return promote_point_to_top(model, X_883)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(883) on the given reference triangle."""
    model = create_model('X(883) = INTERSECTION OF LINES X(7)X(8) AND X(190)X(644)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00883(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00883.json"))
    write_center_svg(
        model_acute,
        here / "x-00883.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
