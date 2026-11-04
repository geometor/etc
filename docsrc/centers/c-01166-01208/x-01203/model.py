"""GEOMETOR construction model for X_1203 = 3rd SARAGOSSA POINT OF X_58."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01203(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1203 = 3rd SARAGOSSA POINT OF X_58 on reference triangle ABC."""
    X_1203 = eval_trilinear_point(model, A, B, C, '(a*((a + b + c)**(2) - b*c))', ID="X_1203", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center", "incident"])
    central_line(model, X_31, X_35, 31, 35, incident=True)
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    central_line(model, X_36, X_58, 36, 58, incident=True)
    return promote_point_to_top(model, X_1203)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1203 on the given reference triangle."""
    model = create_model('X_1203 = 3rd SARAGOSSA POINT OF X_58')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01203(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01203.json"))
    write_center_svg(
        model_acute,
        here / "x-01203.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
