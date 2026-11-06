"""GEOMETOR construction model for X_3481 = INTERSECTION OF LINES X_3X_2120 and X_4X_2121."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03481(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3481 = INTERSECTION OF LINES X_3X_2120 and X_4X_2121 on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_2120 = point_from_barycentrics(model, A, B, C, 0.30475192, 0.22664215, 0.46860594, ID="X_2120", classes=["center"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_2121 = point_from_barycentrics(model, A, B, C, 0.23747658, 0.45982126, 0.30270216, ID="X_2121", classes=["center"])
    central_line(model, X_3, X_2120, 3, 2120)
    central_line(model, X_4, X_2121, 4, 2121)
    X_3481 = intersect_lines(model, X_3, X_2120, X_4, X_2121, ID="X_3481", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_3482 = point_from_barycentrics(model, A, B, C, 0.79438361, 0.27851823, -0.072901845, ID="X_3482", classes=["center", "incident"])
    central_line(model, X_30, X_3482, 30, 3482, incident=True)
    return promote_point_to_top(model, X_3481)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3481 on the given reference triangle."""
    model = create_model('X_3481 = INTERSECTION OF LINES X_3X_2120 and X_4X_2121')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03481(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03481.json"))
    write_center_svg(
        model_acute,
        here / "x-03481.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
