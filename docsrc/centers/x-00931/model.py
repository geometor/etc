"""GEOMETOR construction model for X(931) = POINT ALCHIBA."""

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


def construct_x_00931(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(931) = POINT ALCHIBA on reference triangle ABC."""
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center"])
    X_643 = point_from_barycentrics(model, A, B, C, 0.74639525, -0.36386768, 0.61747243, ID="X(643)", classes=["center"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X(100)", classes=["center"])
    X_645 = point_from_barycentrics(model, A, B, C, 0.8441247, -0.34292566, 0.49880096, ID="X(645)", classes=["center"])
    central_line(model, X_101, X_643, 101, 643)
    central_line(model, X_100, X_645, 100, 645)
    X_931 = intersect_lines(model, X_101, X_643, X_100, X_645, ID="X(931)", classes=["selected", "target"])
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X(108)", classes=["center", "incident"])
    X_648 = eval_trilinear_point(model, A, B, C, '1/(a*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2)))', ID="X(648)", classes=["center", "incident"])
    central_line(model, X_108, X_648, 108, 648, incident=True)
    return promote_point_to_top(model, X_931)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(931) on the given reference triangle."""
    model = create_model('X(931) = POINT ALCHIBA')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00931(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00931.json"))
    write_center_svg(
        model_acute,
        here / "x-00931.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
