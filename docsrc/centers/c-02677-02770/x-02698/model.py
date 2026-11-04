"""GEOMETOR construction model for X_2698 = SR(X_98, X_99)."""

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


def construct_x_02698(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2698 = SR(X_98, X_99) on reference triangle ABC."""
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center"])
    X_237 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A +  omega  )', ID="X_237", classes=["center"])
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X_107", classes=["center"])
    X_419 = eval_barycentric_point(model, A, B, C, '(a**(2) - b*c) * (a**(2) + b*c) * (a**(2) + b**(2) - c**(2)) * (a**(2) - b**(2) + c**(2))', ID="X_419", classes=["center"])
    central_line(model, X_110, X_237, 110, 237)
    central_line(model, X_107, X_419, 107, 419)
    X_2698 = intersect_lines(model, X_110, X_237, X_107, X_419, ID="X_2698", classes=["selected", "target"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center", "incident"])
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center", "incident"])
    central_line(model, X_98, X_512, 98, 512, incident=True)
    return promote_point_to_top(model, X_2698)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2698 on the given reference triangle."""
    model = create_model('X_2698 = SR(X_98, X_99)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02698(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02698.json"))
    write_center_svg(
        model_acute,
        here / "x-02698.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
