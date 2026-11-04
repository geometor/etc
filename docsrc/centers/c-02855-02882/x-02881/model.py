"""GEOMETOR construction model for X_2881 = ISOGONAL CONJUGATE OF X_2867."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02881(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2881 = ISOGONAL CONJUGATE OF X_2867 on reference triangle ABC."""
    X_2867 = point_from_barycentrics(model, A, B, C, 0.027913757, -0.038130739, 1.010217, ID="X_2867", classes=["center"])
    X_2881 = isogonal_conjugate(model, A, B, C, X_2867, ID="X_2881", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center", "incident"])
    X_1576 = eval_trilinear_point(model, A, B, C, 'a**(3)/(b**(2) - c**(2))', ID="X_1576", classes=["center", "incident"])
    central_line(model, X_112, X_1576, 112, 1576, incident=True)
    X_154 = eval_trilinear_point(model, A, B, C, '(cos(A) - cos(B)*cos(C))*a**(2)', ID="X_154", classes=["center", "incident"])
    X_1636 = eval_trilinear_point(model, A, B, C, '(cos(A))*(tan(B) - tan(C))*(tan(B) + tan(C) - 2*tan(A))', ID="X_1636", classes=["center", "incident"])
    central_line(model, X_154, X_1636, 154, 1636, incident=True)
    return promote_point_to_top(model, X_2881)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2881 on the given reference triangle."""
    model = create_model('X_2881 = ISOGONAL CONJUGATE OF X_2867')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02881(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02881.json"))
    write_center_svg(
        model_acute,
        here / "x-02881.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
