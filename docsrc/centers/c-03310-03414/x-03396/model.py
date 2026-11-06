"""GEOMETOR construction model for X_3396 = SIN(A + 2π/5) POINT."""

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
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03396(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3396 = SIN(A + 2π/5) POINT on reference triangle ABC."""
    X_1139 = eval_trilinear_point(model, A, B, C, '(csc(A))/(cot(A) + cot(2*pi/5))', ID="X_1139", classes=["center"])
    X_3396 = isogonal_conjugate(model, A, B, C, X_1139, ID="X_3396", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_1140 = eval_trilinear_point(model, A, B, C, '(csc(A))/(cot(A) - cot(2*pi/5))', ID="X_1140", classes=["center", "incident"])
    central_line(model, X_2, X_1140, 2, 1140, incident=True)
    return promote_point_to_top(model, X_3396)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3396 on the given reference triangle."""
    model = create_model('X_3396 = SIN(A + 2π/5) POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03396(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03396.json"))
    write_center_svg(
        model_acute,
        here / "x-03396.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
