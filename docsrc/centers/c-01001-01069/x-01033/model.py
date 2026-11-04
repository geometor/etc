"""GEOMETOR construction model for X_1033 = X_3-CEVA CONJUGATE OF X_25."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01033(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1033 = X_3-CEVA CONJUGATE OF X_25 on reference triangle ABC."""
    X_1032 = point_from_barycentrics(model, A, B, C, 0.68146836, 0.48642354, -0.1678919, ID="X_1032", classes=["center"])
    X_1033 = isogonal_conjugate(model, A, B, C, X_1032, ID="X_1033", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X_64", classes=["center", "incident"])
    central_line(model, X_6, X_64, 6, 64, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    central_line(model, X_19, X_56, 19, 56, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_204 = eval_trilinear_point(model, A, B, C, '((tan(A))*(tan(B) + tan(C) - tan(A)))', ID="X_204", classes=["center", "incident"])
    central_line(model, X_55, X_204, 55, 204, incident=True)
    return promote_point_to_top(model, X_1033)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1033 on the given reference triangle."""
    model = create_model('X_1033 = X_3-CEVA CONJUGATE OF X_25')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01033(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01033.json"))
    write_center_svg(
        model_acute,
        here / "x-01033.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
