"""GEOMETOR construction model for X(636) = COMPLEMENT OF X(62)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    midpoint,
    nine_point_center_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00636(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(636) = COMPLEMENT OF X(62) on reference triangle ABC."""
    X_62 = eval_trilinear_point(model, A, B, C, 'sin(A - pi /6)', ID="X(62)", classes=["center"])
    X_634 = point_from_barycentrics(model, A, B, C, 0.72998263, 0.40664462, -0.13662725, ID="X(634)", classes=["center"])
    X_636 = midpoint(model, X_62, X_634, ID="X(636)", classes=["selected", "target"], guide=False)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_17 = eval_trilinear_point(model, A, B, C, 'csc(A + pi /6)', ID="X(17)", classes=["center", "incident"])
    central_line(model, X_2, X_17, 2, 17, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center", "incident"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X(141)", classes=["center", "incident"])
    central_line(model, X_5, X_141, 5, 141, incident=True)
    X_18 = eval_trilinear_point(model, A, B, C, 'csc(A - pi /6)', ID="X(18)", classes=["center", "incident"])
    X_298 = eval_barycentric_point(model, A, B, C, 'csc(A)*sin(A + pi /3)', ID="X(298)", classes=["center", "incident"])
    central_line(model, X_18, X_298, 18, 298, incident=True)
    return promote_point_to_top(model, X_636)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(636) on the given reference triangle."""
    model = create_model('X(636) = COMPLEMENT OF X(62)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00636(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00636.json"))
    write_center_svg(
        model_acute,
        here / "x-00636.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
