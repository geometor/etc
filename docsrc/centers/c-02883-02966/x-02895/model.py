"""GEOMETOR construction model for X_2895 = ANTICOMPLEMENTARY CONJUGATE OF X_75."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nagel_point_of,
    promote_point_to_top,
    reflection_in_point,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02895(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2895 = ANTICOMPLEMENTARY CONJUGATE OF X_75 on reference triangle ABC."""
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X_81", classes=["center"])
    X_1211 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c)*(b**(2) + c**(2) + a*b + a*c))', ID="X_1211", classes=["center"])
    X_2895 = reflection_in_point(model, X_81, X_1211, ID="X_2895", classes=["selected", "target"], guide=False)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_79 = eval_trilinear_point(model, A, B, C, '1/(1 + 2*cos(A))', ID="X_79", classes=["center", "incident"])
    central_line(model, X_8, X_79, 8, 79, incident=True)
    X_319 = eval_trilinear_point(model, A, B, C, '(1 + 2*cos(A))/a**(2)', ID="X_319", classes=["center", "incident"])
    X_321 = eval_trilinear_point(model, A, B, C, '(b + c)*b**(2)*c**(2)', ID="X_321", classes=["center", "incident"])
    central_line(model, X_319, X_321, 319, 321, incident=True)
    return promote_point_to_top(model, X_2895)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2895 on the given reference triangle."""
    model = create_model('X_2895 = ANTICOMPLEMENTARY CONJUGATE OF X_75')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02895(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02895.json"))
    write_center_svg(
        model_acute,
        here / "x-02895.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
