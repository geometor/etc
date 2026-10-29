"""GEOMETOR construction model for X(852) = X(2)-LINE CONJUGATE OF X(4)."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00852(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(852) = X(2)-LINE CONJUGATE OF X(4) on reference triangle ABC."""
    X_852 = eval_trilinear_point(model, A, B, C, 'sec(C)*sin(2*B)*sin(C - A) + sec(B)*sin(2*C)*sin(B - A)', ID="X(852)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_216 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*cos(B - C)', ID="X(216)", classes=["center", "incident"])
    X_373 = point_from_barycentrics(model, A, B, C, 0.28382464, 0.3169161, 0.39925926, ID="X(373)", classes=["center", "incident"])
    central_line(model, X_216, X_373, 216, 373, incident=True)
    X_520 = eval_trilinear_point(model, A, B, C, '(cos(A))*(sin(2*B) - sin(2*C))', ID="X(520)", classes=["center", "incident"])
    X_647 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))', ID="X(647)", classes=["center", "incident"])
    central_line(model, X_520, X_647, 520, 647, incident=True)
    return promote_point_to_top(model, X_852)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(852) on the given reference triangle."""
    model = create_model('X(852) = X(2)-LINE CONJUGATE OF X(4)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00852(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00852.json"))
    write_center_svg(
        model_acute,
        here / "x-00852.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
