"""GEOMETOR construction model for X_1977 = BICENTRIC DIFFERENCE OF PU(42)."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01977(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1977 = BICENTRIC DIFFERENCE OF PU(42) on reference triangle ABC."""
    X_1977 = eval_trilinear_point(model, A, B, C, 'a**(3)*(b - c)**(2)', ID="X_1977", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    central_line(model, X_6, X_100, 6, 100, incident=True)
    X_213 = eval_trilinear_point(model, A, B, C, '(b + c)*a**(2)', ID="X_213", classes=["center", "incident"])
    X_1017 = eval_trilinear_point(model, A, B, C, 'a*(b + c - 2*a)**(2)', ID="X_1017", classes=["center", "incident"])
    central_line(model, X_213, X_1017, 213, 1017, incident=True)
    X_291 = eval_trilinear_point(model, A, B, C, '1/(a**(2) - b*c)', ID="X_291", classes=["center", "incident"])
    central_line(model, X_291, X_1017, 291, 1017, incident=True)
    return promote_point_to_top(model, X_1977)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1977 on the given reference triangle."""
    model = create_model('X_1977 = BICENTRIC DIFFERENCE OF PU(42)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01977(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01977.json"))
    write_center_svg(
        model_acute,
        here / "x-01977.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
