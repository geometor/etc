"""GEOMETOR construction model for X_2071 = INVERSE-IN-CIRCUMCIRCLE OF X_20."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    anticomplement,
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02071(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2071 = INVERSE-IN-CIRCUMCIRCLE OF X_20 on reference triangle ABC."""
    X_403 = eval_trilinear_point(model, A, B, C, '(sec(A))*(1 + cos(2*B) + cos(2*C))', ID="X_403", classes=["center"])
    X_2071 = anticomplement(model, A, B, C, X_403, ID="X_2071", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center", "incident"])
    X_323 = eval_trilinear_point(model, A, B, C, 'sin(3*A)*(csc(A))**(2)', ID="X_323", classes=["center", "incident"])
    central_line(model, X_74, X_323, 74, 323, incident=True)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    X_1236 = point_from_barycentrics(model, A, B, C, 1.0358088, 0.50805752, -0.54386633, ID="X_1236", classes=["center", "incident"])
    central_line(model, X_99, X_1236, 99, 1236, incident=True)
    return promote_point_to_top(model, X_2071)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2071 on the given reference triangle."""
    model = create_model('X_2071 = INVERSE-IN-CIRCUMCIRCLE OF X_20')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02071(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02071.json"))
    write_center_svg(
        model_acute,
        here / "x-02071.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
