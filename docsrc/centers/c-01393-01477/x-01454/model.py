"""GEOMETOR construction model for X_1454 = X_498-BETH CONJUGATE OF X_498."""

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
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01454(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1454 = X_498-BETH CONJUGATE OF X_498 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center"])
    central_line(model, X_1, X_3, 1, 3)
    central_line(model, X_12, X_63, 12, 63)
    X_1454 = intersect_lines(model, X_1, X_3, X_12, X_63, ID="X_1454", classes=["selected", "target"])
    X_90 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C) - cos(A))', ID="X_90", classes=["center", "incident"])
    X_381 = eval_trilinear_point(model, A, B, C, '2*cos(B - C) - cos(A)', ID="X_381", classes=["center", "incident"])
    central_line(model, X_90, X_381, 90, 381, incident=True)
    return promote_point_to_top(model, X_1454)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1454 on the given reference triangle."""
    model = create_model('X_1454 = X_498-BETH CONJUGATE OF X_498')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01454(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01454.json"))
    write_center_svg(
        model_acute,
        here / "x-01454.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
