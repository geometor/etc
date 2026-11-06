"""GEOMETOR construction model for X_3842 = X_3688com(4th EULER TRIANGLE)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03842(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3842 = X_3688com(4th EULER TRIANGLE) on reference triangle ABC."""
    X_3842 = eval_barycentric_point(model, A, B, C, '((b + c)*(a**(2) + 2*a*b + 2*a*c + b*c))', ID="X_3842", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_38 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2)', ID="X_38", classes=["center", "incident"])
    central_line(model, X_2, X_38, 2, 38, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    central_line(model, X_10, X_37, 10, 37, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_872 = eval_trilinear_point(model, A, B, C, '(a*(b + c))**(2)', ID="X_872", classes=["center", "incident"])
    central_line(model, X_1, X_872, 1, 872, incident=True)
    return promote_point_to_top(model, X_3842)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3842 on the given reference triangle."""
    model = create_model('X_3842 = X_3688com(4th EULER TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03842(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03842.json"))
    write_center_svg(
        model_acute,
        here / "x-03842.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
