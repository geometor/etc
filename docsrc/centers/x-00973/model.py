"""GEOMETOR construction model for X(973) = 1st EHRMANN POINT."""

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
    nine_point_center_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00973(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(973) = 1st EHRMANN POINT on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X(24)", classes=["center"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X(51)", classes=["center"])
    central_line(model, X_6, X_24, 6, 24)
    central_line(model, X_5, X_51, 5, 51)
    X_973 = intersect_lines(model, X_6, X_24, X_5, X_51, ID="X(973)", classes=["selected", "target"])
    X_68 = eval_trilinear_point(model, A, B, C, 'cos(A)*sec(2*A)', ID="X(68)", classes=["center", "incident"])
    X_568 = eval_trilinear_point(model, A, B, C, 'a*(3*R**(2)*(b**(2) + c**(2) - a**(2)) + a**(2)*b**(2) + a**(2)*c**(2) - b**(4) - c**(4))', ID="X(568)", classes=["center", "incident"])
    central_line(model, X_68, X_568, 68, 568, incident=True)
    return promote_point_to_top(model, X_973)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(973) on the given reference triangle."""
    model = create_model('X(973) = 1st EHRMANN POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00973(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00973.json"))
    write_center_svg(
        model_acute,
        here / "x-00973.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
