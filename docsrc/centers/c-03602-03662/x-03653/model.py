"""GEOMETOR construction model for X_3653 = CENTROID OF {X_1, X_2, X_3}."""

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
    eval_trilinear_point,
    incenter_of,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03653(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3653 = CENTROID OF {X_1, X_2, X_3} on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_355 = eval_trilinear_point(model, A, B, C, 'a*cos(A) - (b + c)*cos(B - C)', ID="X_355", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_549 = eval_trilinear_point(model, A, B, C, 'cos(B - C) + 4*cos(A)', ID="X_549", classes=["center"])
    central_line(model, X_2, X_355, 2, 355)
    central_line(model, X_1, X_549, 1, 549)
    X_3653 = intersect_lines(model, X_2, X_355, X_1, X_549, ID="X_3653", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_551 = eval_trilinear_point(model, A, B, C, '(4*a + b + c)/a', ID="X_551", classes=["center", "incident"])
    central_line(model, X_3, X_551, 3, 551, incident=True)
    return promote_point_to_top(model, X_3653)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3653 on the given reference triangle."""
    model = create_model('X_3653 = CENTROID OF {X_1, X_2, X_3}')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03653(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03653.json"))
    write_center_svg(
        model_acute,
        here / "x-03653.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
