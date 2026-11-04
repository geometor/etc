"""GEOMETOR construction model for X_1152 = ISOGONAL CONJUGATE OF X_1132."""

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
    isogonal_conjugate,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01152(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1152 = ISOGONAL CONJUGATE OF X_1132 on reference triangle ABC."""
    X_1132 = eval_trilinear_point(model, A, B, C, '1/(sin(A) - 2*cos(A))', ID="X_1132", classes=["center"])
    X_1152 = isogonal_conjugate(model, A, B, C, X_1132, ID="X_1152", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_490 = eval_trilinear_point(model, A, B, C, '((cos(A))*(1 + csc(A)*sin(B)*sin(C)) - cos(B)*cos(C))', ID="X_490", classes=["center", "incident"])
    central_line(model, X_2, X_490, 2, 490, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_486 = eval_trilinear_point(model, A, B, C, 'sec(A +  pi  /4)', ID="X_486", classes=["center", "incident"])
    central_line(model, X_30, X_486, 30, 486, incident=True)
    return promote_point_to_top(model, X_1152)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1152 on the given reference triangle."""
    model = create_model('X_1152 = ISOGONAL CONJUGATE OF X_1132')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01152(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01152.json"))
    write_center_svg(
        model_acute,
        here / "x-01152.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
