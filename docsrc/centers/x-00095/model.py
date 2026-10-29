"""GEOMETOR construction model for X(95) = CEVAPOINT OF CENTROID AND CIRCUMCENTER."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcircle,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    medial_triangle,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00095(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(95) = CEVAPOINT OF CENTROID AND CIRCUMCENTER on reference triangle ABC."""
    medial_triangle(model, A, B, C)
    circumcircle(model, A, B, C)
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X(54)", classes=["center"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X(69)", classes=["center"])
    central_line(model, X_54, X_69, 54, 69)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_97 = eval_trilinear_point(model, A, B, C, 'cot(A)*sec(B - C)', ID="X(97)", classes=["center"])
    central_line(model, X_2, X_97, 2, 97)
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X(76)", classes=["center"])
    X_96 = eval_trilinear_point(model, A, B, C, 'sec(2*A)*sec(B - C)', ID="X(96)", classes=["center"])
    central_line(model, X_76, X_96, 76, 96)
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X(51)", classes=["center"])
    X_95 = isogonal_conjugate(model, A, B, C, X_51, ID="X(95)", classes=["selected", "target"])
    return promote_point_to_top(model, X_95)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(95) on the given reference triangle."""
    model = create_model('X(95) = CEVAPOINT OF CENTROID AND CIRCUMCENTER')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00095(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00095.json"))
    write_center_svg(
        model_acute,
        here / "x-00095.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
