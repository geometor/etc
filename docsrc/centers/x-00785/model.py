"""GEOMETOR construction model for X(785) = o-(- 3, - 2) CIRCUMCIRCLE POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00785(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(785) = o-(- 3, - 2) CIRCUMCIRCLE POINT on reference triangle ABC."""
    X_784 = eval_trilinear_point(model, A, B, C, 'a**(-4)*(b**(-2)- c**(-2)) + a**(-3)*(b**(-3)- c**(-3))', ID="X(784)", classes=["center"])
    X_785 = isogonal_conjugate(model, A, B, C, X_784, ID="X(785)", classes=["selected", "target"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    X_692 = eval_trilinear_point(model, A, B, C, 'a**(2)/(b - c)', ID="X(692)", classes=["center", "incident"])
    central_line(model, X_99, X_692, 99, 692, incident=True)
    return promote_point_to_top(model, X_785)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(785) on the given reference triangle."""
    model = create_model('X(785) = o-(- 3, - 2) CIRCUMCIRCLE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00785(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00785.json"))
    write_center_svg(
        model_acute,
        here / "x-00785.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
