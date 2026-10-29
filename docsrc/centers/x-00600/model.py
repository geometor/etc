"""GEOMETOR construction model for X(600) = 3rd HATZIPOLAKIS-YIU POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00600(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(600) = 3rd HATZIPOLAKIS-YIU POINT on reference triangle ABC."""
    X_600 = eval_barycentric_point(model, A, B, C, 'a**(2)*(b*c + 2*S)*(a*b*c*(b + c - a) + 2*(b**(2)+ c**(2)- a**(2))*S)', ID="X(600)", classes=["selected", "target"])
    return promote_point_to_top(model, X_600)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(600) on the given reference triangle."""
    model = create_model('X(600) = 3rd HATZIPOLAKIS-YIU POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00600(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00600.json"))
    write_center_svg(
        model_acute,
        here / "x-00600.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
