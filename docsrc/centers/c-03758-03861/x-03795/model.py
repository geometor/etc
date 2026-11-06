"""GEOMETOR construction model for X_3795 = X_3097com[INVERSE(nT(bc, b²))]."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03795(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3795 = X_3097com[INVERSE(nT(bc, b²))] on reference triangle ABC."""
    X_3795 = eval_barycentric_point(model, A, B, C, '(a*(2*a**(2) + a*b + a*c - b*c)*(b**(2) + c**(2) + b*c))', ID="X_3795", classes=["selected", "target"])
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center", "incident"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    central_line(model, X_43, X_55, 43, 55, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_740 = eval_trilinear_point(model, A, B, C, 'a **(-2)*(b**(1) + c**(1)) - a**(0)*(b **(-1) + c **(-1))', ID="X_740", classes=["center", "incident"])
    central_line(model, X_2, X_740, 2, 740, incident=True)
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_985 = eval_trilinear_point(model, A, B, C, '(1/(b**(2) + b*c + c**(2)))', ID="X_985", classes=["center", "incident"])
    central_line(model, X_100, X_985, 100, 985, incident=True)
    return promote_point_to_top(model, X_3795)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3795 on the given reference triangle."""
    model = create_model('X_3795 = X_3097com[INVERSE(nT(bc, b²))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03795(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03795.json"))
    write_center_svg(
        model_acute,
        here / "x-03795.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
