"""GEOMETOR construction model for X(850) = BARYCENTRIC MULTIPLIER FOR KIEPERT HYPERBOLA."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isotomic_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00850(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(850) = BARYCENTRIC MULTIPLIER FOR KIEPERT HYPERBOLA on reference triangle ABC."""
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center"])
    X_850 = isotomic_conjugate(model, A, B, C, X_110, ID="X(850)", classes=["selected", "target"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    X_476 = eval_trilinear_point(model, A, B, C, '1/((1 + 2*cos(2*A))*sin(B - C))', ID="X(476)", classes=["center", "incident"])
    central_line(model, X_99, X_476, 99, 476, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_647 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))', ID="X(647)", classes=["center", "incident"])
    central_line(model, X_2, X_647, 2, 647, incident=True)
    X_685 = point_from_barycentrics(model, A, B, C, -0.087629621, 0.32545779, 0.76217183, ID="X(685)", classes=["center", "incident"])
    central_line(model, X_110, X_685, 110, 685, incident=True)
    return promote_point_to_top(model, X_850)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(850) on the given reference triangle."""
    model = create_model('X(850) = BARYCENTRIC MULTIPLIER FOR KIEPERT HYPERBOLA')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00850(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00850.json"))
    write_center_svg(
        model_acute,
        here / "x-00850.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
