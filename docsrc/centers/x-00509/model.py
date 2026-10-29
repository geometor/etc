"""GEOMETOR construction model for X(509) = 7th ISOSCELIZER POINT."""

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


def construct_x_00509(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(509) = 7th ISOSCELIZER POINT on reference triangle ABC."""
    X_509 = eval_trilinear_point(model, A, B, C, '(tan(A/2))**(1/2)', ID="X(509)", classes=["selected", "target"])
    return promote_point_to_top(model, X_509)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(509) on the given reference triangle."""
    model = create_model('X(509) = 7th ISOSCELIZER POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00509(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00509.json"))
    write_center_svg(
        model_acute,
        here / "x-00509.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
