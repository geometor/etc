"""GEOMETOR construction model for X_1291 = COLLINGS TRANSFORM OF X_50."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    cevapoint,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01291(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1291 = COLLINGS TRANSFORM OF X_50 on reference triangle ABC."""
    X_50 = eval_trilinear_point(model, A, B, C, 'sin(3*A)', ID="X_50", classes=["center"])
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center"])
    X_1291 = cevapoint(model, A, B, C, X_50, X_512, ID="X_1291", classes=["selected", "target"])
    X_477 = eval_trilinear_point(model, A, B, C, '1/(4*cos(A) + cos(A - 2*B) + cos(A - 2*C) - 3*cos(B - C))', ID="X_477", classes=["center", "incident"])
    X_550 = eval_trilinear_point(model, A, B, C, '- cos(B - C) + 4*cos(A)', ID="X_550", classes=["center", "incident"])
    central_line(model, X_477, X_550, 477, 550, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_1141 = eval_trilinear_point(model, A, B, C, 'b*c/(16*D**(2) + (a**(2)+c**(2)-b**(2))*(a**(2)+b**(2)-c**(2)))*(16*D**(2) - 3*(b**(2)+c**(2)-a**(2))**(2))', ID="X_1141", classes=["center", "incident"])
    central_line(model, X_30, X_1141, 30, 1141, incident=True)
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center", "incident"])
    X_1154 = eval_trilinear_point(model, A, B, C, '(1 - 4*(cos(A))**(2))*cos(B - C)', ID="X_1154", classes=["center", "incident"])
    central_line(model, X_74, X_1154, 74, 1154, incident=True)
    return promote_point_to_top(model, X_1291)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1291 on the given reference triangle."""
    model = create_model('X_1291 = COLLINGS TRANSFORM OF X_50')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01291(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01291.json"))
    write_center_svg(
        model_acute,
        here / "x-01291.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
