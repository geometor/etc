"""GEOMETOR construction model for X_1808 = INVERSE MIMOSA TRANSFORM OF X_511."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01808(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1808 = INVERSE MIMOSA TRANSFORM OF X_511 on reference triangle ABC."""
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center"])
    X_60 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(B - C))', ID="X_60", classes=["center"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center"])
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X_81", classes=["center"])
    central_line(model, X_41, X_60, 41, 60)
    central_line(model, X_42, X_81, 42, 81)
    X_1808 = intersect_lines(model, X_41, X_60, X_42, X_81, ID="X_1808", classes=["selected", "target"])
    X_228 = eval_trilinear_point(model, A, B, C, '(sin(2*A))*(sin(B) + sin(C))', ID="X_228", classes=["center", "incident"])
    X_295 = eval_trilinear_point(model, A, B, C, '(cos(A))/(a**(2) - b*c)', ID="X_295", classes=["center", "incident"])
    central_line(model, X_228, X_295, 228, 295, incident=True)
    return promote_point_to_top(model, X_1808)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1808 on the given reference triangle."""
    model = create_model('X_1808 = INVERSE MIMOSA TRANSFORM OF X_511')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01808(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01808.json"))
    write_center_svg(
        model_acute,
        here / "x-01808.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
