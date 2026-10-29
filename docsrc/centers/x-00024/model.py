"""GEOMETOR construction model for X(24) = PERSPECTOR OF ABC AND ORTHIC-OF-ORTHIC TRIANGLE."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    circumcircle,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthic_triangle,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00024(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(24) = PERSPECTOR OF ABC AND ORTHIC-OF-ORTHIC TRIANGLE on reference triangle ABC."""
    orthic_triangle(model, A, B, C)
    circumcircle(model, A, B, C)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X(54)", classes=["center"])
    central_line(model, X_6, X_54, 6, 54)
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X(33)", classes=["center"])
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X(35)", classes=["center"])
    central_line(model, X_33, X_35, 33, 35)
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X(24)", classes=["selected", "target"])
    return promote_point_to_top(model, X_24)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(24) on the given reference triangle."""
    model = create_model('X(24) = PERSPECTOR OF ABC AND ORTHIC-OF-ORTHIC TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00024(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00024.json"))
    write_center_svg(
        model_acute,
        here / "x-00024.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
