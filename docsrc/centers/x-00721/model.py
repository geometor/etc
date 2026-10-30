"""GEOMETOR construction model for X(721) = EVEN (- 3, 0) CIRCUMCIRCLE POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    construct_baseline_triangle,
    create_model,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00721(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(721) = EVEN (- 3, 0) CIRCUMCIRCLE POINT on reference triangle ABC."""
    X_720 = point_from_barycentrics(model, A, B, C, 0.74206131, -0.076058184, -0.66600313, ID="X(720)", classes=["center"])
    X_721 = isogonal_conjugate(model, A, B, C, X_720, ID="X(721)", classes=["selected", "target"])
    return promote_point_to_top(model, X_721)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(721) on the given reference triangle."""
    model = create_model('X(721) = EVEN (- 3, 0) CIRCUMCIRCLE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00721(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00721.json"))
    write_center_svg(
        model_acute,
        here / "x-00721.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
