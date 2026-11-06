"""GEOMETOR construction model for X_3791 = X_2887com[T(-bc, b²)]."""

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
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03791(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3791 = X_2887com[T(-bc, b²)] on reference triangle ABC."""
    X_3791 = eval_barycentric_point(model, A, B, C, '2*a**(3)+(b+c)*a**(2)-b*c*(b+c)', ID="X_3791", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_333 = eval_trilinear_point(model, A, B, C, 'b*c*(b + c - a)/(b + c)', ID="X_333", classes=["center", "incident"])
    central_line(model, X_1, X_333, 1, 333, incident=True)
    X_171 = eval_trilinear_point(model, A, B, C, 'a**(2) + b*c', ID="X_171", classes=["center", "incident"])
    X_239 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) - b*c)', ID="X_239", classes=["center", "incident"])
    central_line(model, X_171, X_239, 171, 239, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_740 = eval_trilinear_point(model, A, B, C, 'a **(-2)*(b**(1) + c**(1)) - a**(0)*(b **(-1) + c **(-1))', ID="X_740", classes=["center", "incident"])
    central_line(model, X_31, X_740, 31, 740, incident=True)
    return promote_point_to_top(model, X_3791)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3791 on the given reference triangle."""
    model = create_model('X_3791 = X_2887com[T(-bc, b²)]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03791(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03791.json"))
    write_center_svg(
        model_acute,
        here / "x-03791.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
