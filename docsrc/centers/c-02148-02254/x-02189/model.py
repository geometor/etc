"""GEOMETOR construction model for X_2189 = X_2-ISOCONJUGATE OF X_201."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02189(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2189 = X_2-ISOCONJUGATE OF X_201 on reference triangle ABC."""
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center"])
    X_270 = eval_trilinear_point(model, A, B, C, '(sec(A))/(1 + cos(B - C))', ID="X_270", classes=["center"])
    central_line(model, X_19, X_112, 19, 112)
    central_line(model, X_21, X_270, 21, 270)
    X_2189 = intersect_lines(model, X_19, X_112, X_21, X_270, ID="X_2189", classes=["selected", "target"])
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X_27", classes=["center", "incident"])
    X_272 = eval_trilinear_point(model, A, B, C, '(1/((sin(A) + sin(A - B) + sin(A - C))*(sin(B) + sin(C))))', ID="X_272", classes=["center", "incident"])
    central_line(model, X_27, X_272, 27, 272, incident=True)
    return promote_point_to_top(model, X_2189)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2189 on the given reference triangle."""
    model = create_model('X_2189 = X_2-ISOCONJUGATE OF X_201')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02189(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02189.json"))
    write_center_svg(
        model_acute,
        here / "x-02189.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
