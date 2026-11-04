"""GEOMETOR construction model for X_2407 = GIBERT-SIMSON TRANSFORM OF X_110."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02407(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2407 = GIBERT-SIMSON TRANSFORM OF X_110 on reference triangle ABC."""
    X_2407 = eval_trilinear_point(model, A, B, C, '(csc(C - A)*cos(C) - csc(A - B)*cos(B))*(csc(B - C)/a)**(2)', ID="X_2407", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center", "incident"])
    central_line(model, X_99, X_112, 99, 112, incident=True)
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center", "incident"])
    X_895 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) - a**(2))/(b**(2) + c**(2) - 2*a**(2))', ID="X_895", classes=["center", "incident"])
    central_line(model, X_98, X_895, 98, 895, incident=True)
    return promote_point_to_top(model, X_2407)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2407 on the given reference triangle."""
    model = create_model('X_2407 = GIBERT-SIMSON TRANSFORM OF X_110')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02407(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02407.json"))
    write_center_svg(
        model_acute,
        here / "x-02407.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
