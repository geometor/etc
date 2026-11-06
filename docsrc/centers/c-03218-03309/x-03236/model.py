"""GEOMETOR construction model for X_3236 = INTERSECTION OF LINES X_1X_32 and X_3X_2008."""

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


def construct_x_03236(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3236 = INTERSECTION OF LINES X_1X_32 and X_3X_2008 on reference triangle ABC."""
    X_3236 = eval_trilinear_point(model, A, B, C, '(1 - sin(A -  omega  ))', ID="X_3236", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    central_line(model, X_1, X_32, 1, 32, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_1687 = eval_trilinear_point(model, A, B, C, 'sin(A -  omega  /2 +  pi  /4)', ID="X_1687", classes=["center", "incident"])
    central_line(model, X_55, X_1687, 55, 1687, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_1688 = eval_trilinear_point(model, A, B, C, 'cos(A -  omega  ) - sin(A)', ID="X_1688", classes=["center", "incident"])
    central_line(model, X_56, X_1688, 56, 1688, incident=True)
    return promote_point_to_top(model, X_3236)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3236 on the given reference triangle."""
    model = create_model('X_3236 = INTERSECTION OF LINES X_1X_32 and X_3X_2008')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03236(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03236.json"))
    write_center_svg(
        model_acute,
        here / "x-03236.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
