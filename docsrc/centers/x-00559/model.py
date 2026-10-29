"""GEOMETOR construction model for X(559) = (X(1),X(15))-ANSWER TO QUESTION A."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00559(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(559) = (X(1),X(15))-ANSWER TO QUESTION A on reference triangle ABC."""
    X_559 = eval_trilinear_point(model, A, B, C, '(sec(A/2))*sin(A/2 + pi /3)', ID="X(559)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    central_line(model, X_1, X_3, 1, 3, incident=True)
    X_14 = eval_trilinear_point(model, A, B, C, 'csc(A - pi /3)', ID="X(14)", classes=["center", "incident"])
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X(226)", classes=["center", "incident"])
    central_line(model, X_14, X_226, 14, 226, incident=True)
    X_299 = eval_barycentric_point(model, A, B, C, 'csc(A)*sin(A - pi /3)', ID="X(299)", classes=["center", "incident"])
    X_319 = eval_trilinear_point(model, A, B, C, '(1 + 2*cos(A))/a**(2)', ID="X(319)", classes=["center", "incident"])
    central_line(model, X_299, X_319, 299, 319, incident=True)
    return promote_point_to_top(model, X_559)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(559) on the given reference triangle."""
    model = create_model('X(559) = (X(1),X(15))-ANSWER TO QUESTION A')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00559(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00559.json"))
    write_center_svg(
        model_acute,
        here / "x-00559.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
