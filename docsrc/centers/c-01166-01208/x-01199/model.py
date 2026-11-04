"""GEOMETOR construction model for X_1199 = 3rd SARAGOSSA POINT OF X_54."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01199(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1199 = 3rd SARAGOSSA POINT OF X_54 on reference triangle ABC."""
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center"])
    X_1173 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(4) - 3*a**(2)*(b**(2) + c**(2)) + (b**(2) - c**(2))**(2))', ID="X_1173", classes=["center"])
    X_1199 = crosspoint(model, A, B, C, X_54, X_1173, ID="X_1199", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_4, X_6, 4, 6, incident=True)
    X_23 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X_23", classes=["center", "incident"])
    X_143 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cos(2*C - 2*A) + cos(2*A - 2*B))', ID="X_143", classes=["center", "incident"])
    central_line(model, X_23, X_143, 23, 143, incident=True)
    X_186 = eval_trilinear_point(model, A, B, C, '4*cos(A) - sec(A)', ID="X_186", classes=["center", "incident"])
    central_line(model, X_54, X_186, 54, 186, incident=True)
    return promote_point_to_top(model, X_1199)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1199 on the given reference triangle."""
    model = create_model('X_1199 = 3rd SARAGOSSA POINT OF X_54')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01199(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01199.json"))
    write_center_svg(
        model_acute,
        here / "x-01199.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
