"""GEOMETOR construction model for X_1571 = INSIMILICENTER OF EXCENTRAL AND MOSES CIRCLES."""

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


def construct_x_01571(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1571 = INSIMILICENTER OF EXCENTRAL AND MOSES CIRCLES on reference triangle ABC."""
    X_1571 = eval_trilinear_point(model, A, B, C, 'a*(b*c*r + (a**(2) - 2*b**(2) - 2*c**(2))*R)', ID="X_1571", classes=["selected", "target"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    central_line(model, X_39, X_40, 39, 40, incident=True)
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    X_165 = eval_trilinear_point(model, A, B, C, 'tan(B/2) + tan(C/2) - tan(A/2)', ID="X_165", classes=["center", "incident"])
    central_line(model, X_32, X_165, 32, 165, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_574 = eval_trilinear_point(model, A, B, C, 'a*(a**(2) - 2*b**(2) - 2*c**(2))', ID="X_574", classes=["center", "incident"])
    central_line(model, X_1, X_574, 1, 574, incident=True)
    return promote_point_to_top(model, X_1571)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1571 on the given reference triangle."""
    model = create_model('X_1571 = INSIMILICENTER OF EXCENTRAL AND MOSES CIRCLES')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01571(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01571.json"))
    write_center_svg(
        model_acute,
        here / "x-01571.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
