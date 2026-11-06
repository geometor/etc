"""GEOMETOR construction model for X_3473 = ISOGONAL CONJUGATE OF X_3472."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03473(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3473 = ISOGONAL CONJUGATE OF X_3472 on reference triangle ABC."""
    X_3472 = point_from_barycentrics(model, A, B, C, 0.34317873, 0.36369686, 0.2931244, ID="X_3472", classes=["center"])
    X_3473 = isogonal_conjugate(model, A, B, C, X_3472, ID="X_3473", classes=["selected", "target"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    X_3355 = point_from_barycentrics(model, A, B, C, 0.50188901, 0.4191657, 0.078945292, ID="X_3355", classes=["center", "incident"])
    central_line(model, X_40, X_3355, 40, 3355, incident=True)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    central_line(model, X_20, X_3472, 20, 3472, incident=True)
    X_1490 = eval_trilinear_point(model, A, B, C, '1 + sec(A) - sec(B) - sec(C)', ID="X_1490", classes=["center", "incident"])
    X_2130 = point_from_barycentrics(model, A, B, C, 0.19373197, 0.27423005, 0.53203798, ID="X_2130", classes=["center", "incident"])
    central_line(model, X_1490, X_2130, 1490, 2130, incident=True)
    return promote_point_to_top(model, X_3473)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3473 on the given reference triangle."""
    model = create_model('X_3473 = ISOGONAL CONJUGATE OF X_3472')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03473(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03473.json"))
    write_center_svg(
        model_acute,
        here / "x-03473.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
