"""GEOMETOR construction model for X_1710 = MIMOSA TRANSFORM OF X_10."""

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


def construct_x_01710(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1710 = MIMOSA TRANSFORM OF X_10 on reference triangle ABC."""
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_91 = eval_trilinear_point(model, A, B, C, 'sec(2*A)', ID="X_91", classes=["center"])
    central_line(model, X_30, X_40, 30, 40)
    central_line(model, X_19, X_91, 19, 91)
    X_1710 = intersect_lines(model, X_30, X_40, X_19, X_91, ID="X_1710", classes=["selected", "target"])
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center", "incident"])
    X_228 = eval_trilinear_point(model, A, B, C, '(sin(2*A))*(sin(B) + sin(C))', ID="X_228", classes=["center", "incident"])
    central_line(model, X_35, X_228, 35, 228, incident=True)
    return promote_point_to_top(model, X_1710)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1710 on the given reference triangle."""
    model = create_model('X_1710 = MIMOSA TRANSFORM OF X_10')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01710(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01710.json"))
    write_center_svg(
        model_acute,
        here / "x-01710.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
