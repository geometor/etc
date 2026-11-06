"""GEOMETOR construction model for X_1374 = 2nd GRIFFITHS POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01374(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1374 = 2nd GRIFFITHS POINT on reference triangle ABC."""
    X_1374 = eval_trilinear_point(model, A, B, C, '1 - 8*( area )/(a*(b + c - a))', ID="X_1374", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_1, X_7, 1, 7, incident=True)
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X_226", classes=["center", "incident"])
    X_3316 = eval_trilinear_point(model, A, B, C, '1/(cos(A) + 2*sin(A))', ID="X_3316", classes=["center", "incident"])
    central_line(model, X_226, X_3316, 226, 3316, incident=True)
    return promote_point_to_top(model, X_1374)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1374 on the given reference triangle."""
    model = create_model('X_1374 = 2nd GRIFFITHS POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01374(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01374.json"))
    write_center_svg(
        model_acute,
        here / "x-01374.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
