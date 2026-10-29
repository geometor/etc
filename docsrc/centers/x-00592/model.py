"""GEOMETOR construction model for X(592) = VAN LAMOEN CIRCUMCENTERS POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00592(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(592) = VAN LAMOEN CIRCUMCENTERS POINT on reference triangle ABC."""
    X_592 = eval_trilinear_point(model, A, B, C, '1/(cos(A) + 2*cos(B - omega)*cos(C - omega))', ID="X(592)", classes=["selected", "target"])
    return promote_point_to_top(model, X_592)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(592) on the given reference triangle."""
    model = create_model('X(592) = VAN LAMOEN CIRCUMCENTERS POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00592(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00592.json"))
    write_center_svg(
        model_acute,
        here / "x-00592.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
