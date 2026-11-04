"""GEOMETOR construction model for X_1786 = MIMOSA TRANSFORM OF X_1442."""

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


def construct_x_01786(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1786 = MIMOSA TRANSFORM OF X_1442 on reference triangle ABC."""
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X_77", classes=["center"])
    central_line(model, X_33, X_46, 33, 46)
    central_line(model, X_57, X_77, 57, 77)
    X_1786 = intersect_lines(model, X_33, X_46, X_57, X_77, ID="X_1786", classes=["selected", "target"])
    X_1730 = point_from_barycentrics(model, A, B, C, 0.060349255, 0.20441705, 0.73523369, ID="X_1730", classes=["center", "incident"])
    X_1787 = point_from_barycentrics(model, A, B, C, 0.40772532, -0.54935622, 1.1416309, ID="X_1787", classes=["center", "incident"])
    central_line(model, X_1730, X_1787, 1730, 1787, incident=True)
    return promote_point_to_top(model, X_1786)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1786 on the given reference triangle."""
    model = create_model('X_1786 = MIMOSA TRANSFORM OF X_1442')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01786(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01786.json"))
    write_center_svg(
        model_acute,
        here / "x-01786.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
