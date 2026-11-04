"""GEOMETOR construction model for X_2810 = ISOGONAL CONJUGATE OF X_2726."""

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


def construct_x_02810(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2810 = ISOGONAL CONJUGATE OF X_2726 on reference triangle ABC."""
    X_2726 = point_from_barycentrics(model, A, B, C, 0.66071654, -0.32143402, 0.66071748, ID="X_2726", classes=["center"])
    X_2810 = isogonal_conjugate(model, A, B, C, X_2726, ID="X_2810", classes=["selected", "target"])
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center", "incident"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    central_line(model, X_43, X_57, 43, 57, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    central_line(model, X_6, X_101, 6, 101, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    return promote_point_to_top(model, X_2810)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2810 on the given reference triangle."""
    model = create_model('X_2810 = ISOGONAL CONJUGATE OF X_2726')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02810(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02810.json"))
    write_center_svg(
        model_acute,
        here / "x-02810.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
