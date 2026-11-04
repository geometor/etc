"""GEOMETOR construction model for X_1920 = CROSSSUM OF PU(12)."""

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
    isotomic_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01920(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1920 = CROSSSUM OF PU(12) on reference triangle ABC."""
    X_893 = eval_trilinear_point(model, A, B, C, 'a/(a**(2) + b*c)', ID="X_893", classes=["center"])
    X_1920 = isotomic_conjugate(model, A, B, C, X_893, ID="X_1920", classes=["selected", "target"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X_85", classes=["center", "incident"])
    central_line(model, X_76, X_85, 76, 85, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_561 = eval_trilinear_point(model, A, B, C, 'a **(- 4)', ID="X_561", classes=["center", "incident"])
    central_line(model, X_2, X_561, 2, 561, incident=True)
    X_310 = eval_trilinear_point(model, A, B, C, 'b**(3)*c**(3)/(b + c)', ID="X_310", classes=["center", "incident"])
    X_321 = eval_trilinear_point(model, A, B, C, '(b + c)*b**(2)*c**(2)', ID="X_321", classes=["center", "incident"])
    central_line(model, X_310, X_321, 310, 321, incident=True)
    return promote_point_to_top(model, X_1920)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1920 on the given reference triangle."""
    model = create_model('X_1920 = CROSSSUM OF PU(12)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01920(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01920.json"))
    write_center_svg(
        model_acute,
        here / "x-01920.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
