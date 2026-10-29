"""GEOMETOR construction model for X(26) = CIRCUMCENTER OF THE TANGENTIAL TRIANGLE."""

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
    promote_point_to_top,
    tangential_triangle,
)
from geometor.etc.render import write_center_svg


def construct_x_00026(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(26) = CIRCUMCENTER OF THE TANGENTIAL TRIANGLE on reference triangle ABC."""
    tangential_triangle(model, A, B, C)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_26 = eval_trilinear_point(model, A, B, C, 'a*(b**(2)*cos(2*B) + c**(2)*cos(2*C) - a**(2)*cos(2*A))', ID="X(26)", classes=["selected", "target"])
    return promote_point_to_top(model, X_26)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(26) on the given reference triangle."""
    model = create_model('X(26) = CIRCUMCENTER OF THE TANGENTIAL TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00026(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00026.json"))
    write_center_svg(
        model_acute,
        here / "x-00026.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
