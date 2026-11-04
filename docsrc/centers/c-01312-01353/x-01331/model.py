"""GEOMETOR construction model for X_1331 = ORTHOCORRESPONDENT OF X_101."""

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


def construct_x_01331(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1331 = ORTHOCORRESPONDENT OF X_101 on reference triangle ABC."""
    X_1331 = eval_trilinear_point(model, A, B, C, '(cos(A))/(b - c)', ID="X_1331", classes=["selected", "target"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    central_line(model, X_100, X_109, 100, 109, incident=True)
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_101, X_110, 101, 110, incident=True)
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    X_212 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 + cos(A))', ID="X_212", classes=["center", "incident"])
    central_line(model, X_63, X_212, 63, 212, incident=True)
    return promote_point_to_top(model, X_1331)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1331 on the given reference triangle."""
    model = create_model('X_1331 = ORTHOCORRESPONDENT OF X_101')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01331(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01331.json"))
    write_center_svg(
        model_acute,
        here / "x-01331.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
