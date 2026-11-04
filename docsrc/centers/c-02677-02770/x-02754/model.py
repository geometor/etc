"""GEOMETOR construction model for X_2754 = SR(X_105, X_112)."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02754(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2754 = SR(X_105, X_112) on reference triangle ABC."""
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center"])
    X_525 = eval_trilinear_point(model, A, B, C, '(b*cos(B) - c*cos(C))/a', ID="X_525", classes=["center"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center"])
    X_518 = eval_trilinear_point(model, A, B, C, '(a*b + a*c - b**(2) - c**(2))', ID="X_518", classes=["center"])
    central_line(model, X_105, X_525, 105, 525)
    central_line(model, X_112, X_518, 112, 518)
    X_2754 = intersect_lines(model, X_105, X_525, X_112, X_518, ID="X_2754", classes=["selected", "target"])
    X_72 = eval_trilinear_point(model, A, B, C, '(b + c)*cot(A)', ID="X_72", classes=["center", "incident"])
    X_919 = point_from_barycentrics(model, A, B, C, -0.11560694, 0.83236994, 0.28323699, ID="X_919", classes=["center", "incident"])
    central_line(model, X_72, X_919, 72, 919, incident=True)
    return promote_point_to_top(model, X_2754)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2754 on the given reference triangle."""
    model = create_model('X_2754 = SR(X_105, X_112)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02754(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02754.json"))
    write_center_svg(
        model_acute,
        here / "x-02754.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
