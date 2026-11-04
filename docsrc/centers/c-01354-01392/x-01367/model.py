"""GEOMETOR construction model for X_1367 = BRISSE TRANSFORM OF X_112."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01367(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1367 = BRISSE TRANSFORM OF X_112 on reference triangle ABC."""
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center"])
    X_1354 = point_from_barycentrics(model, A, B, C, 0.14777719, 0.075909331, 0.77631348, ID="X_1354", classes=["center"])
    X_222 = eval_trilinear_point(model, A, B, C, 'cos(A)*tan(A/2)', ID="X_222", classes=["center"])
    X_1366 = point_from_barycentrics(model, A, B, C, 0.30869383, 0.0013439731, 0.6899622, ID="X_1366", classes=["center"])
    central_line(model, X_7, X_1354, 7, 1354)
    central_line(model, X_222, X_1366, 222, 1366)
    X_1367 = intersect_lines(model, X_7, X_1354, X_222, X_1366, ID="X_1367", classes=["selected", "target"])
    return promote_point_to_top(model, X_1367)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1367 on the given reference triangle."""
    model = create_model('X_1367 = BRISSE TRANSFORM OF X_112')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01367(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01367.json"))
    write_center_svg(
        model_acute,
        here / "x-01367.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
