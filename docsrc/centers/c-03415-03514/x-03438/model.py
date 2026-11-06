"""GEOMETOR construction model for X_3438 = X_13-VERTEX CONJUGATE OF X_13."""

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
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03438(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3438 = X_13-VERTEX CONJUGATE OF X_13 on reference triangle ABC."""
    X_621 = point_from_barycentrics(model, A, B, C, 0.34668048, 0.27954046, 0.37377907, ID="X_621", classes=["center"])
    X_3438 = isogonal_conjugate(model, A, B, C, X_621, ID="X_3438", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_299 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)*sin(A -  pi  /3)', ID="X_299", classes=["center", "incident"])
    central_line(model, X_3, X_299, 3, 299, incident=True)
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A +  pi  /3)', ID="X_13", classes=["center", "incident"])
    X_1605 = point_from_barycentrics(model, A, B, C, 0.24200161, 0.21576869, 0.54222969, ID="X_1605", classes=["center", "incident"])
    central_line(model, X_13, X_1605, 13, 1605, incident=True)
    X_2174 = eval_trilinear_point(model, A, B, C, '(sin(A) + sin(2*A))', ID="X_2174", classes=["center", "incident"])
    X_2200 = eval_trilinear_point(model, A, B, C, 'a**(3)*(b + c)*(b**(2) + c**(2) - a**(2))', ID="X_2200", classes=["center", "incident"])
    central_line(model, X_2174, X_2200, 2174, 2200, incident=True)
    return promote_point_to_top(model, X_3438)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3438 on the given reference triangle."""
    model = create_model('X_3438 = X_13-VERTEX CONJUGATE OF X_13')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03438(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03438.json"))
    write_center_svg(
        model_acute,
        here / "x-03438.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
