"""GEOMETOR construction model for X_1549 = ORTHOJOIN OF X_73."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01549(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1549 = ORTHOJOIN OF X_73 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_117 = point_from_barycentrics(model, A, B, C, 0.19223485, -0.017045455, 0.82481061, ID="X_117", classes=["center"])
    X_515 = eval_trilinear_point(model, A, B, C, '(b + c)*sec(A) - b*sec(B) - c*sec(C)', ID="X_515", classes=["center"])
    central_line(model, X_4, X_6, 4, 6)
    central_line(model, X_117, X_515, 117, 515)
    X_1549 = intersect_lines(model, X_4, X_6, X_117, X_515, ID="X_1549", classes=["selected", "target"])
    return promote_point_to_top(model, X_1549)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1549 on the given reference triangle."""
    model = create_model('X_1549 = ORTHOJOIN OF X_73')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01549(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01549.json"))
    write_center_svg(
        model_acute,
        here / "x-01549.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
