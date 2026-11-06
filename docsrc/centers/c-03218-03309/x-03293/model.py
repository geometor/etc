"""GEOMETOR construction model for X_3293 = SS(a → b + c) OF X_3."""

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
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_03293(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3293 = SS(a → b + c) OF X_3 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_1193 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) + c**(2) + a*b + a*c))', ID="X_1193", classes=["center"])
    X_3293 = reflection_in_point(model, X_1, X_1193, ID="X_3293", classes=["selected", "target"], guide=False)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    central_line(model, X_58, X_100, 58, 100, incident=True)
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    X_209 = eval_trilinear_point(model, A, B, C, '((sin(B) + sin(C))*(sin(A) + sin(A - B) + sin(A - C)))', ID="X_209", classes=["center", "incident"])
    central_line(model, X_40, X_209, 40, 209, incident=True)
    return promote_point_to_top(model, X_3293)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3293 on the given reference triangle."""
    model = create_model('X_3293 = SS(a → b + c) OF X_3')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03293(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03293.json"))
    write_center_svg(
        model_acute,
        here / "x-03293.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
