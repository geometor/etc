"""GEOMETOR construction model for X_2966 = BARYCENTRIC PRODUCT X_98*X_99."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    midpoint,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02966(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2966 = BARYCENTRIC PRODUCT X_98*X_99 on reference triangle ABC."""
    X_385 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(4) - b**(2)*c**(2))', ID="X_385", classes=["center"])
    X_401 = eval_trilinear_point(model, A, B, C, '(sin(2*B)*sin(2*C) - (sin(2*A))**(2))*(csc(A))', ID="X_401", classes=["center"])
    X_2966 = midpoint(model, X_385, X_401, ID="X_2966", classes=["selected", "target"], guide=False)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center", "incident"])
    central_line(model, X_30, X_98, 30, 98, incident=True)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    X_249 = eval_trilinear_point(model, A, B, C, '(csc(A))*(csc(B - C))**(2)', ID="X_249", classes=["center", "incident"])
    central_line(model, X_99, X_249, 99, 249, incident=True)
    X_230 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*(2*a**(2) - b**(2) - c**(2)) + (b**(2) - c**(2))**(2))', ID="X_230", classes=["center", "incident"])
    X_297 = eval_trilinear_point(model, A, B, C, 'csc(2*A)*cos(A +  omega  )', ID="X_297", classes=["center", "incident"])
    central_line(model, X_230, X_297, 230, 297, incident=True)
    return promote_point_to_top(model, X_2966)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2966 on the given reference triangle."""
    model = create_model('X_2966 = BARYCENTRIC PRODUCT X_98*X_99')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02966(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02966.json"))
    write_center_svg(
        model_acute,
        here / "x-02966.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
