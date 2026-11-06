"""GEOMETOR construction model for X_3057 = INTERSECTION OF LINES X_1X_3 AND X_10X_11."""

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
    feuerbach_point_of,
    incenter_of,
    isogonal_conjugate,
    nagel_point_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03057(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3057 = INTERSECTION OF LINES X_1X_3 AND X_10X_11 on reference triangle ABC."""
    X_1476 = eval_trilinear_point(model, A, B, C, '1/(a**(2)*((sin(B/2))**(2) + (sin(C/2))**(2)))', ID="X_1476", classes=["center"])
    X_3057 = isogonal_conjugate(model, A, B, C, X_1476, ID="X_3057", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    central_line(model, X_1, X_3, 1, 3, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    central_line(model, X_10, X_11, 10, 11, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_210 = eval_trilinear_point(model, A, B, C, '(b + c)*(b + c - a)', ID="X_210", classes=["center", "incident"])
    central_line(model, X_8, X_210, 8, 210, incident=True)
    return promote_point_to_top(model, X_3057)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3057 on the given reference triangle."""
    model = create_model('X_3057 = INTERSECTION OF LINES X_1X_3 AND X_10X_11')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03057(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03057.json"))
    write_center_svg(
        model_acute,
        here / "x-03057.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
