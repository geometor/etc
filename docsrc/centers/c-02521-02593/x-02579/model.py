"""GEOMETOR construction model for X_2579 = X_2-ISOCONJUGATE OF X_1114."""

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


def construct_x_02579(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2579 = X_2-ISOCONJUGATE OF X_1114 on reference triangle ABC."""
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center"])
    X_163 = eval_trilinear_point(model, A, B, C, '(sin(2*A))/(sin(2*B) - sin(2*C))', ID="X_163", classes=["center"])
    X_1823 = point_from_barycentrics(model, A, B, C, 0.72123578, 0.4152025, -0.13643829, ID="X_1823", classes=["center"])
    central_line(model, X_44, X_513, 44, 513)
    central_line(model, X_163, X_1823, 163, 1823)
    X_2579 = intersect_lines(model, X_44, X_513, X_163, X_1823, ID="X_2579", classes=["selected", "target"])
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center", "incident"])
    X_2575 = point_from_barycentrics(model, A, B, C, -0.27702983, -0.52664737, 0.80367719, ID="X_2575", classes=["center", "incident"])
    central_line(model, X_71, X_2575, 71, 2575, incident=True)
    return promote_point_to_top(model, X_2579)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2579 on the given reference triangle."""
    model = create_model('X_2579 = X_2-ISOCONJUGATE OF X_1114')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02579(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02579.json"))
    write_center_svg(
        model_acute,
        here / "x-02579.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
