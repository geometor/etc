"""GEOMETOR construction model for X_2472 = EXSIMILICENTER(ORTHOCENTROIDAL CIRCLE, 1st LEMOINE CIRCLE)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02472(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2472 = EXSIMILICENTER(ORTHOCENTROIDAL CIRCLE, 1st LEMOINE CIRCLE) on reference triangle ABC."""
    X_2472 = eval_trilinear_point(model, A, B, C, '(cos(A) + 4*cos(B)*cos(C) - J*cos(A -  omega  ))', ID="X_2472", classes=["selected", "target"])
    X_181 = eval_trilinear_point(model, A, B, C, 'a*(b + c)**(2)/(b + c - a)', ID="X_181", classes=["center", "incident"])
    X_381 = eval_trilinear_point(model, A, B, C, '2*cos(B - C) - cos(A)', ID="X_381", classes=["center", "incident"])
    central_line(model, X_181, X_381, 181, 381, incident=True)
    X_1672 = eval_trilinear_point(model, A, B, C, '1 + cos(A -  omega  )', ID="X_1672", classes=["center", "incident"])
    X_2463 = eval_trilinear_point(model, A, B, C, '(J + cos(A) + 4*cos(B)*cos(C))', ID="X_2463", classes=["center", "incident"])
    central_line(model, X_1672, X_2463, 1672, 2463, incident=True)
    X_1673 = eval_trilinear_point(model, A, B, C, '1 - cos(A -  omega  )', ID="X_1673", classes=["center", "incident"])
    X_2464 = eval_trilinear_point(model, A, B, C, '(J - cos(A) - 4*cos(B)*cos(C))', ID="X_2464", classes=["center", "incident"])
    central_line(model, X_1673, X_2464, 1673, 2464, incident=True)
    return promote_point_to_top(model, X_2472)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2472 on the given reference triangle."""
    model = create_model('X_2472 = EXSIMILICENTER(ORTHOCENTROIDAL CIRCLE, 1st LEMOINE CIRCLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02472(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02472.json"))
    write_center_svg(
        model_acute,
        here / "x-02472.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
