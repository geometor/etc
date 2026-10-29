"""GEOMETOR construction model for X(705) = EVEN (- 4, 1) CIRCUMCIRCLE POINT."""

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


def construct_x_00705(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(705) = EVEN (- 4, 1) CIRCUMCIRCLE POINT on reference triangle ABC."""
    X_704 = eval_trilinear_point(model, A, B, C, 'a**(-5)*(b**(1)+ c**(1)) - a**(0)*(b**(-4)+ c**(-4))', ID="X(704)", classes=["center"])
    X_705 = isogonal_conjugate(model, A, B, C, X_704, ID="X(705)", classes=["selected", "target"])
    return promote_point_to_top(model, X_705)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(705) on the given reference triangle."""
    model = create_model('X(705) = EVEN (- 4, 1) CIRCUMCIRCLE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00705(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00705.json"))
    write_center_svg(
        model_acute,
        here / "x-00705.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
