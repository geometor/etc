"""GEOMETOR construction model for X_2463 = INSIMILICENTER(ORTHOCENTROIDAL CIRCLE, INCIRCLE)."""

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
    incenter_of,
    nagel_point_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02463(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2463 = INSIMILICENTER(ORTHOCENTROIDAL CIRCLE, INCIRCLE) on reference triangle ABC."""
    X_2463 = eval_trilinear_point(model, A, B, C, '(J + cos(A) + 4*cos(B)*cos(C))', ID="X_2463", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_381 = eval_trilinear_point(model, A, B, C, '2*cos(B - C) - cos(A)', ID="X_381", classes=["center", "incident"])
    central_line(model, X_1, X_381, 1, 381, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_2468 = eval_trilinear_point(model, A, B, C, '(b*c*(a*cos(A) + 4*a*cos(B)*cos(C) - (b + c)*J))', ID="X_2468", classes=["center", "incident"])
    central_line(model, X_2, X_2468, 2, 2468, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_2467 = point_from_barycentrics(model, A, B, C, 0.29344052, 0.3004125, 0.40614698, ID="X_2467", classes=["center", "incident"])
    central_line(model, X_8, X_2467, 8, 2467, incident=True)
    return promote_point_to_top(model, X_2463)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2463 on the given reference triangle."""
    model = create_model('X_2463 = INSIMILICENTER(ORTHOCENTROIDAL CIRCLE, INCIRCLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02463(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02463.json"))
    write_center_svg(
        model_acute,
        here / "x-02463.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
