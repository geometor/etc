"""GEOMETOR construction model for X_1874 = ZOSMA TRANSFORM OF X_511."""

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
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01874(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1874 = ZOSMA TRANSFORM OF X_511 on reference triangle ABC."""
    X_1808 = point_from_barycentrics(model, A, B, C, -0.084715225, 1.0671577, 0.017557534, ID="X_1808", classes=["center"])
    X_1874 = isogonal_conjugate(model, A, B, C, X_1808, ID="X_1874", classes=["selected", "target"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    central_line(model, X_12, X_37, 12, 37, incident=True)
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X_29", classes=["center", "incident"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center", "incident"])
    central_line(model, X_29, X_34, 29, 34, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_240 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(A + omega )', ID="X_240", classes=["center", "incident"])
    central_line(model, X_4, X_240, 4, 240, incident=True)
    return promote_point_to_top(model, X_1874)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1874 on the given reference triangle."""
    model = create_model('X_1874 = ZOSMA TRANSFORM OF X_511')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01874(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01874.json"))
    write_center_svg(
        model_acute,
        here / "x-01874.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
