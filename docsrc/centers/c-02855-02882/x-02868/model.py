"""GEOMETOR construction model for X_2868 = SM(X_110, X_111)."""

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


def construct_x_02868(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2868 = SM(X_110, X_111) on reference triangle ABC."""
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center"])
    X_385 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(4) - b**(2)*c**(2))', ID="X_385", classes=["center"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center"])
    X_691 = eval_trilinear_point(model, A, B, C, 'a/((b**(2) - c**(2))*(2*a**(2) - b**(2) - c**(2)))', ID="X_691", classes=["center"])
    central_line(model, X_112, X_385, 112, 385)
    central_line(model, X_76, X_691, 76, 691)
    X_2868 = intersect_lines(model, X_112, X_385, X_76, X_691, ID="X_2868", classes=["selected", "target"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    X_805 = eval_trilinear_point(model, A, B, C, '(1/(a **(-3)*(b**(2) - c**(2)) + a**(1)*(b **(-2) - c **(-2))))', ID="X_805", classes=["center", "incident"])
    central_line(model, X_69, X_805, 69, 805, incident=True)
    return promote_point_to_top(model, X_2868)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2868 on the given reference triangle."""
    model = create_model('X_2868 = SM(X_110, X_111)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02868(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02868.json"))
    write_center_svg(
        model_acute,
        here / "x-02868.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
