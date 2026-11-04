"""GEOMETOR construction model for X_2015 = INSIMILICENTER(GALLATLY CIRCLE, ORTHOCENTROIDAL CIRCLE)."""

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


def construct_x_02015(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2015 = INSIMILICENTER(GALLATLY CIRCLE, ORTHOCENTROIDAL CIRCLE) on reference triangle ABC."""
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center"])
    X_381 = eval_trilinear_point(model, A, B, C, '2*cos(B - C) - cos(A)', ID="X_381", classes=["center"])
    X_1344 = eval_trilinear_point(model, A, B, C, '( OH  + R)*cos(A) + 4*R*cos(B)*cos(C)', ID="X_1344", classes=["center"])
    X_1689 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  /2 +  pi  /4)', ID="X_1689", classes=["center"])
    central_line(model, X_39, X_381, 39, 381)
    central_line(model, X_1344, X_1689, 1344, 1689)
    X_2015 = intersect_lines(model, X_39, X_381, X_1344, X_1689, ID="X_2015", classes=["selected", "target"])
    X_1345 = eval_trilinear_point(model, A, B, C, '( OH  - R)*cos(A) - 4*R*cos(B)*cos(C)', ID="X_1345", classes=["center", "incident"])
    X_1690 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  /2 -  pi  /4)', ID="X_1690", classes=["center", "incident"])
    central_line(model, X_1345, X_1690, 1345, 1690, incident=True)
    return promote_point_to_top(model, X_2015)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2015 on the given reference triangle."""
    model = create_model('X_2015 = INSIMILICENTER(GALLATLY CIRCLE, ORTHOCENTROIDAL CIRCLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02015(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02015.json"))
    write_center_svg(
        model_acute,
        here / "x-02015.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
