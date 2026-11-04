"""GEOMETOR construction model for X_2132 = EIGENTRANSFORM OF X_30."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02132(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2132 = EIGENTRANSFORM OF X_30 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_1138 = eval_trilinear_point(model, A, B, C, '(1/(5*cos(A) - 4*cos(B)*cos(C) - 8*(cos(A))**(2)*sin(B)*sin(C)))', ID="X_1138", classes=["center"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center"])
    X_2133 = point_from_barycentrics(model, A, B, C, -0.66648885, 0.7236793, 0.94280955, ID="X_2133", classes=["center"])
    central_line(model, X_4, X_1138, 4, 1138)
    central_line(model, X_30, X_2133, 30, 2133)
    X_2132 = intersect_lines(model, X_4, X_1138, X_30, X_2133, ID="X_2132", classes=["selected", "target"])
    return promote_point_to_top(model, X_2132)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2132 on the given reference triangle."""
    model = create_model('X_2132 = EIGENTRANSFORM OF X_30')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02132(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02132.json"))
    write_center_svg(
        model_acute,
        here / "x-02132.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
