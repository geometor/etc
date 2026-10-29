"""GEOMETOR construction model for X(145) = ANTICOMPLEMENT OF NAGEL POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    anticomplement,
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00145(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(145) = ANTICOMPLEMENT OF NAGEL POINT on reference triangle ABC."""
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center"])
    X_145 = anticomplement(model, A, B, C, X_8, ID="X(145)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)
    central_line(model, X_8, X_1, 8, 1, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X(56)", classes=["center", "incident"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X(100)", classes=["center", "incident"])
    central_line(model, X_56, X_100, 56, 100, incident=True)
    return promote_point_to_top(model, X_145)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(145) on the given reference triangle."""
    model = create_model('X(145) = ANTICOMPLEMENT OF NAGEL POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00145(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00145.json"))
    write_center_svg(
        model_acute,
        here / "x-00145.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
