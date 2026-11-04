"""GEOMETOR construction model for X_1638 = TRIPOLAR CENTROID OF X_7."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    feuerbach_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01638(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1638 = TRIPOLAR CENTROID OF X_7 on reference triangle ABC."""
    X_1638 = eval_barycentric_point(model, A, B, C, '(b - c)*(2*a**(2) - b**(2) - c**(2) - a*b - a*c + 2*b*c)', ID="X_1638", classes=["selected", "target"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_244 = eval_trilinear_point(model, A, B, C, '(b - c)**(2)', ID="X_244", classes=["center", "incident"])
    central_line(model, X_11, X_244, 11, 244, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_654 = eval_trilinear_point(model, A, B, C, 'cos(A - B) - cos(C - A)', ID="X_654", classes=["center", "incident"])
    central_line(model, X_57, X_654, 57, 654, incident=True)
    X_241 = eval_trilinear_point(model, A, B, C, '(cos(B/2))**(4) - ((cos(A/2))**(2))*((cos(B/2))**(2) +(cos(C/2))**(2)) + (cos(C/2))**(4)', ID="X_241", classes=["center", "incident"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center", "incident"])
    central_line(model, X_241, X_514, 241, 514, incident=True)
    return promote_point_to_top(model, X_1638)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1638 on the given reference triangle."""
    model = create_model('X_1638 = TRIPOLAR CENTROID OF X_7')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01638(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01638.json"))
    write_center_svg(
        model_acute,
        here / "x-01638.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
