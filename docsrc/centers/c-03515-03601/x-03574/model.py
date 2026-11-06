"""GEOMETOR construction model for X_3574 = INTERSECTION OF LINES X_4X_54 AND X_5X_51."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    midpoint,
    nine_point_center_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03574(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3574 = INTERSECTION OF LINES X_4X_54 AND X_5X_51 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center"])
    X_3574 = midpoint(model, X_4, X_54, ID="X_3574", classes=["selected", "target"], guide=False)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X_51", classes=["center", "incident"])
    central_line(model, X_5, X_51, 5, 51, incident=True)
    central_line(model, X_4, X_54, 4, 54, incident=True)
    X_113 = eval_trilinear_point(model, A, B, C, 'sin(B)*sin(C)*((sin(C))/(cos(C) - 2*cos(A)*cos(B)) + (sin(B))/(cos(B) - 2*cos(A)*cos(C)))', ID="X_113", classes=["center", "incident"])
    X_137 = point_from_barycentrics(model, A, B, C, 0.1354431, 0.64976082, 0.21479608, ID="X_137", classes=["center", "incident"])
    central_line(model, X_113, X_137, 113, 137, incident=True)
    return promote_point_to_top(model, X_3574)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3574 on the given reference triangle."""
    model = create_model('X_3574 = INTERSECTION OF LINES X_4X_54 AND X_5X_51')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03574(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03574.json"))
    write_center_svg(
        model_acute,
        here / "x-03574.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
