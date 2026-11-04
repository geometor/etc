"""GEOMETOR construction model for X_1157 = INVERSE-IN-CIRCUMCIRCLE OF X_54."""

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
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01157(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1157 = INVERSE-IN-CIRCUMCIRCLE OF X_54 on reference triangle ABC."""
    X_1157 = eval_trilinear_point(model, A, B, C, '4*cos(A) + cos(3*A)*sec(A)*sec(B - C)', ID="X_1157", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    central_line(model, X_3, X_54, 3, 54, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_252 = eval_trilinear_point(model, A, B, C, '(sec(B - C)/(1 - 2*cos(2*A)))', ID="X_252", classes=["center", "incident"])
    central_line(model, X_5, X_252, 5, 252, incident=True)
    X_186 = eval_trilinear_point(model, A, B, C, '4*cos(A) - sec(A)', ID="X_186", classes=["center", "incident"])
    X_933 = eval_trilinear_point(model, A, B, C, 'sec(A)*csc(2*B - 2*C)', ID="X_933", classes=["center", "incident"])
    central_line(model, X_186, X_933, 186, 933, incident=True)
    return promote_point_to_top(model, X_1157)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1157 on the given reference triangle."""
    model = create_model('X_1157 = INVERSE-IN-CIRCUMCIRCLE OF X_54')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01157(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01157.json"))
    write_center_svg(
        model_acute,
        here / "x-01157.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
