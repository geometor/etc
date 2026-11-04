"""GEOMETOR construction model for X_2370 = CIR(X_56)."""

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
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02370(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2370 = CIR(X_56) on reference triangle ABC."""
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center"])
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center"])
    X_318 = eval_trilinear_point(model, A, B, C, '(1 + sec(A))/a**(2)', ID="X_318", classes=["center"])
    central_line(model, X_8, X_109, 8, 109)
    central_line(model, X_108, X_318, 108, 318)
    X_2370 = intersect_lines(model, X_8, X_109, X_108, X_318, ID="X_2370", classes=["selected", "target"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_341 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*(b + c - a)**(2)', ID="X_341", classes=["center", "incident"])
    central_line(model, X_100, X_341, 100, 341, incident=True)
    return promote_point_to_top(model, X_2370)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2370 on the given reference triangle."""
    model = create_model('X_2370 = CIR(X_56)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02370(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02370.json"))
    write_center_svg(
        model_acute,
        here / "x-02370.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
