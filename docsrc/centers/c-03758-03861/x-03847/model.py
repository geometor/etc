"""GEOMETOR construction model for X_3847 = X_1420com(3rd EULER TRIANGLE)."""

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
    nagel_point_of,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03847(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3847 = X_1420com(3rd EULER TRIANGLE) on reference triangle ABC."""
    X_3847 = eval_barycentric_point(model, A, B, C, '(b + c - a)*(3*b**(3) + 3*c**(3) + 3*a*b**(2) + 3*a*c**(2) - 3*b**(2)*c - 3*b*c**(2) - 4*a*b*c)', ID="X_3847", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    central_line(model, X_8, X_11, 8, 11, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_515 = eval_trilinear_point(model, A, B, C, '(b + c)*sec(A) - b*sec(B) - c*sec(C)', ID="X_515", classes=["center", "incident"])
    central_line(model, X_5, X_515, 5, 515, incident=True)
    X_1698 = eval_trilinear_point(model, A, B, C, '2*cos(B - C) + cos(A) - cos(B) - cos(C) + 1', ID="X_1698", classes=["center", "incident"])
    X_1706 = eval_trilinear_point(model, A, B, C, '(b*c*(2*(b + c) - a*(cos(A) - cos(B) - cos(C) + 1)))', ID="X_1706", classes=["center", "incident"])
    central_line(model, X_1698, X_1706, 1698, 1706, incident=True)
    return promote_point_to_top(model, X_3847)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3847 on the given reference triangle."""
    model = create_model('X_3847 = X_1420com(3rd EULER TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03847(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03847.json"))
    write_center_svg(
        model_acute,
        here / "x-03847.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
