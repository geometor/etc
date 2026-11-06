"""GEOMETOR construction model for X_3464 = X_30-CEVA CONJUGATE OF X_1."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03464(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3464 = X_30-CEVA CONJUGATE OF X_1 on reference triangle ABC."""
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_3464 = ceva_conjugate(model, A, B, C, X_30, X_1, ID="X_3464", classes=["selected", "target"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center", "incident"])
    central_line(model, X_1, X_74, 1, 74, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_1354 = point_from_barycentrics(model, A, B, C, 0.14777719, 0.075909331, 0.77631348, ID="X_1354", classes=["center", "incident"])
    central_line(model, X_57, X_1354, 57, 1354, incident=True)
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A +  pi  /3)', ID="X_13", classes=["center", "incident"])
    X_1652 = eval_trilinear_point(model, A, B, C, '(sqrt(3/4) - sin(A +  pi  /3) + sin(B +  pi  /3) + sin(C +  pi  /3))', ID="X_1652", classes=["center", "incident"])
    central_line(model, X_13, X_1652, 13, 1652, incident=True)
    return promote_point_to_top(model, X_3464)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3464 on the given reference triangle."""
    model = create_model('X_3464 = X_30-CEVA CONJUGATE OF X_1')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03464(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03464.json"))
    write_center_svg(
        model_acute,
        here / "x-03464.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
