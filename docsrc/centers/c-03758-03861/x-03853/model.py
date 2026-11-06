"""GEOMETOR construction model for X_3853 = X_3627com(EULER TRIANGLE)."""

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
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03853(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3853 = X_3627com(EULER TRIANGLE) on reference triangle ABC."""
    X_3853 = eval_barycentric_point(model, A, B, C, '(6*a**(4) - 5*b**(4) - 5*c**(4) - a**(2)*b**(2) - a**(2)*c**(2) + 10*b**(2)*c**(2))', ID="X_3853", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_1327 = eval_trilinear_point(model, A, B, C, '(1/(sin(A) + 3*cos(A)))', ID="X_1327", classes=["center", "incident"])
    X_3592 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) + c**(2) - a**(2) + 6*area ))', ID="X_3592", classes=["center", "incident"])
    central_line(model, X_1327, X_3592, 1327, 3592, incident=True)
    X_1328 = eval_trilinear_point(model, A, B, C, '1/(sin(A) - 3*cos(A))', ID="X_1328", classes=["center", "incident"])
    X_3594 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) + c**(2) - a**(2) - 6*area ))', ID="X_3594", classes=["center", "incident"])
    central_line(model, X_1328, X_3594, 1328, 3594, incident=True)
    return promote_point_to_top(model, X_3853)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3853 on the given reference triangle."""
    model = create_model('X_3853 = X_3627com(EULER TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03853(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03853.json"))
    write_center_svg(
        model_acute,
        here / "x-03853.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
