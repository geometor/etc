"""GEOMETOR construction model for X_1642 = TRIPOLAR CENTROID OF X_100."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01642(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1642 = TRIPOLAR CENTROID OF X_100 on reference triangle ABC."""
    X_1642 = eval_trilinear_point(model, A, B, C, '(a*b + a*c - b**(2) - c**(2))*(2*a**(3) - 2*a**(2)*(b + c) + a*(b**(2) + c**(2)) - (b - c)**(2)*(b + c))', ID="X_1642", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_241 = eval_trilinear_point(model, A, B, C, '(cos(B/2))**(4) - ((cos(A/2))**(2))*((cos(B/2))**(2) +(cos(C/2))**(2)) + (cos(C/2))**(4)', ID="X_241", classes=["center", "incident"])
    X_1025 = eval_trilinear_point(model, A, B, C, '((b**(2) + c**(2) - a*(b + c))/((b - c)*(b + c - a)))', ID="X_1025", classes=["center", "incident"])
    central_line(model, X_241, X_1025, 241, 1025, incident=True)
    return promote_point_to_top(model, X_1642)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1642 on the given reference triangle."""
    model = create_model('X_1642 = TRIPOLAR CENTROID OF X_100')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01642(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01642.json"))
    write_center_svg(
        model_acute,
        here / "x-01642.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
