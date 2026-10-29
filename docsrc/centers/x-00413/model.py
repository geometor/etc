"""GEOMETOR construction model for X(413) = EULER X(21)-3rd-SUBSTITUTION POINT."""

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


def construct_x_00413(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(413) = EULER X(21)-3rd-SUBSTITUTION POINT on reference triangle ABC."""
    X_413 = eval_barycentric_point(model, A, B, C, 'a*(a + b)*(a - b - c)**(3)*(a + c)*(a**(4) + a**(3)*b + a*b**(3) + b**(4) + a**(3)*c + a**(2)*b*c - a*b**(2)*c - b**(3)*c - a*b*c**(2) + a*c**(3) - b*c**(3) + c**(4))', ID="X(413)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    return promote_point_to_top(model, X_413)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(413) on the given reference triangle."""
    model = create_model('X(413) = EULER X(21)-3rd-SUBSTITUTION POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00413(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00413.json"))
    write_center_svg(
        model_acute,
        here / "x-00413.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
