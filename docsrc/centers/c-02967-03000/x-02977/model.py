"""GEOMETOR construction model for X_2977 = RADICAL CENTER OF {CIRCUMCIRCLE, NINE-POINT CIRCLE, AC-INCIRCLE}."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02977(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2977 = RADICAL CENTER OF {CIRCUMCIRCLE, NINE-POINT CIRCLE, AC-INCIRCLE} on reference triangle ABC."""
    X_2977 = eval_trilinear_point(model, A, B, C, '(b*c*((a - b)**(2)*(c**(2) + a**(2) - b**(2)) - (a - c)**(2)*(a**(2) + b**(2) - c**(2))))', ID="X_2977", classes=["selected", "target"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X_190", classes=["center", "incident"])
    central_line(model, X_100, X_190, 100, 190, incident=True)
    X_230 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*(2*a**(2) - b**(2) - c**(2)) + (b**(2) - c**(2))**(2))', ID="X_230", classes=["center", "incident"])
    X_231 = eval_trilinear_point(model, A, B, C, '(cos(B))*(4*(sin(C))**(2) - 1)*(cos(A)*sin(B) - sin(A)*cos(B)) - (cos(C))*(4*(sin(B))**(2) - 1)*(cos(C)*sin(A) - sin(C)*cos(A))', ID="X_231", classes=["center", "incident"])
    central_line(model, X_230, X_231, 230, 231, incident=True)
    return promote_point_to_top(model, X_2977)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2977 on the given reference triangle."""
    model = create_model('X_2977 = RADICAL CENTER OF {CIRCUMCIRCLE, NINE-POINT CIRCLE, AC-INCIRCLE}')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02977(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02977.json"))
    write_center_svg(
        model_acute,
        here / "x-02977.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
