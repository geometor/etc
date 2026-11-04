"""GEOMETOR construction model for X_2722 = SR(X_100, X_112)."""

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


def construct_x_02722(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2722 = SR(X_100, X_112) on reference triangle ABC."""
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center"])
    X_525 = eval_trilinear_point(model, A, B, C, '(b*cos(B) - c*cos(C))/a', ID="X_525", classes=["center"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center"])
    central_line(model, X_100, X_525, 100, 525)
    central_line(model, X_112, X_513, 112, 513)
    X_2722 = intersect_lines(model, X_100, X_525, X_112, X_513, ID="X_2722", classes=["selected", "target"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    X_656 = eval_trilinear_point(model, A, B, C, 'tan(B) - tan(C)', ID="X_656", classes=["center", "incident"])
    central_line(model, X_101, X_656, 101, 656, incident=True)
    return promote_point_to_top(model, X_2722)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2722 on the given reference triangle."""
    model = create_model('X_2722 = SR(X_100, X_112)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02722(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02722.json"))
    write_center_svg(
        model_acute,
        here / "x-02722.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
