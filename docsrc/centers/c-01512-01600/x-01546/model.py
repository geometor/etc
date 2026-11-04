"""GEOMETOR construction model for X_1546 = ORTHOJOIN OF X_62."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01546(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1546 = ORTHOJOIN OF X_62 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_16 = eval_trilinear_point(model, A, B, C, 'sin(A-  pi  /3)', ID="X_16", classes=["center"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center"])
    X_113 = eval_trilinear_point(model, A, B, C, 'sin(B)*sin(C)*((sin(C))/(cos(C) - 2*cos(A)*cos(B)) + (sin(B))/(cos(B) - 2*cos(A)*cos(C)))', ID="X_113", classes=["center"])
    central_line(model, X_4, X_16, 4, 16)
    central_line(model, X_30, X_113, 30, 113)
    X_1546 = intersect_lines(model, X_4, X_16, X_30, X_113, ID="X_1546", classes=["selected", "target"])
    return promote_point_to_top(model, X_1546)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1546 on the given reference triangle."""
    model = create_model('X_1546 = ORTHOJOIN OF X_62')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01546(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01546.json"))
    write_center_svg(
        model_acute,
        here / "x-01546.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
