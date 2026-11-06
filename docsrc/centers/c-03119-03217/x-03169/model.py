"""GEOMETOR construction model for X_3169 = X_6-CEVA CONJUGATE OF X_9."""

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
    nagel_point_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03169(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3169 = X_6-CEVA CONJUGATE OF X_9 on reference triangle ABC."""
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center"])
    X_604 = eval_trilinear_point(model, A, B, C, 'a*(1 - cos(A))', ID="X_604", classes=["center"])
    central_line(model, X_8, X_9, 8, 9)
    central_line(model, X_100, X_604, 100, 604)
    X_3169 = intersect_lines(model, X_8, X_9, X_100, X_604, ID="X_3169", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_979 = eval_trilinear_point(model, A, B, C, '(1/(a**(2)*(b + c) + a*(b**(2) - b*c + c**(2)) - b*c*(b + c)))', ID="X_979", classes=["center", "incident"])
    central_line(model, X_6, X_979, 6, 979, incident=True)
    return promote_point_to_top(model, X_3169)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3169 on the given reference triangle."""
    model = create_model('X_3169 = X_6-CEVA CONJUGATE OF X_9')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03169(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03169.json"))
    write_center_svg(
        model_acute,
        here / "x-03169.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
