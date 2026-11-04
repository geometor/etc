"""GEOMETOR construction model for X_1414 = X_99-BETH CONJUGATE OF X_99."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01414(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1414 = X_99-BETH CONJUGATE OF X_99 on reference triangle ABC."""
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center"])
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X_85", classes=["center"])
    X_603 = eval_trilinear_point(model, A, B, C, '(cos(A))**(2) - cos(A)', ID="X_603", classes=["center"])
    central_line(model, X_99, X_109, 99, 109)
    central_line(model, X_85, X_603, 85, 603)
    X_1414 = intersect_lines(model, X_99, X_109, X_85, X_603, ID="X_1414", classes=["selected", "target"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_757 = eval_trilinear_point(model, A, B, C, '(b + c) **(-2)', ID="X_757", classes=["center", "incident"])
    central_line(model, X_7, X_757, 7, 757, incident=True)
    return promote_point_to_top(model, X_1414)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1414 on the given reference triangle."""
    model = create_model('X_1414 = X_99-BETH CONJUGATE OF X_99')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01414(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01414.json"))
    write_center_svg(
        model_acute,
        here / "x-01414.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
