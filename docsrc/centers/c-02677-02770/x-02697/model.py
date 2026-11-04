"""GEOMETOR construction model for X_2697 = SR(X_74, X_112)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_02697(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2697 = SR(X_74, X_112) on reference triangle ABC."""
    X_935 = eval_barycentric_point(model, A, B, C, '1/((b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2)))', ID="X_935", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_2697 = reflection_in_point(model, X_935, X_3, ID="X_2697", classes=["selected", "target"], guide=False)
    X_23 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X_23", classes=["center", "incident"])
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X_107", classes=["center", "incident"])
    central_line(model, X_23, X_107, 23, 107, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center", "incident"])
    central_line(model, X_30, X_112, 30, 112, incident=True)
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X_22", classes=["center", "incident"])
    X_476 = eval_trilinear_point(model, A, B, C, '1/((1 + 2*cos(2*A))*sin(B - C))', ID="X_476", classes=["center", "incident"])
    central_line(model, X_22, X_476, 22, 476, incident=True)
    return promote_point_to_top(model, X_2697)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2697 on the given reference triangle."""
    model = create_model('X_2697 = SR(X_74, X_112)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02697(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02697.json"))
    write_center_svg(
        model_acute,
        here / "x-02697.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
