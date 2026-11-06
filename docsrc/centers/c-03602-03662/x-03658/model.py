"""GEOMETOR construction model for X_3658 = ISOGONAL CONJUGATE OF AYME PERSPECTOR."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03658(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3658 = ISOGONAL CONJUGATE OF AYME PERSPECTOR on reference triangle ABC."""
    X_3657 = point_from_barycentrics(model, A, B, C, 0.22247024, 0.90357143, -0.12604167, ID="X_3657", classes=["center"])
    X_3658 = isogonal_conjugate(model, A, B, C, X_3657, ID="X_3658", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_100, X_110, 100, 110, incident=True)
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center", "incident"])
    X_925 = eval_trilinear_point(model, A, B, C, '(sin(A))/(sec(2*B) - sec(2*C))', ID="X_925", classes=["center", "incident"])
    central_line(model, X_108, X_925, 108, 925, incident=True)
    return promote_point_to_top(model, X_3658)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3658 on the given reference triangle."""
    model = create_model('X_3658 = ISOGONAL CONJUGATE OF AYME PERSPECTOR')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03658(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03658.json"))
    write_center_svg(
        model_acute,
        here / "x-03658.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
