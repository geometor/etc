"""GEOMETOR construction model for X(697) = EVEN (- 4, - 3) CIRCUMCIRCLE POINT."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00697(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(697) = EVEN (- 4, - 3) CIRCUMCIRCLE POINT on reference triangle ABC."""
    X_696 = point_from_barycentrics(model, A, B, C, 0.80539263, -0.28647653, -0.5189161, ID="X(696)", classes=["center"])
    X_697 = isogonal_conjugate(model, A, B, C, X_696, ID="X(697)", classes=["selected", "target"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X(100)", classes=["center", "incident"])
    X_560 = eval_trilinear_point(model, A, B, C, 'a**(4)', ID="X(560)", classes=["center", "incident"])
    central_line(model, X_100, X_560, 100, 560, incident=True)
    return promote_point_to_top(model, X_697)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(697) on the given reference triangle."""
    model = create_model('X(697) = EVEN (- 4, - 3) CIRCUMCIRCLE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00697(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00697.json"))
    write_center_svg(
        model_acute,
        here / "x-00697.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
