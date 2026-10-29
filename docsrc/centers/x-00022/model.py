"""GEOMETOR construction model for X(22) = EXETER POINT."""

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
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00022(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(22) = EXETER POINT on reference triangle ABC."""
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X(22)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X(69)", classes=["center", "incident"])
    X_159 = eval_trilinear_point(model, A, B, C, 'a*((a**(2)+ b**(2)+ c**(2))*sin(2*A) + (c**(2)- b**(2)- a**(2))*sin(2*B) + (b**(2)- c**(2)- a**(2))*sin(2*C))', ID="X(159)", classes=["center", "incident"])
    central_line(model, X_69, X_159, 69, 159, incident=True)
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X(51)", classes=["center", "incident"])
    X_182 = eval_trilinear_point(model, A, B, C, 'cos(A- omega )', ID="X(182)", classes=["center", "incident"])
    central_line(model, X_51, X_182, 51, 182, incident=True)
    return promote_point_to_top(model, X_22)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(22) on the given reference triangle."""
    model = create_model('X(22) = EXETER POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00022(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00022.json"))
    write_center_svg(
        model_acute,
        here / "x-00022.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
