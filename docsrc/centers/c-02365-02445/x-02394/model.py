"""GEOMETOR construction model for X_2394 = GIBERT-SIMSON TRANSFORM OF X_74."""

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
    intersect_lines,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02394(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2394 = GIBERT-SIMSON TRANSFORM OF X_74 on reference triangle ABC."""
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_525 = eval_trilinear_point(model, A, B, C, '(b*cos(B) - c*cos(C))/a', ID="X_525", classes=["center"])
    central_line(model, X_74, X_98, 74, 98)
    central_line(model, X_2, X_525, 2, 525)
    X_2394 = intersect_lines(model, X_74, X_98, X_2, X_525, ID="X_2394", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center", "incident"])
    central_line(model, X_4, X_523, 4, 523, incident=True)
    return promote_point_to_top(model, X_2394)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2394 on the given reference triangle."""
    model = create_model('X_2394 = GIBERT-SIMSON TRANSFORM OF X_74')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02394(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02394.json"))
    write_center_svg(
        model_acute,
        here / "x-02394.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
