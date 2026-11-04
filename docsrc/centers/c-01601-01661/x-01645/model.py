"""GEOMETOR construction model for X_1645 = TRIPOLAR CENTROID OF X_512."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01645(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1645 = TRIPOLAR CENTROID OF X_512 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center"])
    X_351 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) - c**(2))*(b**(2) + c**(2) - 2*a**(2)))', ID="X_351", classes=["center"])
    X_865 = eval_trilinear_point(model, A, B, C, '(sin(2*B)*(csc(C))**(2)*sin(C - A)*csc(A - B) - sin(2*C)*(csc(B))**(2)*sin(B - A)*csc(A - C))', ID="X_865", classes=["center"])
    central_line(model, X_2, X_39, 2, 39)
    central_line(model, X_351, X_865, 351, 865)
    X_1645 = intersect_lines(model, X_2, X_39, X_351, X_865, ID="X_1645", classes=["selected", "target"])
    return promote_point_to_top(model, X_1645)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1645 on the given reference triangle."""
    model = create_model('X_1645 = TRIPOLAR CENTROID OF X_512')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01645(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01645.json"))
    write_center_svg(
        model_acute,
        here / "x-01645.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
