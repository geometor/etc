"""GEOMETOR construction model for X(737) = EVEN (- 2, 4) CIRCUMCIRCLE POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00737(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(737) = EVEN (- 2, 4) CIRCUMCIRCLE POINT on reference triangle ABC."""
    X_736 = eval_barycentric_point(model, A, B, C, 'a**(6)*(b**(2) + c**(2)) - b**(2)*c**(2)*(b**(4) + c**(4))', ID="X(736)", classes=["center"])
    X_737 = isogonal_conjugate(model, A, B, C, X_736, ID="X(737)", classes=["selected", "target"])
    return promote_point_to_top(model, X_737)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(737) on the given reference triangle."""
    model = create_model('X(737) = EVEN (- 2, 4) CIRCUMCIRCLE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00737(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00737.json"))
    write_center_svg(
        model_acute,
        here / "x-00737.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
