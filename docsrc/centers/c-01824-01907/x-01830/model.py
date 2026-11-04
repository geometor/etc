"""GEOMETOR construction model for X_1830 = ZOSMA TRANSFORM OF X_11."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_01830(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1830 = ZOSMA TRANSFORM OF X_11 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_80 = eval_trilinear_point(model, A, B, C, '1/(1 - 2*cos(A))', ID="X_80", classes=["center"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    central_line(model, X_4, X_80, 4, 80)
    central_line(model, X_33, X_57, 33, 57)
    X_1830 = intersect_lines(model, X_4, X_80, X_33, X_57, ID="X_1830", classes=["selected", "target"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    X_1846 = point_from_barycentrics(model, A, B, C, 0.090909091, -1.5936216e-17, 0.90909091, ID="X_1846", classes=["center", "incident"])
    central_line(model, X_65, X_1846, 65, 1846, incident=True)
    return promote_point_to_top(model, X_1830)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1830 on the given reference triangle."""
    model = create_model('X_1830 = ZOSMA TRANSFORM OF X_11')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01830(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01830.json"))
    write_center_svg(
        model_acute,
        here / "x-01830.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
