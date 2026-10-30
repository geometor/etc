"""GEOMETOR construction model for X(611) = INTERSECTION OF LINES X(1)X(6) AND X(55)X(511)."""

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


def construct_x_00611(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(611) = INTERSECTION OF LINES X(1)X(6) AND X(55)X(511) on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X(56)", classes=["center"])
    X_182 = eval_trilinear_point(model, A, B, C, 'cos(A- omega )', ID="X(182)", classes=["center"])
    central_line(model, X_1, X_6, 1, 6)
    central_line(model, X_56, X_182, 56, 182)
    X_611 = intersect_lines(model, X_1, X_6, X_56, X_182, ID="X(611)", classes=["selected", "target"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X(55)", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X(511)", classes=["center", "incident"])
    central_line(model, X_55, X_511, 55, 511, incident=True)
    return promote_point_to_top(model, X_611)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(611) on the given reference triangle."""
    model = create_model('X(611) = INTERSECTION OF LINES X(1)X(6) AND X(55)X(511)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00611(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00611.json"))
    write_center_svg(
        model_acute,
        here / "x-00611.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
