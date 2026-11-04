"""GEOMETOR construction model for X_2468 = EXSIMILICENTER(ORTHOCENTROIDALCIRCLE, SPIEKER CIRCLE)."""

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
    nagel_point_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02468(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2468 = EXSIMILICENTER(ORTHOCENTROIDALCIRCLE, SPIEKER CIRCLE) on reference triangle ABC."""
    X_2468 = eval_trilinear_point(model, A, B, C, '(b*c*(a*cos(A) + 4*a*cos(B)*cos(C) - (b + c)*J))', ID="X_2468", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_381 = eval_trilinear_point(model, A, B, C, '2*cos(B - C) - cos(A)', ID="X_381", classes=["center", "incident"])
    central_line(model, X_10, X_381, 10, 381, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_2463 = eval_trilinear_point(model, A, B, C, '(J + cos(A) + 4*cos(B)*cos(C))', ID="X_2463", classes=["center", "incident"])
    central_line(model, X_2, X_2463, 2, 2463, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_2464 = eval_trilinear_point(model, A, B, C, '(J - cos(A) - 4*cos(B)*cos(C))', ID="X_2464", classes=["center", "incident"])
    central_line(model, X_8, X_2464, 8, 2464, incident=True)
    return promote_point_to_top(model, X_2468)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2468 on the given reference triangle."""
    model = create_model('X_2468 = EXSIMILICENTER(ORTHOCENTROIDALCIRCLE, SPIEKER CIRCLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02468(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02468.json"))
    write_center_svg(
        model_acute,
        here / "x-02468.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
