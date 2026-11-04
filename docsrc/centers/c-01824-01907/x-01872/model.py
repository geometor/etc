"""GEOMETOR construction model for X_1872 = ZOSMA TRANSFORM OF X_499."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    nagel_point_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01872(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1872 = ZOSMA TRANSFORM OF X_499 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center"])
    central_line(model, X_4, X_8, 4, 8)
    central_line(model, X_3, X_33, 3, 33)
    X_1872 = intersect_lines(model, X_4, X_8, X_3, X_33, ID="X_1872", classes=["selected", "target"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center", "incident"])
    X_1482 = point_from_barycentrics(model, A, B, C, 0.12152778, 0.27083333, 0.60763889, ID="X_1482", classes=["center", "incident"])
    central_line(model, X_34, X_1482, 34, 1482, incident=True)
    return promote_point_to_top(model, X_1872)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1872 on the given reference triangle."""
    model = create_model('X_1872 = ZOSMA TRANSFORM OF X_499')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01872(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01872.json"))
    write_center_svg(
        model_acute,
        here / "x-01872.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
