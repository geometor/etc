"""GEOMETOR construction model for X_3484 = INTERSECTION OF LINES X_3X_2120 and X_4X_54."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03484(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3484 = INTERSECTION OF LINES X_3X_2120 and X_4X_54 on reference triangle ABC."""
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center"])
    X_1157 = eval_trilinear_point(model, A, B, C, '4*cos(A) + cos(3*A)*sec(A)*sec(B - C)', ID="X_1157", classes=["center"])
    X_3484 = ceva_conjugate(model, A, B, C, X_30, X_1157, ID="X_3484", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    central_line(model, X_4, X_54, 4, 54, incident=True)
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center", "incident"])
    central_line(model, X_74, X_1157, 74, 1157, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_2120 = point_from_barycentrics(model, A, B, C, 0.30475192, 0.22664215, 0.46860594, ID="X_2120", classes=["center", "incident"])
    central_line(model, X_3, X_2120, 3, 2120, incident=True)
    return promote_point_to_top(model, X_3484)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3484 on the given reference triangle."""
    model = create_model('X_3484 = INTERSECTION OF LINES X_3X_2120 and X_4X_54')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03484(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03484.json"))
    write_center_svg(
        model_acute,
        here / "x-03484.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
