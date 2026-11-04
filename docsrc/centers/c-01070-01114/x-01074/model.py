"""GEOMETOR construction model for X_1074 = POINT ALNITAK."""

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
    incenter_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01074(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1074 = POINT ALNITAK on reference triangle ABC."""
    X_1074 = eval_trilinear_point(model, A, B, C, '(cos(A) + (cos(B))**(2)*cos(C) + cos(B)*(cos(C))**(2))', ID="X_1074", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_224 = eval_trilinear_point(model, A, B, C, '(cot(B)*(cos(B/2))**(2) + cot(C)*(cos(C/2))**(2) - cot(A)*(cos(A/2))**(2))*cot(A)', ID="X_224", classes=["center", "incident"])
    central_line(model, X_1, X_224, 1, 224, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_225 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cos(B) + cos(C))', ID="X_225", classes=["center", "incident"])
    central_line(model, X_3, X_225, 3, 225, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_1040 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(A)*cos(B)*cos(C)', ID="X_1040", classes=["center", "incident"])
    central_line(model, X_4, X_1040, 4, 1040, incident=True)
    return promote_point_to_top(model, X_1074)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1074 on the given reference triangle."""
    model = create_model('X_1074 = POINT ALNITAK')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01074(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01074.json"))
    write_center_svg(
        model_acute,
        here / "x-01074.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
