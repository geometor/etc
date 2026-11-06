"""GEOMETOR construction model for X_3083 = INTERSECTION OF LINES X_1X_2 AND X_37X_494."""

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


def construct_x_03083(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3083 = INTERSECTION OF LINES X_1X_2 AND X_37X_494 on reference triangle ABC."""
    X_3083 = eval_trilinear_point(model, A, B, C, '1 + csc(A)', ID="X_3083", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)
    X_176 = eval_trilinear_point(model, A, B, C, '1 + sec(A/2)*cos(B/2)*cos(C/2)', ID="X_176", classes=["center", "incident"])
    X_329 = eval_trilinear_point(model, A, B, C, '( -1 - cos(A) + cos(B) + cos(C))*(csc(A))', ID="X_329", classes=["center", "incident"])
    central_line(model, X_176, X_329, 176, 329, incident=True)
    X_38 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2)', ID="X_38", classes=["center", "incident"])
    X_494 = eval_trilinear_point(model, A, B, C, '1/(sin(A) - sin(B)*sin(C))', ID="X_494", classes=["center", "incident"])
    central_line(model, X_38, X_494, 38, 494, incident=True)
    return promote_point_to_top(model, X_3083)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3083 on the given reference triangle."""
    model = create_model('X_3083 = INTERSECTION OF LINES X_1X_2 AND X_37X_494')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03083(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03083.json"))
    write_center_svg(
        model_acute,
        here / "x-03083.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
