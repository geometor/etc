"""GEOMETOR construction model for X(379) = EULER LINE INTERCEPT OF LINE X(6)X(7)."""

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
    gergonne_point_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00379(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(379) = EULER LINE INTERCEPT OF LINE X(6)X(7) on reference triangle ABC."""
    X_379 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(5)+ (b + c)*(b*c*a**(2)- (b*c + c*a + a*b)*(b - c)**(2)))', ID="X(379)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    central_line(model, X_6, X_7, 6, 7, incident=True)
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X(63)", classes=["center", "incident"])
    X_169 = eval_trilinear_point(model, A, B, C, '- (sin(A))*(cos(A/2))**(2) + (sin(B))*(cos(B/2))**(2) + (sin(C))*(cos(C/2))**(2)', ID="X(169)", classes=["center", "incident"])
    central_line(model, X_63, X_169, 63, 169, incident=True)
    return promote_point_to_top(model, X_379)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(379) on the given reference triangle."""
    model = create_model('X(379) = EULER LINE INTERCEPT OF LINE X(6)X(7)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00379(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00379.json"))
    write_center_svg(
        model_acute,
        here / "x-00379.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
