"""GEOMETOR construction model for X_2859 = SM(X_100, X_112)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02859(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2859 = SM(X_100, X_112) on reference triangle ABC."""
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center"])
    X_693 = eval_trilinear_point(model, A, B, C, '(b - c)/a**(2)', ID="X_693", classes=["center"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center"])
    X_3267 = eval_trilinear_point(model, A, B, C, '((b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))/a**(3))', ID="X_3267", classes=["center"])
    central_line(model, X_112, X_693, 112, 693)
    central_line(model, X_100, X_3267, 100, 3267)
    X_2859 = intersect_lines(model, X_112, X_693, X_100, X_3267, ID="X_2859", classes=["selected", "target"])
    return promote_point_to_top(model, X_2859)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2859 on the given reference triangle."""
    model = create_model('X_2859 = SM(X_100, X_112)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02859(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02859.json"))
    write_center_svg(
        model_acute,
        here / "x-02859.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
