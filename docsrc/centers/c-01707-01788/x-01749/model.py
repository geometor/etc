"""GEOMETOR construction model for X_1749 = MIMOSA TRANSFORM OF X_265."""

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
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01749(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1749 = MIMOSA TRANSFORM OF X_265 on reference triangle ABC."""
    X_1749 = eval_trilinear_point(model, A, B, C, 'a**(6) - 3*a**(4)*(b**(2) + c**(2)) + a**(2)*(3*b**(4) - b**(2)*c**(2) + 3*c**(4)) - (b**(2) - c**(2))**(2)*(b**(2) + c**(2))', ID="X_1749", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    central_line(model, X_1, X_21, 1, 21, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_79 = eval_trilinear_point(model, A, B, C, '1/(1 + 2*cos(A))', ID="X_79", classes=["center", "incident"])
    central_line(model, X_5, X_79, 5, 79, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_80 = eval_trilinear_point(model, A, B, C, '1/(1 - 2*cos(A))', ID="X_80", classes=["center", "incident"])
    central_line(model, X_30, X_80, 30, 80, incident=True)
    return promote_point_to_top(model, X_1749)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1749 on the given reference triangle."""
    model = create_model('X_1749 = MIMOSA TRANSFORM OF X_265')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01749(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01749.json"))
    write_center_svg(
        model_acute,
        here / "x-01749.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
