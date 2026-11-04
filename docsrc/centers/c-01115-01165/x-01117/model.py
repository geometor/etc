"""GEOMETOR construction model for X_1117 = POINT ALRESCHA."""

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


def construct_x_01117(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1117 = POINT ALRESCHA on reference triangle ABC."""
    X_1117 = eval_barycentric_point(model, A, B, C, '(a**(2)-a*b+b**(2)-c**(2))*(a**(2)+a*b+b**(2)-c**(2))*(a**(2)-b**(2)-a*c+c**(2))*(a**(2)-b**(2)+a*c+c**(2))*(a**(6)-a**(4)*b**(2)-a**(2)*b**(4)+b**(6)-3*a**(4)*c**(2)+a**(2)*b**(2)*c**(2)-3*b**(4)*c**(2)+3*a**(2)*c**(4)+3*b**(2)*c**(4)-c**(6))*(a**(6)-3*a**(4)*b**(2)+3*a**(2)*b**(4)-b**(6)-a**(4)*c**(2)+a**(2)*b**(2)*c**(2)+3*b**(4)*c**(2)-a**(2)*c**(4)-3*b**(2)*c**(4)+c**(6))*(a**(8)-4*a**(6)*b**(2)+6*a**(4)*b**(4)-4*a**(2)*b**(6)+b**(8)-4*a**(6)*c**(2)+a**(4)*b**(2)*c**(2)+a**(2)*b**(4)*c**(2)+2*b**(6)*c**(2)+6*a**(4)*c**(4)+a**(2)*b**(2)*c**(4)-6*b**(4)*c**(4)-4*a**(2)*c**(6)+2*b**(2)*c**(6)+c**(8))', ID="X_1117", classes=["selected", "target"])
    return promote_point_to_top(model, X_1117)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1117 on the given reference triangle."""
    model = create_model('X_1117 = POINT ALRESCHA')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01117(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01117.json"))
    write_center_svg(
        model_acute,
        here / "x-01117.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
