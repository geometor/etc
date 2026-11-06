"""GEOMETOR construction model for X_3573 = TRILINEAR PRODUCT X_6*X_3570."""

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
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03573(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3573 = TRILINEAR PRODUCT X_6*X_3570 on reference triangle ABC."""
    X_876 = point_from_barycentrics(model, A, B, C, 0.024662513, 1.0062305, -0.030893043, ID="X_876", classes=["center"])
    X_3573 = isogonal_conjugate(model, A, B, C, X_876, ID="X_3573", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    central_line(model, X_1, X_21, 1, 21, incident=True)
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    central_line(model, X_100, X_101, 100, 101, incident=True)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_99, X_110, 99, 110, incident=True)
    return promote_point_to_top(model, X_3573)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3573 on the given reference triangle."""
    model = create_model('X_3573 = TRILINEAR PRODUCT X_6*X_3570')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03573(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03573.json"))
    write_center_svg(
        model_acute,
        here / "x-03573.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
