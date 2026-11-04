"""GEOMETOR construction model for X_2007 = INSIMILICENTER(GALLATLY CIRCLE, INCIRCLE)."""

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


def construct_x_02007(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2007 = INSIMILICENTER(GALLATLY CIRCLE, INCIRCLE) on reference triangle ABC."""
    X_2007 = eval_trilinear_point(model, A, B, C, '(1 + sin(A +  omega  ))', ID="X_2007", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    central_line(model, X_1, X_39, 1, 39, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_1689 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  /2 +  pi  /4)', ID="X_1689", classes=["center", "incident"])
    central_line(model, X_55, X_1689, 55, 1689, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_1690 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  /2 -  pi  /4)', ID="X_1690", classes=["center", "incident"])
    central_line(model, X_56, X_1690, 56, 1690, incident=True)
    return promote_point_to_top(model, X_2007)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2007 on the given reference triangle."""
    model = create_model('X_2007 = INSIMILICENTER(GALLATLY CIRCLE, INCIRCLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02007(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02007.json"))
    write_center_svg(
        model_acute,
        here / "x-02007.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
