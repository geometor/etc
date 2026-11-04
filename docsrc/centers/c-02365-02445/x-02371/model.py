"""GEOMETOR construction model for X_2371 = CIR(X_57)."""

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
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02371(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2371 = CIR(X_57) on reference triangle ABC."""
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center"])
    X_220 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)**(2)', ID="X_220", classes=["center"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center"])
    X_480 = eval_trilinear_point(model, A, B, C, '(cot(A/2)*cos(A/2))**(2)', ID="X_480", classes=["center"])
    central_line(model, X_109, X_220, 109, 220)
    central_line(model, X_101, X_480, 101, 480)
    X_2371 = intersect_lines(model, X_109, X_220, X_101, X_480, ID="X_2371", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_934 = eval_trilinear_point(model, A, B, C, '1/((b - c)*(b + c - a)**(2))', ID="X_934", classes=["center", "incident"])
    central_line(model, X_9, X_934, 9, 934, incident=True)
    return promote_point_to_top(model, X_2371)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2371 on the given reference triangle."""
    model = create_model('X_2371 = CIR(X_57)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02371(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02371.json"))
    write_center_svg(
        model_acute,
        here / "x-02371.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
