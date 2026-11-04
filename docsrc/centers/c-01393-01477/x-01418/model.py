"""GEOMETOR construction model for X_1418 = X_142-BETH CONJUGATE OF X_142."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    intersect_lines,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01418(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1418 = X_142-BETH CONJUGATE OF X_142 on reference triangle ABC."""
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    central_line(model, X_7, X_37, 7, 37)
    central_line(model, X_6, X_57, 6, 57)
    X_1418 = intersect_lines(model, X_7, X_37, X_6, X_57, ID="X_1418", classes=["selected", "target"])
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X_77", classes=["center", "incident"])
    X_1100 = eval_trilinear_point(model, A, B, C, '2*a + b + c', ID="X_1100", classes=["center", "incident"])
    central_line(model, X_77, X_1100, 77, 1100, incident=True)
    return promote_point_to_top(model, X_1418)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1418 on the given reference triangle."""
    model = create_model('X_1418 = X_142-BETH CONJUGATE OF X_142')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01418(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01418.json"))
    write_center_svg(
        model_acute,
        here / "x-01418.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
