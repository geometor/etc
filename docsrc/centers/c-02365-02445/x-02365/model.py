"""GEOMETOR construction model for X_2365 = CIR(X_19)."""

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


def construct_x_02365(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2365 = CIR(X_19) on reference triangle ABC."""
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center"])
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center"])
    X_283 = eval_trilinear_point(model, A, B, C, '(cos(A))/(cos(B) + cos(C))', ID="X_283", classes=["center"])
    central_line(model, X_63, X_108, 63, 108)
    central_line(model, X_112, X_283, 112, 283)
    X_2365 = intersect_lines(model, X_63, X_108, X_112, X_283, ID="X_2365", classes=["selected", "target"])
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X_107", classes=["center", "incident"])
    X_333 = eval_trilinear_point(model, A, B, C, 'b*c*(b + c - a)/(b + c)', ID="X_333", classes=["center", "incident"])
    central_line(model, X_107, X_333, 107, 333, incident=True)
    return promote_point_to_top(model, X_2365)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2365 on the given reference triangle."""
    model = create_model('X_2365 = CIR(X_19)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02365(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02365.json"))
    write_center_svg(
        model_acute,
        here / "x-02365.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
