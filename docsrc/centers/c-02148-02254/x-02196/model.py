"""GEOMETOR construction model for X_2196 = X_2-ISOCONJUGATE OF X_242."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02196(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2196 = X_2-ISOCONJUGATE OF X_242 on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_295 = eval_trilinear_point(model, A, B, C, '(cos(A))/(a**(2) - b*c)', ID="X_295", classes=["center"])
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X_28", classes=["center"])
    X_291 = eval_trilinear_point(model, A, B, C, '1/(a**(2) - b*c)', ID="X_291", classes=["center"])
    central_line(model, X_3, X_295, 3, 295)
    central_line(model, X_28, X_291, 28, 291)
    X_2196 = intersect_lines(model, X_3, X_295, X_28, X_291, ID="X_2196", classes=["selected", "target"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_292 = eval_trilinear_point(model, A, B, C, 'a/(a**(2) - b*c)', ID="X_292", classes=["center", "incident"])
    central_line(model, X_56, X_292, 56, 292, incident=True)
    return promote_point_to_top(model, X_2196)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2196 on the given reference triangle."""
    model = create_model('X_2196 = X_2-ISOCONJUGATE OF X_242')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02196(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02196.json"))
    write_center_svg(
        model_acute,
        here / "x-02196.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
