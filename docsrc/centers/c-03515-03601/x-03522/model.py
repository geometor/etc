"""GEOMETOR construction model for X_3522 = EULER LINE INTERCEPT OF LINE X_8X_165."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    midpoint,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03522(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3522 = EULER LINE INTERCEPT OF LINE X_8X_165 on reference triangle ABC."""
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center"])
    X_3091 = eval_trilinear_point(model, A, B, C, 'cos(B)*cos(C) + cos(B - C)', ID="X_3091", classes=["center"])
    X_3522 = midpoint(model, X_20, X_3091, ID="X_3522", classes=["selected", "target"], guide=False)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_165 = eval_trilinear_point(model, A, B, C, 'tan(B/2) + tan(C/2) - tan(A/2)', ID="X_165", classes=["center", "incident"])
    central_line(model, X_8, X_165, 8, 165, incident=True)
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    X_145 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a - b - c)', ID="X_145", classes=["center", "incident"])
    central_line(model, X_40, X_145, 40, 145, incident=True)
    return promote_point_to_top(model, X_3522)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3522 on the given reference triangle."""
    model = create_model('X_3522 = EULER LINE INTERCEPT OF LINE X_8X_165')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03522(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03522.json"))
    write_center_svg(
        model_acute,
        here / "x-03522.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
