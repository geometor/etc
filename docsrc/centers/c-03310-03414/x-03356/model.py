"""GEOMETOR construction model for X_3356 = X_6-CROSS CONJUGATE OF X_3350."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03356(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3356 = X_6-CROSS CONJUGATE OF X_3350 on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_2131 = point_from_barycentrics(model, A, B, C, 0.36616655, 0.37250097, 0.26133249, ID="X_2131", classes=["center"])
    X_223 = eval_trilinear_point(model, A, B, C, '(tan(A/2))*(cos(B) + cos(C) - cos(A) - 1)', ID="X_223", classes=["center"])
    X_3351 = point_from_barycentrics(model, A, B, C, 0.20257124, 0.3139591, 0.48346966, ID="X_3351", classes=["center"])
    central_line(model, X_3, X_2131, 3, 2131)
    central_line(model, X_223, X_3351, 223, 3351)
    X_3356 = intersect_lines(model, X_3, X_2131, X_223, X_3351, ID="X_3356", classes=["selected", "target"])
    X_1249 = eval_trilinear_point(model, A, B, C, '(tan(A))*(cos(A) - cos(B)*cos(C))', ID="X_1249", classes=["center", "incident"])
    X_3343 = point_from_barycentrics(model, A, B, C, 0.15926582, 0.25678823, 0.58394595, ID="X_3343", classes=["center", "incident"])
    central_line(model, X_1249, X_3343, 1249, 3343, incident=True)
    return promote_point_to_top(model, X_3356)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3356 on the given reference triangle."""
    model = create_model('X_3356 = X_6-CROSS CONJUGATE OF X_3350')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03356(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03356.json"))
    write_center_svg(
        model_acute,
        here / "x-03356.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
