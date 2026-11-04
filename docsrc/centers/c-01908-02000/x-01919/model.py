"""GEOMETOR construction model for X_1919 = BICENTRIC DIFFERENCE OF PU(12)."""

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


def construct_x_01919(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1919 = BICENTRIC DIFFERENCE OF PU(12) on reference triangle ABC."""
    X_1919 = eval_trilinear_point(model, A, B, C, '(a**(3)*(b - c))', ID="X_1919", classes=["selected", "target"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    X_765 = eval_trilinear_point(model, A, B, C, '(b - c) **(-2)', ID="X_765", classes=["center", "incident"])
    central_line(model, X_101, X_765, 101, 765, incident=True)
    X_669 = eval_trilinear_point(model, A, B, C, 'a**(3)*(b**(2) - c**(2))', ID="X_669", classes=["center", "incident"])
    X_688 = eval_trilinear_point(model, A, B, C, '(a**(3)*(b**(4) - c**(4)))', ID="X_688", classes=["center", "incident"])
    central_line(model, X_669, X_688, 669, 688, incident=True)
    X_667 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b - c)', ID="X_667", classes=["center", "incident"])
    X_788 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b**(3) - c**(3))', ID="X_788", classes=["center", "incident"])
    central_line(model, X_667, X_788, 667, 788, incident=True)
    return promote_point_to_top(model, X_1919)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1919 on the given reference triangle."""
    model = create_model('X_1919 = BICENTRIC DIFFERENCE OF PU(12)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01919(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01919.json"))
    write_center_svg(
        model_acute,
        here / "x-01919.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
