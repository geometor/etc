"""GEOMETOR construction model for X_3338 = INTERSECTION OF LINES X_1X_3 AND X_7X_90."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    incenter_of,
    mittenpunkt_of,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_03338(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3338 = INTERSECTION OF LINES X_1X_3 AND X_7X_90 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_3304 = eval_trilinear_point(model, A, B, C, '3 - cos(A)', ID="X_3304", classes=["center"])
    X_3338 = reflection_in_point(model, X_1, X_3304, ID="X_3338", classes=["selected", "target"], guide=False)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    central_line(model, X_1, X_3, 1, 3, incident=True)
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_90 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C) - cos(A))', ID="X_90", classes=["center", "incident"])
    central_line(model, X_7, X_90, 7, 90, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_583 = eval_trilinear_point(model, A, B, C, '(a*(a**(2)*b + a**(2)*c + 2*a*b*c - b**(3) - c**(3)))', ID="X_583", classes=["center", "incident"])
    central_line(model, X_9, X_583, 9, 583, incident=True)
    return promote_point_to_top(model, X_3338)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3338 on the given reference triangle."""
    model = create_model('X_3338 = INTERSECTION OF LINES X_1X_3 AND X_7X_90')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03338(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03338.json"))
    write_center_svg(
        model_acute,
        here / "x-03338.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
