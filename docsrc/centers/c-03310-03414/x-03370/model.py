"""GEOMETOR construction model for X_3370 = SEC(A - 2π/5) POINT."""

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
    isogonal_conjugate,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03370(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3370 = SEC(A - 2π/5) POINT on reference triangle ABC."""
    X_3368 = eval_trilinear_point(model, A, B, C, '(cos(A - 2*pi  /5))', ID="X_3368", classes=["center"])
    X_3370 = isogonal_conjugate(model, A, B, C, X_3368, ID="X_3370", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_1139 = eval_trilinear_point(model, A, B, C, '(csc(A))/(cot(A) + cot(2*pi/5))', ID="X_1139", classes=["center", "incident"])
    central_line(model, X_3, X_1139, 3, 1139, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_1140 = eval_trilinear_point(model, A, B, C, '(csc(A))/(cot(A) - cot(2*pi/5))', ID="X_1140", classes=["center", "incident"])
    central_line(model, X_5, X_1140, 5, 1140, incident=True)
    return promote_point_to_top(model, X_3370)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3370 on the given reference triangle."""
    model = create_model('X_3370 = SEC(A - 2π/5) POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03370(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03370.json"))
    write_center_svg(
        model_acute,
        here / "x-03370.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
