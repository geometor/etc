"""GEOMETOR construction model for X(665) = CROSSDIFFERENCE OF X(2) AND X(11)."""

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


def construct_x_00665(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(665) = CROSSDIFFERENCE OF X(2) AND X(11) on reference triangle ABC."""
    X_665 = eval_trilinear_point(model, A, B, C, 'a*((a - b)**(2)*(a + b - c) - (c - a)**(2)*(c + a - b))', ID="X(665)", classes=["selected", "target"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center", "incident"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X(109)", classes=["center", "incident"])
    central_line(model, X_101, X_109, 101, 109, incident=True)
    X_187 = eval_trilinear_point(model, A, B, C, 'a*(2*a**(2) - b**(2) - c**(2))', ID="X(187)", classes=["center", "incident"])
    X_237 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A + omega )', ID="X(237)", classes=["center", "incident"])
    central_line(model, X_187, X_237, 187, 237, incident=True)
    X_241 = eval_trilinear_point(model, A, B, C, '(b**(2) + c**(2) - a*b - a*c)/(a - b - c)', ID="X(241)", classes=["center", "incident"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X(514)", classes=["center", "incident"])
    central_line(model, X_241, X_514, 241, 514, incident=True)
    return promote_point_to_top(model, X_665)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(665) on the given reference triangle."""
    model = create_model('X(665) = CROSSDIFFERENCE OF X(2) AND X(11)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00665(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00665.json"))
    write_center_svg(
        model_acute,
        here / "x-00665.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
