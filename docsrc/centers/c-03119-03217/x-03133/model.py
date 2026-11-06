"""GEOMETOR construction model for X_3133 = X_24-CEVA CONJUGATE OF X_52."""

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


def construct_x_03133(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3133 = X_24-CEVA CONJUGATE OF X_52 on reference triangle ABC."""
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X_24", classes=["center"])
    X_52 = eval_trilinear_point(model, A, B, C, 'cos(2*A)*cos(B - C)', ID="X_52", classes=["center"])
    X_3133 = ceva_conjugate(model, A, B, C, X_24, X_52, ID="X_3133", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_571 = eval_trilinear_point(model, A, B, C, 'sin(A)*cos(2*A)', ID="X_571", classes=["center", "incident"])
    X_1147 = eval_trilinear_point(model, A, B, C, '(sin(4*A))/sin(A)', ID="X_1147", classes=["center", "incident"])
    central_line(model, X_571, X_1147, 571, 1147, incident=True)
    return promote_point_to_top(model, X_3133)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3133 on the given reference triangle."""
    model = create_model('X_3133 = X_24-CEVA CONJUGATE OF X_52')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03133(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03133.json"))
    write_center_svg(
        model_acute,
        here / "x-03133.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
