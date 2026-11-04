"""GEOMETOR construction model for X_1674 = INSIMILICENTER(INCIRCLE, BROCARD CIRCLE)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01674(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1674 = INSIMILICENTER(INCIRCLE, BROCARD CIRCLE) on reference triangle ABC."""
    X_1674 = eval_trilinear_point(model, A, B, C, 'e + cos(A -  omega  )', ID="X_1674", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_182 = eval_trilinear_point(model, A, B, C, 'cos(A-  omega  )', ID="X_182", classes=["center", "incident"])
    central_line(model, X_1, X_182, 1, 182, incident=True)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_1348 = eval_trilinear_point(model, A, B, C, 'e*cos(B - C) + cos(A -  omega  )', ID="X_1348", classes=["center", "incident"])
    central_line(model, X_11, X_1348, 11, 1348, incident=True)
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    X_1349 = eval_trilinear_point(model, A, B, C, 'e*cos(B - C) - cos(A -  omega  )', ID="X_1349", classes=["center", "incident"])
    central_line(model, X_12, X_1349, 12, 1349, incident=True)
    return promote_point_to_top(model, X_1674)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1674 on the given reference triangle."""
    model = create_model('X_1674 = INSIMILICENTER(INCIRCLE, BROCARD CIRCLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01674(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01674.json"))
    write_center_svg(
        model_acute,
        here / "x-01674.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
