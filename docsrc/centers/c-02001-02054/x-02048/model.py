"""GEOMETOR construction model for X_2048 = {X_3,X_5}-HARMONIC CONJUGATE OF X_2047."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02048(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2048 = {X_3,X_5}-HARMONIC CONJUGATE OF X_2047 on reference triangle ABC."""
    X_2048 = eval_trilinear_point(model, A, B, C, '((s - r)*cos(A) - (s + r)*cos(B - C))', ID="X_2048", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_486 = eval_trilinear_point(model, A, B, C, 'sec(A +  pi  /4)', ID="X_486", classes=["center", "incident"])
    X_1686 = eval_trilinear_point(model, A, B, C, '((r + s)*sin(A) + (r - s)*cos(A))', ID="X_1686", classes=["center", "incident"])
    central_line(model, X_486, X_1686, 486, 1686, incident=True)
    return promote_point_to_top(model, X_2048)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2048 on the given reference triangle."""
    model = create_model('X_2048 = {X_3,X_5}-HARMONIC CONJUGATE OF X_2047')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02048(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02048.json"))
    write_center_svg(
        model_acute,
        here / "x-02048.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
