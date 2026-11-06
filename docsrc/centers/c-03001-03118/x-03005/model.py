"""GEOMETOR construction model for X_3005 = (DE LONGCHAMPS LINE)∩(LEMOINE AXIS)."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03005(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3005 = (DE LONGCHAMPS LINE)∩(LEMOINE AXIS) on reference triangle ABC."""
    X_689 = eval_trilinear_point(model, A, B, C, '1/(a**(3)*(b**(4) - c**(4)))', ID="X_689", classes=["center"])
    X_3005 = isotomic_conjugate(model, A, B, C, X_689, ID="X_3005", classes=["selected", "target"])
    X_187 = eval_trilinear_point(model, A, B, C, 'a*(2*a**(2) - b**(2) - c**(2))', ID="X_187", classes=["center", "incident"])
    X_237 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A +  omega  )', ID="X_237", classes=["center", "incident"])
    central_line(model, X_187, X_237, 187, 237, incident=True)
    X_325 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)', ID="X_325", classes=["center", "incident"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center", "incident"])
    central_line(model, X_325, X_523, 325, 523, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_881 = point_from_barycentrics(model, A, B, C, 0.016681659, 1.0244659, -0.041147528, ID="X_881", classes=["center", "incident"])
    central_line(model, X_2, X_881, 2, 881, incident=True)
    return promote_point_to_top(model, X_3005)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3005 on the given reference triangle."""
    model = create_model('X_3005 = (DE LONGCHAMPS LINE)∩(LEMOINE AXIS)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03005(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03005.json"))
    write_center_svg(
        model_acute,
        here / "x-03005.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
