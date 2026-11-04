"""GEOMETOR construction model for X_2437 = ISOGONAL CONJUGATE OF X_2411."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02437(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2437 = ISOGONAL CONJUGATE OF X_2411 on reference triangle ABC."""
    X_2411 = point_from_barycentrics(model, A, B, C, 0.98172677, -0.017599034, 0.035872262, ID="X_2411", classes=["center"])
    X_2437 = isogonal_conjugate(model, A, B, C, X_2411, ID="X_2437", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A +  pi  /3)', ID="X_13", classes=["center", "incident"])
    central_line(model, X_6, X_13, 6, 13, incident=True)
    X_2420 = point_from_barycentrics(model, A, B, C, -0.30880929, 0.14950629, 1.159303, ID="X_2420", classes=["center", "incident"])
    X_2433 = eval_trilinear_point(model, A, B, C, '(sin(B - C)*sin(A))**(2)/(csc(C - A)*cos(C) - csc(A - B)*cos(B))', ID="X_2433", classes=["center", "incident"])
    central_line(model, X_2420, X_2433, 2420, 2433, incident=True)
    return promote_point_to_top(model, X_2437)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2437 on the given reference triangle."""
    model = create_model('X_2437 = ISOGONAL CONJUGATE OF X_2411')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02437(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02437.json"))
    write_center_svg(
        model_acute,
        here / "x-02437.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
