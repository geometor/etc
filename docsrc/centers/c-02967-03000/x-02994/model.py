"""GEOMETOR construction model for X_2994 = CD(X_19)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    nagel_point_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02994(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2994 = CD(X_19) on reference triangle ABC."""
    X_2178 = point_from_barycentrics(model, A, B, C, 0.010841284, 0.20294883, 0.78620989, ID="X_2178", classes=["center"])
    X_2994 = isogonal_conjugate(model, A, B, C, X_2178, ID="X_2994", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_90 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C) - cos(A))', ID="X_90", classes=["center", "incident"])
    central_line(model, X_8, X_90, 8, 90, incident=True)
    X_312 = eval_trilinear_point(model, A, B, C, '(b + c - a)*b**(2)*c**(2)', ID="X_312", classes=["center", "incident"])
    X_319 = eval_trilinear_point(model, A, B, C, '(1 + 2*cos(A))/a**(2)', ID="X_319", classes=["center", "incident"])
    central_line(model, X_312, X_319, 312, 319, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_914 = point_from_barycentrics(model, A, B, C, 4.2307692, -1.4615385, -1.7692308, ID="X_914", classes=["center", "incident"])
    central_line(model, X_2, X_914, 2, 914, incident=True)
    return promote_point_to_top(model, X_2994)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2994 on the given reference triangle."""
    model = create_model('X_2994 = CD(X_19)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02994(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02994.json"))
    write_center_svg(
        model_acute,
        here / "x-02994.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
