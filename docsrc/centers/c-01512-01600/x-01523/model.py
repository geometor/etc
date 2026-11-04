"""GEOMETOR construction model for X_1523 = ORTHOJOIN OF X_14."""

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


def construct_x_01523(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1523 = ORTHOJOIN OF X_14 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A +  pi  /3)', ID="X_13", classes=["center"])
    X_1522 = point_from_barycentrics(model, A, B, C, 0.38293819, 7.4446686, -6.8276068, ID="X_1522", classes=["center"])
    X_1553 = point_from_barycentrics(model, A, B, C, -0.051778529, -0.24504162, 1.2968202, ID="X_1553", classes=["center"])
    central_line(model, X_4, X_13, 4, 13)
    central_line(model, X_1522, X_1553, 1522, 1553)
    X_1523 = intersect_lines(model, X_4, X_13, X_1522, X_1553, ID="X_1523", classes=["selected", "target"])
    return promote_point_to_top(model, X_1523)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1523 on the given reference triangle."""
    model = create_model('X_1523 = ORTHOJOIN OF X_14')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01523(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01523.json"))
    write_center_svg(
        model_acute,
        here / "x-01523.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
