"""GEOMETOR construction model for X_2467 = INSIMILICENTER(ORTHOCENTROIDAL CIRCLE, SPIEKER CIRCLE)."""

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
    intersect_lines,
    nagel_point_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02467(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2467 = INSIMILICENTER(ORTHOCENTROIDAL CIRCLE, SPIEKER CIRCLE) on reference triangle ABC."""
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center"])
    X_381 = eval_trilinear_point(model, A, B, C, '2*cos(B - C) - cos(A)', ID="X_381", classes=["center"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_2464 = eval_trilinear_point(model, A, B, C, '(J - cos(A) - 4*cos(B)*cos(C))', ID="X_2464", classes=["center"])
    central_line(model, X_10, X_381, 10, 381)
    central_line(model, X_2, X_2464, 2, 2464)
    X_2467 = intersect_lines(model, X_10, X_381, X_2, X_2464, ID="X_2467", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_2463 = eval_trilinear_point(model, A, B, C, '(J + cos(A) + 4*cos(B)*cos(C))', ID="X_2463", classes=["center", "incident"])
    central_line(model, X_8, X_2463, 8, 2463, incident=True)
    return promote_point_to_top(model, X_2467)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2467 on the given reference triangle."""
    model = create_model('X_2467 = INSIMILICENTER(ORTHOCENTROIDAL CIRCLE, SPIEKER CIRCLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02467(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02467.json"))
    write_center_svg(
        model_acute,
        here / "x-02467.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
