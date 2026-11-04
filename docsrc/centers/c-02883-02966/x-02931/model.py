"""GEOMETOR construction model for X_2931 = TANGENTIAL-ISOGONAL CONJUGATE OF X_30."""

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
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_02931(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2931 = TANGENTIAL-ISOGONAL CONJUGATE OF X_30 on reference triangle ABC."""
    X_155 = eval_trilinear_point(model, A, B, C, '(cos(A))*((cos(B))**(2) + (cos(C))**(2) - (cos(A))**(2))', ID="X_155", classes=["center"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center"])
    X_2931 = reflection_in_point(model, X_155, X_110, ID="X_2931", classes=["selected", "target"], guide=False)
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X_22", classes=["center", "incident"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center", "incident"])
    central_line(model, X_22, X_74, 22, 74, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X_125", classes=["center", "incident"])
    central_line(model, X_3, X_125, 3, 125, incident=True)
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X_24", classes=["center", "incident"])
    central_line(model, X_24, X_110, 24, 110, incident=True)
    return promote_point_to_top(model, X_2931)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2931 on the given reference triangle."""
    model = create_model('X_2931 = TANGENTIAL-ISOGONAL CONJUGATE OF X_30')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02931(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02931.json"))
    write_center_svg(
        model_acute,
        here / "x-02931.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
