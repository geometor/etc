"""GEOMETOR construction model for X_3353 = X_20-CEVA CONJUGATE OF X_84."""

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
    incenter_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_03353(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3353 = X_20-CEVA CONJUGATE OF X_84 on reference triangle ABC."""
    X_3347 = point_from_barycentrics(model, A, B, C, 0.82737762, 0.71982677, -0.54720439, ID="X_3347", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_3353 = reflection_in_point(model, X_3347, X_3, ID="X_3353", classes=["selected", "target"], guide=False)
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X_64", classes=["center", "incident"])
    X_84 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C) - cos(A) - 1)', ID="X_84", classes=["center", "incident"])
    central_line(model, X_64, X_84, 64, 84, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_282 = eval_trilinear_point(model, A, B, C, '(cot(A/2))/(-1 - cos(A) + cos(B) + cos(C))', ID="X_282", classes=["center", "incident"])
    central_line(model, X_4, X_282, 4, 282, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_3346 = eval_trilinear_point(model, A, B, C, '1/((sin(A))*((tan(A))**(2) - (tan(B))**(2) - (tan(C))**(2)))', ID="X_3346", classes=["center", "incident"])
    central_line(model, X_1, X_3346, 1, 3346, incident=True)
    return promote_point_to_top(model, X_3353)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3353 on the given reference triangle."""
    model = create_model('X_3353 = X_20-CEVA CONJUGATE OF X_84')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03353(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03353.json"))
    write_center_svg(
        model_acute,
        here / "x-03353.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
