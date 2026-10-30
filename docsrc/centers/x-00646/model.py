"""GEOMETOR construction model for X(646) = BARYCENTRIC MULTIPLIER FOR YFF PARABOLA."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00646(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(646) = BARYCENTRIC MULTIPLIER FOR YFF PARABOLA on reference triangle ABC."""
    X_644 = point_from_barycentrics(model, A, B, C, 0.8, -0.36, 0.56, ID="X(644)", classes=["center"])
    X_645 = point_from_barycentrics(model, A, B, C, 0.8441247, -0.34292566, 0.49880096, ID="X(645)", classes=["center"])
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X(190)", classes=["center"])
    X_668 = eval_trilinear_point(model, A, B, C, '1/(a**(2)*(b - c))', ID="X(668)", classes=["center"])
    central_line(model, X_644, X_645, 644, 645)
    central_line(model, X_190, X_668, 190, 668)
    X_646 = intersect_lines(model, X_644, X_645, X_190, X_668, ID="X(646)", classes=["selected", "target"])
    return promote_point_to_top(model, X_646)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(646) on the given reference triangle."""
    model = create_model('X(646) = BARYCENTRIC MULTIPLIER FOR YFF PARABOLA')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00646(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00646.json"))
    write_center_svg(
        model_acute,
        here / "x-00646.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
