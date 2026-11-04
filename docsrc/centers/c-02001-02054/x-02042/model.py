"""GEOMETOR construction model for X_2042 = 2nd EULER-VECTEN-GIBERT POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_02042(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2042 = 2nd EULER-VECTEN-GIBERT POINT on reference triangle ABC."""
    X_2041 = eval_trilinear_point(model, A, B, C, '(b*c*((b**(2) - c**(2))**(2) - a**(2)*(b**(2) + c**(2)) + 3**(1/2)*a**(2)*(b**(2) + c**(2) - a**(2))))', ID="X_2041", classes=["center"])
    X_382 = eval_trilinear_point(model, A, B, C, 'cos(A) - 4*cos(B)*cos(C)', ID="X_382", classes=["center"])
    X_2042 = reflection_in_point(model, X_2041, X_382, ID="X_2042", classes=["selected", "target"], guide=False)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_15 = eval_trilinear_point(model, A, B, C, 'sin(A +  pi  /3)', ID="X_15", classes=["center", "incident"])
    X_486 = eval_trilinear_point(model, A, B, C, 'sec(A +  pi  /4)', ID="X_486", classes=["center", "incident"])
    central_line(model, X_15, X_486, 15, 486, incident=True)
    X_16 = eval_trilinear_point(model, A, B, C, 'sin(A-  pi  /3)', ID="X_16", classes=["center", "incident"])
    X_485 = eval_trilinear_point(model, A, B, C, 'sec(A -  pi  /4)', ID="X_485", classes=["center", "incident"])
    central_line(model, X_16, X_485, 16, 485, incident=True)
    return promote_point_to_top(model, X_2042)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2042 on the given reference triangle."""
    model = create_model('X_2042 = 2nd EULER-VECTEN-GIBERT POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02042(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02042.json"))
    write_center_svg(
        model_acute,
        here / "x-02042.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
