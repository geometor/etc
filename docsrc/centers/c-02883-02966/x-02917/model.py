"""GEOMETOR construction model for X_2917 = TANGENTIAL-ISOGONAL CONJUGATE OF X_4."""

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
    intersect_lines,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02917(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2917 = TANGENTIAL-ISOGONAL CONJUGATE OF X_4 on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X_24", classes=["center"])
    X_49 = eval_trilinear_point(model, A, B, C, 'cos(3*A)', ID="X_49", classes=["center"])
    X_52 = eval_trilinear_point(model, A, B, C, 'cos(2*A)*cos(B - C)', ID="X_52", classes=["center"])
    central_line(model, X_6, X_24, 6, 24)
    central_line(model, X_49, X_52, 49, 52)
    X_2917 = intersect_lines(model, X_6, X_24, X_49, X_52, ID="X_2917", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_161 = eval_trilinear_point(model, A, B, C, '(a*((a**(2) + b**(2) + c**(2))*(sin(2*A))**(2) + (c**(2) - b**(2) - a**(2))*(sin(2*B))**(2) + (b**(2) - c**(2) - a**(2))*(sin(2*C))**(2)))', ID="X_161", classes=["center", "incident"])
    central_line(model, X_3, X_161, 3, 161, incident=True)
    return promote_point_to_top(model, X_2917)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2917 on the given reference triangle."""
    model = create_model('X_2917 = TANGENTIAL-ISOGONAL CONJUGATE OF X_4')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02917(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02917.json"))
    write_center_svg(
        model_acute,
        here / "x-02917.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
