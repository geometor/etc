"""GEOMETOR construction model for X_3476 = INTERSECTION OF LINES X_1X_4 AND X_8X_56."""

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
    incenter_of,
    nagel_point_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03476(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3476 = INTERSECTION OF LINES X_1X_4 AND X_8X_56 on reference triangle ABC."""
    X_3476 = eval_trilinear_point(model, A, B, C, '(2 - cos(A) - cos(B) - cos(C) + cos(B)*cos(C))', ID="X_3476", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    central_line(model, X_1, X_4, 1, 4, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    central_line(model, X_8, X_56, 8, 56, incident=True)
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_528 = point_from_barycentrics(model, A, B, C, -0.26726124, 0.80178373, -0.53452248, ID="X_528", classes=["center", "incident"])
    central_line(model, X_7, X_528, 7, 528, incident=True)
    return promote_point_to_top(model, X_3476)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3476 on the given reference triangle."""
    model = create_model('X_3476 = INTERSECTION OF LINES X_1X_4 AND X_8X_56')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03476(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03476.json"))
    write_center_svg(
        model_acute,
        here / "x-03476.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
