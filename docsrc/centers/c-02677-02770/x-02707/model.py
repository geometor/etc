"""GEOMETOR construction model for X_2707 = SR(X_98, X_108)."""

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
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02707(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2707 = SR(X_98, X_108) on reference triangle ABC."""
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X_107", classes=["center"])
    X_425 = eval_barycentric_point(model, A, B, C, '(a + b) * (a + c) * (a**(2) + b**(2) - c**(2)) * (a**(2) - b**(2) + c**(2)) * (a**(6) - a**(5)*b - a**(4)*b**(2) + a**(3)*b**(3) - a**(5)*c + a**(4)*b*c + a**(3)*b**(2)*c - b**(5)*c - a**(4)*c**(2) + a**(3)*b*c**(2) + 2*a**(2)*b**(2)*c**(2) - 2*a*b**(3)*c**(2) + a**(3)*c**(3) - 2*a*b**(2)*c**(3) + 2*b**(3)*c**(3) - b*c**(5))', ID="X_425", classes=["center"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center"])
    X_521 = eval_trilinear_point(model, A, B, C, '(sec(B) - sec(C))*(csc(A))', ID="X_521", classes=["center"])
    central_line(model, X_107, X_425, 107, 425)
    central_line(model, X_98, X_521, 98, 521)
    X_2707 = intersect_lines(model, X_107, X_425, X_98, X_521, ID="X_2707", classes=["selected", "target"])
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_108, X_511, 108, 511, incident=True)
    return promote_point_to_top(model, X_2707)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2707 on the given reference triangle."""
    model = create_model('X_2707 = SR(X_98, X_108)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02707(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02707.json"))
    write_center_svg(
        model_acute,
        here / "x-02707.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
