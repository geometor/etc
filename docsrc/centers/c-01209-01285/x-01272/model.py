"""GEOMETOR construction model for X_1272 = ISOTOMIC CONJUGATE OF X_1138."""

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
    isotomic_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01272(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1272 = ISOTOMIC CONJUGATE OF X_1138 on reference triangle ABC."""
    X_1138 = eval_trilinear_point(model, A, B, C, '(1/(5*cos(A) - 4*cos(B)*cos(C) - 8*(cos(A))**(2)*sin(B)*sin(C)))', ID="X_1138", classes=["center"])
    X_1272 = isotomic_conjugate(model, A, B, C, X_1138, ID="X_1272", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_94 = eval_trilinear_point(model, A, B, C, 'csc(3*A)', ID="X_94", classes=["center", "incident"])
    central_line(model, X_2, X_94, 2, 94, incident=True)
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center", "incident"])
    central_line(model, X_69, X_74, 69, 74, incident=True)
    return promote_point_to_top(model, X_1272)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1272 on the given reference triangle."""
    model = create_model('X_1272 = ISOTOMIC CONJUGATE OF X_1138')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01272(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01272.json"))
    write_center_svg(
        model_acute,
        here / "x-01272.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
