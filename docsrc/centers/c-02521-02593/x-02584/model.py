"""GEOMETOR construction model for X_2584 = X_4-ISOCONJUGATE OF X_1113."""

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


def construct_x_02584(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2584 = X_4-ISOCONJUGATE OF X_1113 on reference triangle ABC."""
    X_521 = eval_trilinear_point(model, A, B, C, '(sec(B) - sec(C))*(csc(A))', ID="X_521", classes=["center"])
    X_656 = eval_trilinear_point(model, A, B, C, 'tan(B) - tan(C)', ID="X_656", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_2582 = point_from_barycentrics(model, A, B, C, 5.5469882, -4.0939764, -0.45301178, ID="X_2582", classes=["center"])
    central_line(model, X_521, X_656, 521, 656)
    central_line(model, X_1, X_2582, 1, 2582)
    X_2584 = intersect_lines(model, X_521, X_656, X_1, X_2582, ID="X_2584", classes=["selected", "target"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    X_2578 = point_from_barycentrics(model, A, B, C, -4.4869799, 4.7687517, 0.71822818, ID="X_2578", classes=["center", "incident"])
    central_line(model, X_48, X_2578, 48, 2578, incident=True)
    return promote_point_to_top(model, X_2584)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2584 on the given reference triangle."""
    model = create_model('X_2584 = X_4-ISOCONJUGATE OF X_1113')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02584(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02584.json"))
    write_center_svg(
        model_acute,
        here / "x-02584.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
