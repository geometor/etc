"""GEOMETOR construction model for X(613) = INTERSECTION OF LINES X(1)X(6) AND X(56)X(511)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00613(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(613) = INTERSECTION OF LINES X(1)X(6) AND X(56)X(511) on reference triangle ABC."""
    X_613 = eval_trilinear_point(model, A, B, C, 'a*(S**(2) - b*c*SW)', ID="X(613)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X(55)", classes=["center", "incident"])
    X_182 = eval_trilinear_point(model, A, B, C, 'cos(A- omega )', ID="X(182)", classes=["center", "incident"])
    central_line(model, X_55, X_182, 55, 182, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X(56)", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X(511)", classes=["center", "incident"])
    central_line(model, X_56, X_511, 56, 511, incident=True)
    return promote_point_to_top(model, X_613)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(613) on the given reference triangle."""
    model = create_model('X(613) = INTERSECTION OF LINES X(1)X(6) AND X(56)X(511)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00613(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00613.json"))
    write_center_svg(
        model_acute,
        here / "x-00613.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
