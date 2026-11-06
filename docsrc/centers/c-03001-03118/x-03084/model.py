"""GEOMETOR construction model for X_3084 = INTERSECTION OF LINES X_1X_2 AND X_37X_493."""

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
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03084(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3084 = INTERSECTION OF LINES X_1X_2 AND X_37X_493 on reference triangle ABC."""
    X_3084 = eval_trilinear_point(model, A, B, C, '1 - csc(A)', ID="X_3084", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)
    X_175 = eval_trilinear_point(model, A, B, C, '-1 + sec(A/2)*cos(B/2)*cos(C/2)', ID="X_175", classes=["center", "incident"])
    X_329 = eval_trilinear_point(model, A, B, C, '( -1 - cos(A) + cos(B) + cos(C))*(csc(A))', ID="X_329", classes=["center", "incident"])
    central_line(model, X_175, X_329, 175, 329, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_493 = eval_trilinear_point(model, A, B, C, '1/(sin(A) + sin(B)*sin(C))', ID="X_493", classes=["center", "incident"])
    central_line(model, X_37, X_493, 37, 493, incident=True)
    return promote_point_to_top(model, X_3084)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3084 on the given reference triangle."""
    model = create_model('X_3084 = INTERSECTION OF LINES X_1X_2 AND X_37X_493')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03084(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03084.json"))
    write_center_svg(
        model_acute,
        here / "x-03084.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
