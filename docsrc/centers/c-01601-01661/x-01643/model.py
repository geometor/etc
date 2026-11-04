"""GEOMETOR construction model for X_1643 = TRIPOLAR CENTROID OF X_105."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01643(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1643 = TRIPOLAR CENTROID OF X_105 on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_650 = eval_trilinear_point(model, A, B, C, 'cos(B) - cos(C)', ID="X_650", classes=["center"])
    central_line(model, X_6, X_513, 6, 513)
    central_line(model, X_1, X_650, 1, 650)
    X_1643 = intersect_lines(model, X_6, X_513, X_1, X_650, ID="X_1643", classes=["selected", "target"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    X_663 = eval_trilinear_point(model, A, B, C, 'a*(b - c)*(b + c - a)', ID="X_663", classes=["center", "incident"])
    central_line(model, X_42, X_663, 42, 663, incident=True)
    return promote_point_to_top(model, X_1643)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1643 on the given reference triangle."""
    model = create_model('X_1643 = TRIPOLAR CENTROID OF X_105')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01643(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01643.json"))
    write_center_svg(
        model_acute,
        here / "x-01643.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
