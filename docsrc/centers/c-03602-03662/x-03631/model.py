"""GEOMETOR construction model for X_3631 = H⁻¹(X_6; M, -2)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    midpoint,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03631(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3631 = H⁻¹(X_6; M, -2) on reference triangle ABC."""
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X_141", classes=["center"])
    X_3631 = midpoint(model, X_69, X_141, ID="X_3631", classes=["selected", "target"], guide=False)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_320 = eval_trilinear_point(model, A, B, C, '(1 - 2*cos(A))/a**(2)', ID="X_320", classes=["center", "incident"])
    X_594 = eval_trilinear_point(model, A, B, C, '(b + c)**(2)/a', ID="X_594", classes=["center", "incident"])
    central_line(model, X_320, X_594, 320, 594, incident=True)
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    X_546 = eval_trilinear_point(model, A, B, C, '3*cos(B - C) - 2*cos(A)', ID="X_546", classes=["center", "incident"])
    central_line(model, X_511, X_546, 511, 546, incident=True)
    return promote_point_to_top(model, X_3631)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3631 on the given reference triangle."""
    model = create_model('X_3631 = H⁻¹(X_6; M, -2)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03631(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03631.json"))
    write_center_svg(
        model_acute,
        here / "x-03631.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
