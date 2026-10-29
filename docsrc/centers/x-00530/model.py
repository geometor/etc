"""GEOMETOR construction model for X(530) = DIRECTION OF VECTOR AX + BX + CX, where X = X(13)."""

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
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00530(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(530) = DIRECTION OF VECTOR AX + BX + CX, where X = X(13) on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A + pi /3)', ID="X(13)", classes=["center"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center"])
    X_299 = eval_barycentric_point(model, A, B, C, 'csc(A)*sin(A - pi /3)', ID="X(299)", classes=["center"])
    central_line(model, X_2, X_13, 2, 13)
    central_line(model, X_99, X_299, 99, 299)
    X_530 = intersect_lines(model, X_2, X_13, X_99, X_299, ID="X(530)", classes=["selected", "target"])
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X(115)", classes=["center", "incident"])
    X_395 = eval_trilinear_point(model, A, B, C, 'cos(B - C) + 2*cos(A + pi /3)', ID="X(395)", classes=["center", "incident"])
    central_line(model, X_115, X_395, 115, 395, incident=True)
    return promote_point_to_top(model, X_530)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(530) on the given reference triangle."""
    model = create_model('X(530) = DIRECTION OF VECTOR AX + BX + CX, where X = X(13)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00530(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00530.json"))
    write_center_svg(
        model_acute,
        here / "x-00530.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
