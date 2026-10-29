"""GEOMETOR construction model for X(644) = TRILINEAR MULTIPLIER FOR YFF PARABOLA."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00644(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(644) = TRILINEAR MULTIPLIER FOR YFF PARABOLA on reference triangle ABC."""
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X(190)", classes=["center"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X(100)", classes=["center"])
    X_644 = ceva_conjugate(model, A, B, C, X_190, X_100, ID="X(644)", classes=["selected", "target"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center", "incident"])
    central_line(model, X_100, X_101, 100, 101, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    X_220 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)**(2)', ID="X(220)", classes=["center", "incident"])
    central_line(model, X_8, X_220, 8, 220, incident=True)
    X_145 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a - b - c)', ID="X(145)", classes=["center", "incident"])
    X_218 = eval_trilinear_point(model, A, B, C, '(cos(A/2))**(2)*((cos(B/2))**(4) + (cos(C/2))**(4) - (cos(A/2))**(4))', ID="X(218)", classes=["center", "incident"])
    central_line(model, X_145, X_218, 145, 218, incident=True)
    return promote_point_to_top(model, X_644)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(644) on the given reference triangle."""
    model = create_model('X(644) = TRILINEAR MULTIPLIER FOR YFF PARABOLA')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00644(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00644.json"))
    write_center_svg(
        model_acute,
        here / "x-00644.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
