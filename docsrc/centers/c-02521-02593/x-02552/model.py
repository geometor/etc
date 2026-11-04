"""GEOMETOR construction model for X_2552 = INSIMILICENTER(ORTHOCENTROIDAL CIRCLE, (X_4,2R))."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02552(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2552 = INSIMILICENTER(ORTHOCENTROIDAL CIRCLE, (X_4,2R)) on reference triangle ABC."""
    X_2552 = eval_trilinear_point(model, A, B, C, '(cos(A) + (4 + J)*cos(B)*cos(C))', ID="X_2552", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_388 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) + (b + c)**(2))/(b + c - a)', ID="X_388", classes=["center", "incident"])
    X_2464 = eval_trilinear_point(model, A, B, C, '(J - cos(A) - 4*cos(B)*cos(C))', ID="X_2464", classes=["center", "incident"])
    central_line(model, X_388, X_2464, 388, 2464, incident=True)
    X_497 = eval_trilinear_point(model, A, B, C, '1 - cos(B)*cos(C)', ID="X_497", classes=["center", "incident"])
    X_2463 = eval_trilinear_point(model, A, B, C, '(J + cos(A) + 4*cos(B)*cos(C))', ID="X_2463", classes=["center", "incident"])
    central_line(model, X_497, X_2463, 497, 2463, incident=True)
    return promote_point_to_top(model, X_2552)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2552 on the given reference triangle."""
    model = create_model('X_2552 = INSIMILICENTER(ORTHOCENTROIDAL CIRCLE, (X_4,2R))')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02552(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02552.json"))
    write_center_svg(
        model_acute,
        here / "x-02552.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
