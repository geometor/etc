"""GEOMETOR construction model for X(147) = TARRY POINT OF ANTICOMPLEMENTARY TRIANGLE."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00147(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(147) = TARRY POINT OF ANTICOMPLEMENTARY TRIANGLE on reference triangle ABC."""
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A + omega )', ID="X(98)", classes=["center"])
    X_147 = anticomplement(model, A, B, C, X_98, ID="X(147)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    central_line(model, X_2, X_98, 2, 98, incident=True)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X(20)", classes=["center", "incident"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    central_line(model, X_20, X_99, 20, 99, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_150 = point_from_barycentrics(model, A, B, C, 0.10714286, 1.6428571, -0.75, ID="X(150)", classes=["center", "incident"])
    central_line(model, X_1, X_150, 1, 150, incident=True)
    return promote_point_to_top(model, X_147)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(147) on the given reference triangle."""
    model = create_model('X(147) = TARRY POINT OF ANTICOMPLEMENTARY TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00147(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00147.json"))
    write_center_svg(
        model_acute,
        here / "x-00147.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
