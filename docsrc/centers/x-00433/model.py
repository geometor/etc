"""GEOMETOR construction model for X(433) = EULER X(159)-6th-SUBSTITUTION POINT."""

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


def construct_x_00433(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(433) = EULER X(159)-6th-SUBSTITUTION POINT on reference triangle ABC."""
    X_433 = eval_barycentric_point(model, A, B, C, '(a**(2) + b**(2) - c**(2))*(a**(2) - b**(2) + c**(2))*(a**(12)*b**(2) + 2*a**(10)*b**(4) - a**(8)*b**(6) - 4*a**(6)*b**(8) - a**(4)*b**(10) + 2*a**(2)*b**(12) + b**(14) + a**(12)*c**(2) - 4*a**(10)*b**(2)*c**(2) + a**(8)*b**(4)*c**(2) + 8*a**(6)*b**(6)*c**(2) - 5*a**(4)*b**(8)*c**(2) - 4*a**(2)*b**(10)*c**(2) + 3*b**(12)*c**(2) + 2*a**(10)*c**(4) + a**(8)*b**(2)*c**(4) - 8*a**(6)*b**(4)*c**(4) + 6*a**(4)*b**(6)*c**(4) - 2*a**(2)*b**(8)*c**(4) + b**(10)*c**(4) - a**(8)*c**(6) + 8*a**(6)*b**(2)*c**(6) + 6*a**(4)*b**(4)*c**(6) + 8*a**(2)*b**(6)*c**(6) - 5*b**(8)*c**(6) - 4*a**(6)*c**(8) - 5*a**(4)*b**(2)*c**(8) - 2*a**(2)*b**(4)*c**(8) - 5*b**(6)*c**(8) - a**(4)*c**(10) - 4*a**(2)*b**(2)*c**(10) + b**(4)*c**(10) + 2*a**(2)*c**(12) + 3*b**(2)*c**(12) + c**(14))', ID="X(433)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    return promote_point_to_top(model, X_433)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(433) on the given reference triangle."""
    model = create_model('X(433) = EULER X(159)-6th-SUBSTITUTION POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00433(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00433.json"))
    write_center_svg(
        model_acute,
        here / "x-00433.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
