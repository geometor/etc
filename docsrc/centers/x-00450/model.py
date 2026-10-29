"""GEOMETOR construction model for X(450) = X(3)-HIRST INVERSE OF X(4)."""

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


def construct_x_00450(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(450) = X(3)-HIRST INVERSE OF X(4) on reference triangle ABC."""
    X_450 = eval_barycentric_point(model, A, B, C, '(a**(2) + b**(2) - c**(2))*(a**(2) - b**(2) + c**(2))*(a**(4) - a**(2)*b**(2) + a**(2)*b*c - b**(3)*c - a**(2)*c**(2) + 2*b**(2)*c**(2) - b*c**(3))*(a**(4) - a**(2)*b**(2) - a**(2)*b*c + b**(3)*c - a**(2)*c**(2) + 2*b**(2)*c**(2) + b*c**(3))', ID="X(450)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X(107)", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X(511)", classes=["center", "incident"])
    central_line(model, X_107, X_511, 107, 511, incident=True)
    return promote_point_to_top(model, X_450)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(450) on the given reference triangle."""
    model = create_model('X(450) = X(3)-HIRST INVERSE OF X(4)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00450(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00450.json"))
    write_center_svg(
        model_acute,
        here / "x-00450.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
