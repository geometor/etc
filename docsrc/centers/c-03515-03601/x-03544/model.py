"""GEOMETOR construction model for X_3544 = EULER LINE INTERCEPT OF LINE X_6X_14842."""

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
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03544(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3544 = EULER LINE INTERCEPT OF LINE X_6X_14842 on reference triangle ABC."""
    X_3544 = eval_barycentric_point(model, A, B, C, 'a**(4) + 8*a**(2)*b**(2) - 9*b**(4) + 8*a**(2)*c**(2) + 18*b**(2)*c**(2) - 9*c**(4)', ID="X_3544", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_3070 = eval_trilinear_point(model, A, B, C, 'sin(A) + 2*cos(B)*cos(C)', ID="X_3070", classes=["center", "incident"])
    X_3317 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*sin(A))', ID="X_3317", classes=["center", "incident"])
    central_line(model, X_3070, X_3317, 3070, 3317, incident=True)
    X_3071 = eval_trilinear_point(model, A, B, C, 'sin(A) - 2*cos(B)*cos(C)', ID="X_3071", classes=["center", "incident"])
    X_3316 = eval_trilinear_point(model, A, B, C, '1/(cos(A) + 2*sin(A))', ID="X_3316", classes=["center", "incident"])
    central_line(model, X_3071, X_3316, 3071, 3316, incident=True)
    return promote_point_to_top(model, X_3544)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3544 on the given reference triangle."""
    model = create_model('X_3544 = EULER LINE INTERCEPT OF LINE X_6X_14842')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03544(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03544.json"))
    write_center_svg(
        model_acute,
        here / "x-03544.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
