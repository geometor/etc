"""GEOMETOR construction model for X(323) = ISOTOMIC CONJUGATE OF X(94)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
    reflection_in_point,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00323(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(323) = ISOTOMIC CONJUGATE OF X(94) on reference triangle ABC."""
    X_23 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X(23)", classes=["center"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center"])
    X_323 = reflection_in_point(model, X_23, X_110, ID="X(323)", classes=["selected", "target"], guide=False)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    central_line(model, X_23, X_110, 23, 110, incident=True)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X(20)", classes=["center", "incident"])
    X_155 = eval_barycentric_point(model, A, B, C, 'a**(2)*(a**(2) - b**(2) - c**(2))*(a**(6) - 3*a**(4)*(b**(2) + c**(2)) + a**(2)*(3*b**(4) - 2*b**(2)*c**(2) + 3*c**(4)) - (b**(2) - c**(2))**(2)*(b**(2) + c**(2)))', ID="X(155)", classes=["center", "incident"])
    central_line(model, X_20, X_155, 20, 155, incident=True)
    return promote_point_to_top(model, X_323)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(323) on the given reference triangle."""
    model = create_model('X(323) = ISOTOMIC CONJUGATE OF X(94)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00323(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00323.json"))
    write_center_svg(
        model_acute,
        here / "x-00323.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
