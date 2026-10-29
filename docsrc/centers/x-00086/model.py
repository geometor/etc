"""GEOMETOR construction model for X(86) = CEVAPOINT OF INCENTER AND CENTROID."""

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
    gergonne_point_of,
    incircle,
    isogonal_conjugate,
    medial_triangle,
    nine_point_circle,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00086(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(86) = CEVAPOINT OF INCENTER AND CENTROID on reference triangle ABC."""
    medial_triangle(model, A, B, C)
    incircle(model, A, B, C)
    circumcircle(model, A, B, C)
    nine_point_circle(model, A, B, C)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    central_line(model, X_2, X_6, 2, 6)
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X(21)", classes=["center"])
    central_line(model, X_7, X_21, 7, 21)
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X(29)", classes=["center"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X(34)", classes=["center"])
    central_line(model, X_29, X_34, 29, 34)
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X(42)", classes=["center"])
    X_86 = isogonal_conjugate(model, A, B, C, X_42, ID="X(86)", classes=["selected", "target"])
    return promote_point_to_top(model, X_86)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(86) on the given reference triangle."""
    model = create_model('X(86) = CEVAPOINT OF INCENTER AND CENTROID')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00086(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00086.json"))
    write_center_svg(
        model_acute,
        here / "x-00086.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
