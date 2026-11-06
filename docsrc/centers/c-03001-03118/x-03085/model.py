"""GEOMETOR construction model for X_3085 = INTERSECTION OF LINES X_1X_2 AND X_4X_12."""

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
    gergonne_point_of,
    incenter_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03085(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3085 = INTERSECTION OF LINES X_1X_2 AND X_4X_12 on reference triangle ABC."""
    X_3085 = eval_trilinear_point(model, A, B, C, '(1 + sin(B)*sin(C))', ID="X_3085", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    central_line(model, X_4, X_12, 4, 12, incident=True)
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center", "incident"])
    central_line(model, X_7, X_46, 7, 46, incident=True)
    return promote_point_to_top(model, X_3085)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3085 on the given reference triangle."""
    model = create_model('X_3085 = INTERSECTION OF LINES X_1X_2 AND X_4X_12')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03085(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03085.json"))
    write_center_svg(
        model_acute,
        here / "x-03085.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
