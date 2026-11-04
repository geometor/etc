"""GEOMETOR construction model for X_2140 = EIGENTRANSFORM OF X_101."""

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
    intersect_lines,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02140(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2140 = EIGENTRANSFORM OF X_101 on reference triangle ABC."""
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center"])
    X_116 = eval_trilinear_point(model, A, B, C, 'b*c*((b - c)**(2)*(b**(2) + b*c + c**(2) - a*b - a*c))', ID="X_116", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_142 = eval_trilinear_point(model, A, B, C, 'b + c - ((b - c)**(2))/a', ID="X_142", classes=["center"])
    central_line(model, X_5, X_116, 5, 116)
    central_line(model, X_3, X_142, 3, 142)
    X_2140 = intersect_lines(model, X_5, X_116, X_3, X_142, ID="X_2140", classes=["selected", "target"])
    X_218 = eval_trilinear_point(model, A, B, C, '((cos(A/2))**(2)*((cos(B/2))**(4) + (cos(C/2))**(4) - (cos(A/2))**(4)))', ID="X_218", classes=["center", "incident"])
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X_226", classes=["center", "incident"])
    central_line(model, X_218, X_226, 218, 226, incident=True)
    return promote_point_to_top(model, X_2140)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2140 on the given reference triangle."""
    model = create_model('X_2140 = EIGENTRANSFORM OF X_101')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02140(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02140.json"))
    write_center_svg(
        model_acute,
        here / "x-02140.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
