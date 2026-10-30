"""GEOMETOR construction model for X(992) = INTERSECTION OF LINES X(2)X(6) AND X(9)X(39)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    mittenpunkt_of,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00992(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(992) = INTERSECTION OF LINES X(2)X(6) AND X(9)X(39) on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X(39)", classes=["center"])
    central_line(model, X_2, X_6, 2, 6)
    central_line(model, X_9, X_39, 9, 39)
    X_992 = intersect_lines(model, X_2, X_6, X_9, X_39, ID="X(992)", classes=["selected", "target"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X(44)", classes=["center", "incident"])
    X_583 = point_from_barycentrics(model, A, B, C, 0.095372877, 0.28353433, 0.62109279, ID="X(583)", classes=["center", "incident"])
    central_line(model, X_44, X_583, 44, 583, incident=True)
    return promote_point_to_top(model, X_992)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(992) on the given reference triangle."""
    model = create_model('X(992) = INTERSECTION OF LINES X(2)X(6) AND X(9)X(39)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00992(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00992.json"))
    write_center_svg(
        model_acute,
        here / "x-00992.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
