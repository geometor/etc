"""GEOMETOR construction model for X(477) = TIXIER ANTIPODE."""

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
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_00477(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(477) = TIXIER ANTIPODE on reference triangle ABC."""
    X_476 = eval_trilinear_point(model, A, B, C, '1/((1 + 2*cos(2*A))*sin(B - C))', ID="X(476)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_477 = reflection_in_point(model, X_476, X_3, ID="X(477)", classes=["selected", "target"], guide=False)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    central_line(model, X_30, X_110, 30, 110, incident=True)
    X_50 = eval_trilinear_point(model, A, B, C, 'sin(3*A)', ID="X(50)", classes=["center", "incident"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X(112)", classes=["center", "incident"])
    central_line(model, X_50, X_112, 50, 112, incident=True)
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X(107)", classes=["center", "incident"])
    X_186 = eval_trilinear_point(model, A, B, C, '4*cos(A) - sec(A)', ID="X(186)", classes=["center", "incident"])
    central_line(model, X_107, X_186, 107, 186, incident=True)
    return promote_point_to_top(model, X_477)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(477) on the given reference triangle."""
    model = create_model('X(477) = TIXIER ANTIPODE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00477(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00477.json"))
    write_center_svg(
        model_acute,
        here / "x-00477.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
