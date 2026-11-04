"""GEOMETOR construction model for X_1728 = MIMOSA TRANSFORM OF X_84."""

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
    intersect_lines,
    nine_point_center_of,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01728(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1728 = MIMOSA TRANSFORM OF X_84 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center"])
    central_line(model, X_1, X_6, 1, 6)
    central_line(model, X_4, X_46, 4, 46)
    X_1728 = intersect_lines(model, X_1, X_6, X_4, X_46, ID="X_1728", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    central_line(model, X_5, X_57, 5, 57, incident=True)
    return promote_point_to_top(model, X_1728)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1728 on the given reference triangle."""
    model = create_model('X_1728 = MIMOSA TRANSFORM OF X_84')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01728(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01728.json"))
    write_center_svg(
        model_acute,
        here / "x-01728.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
