"""GEOMETOR construction model for X_2576 = X_2-ISOCONJUGATE OF X_2574."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02576(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2576 = X_2-ISOCONJUGATE OF X_2574 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center"])
    X_1113 = eval_trilinear_point(model, A, B, C, '(R - d)*cos(A) - 2*R*cos(B)*cos(C)', ID="X_1113", classes=["center"])
    central_line(model, X_1, X_19, 1, 19)
    central_line(model, X_101, X_1113, 101, 1113)
    X_2576 = intersect_lines(model, X_1, X_19, X_101, X_1113, ID="X_2576", classes=["selected", "target"])
    X_163 = eval_trilinear_point(model, A, B, C, '(sin(2*A))/(sin(2*B) - sin(2*C))', ID="X_163", classes=["center", "incident"])
    X_1822 = point_from_barycentrics(model, A, B, C, -0.19858607, 0.24538924, 0.95319683, ID="X_1822", classes=["center", "incident"])
    central_line(model, X_163, X_1822, 163, 1822, incident=True)
    return promote_point_to_top(model, X_2576)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2576 on the given reference triangle."""
    model = create_model('X_2576 = X_2-ISOCONJUGATE OF X_2574')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02576(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02576.json"))
    write_center_svg(
        model_acute,
        here / "x-02576.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
