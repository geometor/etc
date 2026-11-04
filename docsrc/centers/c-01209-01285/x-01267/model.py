"""GEOMETOR construction model for X_1267 = ISOTOMIC CONJUGATE OF X_1123."""

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
    isotomic_conjugate,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01267(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1267 = ISOTOMIC CONJUGATE OF X_1123 on reference triangle ABC."""
    X_1123 = eval_trilinear_point(model, A, B, C, '1/(1 +sin(A))', ID="X_1123", classes=["center"])
    X_1267 = isotomic_conjugate(model, A, B, C, X_1123, ID="X_1267", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    central_line(model, X_2, X_37, 2, 37, incident=True)
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_492 = eval_trilinear_point(model, A, B, C, '((cos(A))*(1 + csc(A)*sin(B)*sin(C)) + cos(B)*cos(C))', ID="X_492", classes=["center", "incident"])
    central_line(model, X_7, X_492, 7, 492, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_491 = eval_trilinear_point(model, A, B, C, '((cos(A))*(1 - csc(A)*sin(B)*sin(C)) + cos(B)*cos(C))', ID="X_491", classes=["center", "incident"])
    central_line(model, X_8, X_491, 8, 491, incident=True)
    return promote_point_to_top(model, X_1267)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1267 on the given reference triangle."""
    model = create_model('X_1267 = ISOTOMIC CONJUGATE OF X_1123')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01267(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01267.json"))
    write_center_svg(
        model_acute,
        here / "x-01267.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
