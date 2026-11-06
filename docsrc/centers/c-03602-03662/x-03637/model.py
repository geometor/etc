"""GEOMETOR construction model for X_3637 = ISOGONAL CONJUGATE OF X_3355."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03637(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3637 = ISOGONAL CONJUGATE OF X_3355 on reference triangle ABC."""
    X_3355 = point_from_barycentrics(model, A, B, C, 0.50188901, 0.4191657, 0.078945292, ID="X_3355", classes=["center"])
    X_3637 = isogonal_conjugate(model, A, B, C, X_3355, ID="X_3637", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_3356 = point_from_barycentrics(model, A, B, C, 0.20864715, 0.31834191, 0.47301094, ID="X_3356", classes=["center", "incident"])
    central_line(model, X_4, X_3356, 4, 3356, incident=True)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    central_line(model, X_20, X_3355, 20, 3355, incident=True)
    X_1498 = eval_trilinear_point(model, A, B, C, '(sin(A))*((tan(B))**(2) + (tan(C))**(2) - (tan(A))**(2))', ID="X_1498", classes=["center", "incident"])
    X_2130 = point_from_barycentrics(model, A, B, C, 0.19373197, 0.27423005, 0.53203798, ID="X_2130", classes=["center", "incident"])
    central_line(model, X_1498, X_2130, 1498, 2130, incident=True)
    return promote_point_to_top(model, X_3637)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3637 on the given reference triangle."""
    model = create_model('X_3637 = ISOGONAL CONJUGATE OF X_3355')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03637(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03637.json"))
    write_center_svg(
        model_acute,
        here / "x-03637.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
