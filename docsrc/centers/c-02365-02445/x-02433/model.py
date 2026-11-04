"""GEOMETOR construction model for X_2433 = ISOGONAL CONJUGATE OF X_2407."""

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
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02433(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2433 = ISOGONAL CONJUGATE OF X_2407 on reference triangle ABC."""
    X_2407 = eval_trilinear_point(model, A, B, C, '(csc(C - A)*cos(C) - csc(A - B)*cos(B))*(csc(B - C)/a)**(2)', ID="X_2407", classes=["center"])
    X_2433 = isogonal_conjugate(model, A, B, C, X_2407, ID="X_2433", classes=["selected", "target"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center", "incident"])
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X_111", classes=["center", "incident"])
    central_line(model, X_74, X_111, 74, 111, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_525 = eval_trilinear_point(model, A, B, C, '(b*cos(B) - c*cos(C))/a', ID="X_525", classes=["center", "incident"])
    central_line(model, X_2, X_525, 2, 525, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center", "incident"])
    central_line(model, X_25, X_512, 25, 512, incident=True)
    return promote_point_to_top(model, X_2433)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2433 on the given reference triangle."""
    model = create_model('X_2433 = ISOGONAL CONJUGATE OF X_2407')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02433(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02433.json"))
    write_center_svg(
        model_acute,
        here / "x-02433.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
