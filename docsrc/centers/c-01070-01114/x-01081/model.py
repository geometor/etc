"""GEOMETOR construction model for X_1081 = POINT ALPHECCA."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01081(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1081 = POINT ALPHECCA on reference triangle ABC."""
    X_1081 = eval_trilinear_point(model, A, B, C, 'sec(A/2)*csc(A/2 - pi /3)', ID="X_1081", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    central_line(model, X_1, X_30, 1, 30, incident=True)
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A + pi /3)', ID="X_13", classes=["center", "incident"])
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X_226", classes=["center", "incident"])
    central_line(model, X_13, X_226, 13, 226, incident=True)
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    X_298 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)*sin(A + pi /3)', ID="X_298", classes=["center", "incident"])
    central_line(model, X_75, X_298, 75, 298, incident=True)
    return promote_point_to_top(model, X_1081)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1081 on the given reference triangle."""
    model = create_model('X_1081 = POINT ALPHECCA')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01081(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01081.json"))
    write_center_svg(
        model_acute,
        here / "x-01081.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
