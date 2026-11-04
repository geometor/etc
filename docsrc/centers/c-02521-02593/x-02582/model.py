"""GEOMETOR construction model for X_2582 = X_6-ISOCONJUGATE OF X_1113."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02582(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2582 = X_6-ISOCONJUGATE OF X_1113 on reference triangle ABC."""
    X_2576 = point_from_barycentrics(model, A, B, C, -0.040079089, 0.078197387, 0.9618817, ID="X_2576", classes=["center"])
    X_2582 = isogonal_conjugate(model, A, B, C, X_2576, ID="X_2582", classes=["selected", "target"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center", "incident"])
    X_661 = eval_trilinear_point(model, A, B, C, 'cot(B) - cot(C)', ID="X_661", classes=["center", "incident"])
    central_line(model, X_514, X_661, 514, 661, incident=True)
    X_293 = eval_trilinear_point(model, A, B, C, 'cos(A)*sec(A +  omega  )', ID="X_293", classes=["center", "incident"])
    X_1823 = point_from_barycentrics(model, A, B, C, 0.72123578, 0.4152025, -0.13643829, ID="X_1823", classes=["center", "incident"])
    central_line(model, X_293, X_1823, 293, 1823, incident=True)
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    X_2578 = point_from_barycentrics(model, A, B, C, -4.4869799, 4.7687517, 0.71822818, ID="X_2578", classes=["center", "incident"])
    central_line(model, X_63, X_2578, 63, 2578, incident=True)
    return promote_point_to_top(model, X_2582)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2582 on the given reference triangle."""
    model = create_model('X_2582 = X_6-ISOCONJUGATE OF X_1113')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02582(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02582.json"))
    write_center_svg(
        model_acute,
        here / "x-02582.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
