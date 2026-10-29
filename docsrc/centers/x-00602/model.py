"""GEOMETOR construction model for X(602) = INTERSECTION OF LINES X(3)X(31) AND X(56)X(255)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00602(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(602) = INTERSECTION OF LINES X(3)X(31) AND X(56)X(255) on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X(31)", classes=["center"])
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X(36)", classes=["center"])
    X_47 = eval_trilinear_point(model, A, B, C, 'cos(2*A)', ID="X(47)", classes=["center"])
    central_line(model, X_3, X_31, 3, 31)
    central_line(model, X_36, X_47, 36, 47)
    X_602 = intersect_lines(model, X_3, X_31, X_36, X_47, ID="X(602)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_201 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 + cos(B - C))', ID="X(201)", classes=["center", "incident"])
    central_line(model, X_1, X_201, 1, 201, incident=True)
    return promote_point_to_top(model, X_602)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(602) on the given reference triangle."""
    model = create_model('X(602) = INTERSECTION OF LINES X(3)X(31) AND X(56)X(255)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00602(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00602.json"))
    write_center_svg(
        model_acute,
        here / "x-00602.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
