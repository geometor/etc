"""GEOMETOR construction model for X_1173 = 1st SARAGOSSA POINT OF X_54."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01173(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1173 = 1st SARAGOSSA POINT OF X_54 on reference triangle ABC."""
    X_140 = eval_trilinear_point(model, A, B, C, '2*cos(A) + cos(B - C)', ID="X_140", classes=["center"])
    X_1173 = isogonal_conjugate(model, A, B, C, X_140, ID="X_1173", classes=["selected", "target"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X_51", classes=["center", "incident"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    central_line(model, X_51, X_54, 51, 54, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_143 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cos(2*C - 2*A) + cos(2*A - 2*B))', ID="X_143", classes=["center", "incident"])
    central_line(model, X_3, X_143, 3, 143, incident=True)
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center", "incident"])
    X_389 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(2*A)*cos(B - C)', ID="X_389", classes=["center", "incident"])
    central_line(model, X_74, X_389, 74, 389, incident=True)
    return promote_point_to_top(model, X_1173)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1173 on the given reference triangle."""
    model = create_model('X_1173 = 1st SARAGOSSA POINT OF X_54')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01173(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01173.json"))
    write_center_svg(
        model_acute,
        here / "x-01173.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
