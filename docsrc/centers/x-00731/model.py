"""GEOMETOR construction model for X(731) = EVEN (- 2, 1) CIRCUMCIRCLE POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00731(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(731) = EVEN (- 2, 1) CIRCUMCIRCLE POINT on reference triangle ABC."""
    X_730 = point_from_barycentrics(model, A, B, C, 0.74265678, -0.077482027, -0.66517475, ID="X(730)", classes=["center"])
    X_731 = isogonal_conjugate(model, A, B, C, X_730, ID="X(731)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_789 = eval_trilinear_point(model, A, B, C, 'a **(- 2)/(b**(3) - c**(3))', ID="X(789)", classes=["center", "incident"])
    central_line(model, X_1, X_789, 1, 789, incident=True)
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X(32)", classes=["center", "incident"])
    X_825 = eval_trilinear_point(model, A, B, C, '1/(a**(-1)*(b**(3) - c**(3)) + a**(2)*(b**(0) - c**(0)))', ID="X(825)", classes=["center", "incident"])
    central_line(model, X_32, X_825, 32, 825, incident=True)
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X(100)", classes=["center", "incident"])
    X_869 = point_from_barycentrics(model, A, B, C, 0.22475648, 0.33333333, 0.44191018, ID="X(869)", classes=["center", "incident"])
    central_line(model, X_100, X_869, 100, 869, incident=True)
    return promote_point_to_top(model, X_731)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(731) on the given reference triangle."""
    model = create_model('X(731) = EVEN (- 2, 1) CIRCUMCIRCLE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00731(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00731.json"))
    write_center_svg(
        model_acute,
        here / "x-00731.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
