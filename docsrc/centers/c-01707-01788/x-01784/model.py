"""GEOMETOR construction model for X_1784 = MIMOSA TRANSFORM OF X_1294."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    intersect_lines,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01784(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1784 = MIMOSA TRANSFORM OF X_1294 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X_29", classes=["center"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_79 = eval_trilinear_point(model, A, B, C, '1/(1 + 2*cos(A))', ID="X_79", classes=["center"])
    central_line(model, X_1, X_29, 1, 29)
    central_line(model, X_4, X_79, 4, 79)
    X_1784 = intersect_lines(model, X_1, X_29, X_4, X_79, ID="X_1784", classes=["selected", "target"])
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_243 = eval_trilinear_point(model, A, B, C, '(sec(A))*((cos(A))**(2) - cos(B)*cos(C))', ID="X_243", classes=["center", "incident"])
    central_line(model, X_36, X_243, 36, 243, incident=True)
    return promote_point_to_top(model, X_1784)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1784 on the given reference triangle."""
    model = create_model('X_1784 = MIMOSA TRANSFORM OF X_1294')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01784(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01784.json"))
    write_center_svg(
        model_acute,
        here / "x-01784.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
