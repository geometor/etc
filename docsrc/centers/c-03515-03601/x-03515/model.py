"""GEOMETOR construction model for X_3515 = EULER LINE INTERCEPT OF LINE X_154X_185."""

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
    crosspoint,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03515(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3515 = EULER LINE INTERCEPT OF LINE X_154X_185 on reference triangle ABC."""
    X_250 = eval_trilinear_point(model, A, B, C, '(sec(A))*(csc(B - C))**(2)', ID="X_250", classes=["center"])
    X_1301 = point_from_barycentrics(model, A, B, C, -0.036707118, 0.057047829, 0.97965929, ID="X_1301", classes=["center"])
    X_3515 = crosspoint(model, A, B, C, X_250, X_1301, ID="X_3515", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_154 = eval_trilinear_point(model, A, B, C, '(cos(A) - cos(B)*cos(C))*a**(2)', ID="X_154", classes=["center", "incident"])
    X_185 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 - cos(A)*cos(B - C))', ID="X_185", classes=["center", "incident"])
    central_line(model, X_154, X_185, 154, 185, incident=True)
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_1398 = eval_trilinear_point(model, A, B, C, '(sec(A)*(sin(A/2))**(4))', ID="X_1398", classes=["center", "incident"])
    central_line(model, X_36, X_1398, 36, 1398, incident=True)
    return promote_point_to_top(model, X_3515)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3515 on the given reference triangle."""
    model = create_model('X_3515 = EULER LINE INTERCEPT OF LINE X_154X_185')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03515(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03515.json"))
    write_center_svg(
        model_acute,
        here / "x-03515.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
