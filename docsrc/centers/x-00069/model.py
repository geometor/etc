"""GEOMETOR construction model for X(69) = SYMMEDIAN POINT OF THE ANTICOMPLEMENTARY TRIANGLE."""

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
    gergonne_point_of,
    isogonal_conjugate,
    nagel_point_of,
    promote_point_to_top,
    symmedian_point_of,
    tangential_triangle,
)
from geometor.etc.render import write_center_svg


def construct_x_00069(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(69) = SYMMEDIAN POINT OF THE ANTICOMPLEMENTARY TRIANGLE on reference triangle ABC."""
    tangential_triangle(model, A, B, C)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    central_line(model, X_2, X_6, 2, 6)
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center"])
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center"])
    central_line(model, X_7, X_8, 7, 8)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X(20)", classes=["center"])
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X(64)", classes=["center"])
    central_line(model, X_20, X_64, 20, 64)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X(25)", classes=["center"])
    X_69 = isogonal_conjugate(model, A, B, C, X_25, ID="X(69)", classes=["selected", "target"])
    return promote_point_to_top(model, X_69)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(69) on the given reference triangle."""
    model = create_model('X(69) = SYMMEDIAN POINT OF THE ANTICOMPLEMENTARY TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00069(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00069.json"))
    write_center_svg(
        model_acute,
        here / "x-00069.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
