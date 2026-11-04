"""GEOMETOR construction model for X_1878 = ZOSMA TRANSFORM OF X_519."""

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
    nagel_point_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01878(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1878 = ZOSMA TRANSFORM OF X_519 on reference triangle ABC."""
    X_1811 = point_from_barycentrics(model, A, B, C, -0.64102564, 1.4615385, 0.17948718, ID="X_1811", classes=["center"])
    X_1878 = isogonal_conjugate(model, A, B, C, X_1811, ID="X_1878", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    central_line(model, X_4, X_8, 4, 8, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    central_line(model, X_25, X_36, 25, 36, incident=True)
    X_428 = eval_trilinear_point(model, A, B, C, '3*sec(A) - csc(A)*tan(omega)', ID="X_428", classes=["center", "incident"])
    X_535 = point_from_barycentrics(model, A, B, C, -0.5703697, -0.22078827, 0.79115797, ID="X_535", classes=["center", "incident"])
    central_line(model, X_428, X_535, 428, 535, incident=True)
    return promote_point_to_top(model, X_1878)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1878 on the given reference triangle."""
    model = create_model('X_1878 = ZOSMA TRANSFORM OF X_519')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01878(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01878.json"))
    write_center_svg(
        model_acute,
        here / "x-01878.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
