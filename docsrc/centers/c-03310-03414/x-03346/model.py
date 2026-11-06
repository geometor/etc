"""GEOMETOR construction model for X_3346 = ISOGONAL CONJUGATE OF X_1498."""

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
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_03346(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3346 = ISOGONAL CONJUGATE OF X_1498 on reference triangle ABC."""
    X_3183 = point_from_barycentrics(model, A, B, C, -0.24902136, -0.46731562, 1.716337, ID="X_3183", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_3346 = reflection_in_point(model, X_3183, X_3, ID="X_3346", classes=["selected", "target"], guide=False)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_394 = eval_trilinear_point(model, A, B, C, 'cos(A)*cot(A)', ID="X_394", classes=["center", "incident"])
    central_line(model, X_20, X_394, 20, 394, incident=True)
    X_1033 = point_from_barycentrics(model, A, B, C, -0.20250392, -0.4085329, 1.6110368, ID="X_1033", classes=["center", "incident"])
    central_line(model, X_3, X_1033, 3, 1033, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_1073 = eval_trilinear_point(model, A, B, C, '((cot(A))/(cos(A) - cos(B)*cos(C)))', ID="X_1073", classes=["center", "incident"])
    central_line(model, X_4, X_1073, 4, 1073, incident=True)
    return promote_point_to_top(model, X_3346)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3346 on the given reference triangle."""
    model = create_model('X_3346 = ISOGONAL CONJUGATE OF X_1498')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03346(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03346.json"))
    write_center_svg(
        model_acute,
        here / "x-03346.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
