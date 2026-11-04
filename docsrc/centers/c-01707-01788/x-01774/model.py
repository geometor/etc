"""GEOMETOR construction model for X_1774 = MIMOSA TRANSFORM OF X_1061."""

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
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01774(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1774 = MIMOSA TRANSFORM OF X_1061 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center"])
    X_47 = eval_trilinear_point(model, A, B, C, 'cos(2*A)', ID="X_47", classes=["center"])
    central_line(model, X_4, X_46, 4, 46)
    central_line(model, X_40, X_47, 40, 47)
    X_1774 = intersect_lines(model, X_4, X_46, X_40, X_47, ID="X_1774", classes=["selected", "target"])
    X_378 = eval_trilinear_point(model, A, B, C, 'sec(A) + 2*cos(A)', ID="X_378", classes=["center", "incident"])
    X_1061 = eval_trilinear_point(model, A, B, C, '(1/(2 + sec(B)*sec(C)))', ID="X_1061", classes=["center", "incident"])
    central_line(model, X_378, X_1061, 378, 1061, incident=True)
    return promote_point_to_top(model, X_1774)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1774 on the given reference triangle."""
    model = create_model('X_1774 = MIMOSA TRANSFORM OF X_1061')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01774(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01774.json"))
    write_center_svg(
        model_acute,
        here / "x-01774.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
