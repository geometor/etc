"""GEOMETOR construction model for X_467 = EULER LINE INTERCEPT OF LINE X_53X_311."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    ceva_conjugate,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00467(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_467 = EULER LINE INTERCEPT OF LINE X_53X_311 on reference triangle ABC."""
    X_317 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)*(csc(A))**(2)', ID="X_317", classes=["center"])
    X_52 = eval_trilinear_point(model, A, B, C, 'cos(2*A)*cos(B - C)', ID="X_52", classes=["center"])
    X_467 = ceva_conjugate(model, A, B, C, X_317, X_52, ID="X_467", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_53 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(B - C)', ID="X_53", classes=["center", "incident"])
    X_311 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)*cos(B - C)', ID="X_311", classes=["center", "incident"])
    central_line(model, X_53, X_311, 53, 311, incident=True)
    return promote_point_to_top(model, X_467)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_467 on the given reference triangle."""
    model = create_model('X_467 = EULER LINE INTERCEPT OF LINE X_53X_311')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00467(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00467.json"))
    write_center_svg(
        model_acute,
        here / "x-00467.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
