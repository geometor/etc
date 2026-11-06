"""GEOMETOR construction model for X_3376 = COT(A - π/3) POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03376(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3376 = COT(A - π/3) POINT on reference triangle ABC."""
    X_3375 = eval_trilinear_point(model, A, B, C, '(tan(A -  pi  /3))', ID="X_3375", classes=["center"])
    X_3376 = isogonal_conjugate(model, A, B, C, X_3375, ID="X_3376", classes=["selected", "target"])
    X_14 = eval_trilinear_point(model, A, B, C, 'csc(A -  pi  /3)', ID="X_14", classes=["center", "incident"])
    X_484 = eval_trilinear_point(model, A, B, C, '1 + 2*(cos(A) - cos(B) - cos(C))', ID="X_484", classes=["center", "incident"])
    central_line(model, X_14, X_484, 14, 484, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_1095 = eval_trilinear_point(model, A, B, C, '((sin(A -  pi  /3))**(2))', ID="X_1095", classes=["center", "incident"])
    central_line(model, X_1, X_1095, 1, 1095, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_2166 = eval_trilinear_point(model, A, B, C, '(sin(A)*csc(3*A))', ID="X_2166", classes=["center", "incident"])
    central_line(model, X_19, X_2166, 19, 2166, incident=True)
    return promote_point_to_top(model, X_3376)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3376 on the given reference triangle."""
    model = create_model('X_3376 = COT(A - π/3) POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03376(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03376.json"))
    write_center_svg(
        model_acute,
        here / "x-03376.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
