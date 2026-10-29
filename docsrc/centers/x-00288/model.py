"""GEOMETOR construction model for X(288) = CEVAPOINT OF X(6) AND X(54)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00288(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(288) = CEVAPOINT OF X(6) AND X(54) on reference triangle ABC."""
    X_233 = eval_trilinear_point(model, A, B, C, '(b*cos(C - A) + c*cos(B - A))*cos(B - C)', ID="X(233)", classes=["center"])
    X_288 = isogonal_conjugate(model, A, B, C, X_233, ID="X(288)", classes=["selected", "target"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X(51)", classes=["center", "incident"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X(54)", classes=["center", "incident"])
    central_line(model, X_51, X_54, 51, 54, incident=True)
    X_97 = eval_trilinear_point(model, A, B, C, 'cot(A)*sec(B - C)', ID="X(97)", classes=["center", "incident"])
    X_216 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*cos(B - C)', ID="X(216)", classes=["center", "incident"])
    central_line(model, X_97, X_216, 97, 216, incident=True)
    X_53 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(B - C)', ID="X(53)", classes=["center", "incident"])
    X_275 = eval_trilinear_point(model, A, B, C, 'csc(2*A)*sec(B - C)', ID="X(275)", classes=["center", "incident"])
    central_line(model, X_53, X_275, 53, 275, incident=True)
    return promote_point_to_top(model, X_288)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(288) on the given reference triangle."""
    model = create_model('X(288) = CEVAPOINT OF X(6) AND X(54)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00288(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00288.json"))
    write_center_svg(
        model_acute,
        here / "x-00288.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
