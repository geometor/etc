"""GEOMETOR construction model for X_2704 = SR(X_98, X_105)."""

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


def construct_x_02704(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2704 = SR(X_98, X_105) on reference triangle ABC."""
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center"])
    X_518 = eval_trilinear_point(model, A, B, C, '(a*b + a*c - b**(2) - c**(2))', ID="X_518", classes=["center"])
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center"])
    central_line(model, X_98, X_518, 98, 518)
    central_line(model, X_105, X_511, 105, 511)
    X_2704 = intersect_lines(model, X_98, X_518, X_105, X_511, ID="X_2704", classes=["selected", "target"])
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center", "incident"])
    X_1292 = eval_trilinear_point(model, A, B, C, '1/((b - c)*(a**(2) + b**(2) + c**(2) - 2*a*b - 2*a*c))', ID="X_1292", classes=["center", "incident"])
    central_line(model, X_512, X_1292, 512, 1292, incident=True)
    return promote_point_to_top(model, X_2704)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2704 on the given reference triangle."""
    model = create_model('X_2704 = SR(X_98, X_105)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02704(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02704.json"))
    write_center_svg(
        model_acute,
        here / "x-02704.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
