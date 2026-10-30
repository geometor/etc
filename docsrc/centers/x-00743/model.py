"""GEOMETOR construction model for X(743) = EVEN (- 1, 2) CIRCUMCIRCLE POINT."""

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
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00743(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(743) = EVEN (- 1, 2) CIRCUMCIRCLE POINT on reference triangle ABC."""
    X_742 = point_from_barycentrics(model, A, B, C, 0.70747024, -0.00072747582, -0.70674276, ID="X(742)", classes=["center"])
    X_743 = isogonal_conjugate(model, A, B, C, X_742, ID="X(743)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_789 = eval_trilinear_point(model, A, B, C, 'a **(- 2)/(b**(3) - c**(3))', ID="X(789)", classes=["center", "incident"])
    central_line(model, X_2, X_789, 2, 789, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X(31)", classes=["center", "incident"])
    X_825 = eval_trilinear_point(model, A, B, C, '1/(a**(-1)*(b**(3) - c**(3)) + a**(2)*(b**(0) - c**(0)))', ID="X(825)", classes=["center", "incident"])
    central_line(model, X_31, X_825, 31, 825, incident=True)
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center", "incident"])
    X_869 = point_from_barycentrics(model, A, B, C, 0.22475648, 0.33333333, 0.44191018, ID="X(869)", classes=["center", "incident"])
    central_line(model, X_101, X_869, 101, 869, incident=True)
    return promote_point_to_top(model, X_743)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(743) on the given reference triangle."""
    model = create_model('X(743) = EVEN (- 1, 2) CIRCUMCIRCLE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00743(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00743.json"))
    write_center_svg(
        model_acute,
        here / "x-00743.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
