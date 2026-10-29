"""GEOMETOR construction model for X(735) = EVEN (- 2, 3) CIRCUMCIRCLE POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00735(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(735) = EVEN (- 2, 3) CIRCUMCIRCLE POINT on reference triangle ABC."""
    X_734 = eval_trilinear_point(model, A, B, C, 'a**(-3)*(b**(3)+ c**(3)) - a**(2)*(b**(-2)+ c**(-2))', ID="X(734)", classes=["center"])
    X_735 = isogonal_conjugate(model, A, B, C, X_734, ID="X(735)", classes=["selected", "target"])
    return promote_point_to_top(model, X_735)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(735) on the given reference triangle."""
    model = create_model('X(735) = EVEN (- 2, 3) CIRCUMCIRCLE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00735(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00735.json"))
    write_center_svg(
        model_acute,
        here / "x-00735.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
