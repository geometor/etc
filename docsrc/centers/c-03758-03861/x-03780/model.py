"""GEOMETOR construction model for X_3780 = X_3721com[T(-bc, b²)]."""

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
    nagel_point_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03780(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3780 = X_3721com[T(-bc, b²)] on reference triangle ABC."""
    X_3780 = eval_barycentric_point(model, A, B, C, '(a*(a**(2)*b + a**(2)*c + 2*a*b*c - b**(2)*c - b*c**(2)))', ID="X_3780", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    central_line(model, X_6, X_8, 6, 8, incident=True)
    X_213 = eval_trilinear_point(model, A, B, C, '(b + c)*a**(2)', ID="X_213", classes=["center", "incident"])
    X_519 = eval_trilinear_point(model, A, B, C, '(2*a - b - c)/a', ID="X_519", classes=["center", "incident"])
    central_line(model, X_213, X_519, 213, 519, incident=True)
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    X_1107 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) + c**(2)) + b*c*(b + c))', ID="X_1107", classes=["center", "incident"])
    central_line(model, X_42, X_1107, 42, 1107, incident=True)
    return promote_point_to_top(model, X_3780)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3780 on the given reference triangle."""
    model = create_model('X_3780 = X_3721com[T(-bc, b²)]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03780(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03780.json"))
    write_center_svg(
        model_acute,
        here / "x-03780.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
