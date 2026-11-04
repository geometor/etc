"""GEOMETOR construction model for X_2760 = SR(X_106, X_112)."""

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


def construct_x_02760(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2760 = SR(X_106, X_112) on reference triangle ABC."""
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X_106", classes=["center"])
    X_525 = eval_trilinear_point(model, A, B, C, '(b*cos(B) - c*cos(C))/a', ID="X_525", classes=["center"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center"])
    X_519 = eval_trilinear_point(model, A, B, C, '(2*a - b - c)/a', ID="X_519", classes=["center"])
    central_line(model, X_106, X_525, 106, 525)
    central_line(model, X_112, X_519, 112, 519)
    X_2760 = intersect_lines(model, X_106, X_525, X_112, X_519, ID="X_2760", classes=["selected", "target"])
    X_306 = eval_trilinear_point(model, A, B, C, '(b**(2)*c**(2))*(b + c)*cos(A)', ID="X_306", classes=["center", "incident"])
    X_901 = eval_trilinear_point(model, A, B, C, 'a/((b - c)*(b + c - 2*a))', ID="X_901", classes=["center", "incident"])
    central_line(model, X_306, X_901, 306, 901, incident=True)
    return promote_point_to_top(model, X_2760)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2760 on the given reference triangle."""
    model = create_model('X_2760 = SR(X_106, X_112)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02760(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02760.json"))
    write_center_svg(
        model_acute,
        here / "x-02760.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
