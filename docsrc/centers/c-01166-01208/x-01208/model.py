"""GEOMETOR construction model for X_1208 = 3rd SARAGOSSA POINT OF X_84."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01208(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1208 = 3rd SARAGOSSA POINT OF X_84 on reference triangle ABC."""
    X_84 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C) - cos(A) - 1)', ID="X_84", classes=["center"])
    X_947 = eval_trilinear_point(model, A, B, C, '(a/(a**(3)*(b + c) + (b - c)**(2)*(a**(2) - a*b - a*c - b**(2) - c**(2) - 2*b*c)))', ID="X_947", classes=["center"])
    X_1208 = crosspoint(model, A, B, C, X_84, X_947, ID="X_1208", classes=["selected", "target"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X_64", classes=["center", "incident"])
    central_line(model, X_56, X_64, 56, 64, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_963 = eval_trilinear_point(model, A, B, C, 'a/(a**(4) + 2*a**(3)*(b + c) - 4*a**(2)*b*c - (b + c)*(b - c)**(2)*(2*a + b + c))', ID="X_963", classes=["center", "incident"])
    central_line(model, X_6, X_963, 6, 963, incident=True)
    return promote_point_to_top(model, X_1208)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1208 on the given reference triangle."""
    model = create_model('X_1208 = 3rd SARAGOSSA POINT OF X_84')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01208(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01208.json"))
    write_center_svg(
        model_acute,
        here / "x-01208.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
