"""GEOMETOR construction model for X_2777 = ISOGONAL CONJUGATE OF X_2693."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02777(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2777 = ISOGONAL CONJUGATE OF X_2693 on reference triangle ABC."""
    X_2693 = point_from_barycentrics(model, A, B, C, 0.99105015, 0.5476195, -0.53866965, ID="X_2693", classes=["center"])
    X_2777 = isogonal_conjugate(model, A, B, C, X_2693, ID="X_2777", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center", "incident"])
    central_line(model, X_4, X_74, 4, 74, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_113 = eval_trilinear_point(model, A, B, C, 'sin(B)*sin(C)*((sin(C))/(cos(C) - 2*cos(A)*cos(B)) + (sin(B))/(cos(B) - 2*cos(A)*cos(C)))', ID="X_113", classes=["center", "incident"])
    central_line(model, X_3, X_113, 3, 113, incident=True)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_20, X_110, 20, 110, incident=True)
    return promote_point_to_top(model, X_2777)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2777 on the given reference triangle."""
    model = create_model('X_2777 = ISOGONAL CONJUGATE OF X_2693')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02777(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02777.json"))
    write_center_svg(
        model_acute,
        here / "x-02777.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
