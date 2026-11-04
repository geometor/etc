"""GEOMETOR construction model for X_1110 = TRILINEAR SQUARE OF X_101."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01110(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1110 = TRILINEAR SQUARE OF X_101 on reference triangle ABC."""
    X_1110 = eval_trilinear_point(model, A, B, C, '((a/(b - c))**(2))', ID="X_1110", classes=["selected", "target"])
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_59 = eval_trilinear_point(model, A, B, C, '1/(1 - cos(B - C))', ID="X_59", classes=["center", "incident"])
    central_line(model, X_36, X_59, 36, 59, incident=True)
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    X_663 = eval_trilinear_point(model, A, B, C, 'a*(b - c)*(b + c - a)', ID="X_663", classes=["center", "incident"])
    central_line(model, X_101, X_663, 101, 663, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_1053 = point_from_barycentrics(model, A, B, C, 0.37037037, 0.88888889, -0.25925926, ID="X_1053", classes=["center", "incident"])
    central_line(model, X_1, X_1053, 1, 1053, incident=True)
    return promote_point_to_top(model, X_1110)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1110 on the given reference triangle."""
    model = create_model('X_1110 = TRILINEAR SQUARE OF X_101')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01110(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01110.json"))
    write_center_svg(
        model_acute,
        here / "x-01110.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
