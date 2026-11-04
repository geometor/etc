"""GEOMETOR construction model for X_2935 = TANGENTIAL-ISOGONAL CONJUGATE OF X_186."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02935(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2935 = TANGENTIAL-ISOGONAL CONJUGATE OF X_186 on reference triangle ABC."""
    X_1498 = eval_trilinear_point(model, A, B, C, '(sin(A))*((tan(B))**(2) + (tan(C))**(2) - (tan(A))**(2))', ID="X_1498", classes=["center"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center"])
    X_2935 = reflection_in_point(model, X_1498, X_110, ID="X_2935", classes=["selected", "target"], guide=False)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center", "incident"])
    central_line(model, X_6, X_74, 6, 74, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_113 = eval_trilinear_point(model, A, B, C, 'sin(B)*sin(C)*((sin(C))/(cos(C) - 2*cos(A)*cos(B)) + (sin(B))/(cos(B) - 2*cos(A)*cos(C)))', ID="X_113", classes=["center", "incident"])
    central_line(model, X_3, X_113, 3, 113, incident=True)
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X_64", classes=["center", "incident"])
    X_155 = eval_trilinear_point(model, A, B, C, '(cos(A))*((cos(B))**(2) + (cos(C))**(2) - (cos(A))**(2))', ID="X_155", classes=["center", "incident"])
    central_line(model, X_64, X_155, 64, 155, incident=True)
    return promote_point_to_top(model, X_2935)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2935 on the given reference triangle."""
    model = create_model('X_2935 = TANGENTIAL-ISOGONAL CONJUGATE OF X_186')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02935(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02935.json"))
    write_center_svg(
        model_acute,
        here / "x-02935.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
