"""GEOMETOR construction model for X(754) = EVEN (0, 4) INFINITY POINT."""

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
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00754(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(754) = EVEN (0, 4) INFINITY POINT on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X(32)", classes=["center"])
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X(115)", classes=["center"])
    X_316 = point_from_barycentrics(model, A, B, C, 3.0207852, 1.1662818, -3.187067, ID="X(316)", classes=["center"])
    central_line(model, X_2, X_32, 2, 32)
    central_line(model, X_115, X_316, 115, 316)
    X_754 = intersect_lines(model, X_2, X_32, X_115, X_316, ID="X(754)", classes=["selected", "target"])
    X_187 = eval_trilinear_point(model, A, B, C, 'a*(2*a**(2) - b**(2) - c**(2))', ID="X(187)", classes=["center", "incident"])
    X_325 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(4) + c**(4) - a**(2)*b**(2) - a**(2)*c**(2))', ID="X(325)", classes=["center", "incident"])
    central_line(model, X_187, X_325, 187, 325, incident=True)
    return promote_point_to_top(model, X_754)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(754) on the given reference triangle."""
    model = create_model('X(754) = EVEN (0, 4) INFINITY POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00754(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00754.json"))
    write_center_svg(
        model_acute,
        here / "x-00754.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
