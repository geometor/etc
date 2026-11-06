"""GEOMETOR construction model for X_3567 = DON QUIXOTE POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03567(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3567 = DON QUIXOTE POINT on reference triangle ABC."""
    X_3567 = eval_trilinear_point(model, A, B, C, '(a*(a**(6)*(b**(2) + c**(2)) - a**(4)*(3*b**(4) + b**(2)*c**(2) + 3*c**(4)) + 3*a**(2)*(b**(2) + c**(2))*(b**(2) - c**(2))**(2) - (b**(4) -b**(2)*c**(2) + c**(4))*(b**(2) - c**(2))**(2)))', ID="X_3567", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X_24", classes=["center", "incident"])
    central_line(model, X_6, X_24, 6, 24, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_52 = eval_trilinear_point(model, A, B, C, 'cos(2*A)*cos(B - C)', ID="X_52", classes=["center", "incident"])
    central_line(model, X_2, X_52, 2, 52, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X_51", classes=["center", "incident"])
    central_line(model, X_4, X_51, 4, 51, incident=True)
    return promote_point_to_top(model, X_3567)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3567 on the given reference triangle."""
    model = create_model('X_3567 = DON QUIXOTE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03567(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03567.json"))
    write_center_svg(
        model_acute,
        here / "x-03567.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
