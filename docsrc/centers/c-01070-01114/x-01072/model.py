"""GEOMETOR construction model for X_1072 = POINT ALNILAM."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01072(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1072 = POINT ALNILAM on reference triangle ABC."""
    X_1072 = eval_trilinear_point(model, A, B, C, '(1 - (cos(B))**(2)*cos(C) - cos(B)*(cos(C))**(2))', ID="X_1072", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    central_line(model, X_1, X_4, 1, 4, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_1074 = eval_trilinear_point(model, A, B, C, '(cos(A) + (cos(B))**(2)*cos(C) + cos(B)*(cos(C))**(2))', ID="X_1074", classes=["center", "incident"])
    central_line(model, X_55, X_1074, 55, 1074, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_1076 = eval_trilinear_point(model, A, B, C, '(cos(A) - (cos(B))**(2)*cos(C) - cos(B)*(cos(C))**(2))', ID="X_1076", classes=["center", "incident"])
    central_line(model, X_56, X_1076, 56, 1076, incident=True)
    return promote_point_to_top(model, X_1072)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1072 on the given reference triangle."""
    model = create_model('X_1072 = POINT ALNILAM')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01072(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01072.json"))
    write_center_svg(
        model_acute,
        here / "x-01072.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
