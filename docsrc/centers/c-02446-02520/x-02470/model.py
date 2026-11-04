"""GEOMETOR construction model for X_2470 = EXSIMILICENTER(ORTHOCENTROIDAL CIRCLE, BROCARD CIRCLE)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02470(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2470 = EXSIMILICENTER(ORTHOCENTROIDAL CIRCLE, BROCARD CIRCLE) on reference triangle ABC."""
    X_182 = eval_trilinear_point(model, A, B, C, 'cos(A-  omega  )', ID="X_182", classes=["center"])
    X_381 = eval_trilinear_point(model, A, B, C, '2*cos(B - C) - cos(A)', ID="X_381", classes=["center"])
    X_1668 = eval_trilinear_point(model, A, B, C, 'cos(A -  omega  ) - e*sin(A)', ID="X_1668", classes=["center"])
    X_2466 = eval_trilinear_point(model, A, B, C, '(cos(A) + 4*cos(B)*cos(C) - J*sin(A))', ID="X_2466", classes=["center"])
    central_line(model, X_182, X_381, 182, 381)
    central_line(model, X_1668, X_2466, 1668, 2466)
    X_2470 = intersect_lines(model, X_182, X_381, X_1668, X_2466, ID="X_2470", classes=["selected", "target"])
    X_1669 = eval_trilinear_point(model, A, B, C, 'cos(A -  omega  ) + e*sin(A)', ID="X_1669", classes=["center", "incident"])
    X_2465 = eval_trilinear_point(model, A, B, C, '(cos(A) + 4*cos(B)*cos(C) + J*sin(A))', ID="X_2465", classes=["center", "incident"])
    central_line(model, X_1669, X_2465, 1669, 2465, incident=True)
    return promote_point_to_top(model, X_2470)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2470 on the given reference triangle."""
    model = create_model('X_2470 = EXSIMILICENTER(ORTHOCENTROIDAL CIRCLE, BROCARD CIRCLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02470(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02470.json"))
    write_center_svg(
        model_acute,
        here / "x-02470.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
