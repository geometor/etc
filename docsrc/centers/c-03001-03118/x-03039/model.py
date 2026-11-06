"""GEOMETOR construction model for X_3039 = COMPLEMENT OF X_1358."""

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
    midpoint,
    mittenpunkt_of,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03039(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3039 = COMPLEMENT OF X_1358 on reference triangle ABC."""
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center"])
    X_3021 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c - a)*(2*a**(2) - a*(b + c) + (b - c)**(2))**(2))', ID="X_3021", classes=["center"])
    X_3039 = midpoint(model, X_8, X_3021, ID="X_3039", classes=["selected", "target"], guide=False)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_80 = eval_trilinear_point(model, A, B, C, '1/(1 - 2*cos(A))', ID="X_80", classes=["center", "incident"])
    central_line(model, X_9, X_80, 9, 80, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_1358 = eval_trilinear_point(model, A, B, C, '(tan(A/2))**(2)*(sin(B/2 - C/2))**(2)', ID="X_1358", classes=["center", "incident"])
    central_line(model, X_2, X_1358, 2, 1358, incident=True)
    X_1292 = eval_trilinear_point(model, A, B, C, '1/((b - c)*(a**(2) + b**(2) + c**(2) - 2*a*b - 2*a*c))', ID="X_1292", classes=["center", "incident"])
    X_1376 = eval_trilinear_point(model, A, B, C, 'a**(2) - a*b - a*c + 2*b*c', ID="X_1376", classes=["center", "incident"])
    central_line(model, X_1292, X_1376, 1292, 1376, incident=True)
    return promote_point_to_top(model, X_3039)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3039 on the given reference triangle."""
    model = create_model('X_3039 = COMPLEMENT OF X_1358')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03039(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03039.json"))
    write_center_svg(
        model_acute,
        here / "x-03039.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
