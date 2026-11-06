"""GEOMETOR construction model for X_3480 = ISOGONAL CONJUGATE OF X_1338."""

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
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03480(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3480 = ISOGONAL CONJUGATE OF X_1338 on reference triangle ABC."""
    X_1338 = eval_barycentric_point(model, A, B, C, '(a**(2)*(2*D*U + 3**(1/2)*V*W)/(4*D - 3**(1/2)*a**(2)))', ID="X_1338", classes=["center"])
    X_3480 = isogonal_conjugate(model, A, B, C, X_1338, ID="X_3480", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_299 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)*sin(A -  pi  /3)', ID="X_299", classes=["center", "incident"])
    central_line(model, X_3, X_299, 3, 299, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    central_line(model, X_30, X_1338, 30, 1338, incident=True)
    X_3479 = point_from_barycentrics(model, A, B, C, 0.32216521, 1.0604357, -0.38260091, ID="X_3479", classes=["center", "incident"])
    X_3484 = point_from_barycentrics(model, A, B, C, 1.3028444, 1.5329065, -1.8357509, ID="X_3484", classes=["center", "incident"])
    central_line(model, X_3479, X_3484, 3479, 3484, incident=True)
    return promote_point_to_top(model, X_3480)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3480 on the given reference triangle."""
    model = create_model('X_3480 = ISOGONAL CONJUGATE OF X_1338')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03480(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03480.json"))
    write_center_svg(
        model_acute,
        here / "x-03480.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
