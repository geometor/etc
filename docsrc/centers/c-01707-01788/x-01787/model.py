"""GEOMETOR construction model for X_1787 = MIMOSA TRANSFORM OF X_1443."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01787(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1787 = MIMOSA TRANSFORM OF X_1443 on reference triangle ABC."""
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    X_88 = eval_trilinear_point(model, A, B, C, '1/(b + c - 2*a)', ID="X_88", classes=["center"])
    central_line(model, X_34, X_46, 34, 46)
    central_line(model, X_57, X_88, 57, 88)
    X_1787 = intersect_lines(model, X_34, X_46, X_57, X_88, ID="X_1787", classes=["selected", "target"])
    X_1020 = eval_trilinear_point(model, A, B, C, '(cos(B) + cos(C))/(cos(B) - cos(C))', ID="X_1020", classes=["center", "incident"])
    X_1435 = point_from_barycentrics(model, A, B, C, 0.030894309, 0.10406504, 0.86504065, ID="X_1435", classes=["center", "incident"])
    central_line(model, X_1020, X_1435, 1020, 1435, incident=True)
    return promote_point_to_top(model, X_1787)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1787 on the given reference triangle."""
    model = create_model('X_1787 = MIMOSA TRANSFORM OF X_1443')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01787(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01787.json"))
    write_center_svg(
        model_acute,
        here / "x-01787.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
