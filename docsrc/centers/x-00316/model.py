"""GEOMETOR construction model for X(316) = DROUSSENT PIVOT."""

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
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00316(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(316) = DROUSSENT PIVOT on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X(69)", classes=["center"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center"])
    central_line(model, X_4, X_69, 4, 69)
    central_line(model, X_30, X_99, 30, 99)
    X_316 = intersect_lines(model, X_4, X_69, X_30, X_99, ID="X(316)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_187 = eval_trilinear_point(model, A, B, C, 'a*(2*a**(2) - b**(2) - c**(2))', ID="X(187)", classes=["center", "incident"])
    central_line(model, X_2, X_187, 2, 187, incident=True)
    return promote_point_to_top(model, X_316)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(316) on the given reference triangle."""
    model = create_model('X(316) = DROUSSENT PIVOT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00316(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00316.json"))
    write_center_svg(
        model_acute,
        here / "x-00316.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
