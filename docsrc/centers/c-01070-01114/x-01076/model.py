"""GEOMETOR construction model for X_1076 = POINT ALPHARD."""

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
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01076(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1076 = POINT ALPHARD on reference triangle ABC."""
    X_1076 = eval_trilinear_point(model, A, B, C, '(cos(A) - (cos(B))**(2)*cos(C) - cos(B)*(cos(C))**(2))', ID="X_1076", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_225 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cos(B) + cos(C))', ID="X_225", classes=["center", "incident"])
    central_line(model, X_3, X_225, 3, 225, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_1038 = eval_trilinear_point(model, A, B, C, 'cos(A) + cos(A)*cos(B)*cos(C)', ID="X_1038", classes=["center", "incident"])
    central_line(model, X_4, X_1038, 4, 1038, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_1070 = eval_trilinear_point(model, A, B, C, '(1 + cos(B)*cos(C)*(cos(B) + cos(C)))', ID="X_1070", classes=["center", "incident"])
    central_line(model, X_55, X_1070, 55, 1070, incident=True)
    return promote_point_to_top(model, X_1076)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1076 on the given reference triangle."""
    model = create_model('X_1076 = POINT ALPHARD')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01076(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01076.json"))
    write_center_svg(
        model_acute,
        here / "x-01076.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
