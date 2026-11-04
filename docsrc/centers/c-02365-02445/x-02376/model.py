"""GEOMETOR construction model for X_2376 = CIR(X_219)."""

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


def construct_x_02376(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2376 = CIR(X_219) on reference triangle ABC."""
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center"])
    X_278 = eval_trilinear_point(model, A, B, C, 'sec(A)*tan(A/2)', ID="X_278", classes=["center"])
    central_line(model, X_34, X_101, 34, 101)
    central_line(model, X_100, X_278, 100, 278)
    X_2376 = intersect_lines(model, X_34, X_101, X_100, X_278, ID="X_2376", classes=["selected", "target"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    X_1396 = point_from_barycentrics(model, A, B, C, 0.049304081, 0.13493749, 0.81575843, ID="X_1396", classes=["center", "incident"])
    central_line(model, X_110, X_1396, 110, 1396, incident=True)
    return promote_point_to_top(model, X_2376)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2376 on the given reference triangle."""
    model = create_model('X_2376 = CIR(X_219)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02376(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02376.json"))
    write_center_svg(
        model_acute,
        here / "x-02376.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
