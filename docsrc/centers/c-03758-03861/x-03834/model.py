"""GEOMETOR construction model for X_3834 = X_1266com(3rd EULER TRIANGLE)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    complement,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03834(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3834 = X_1266com(3rd EULER TRIANGLE) on reference triangle ABC."""
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center"])
    X_3834 = complement(model, A, B, C, X_44, ID="X_3834", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_2, X_44, 2, 44, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X_141", classes=["center", "incident"])
    central_line(model, X_10, X_141, 10, 141, incident=True)
    X_536 = eval_barycentric_point(model, A, B, C, '2*b*c - c*a - a*b', ID="X_536", classes=["center", "incident"])
    X_1086 = eval_trilinear_point(model, A, B, C, '(b*c*(b - c)**(2))', ID="X_1086", classes=["center", "incident"])
    central_line(model, X_536, X_1086, 536, 1086, incident=True)
    return promote_point_to_top(model, X_3834)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3834 on the given reference triangle."""
    model = create_model('X_3834 = X_1266com(3rd EULER TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03834(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03834.json"))
    write_center_svg(
        model_acute,
        here / "x-03834.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
