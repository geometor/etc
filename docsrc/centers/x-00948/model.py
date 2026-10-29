"""GEOMETOR construction model for X(948) = INTERSECTION OF LINES X(1)X(4) AND X(6)X(7)."""

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
    gergonne_point_of,
    incenter_of,
    intersect_lines,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00948(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(948) = INTERSECTION OF LINES X(1)X(4) AND X(6)X(7) on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center"])
    central_line(model, X_1, X_4, 1, 4)
    central_line(model, X_6, X_7, 6, 7)
    X_948 = intersect_lines(model, X_1, X_4, X_6, X_7, ID="X(948)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X(85)", classes=["center", "incident"])
    central_line(model, X_2, X_85, 2, 85, incident=True)
    return promote_point_to_top(model, X_948)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(948) on the given reference triangle."""
    model = create_model('X(948) = INTERSECTION OF LINES X(1)X(4) AND X(6)X(7)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00948(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00948.json"))
    write_center_svg(
        model_acute,
        here / "x-00948.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
