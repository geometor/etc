"""GEOMETOR construction model for X_3058 = INTERSECTION OF LINES X_1X_30 AND X_2X_11."""

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
    feuerbach_point_of,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03058(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3058 = INTERSECTION OF LINES X_1X_30 AND X_2X_11 on reference triangle ABC."""
    X_3058 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c - a)*(2*a**(2) + b**(2) + c**(2) - 2*b*c))', ID="X_3058", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    central_line(model, X_2, X_11, 2, 11, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    central_line(model, X_1, X_30, 1, 30, incident=True)
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    X_381 = eval_trilinear_point(model, A, B, C, '2*cos(B - C) - cos(A)', ID="X_381", classes=["center", "incident"])
    central_line(model, X_12, X_381, 12, 381, incident=True)
    return promote_point_to_top(model, X_3058)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3058 on the given reference triangle."""
    model = create_model('X_3058 = INTERSECTION OF LINES X_1X_30 AND X_2X_11')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03058(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03058.json"))
    write_center_svg(
        model_acute,
        here / "x-03058.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
