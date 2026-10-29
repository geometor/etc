"""GEOMETOR construction model for X(663) = CROSSDIFFERENCE OF X(2) AND X(7)."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00663(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(663) = CROSSDIFFERENCE OF X(2) AND X(7) on reference triangle ABC."""
    X_663 = eval_trilinear_point(model, A, B, C, 'a*(b - c)*(b + c - a)', ID="X(663)", classes=["selected", "target"])
    X_187 = eval_trilinear_point(model, A, B, C, 'a*(2*a**(2) - b**(2) - c**(2))', ID="X(187)", classes=["center", "incident"])
    X_237 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A + omega )', ID="X(237)", classes=["center", "incident"])
    central_line(model, X_187, X_237, 187, 237, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X(514)", classes=["center", "incident"])
    central_line(model, X_1, X_514, 1, 514, incident=True)
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X(41)", classes=["center", "incident"])
    X_884 = point_from_barycentrics(model, A, B, C, -0.045819015, 0.98969072, 0.056128293, ID="X(884)", classes=["center", "incident"])
    central_line(model, X_41, X_884, 41, 884, incident=True)
    return promote_point_to_top(model, X_663)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(663) on the given reference triangle."""
    model = create_model('X(663) = CROSSDIFFERENCE OF X(2) AND X(7)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00663(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00663.json"))
    write_center_svg(
        model_acute,
        here / "x-00663.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
