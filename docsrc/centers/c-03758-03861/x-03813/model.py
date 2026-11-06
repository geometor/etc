"""GEOMETOR construction model for X_3813 = X_2136com(4th EULER TRIANGLE)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    feuerbach_point_of,
    incenter_of,
    nagel_point_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03813(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3813 = X_2136com(4th EULER TRIANGLE) on reference triangle ABC."""
    X_3813 = eval_barycentric_point(model, A, B, C, '((b**(2)-4*b*c+c**(2))*a-b**(2)*c-b*c**(2)+c**(3)+b**(3)) * (-a+b+c)', ID="X_3813", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    central_line(model, X_8, X_11, 8, 11, incident=True)
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    X_145 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a - b - c)', ID="X_145", classes=["center", "incident"])
    central_line(model, X_12, X_145, 12, 145, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_442 = point_from_barycentrics(model, A, B, C, 0.3215734, 0.32603406, 0.35239254, ID="X_442", classes=["center", "incident"])
    central_line(model, X_1, X_442, 1, 442, incident=True)
    return promote_point_to_top(model, X_3813)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3813 on the given reference triangle."""
    model = create_model('X_3813 = X_2136com(4th EULER TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03813(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03813.json"))
    write_center_svg(
        model_acute,
        here / "x-03813.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
