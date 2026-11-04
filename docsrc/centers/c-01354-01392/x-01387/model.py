"""GEOMETOR construction model for X_1387 = MIDPOINT OF INCENTER AND FEUERBACH POINT."""

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
    incenter_of,
    intersect_lines,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01387(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1387 = MIDPOINT OF INCENTER AND FEUERBACH POINT on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center"])
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center"])
    central_line(model, X_1, X_5, 1, 5)
    central_line(model, X_7, X_104, 7, 104)
    X_1387 = intersect_lines(model, X_1, X_5, X_7, X_104, ID="X_1387", classes=["selected", "target"])
    X_142 = eval_trilinear_point(model, A, B, C, 'b + c - ((b - c)**(2))/a', ID="X_142", classes=["center", "incident"])
    X_214 = eval_trilinear_point(model, A, B, C, '(b + c - 2*a)*(b**(2) + c**(2) - a**(2) - b*c)', ID="X_214", classes=["center", "incident"])
    central_line(model, X_142, X_214, 142, 214, incident=True)
    return promote_point_to_top(model, X_1387)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1387 on the given reference triangle."""
    model = create_model('X_1387 = MIDPOINT OF INCENTER AND FEUERBACH POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01387(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01387.json"))
    write_center_svg(
        model_acute,
        here / "x-01387.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
