"""GEOMETOR construction model for X(582) = HARMONIC OF X(500)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00582(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(582) = HARMONIC OF X(500) on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    X_283 = eval_trilinear_point(model, A, B, C, '(cos(A))/(cos(B) + cos(C))', ID="X(283)", classes=["center"])
    X_474 = eval_trilinear_point(model, A, B, C, 'cos(A) - (a + b + c)/a', ID="X(474)", classes=["center"])
    central_line(model, X_3, X_6, 3, 6)
    central_line(model, X_283, X_474, 283, 474)
    X_582 = intersect_lines(model, X_3, X_6, X_283, X_474, ID="X(582)", classes=["selected", "target"])
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X(517)", classes=["center", "incident"])
    X_602 = point_from_barycentrics(model, A, B, C, -0.21701389, 0.18844697, 1.0285669, ID="X(602)", classes=["center", "incident"])
    central_line(model, X_517, X_602, 517, 602, incident=True)
    return promote_point_to_top(model, X_582)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(582) on the given reference triangle."""
    model = create_model('X(582) = HARMONIC OF X(500)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00582(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00582.json"))
    write_center_svg(
        model_acute,
        here / "x-00582.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
