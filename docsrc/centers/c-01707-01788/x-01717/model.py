"""GEOMETOR construction model for X_1717 = MIMOSA TRANSFORM OF X_35."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01717(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1717 = MIMOSA TRANSFORM OF X_35 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center"])
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center"])
    central_line(model, X_1, X_30, 1, 30)
    central_line(model, X_35, X_37, 35, 37)
    X_1717 = intersect_lines(model, X_1, X_30, X_35, X_37, ID="X_1717", classes=["selected", "target"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center", "incident"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center", "incident"])
    central_line(model, X_33, X_46, 33, 46, incident=True)
    return promote_point_to_top(model, X_1717)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1717 on the given reference triangle."""
    model = create_model('X_1717 = MIMOSA TRANSFORM OF X_35')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01717(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01717.json"))
    write_center_svg(
        model_acute,
        here / "x-01717.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
