"""GEOMETOR construction model for X_3478 = ISOGONAL CONJUGATE OF X_3476."""

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
    incenter_of,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03478(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3478 = ISOGONAL CONJUGATE OF X_3476 on reference triangle ABC."""
    X_3476 = eval_trilinear_point(model, A, B, C, '(2 - cos(A) - cos(B) - cos(C) + cos(B)*cos(C))', ID="X_3476", classes=["center"])
    X_3478 = isogonal_conjugate(model, A, B, C, X_3476, ID="X_3478", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_902 = eval_trilinear_point(model, A, B, C, 'a*(b + c - 2*a)', ID="X_902", classes=["center", "incident"])
    central_line(model, X_3, X_902, 3, 902, incident=True)
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X_77", classes=["center", "incident"])
    X_1122 = eval_trilinear_point(model, A, B, C, '((a*(b + c) + (b - c)**(2))/(b + c - a))', ID="X_1122", classes=["center", "incident"])
    central_line(model, X_77, X_1122, 77, 1122, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_1828 = point_from_barycentrics(model, A, B, C, 0.087301587, 0.19047619, 0.72222222, ID="X_1828", classes=["center", "incident"])
    central_line(model, X_1, X_1828, 1, 1828, incident=True)
    return promote_point_to_top(model, X_3478)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3478 on the given reference triangle."""
    model = create_model('X_3478 = ISOGONAL CONJUGATE OF X_3476')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03478(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03478.json"))
    write_center_svg(
        model_acute,
        here / "x-03478.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
