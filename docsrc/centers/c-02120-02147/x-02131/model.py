"""GEOMETOR construction model for X_2131 = ISOGONAL CONJUGATE OF X_2130."""

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


def construct_x_02131(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2131 = ISOGONAL CONJUGATE OF X_2130 on reference triangle ABC."""
    X_2130 = point_from_barycentrics(model, A, B, C, 0.19373197, 0.27423005, 0.53203798, ID="X_2130", classes=["center"])
    X_2131 = isogonal_conjugate(model, A, B, C, X_2130, ID="X_2131", classes=["selected", "target"])
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    central_line(model, X_20, X_2130, 20, 2130, incident=True)
    return promote_point_to_top(model, X_2131)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2131 on the given reference triangle."""
    model = create_model('X_2131 = ISOGONAL CONJUGATE OF X_2130')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02131(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02131.json"))
    write_center_svg(
        model_acute,
        here / "x-02131.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
