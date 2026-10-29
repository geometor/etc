"""GEOMETOR construction model for X(432) = EULER X(155)-6th-SUBSTITUTION POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00432(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(432) = EULER X(155)-6th-SUBSTITUTION POINT on reference triangle ABC."""
    X_432 = eval_barycentric_point(model, A, B, C, '(a**(2) + b**(2) - c**(2))*(a**(2) - b**(2) + c**(2))*(a**(16)*b**(2) - 8*a**(14)*b**(4) + 28*a**(12)*b**(6) - 56*a**(10)*b**(8) + 70*a**(8)*b**(10) - 56*a**(6)*b**(12) + 28*a**(4)*b**(14) - 8*a**(2)*b**(16) + b**(18) + a**(16)*c**(2) - 4*a**(12)*b**(4)*c**(2) + 8*a**(10)*b**(6)*c**(2) - 34*a**(8)*b**(8)*c**(2) + 80*a**(6)*b**(10)*c**(2) - 84*a**(4)*b**(12)*c**(2) + 40*a**(2)*b**(14)*c**(2) - 7*b**(16)*c**(2) - 8*a**(14)*c**(4) - 4*a**(12)*b**(2)*c**(4) + 32*a**(10)*b**(4)*c**(4) - 20*a**(8)*b**(6)*c**(4) - 40*a**(6)*b**(8)*c**(4) + 100*a**(4)*b**(10)*c**(4) - 80*a**(2)*b**(12)*c**(4) + 20*b**(14)*c**(4) + 28*a**(12)*c**(6) + 8*a**(10)*b**(2)*c**(6) - 20*a**(8)*b**(4)*c**(6) + 32*a**(6)*b**(6)*c**(6) - 44*a**(4)*b**(8)*c**(6) + 88*a**(2)*b**(10)*c**(6) - 28*b**(12)*c**(6) - 56*a**(10)*c**(8) - 34*a**(8)*b**(2)*c**(8) - 40*a**(6)*b**(4)*c**(8) - 44*a**(4)*b**(6)*c**(8) - 80*a**(2)*b**(8)*c**(8) + 14*b**(10)*c**(8) + 70*a**(8)*c**(10) + 80*a**(6)*b**(2)*c**(10) + 100*a**(4)*b**(4)*c**(10) + 88*a**(2)*b**(6)*c**(10) + 14*b**(8)*c**(10) - 56*a**(6)*c**(12) - 84*a**(4)*b**(2)*c**(12) - 80*a**(2)*b**(4)*c**(12) - 28*b**(6)*c**(12) + 28*a**(4)*c**(14) + 40*a**(2)*b**(2)*c**(14) + 20*b**(4)*c**(14) - 8*a**(2)*c**(16) - 7*b**(2)*c**(16) + c**(18))', ID="X(432)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    return promote_point_to_top(model, X_432)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(432) on the given reference triangle."""
    model = create_model('X(432) = EULER X(155)-6th-SUBSTITUTION POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00432(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00432.json"))
    write_center_svg(
        model_acute,
        here / "x-00432.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
