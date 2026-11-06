"""GEOMETOR construction model for X_3453 = 1st SARAGOSSA POINT OF X_10."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03453(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3453 = 1st SARAGOSSA POINT OF X_10 on reference triangle ABC."""
    X_3453 = eval_trilinear_point(model, A, B, C, '(a/ ((b + c)*( a*(b**(2) + c**(2)) + b**(3) + c**(3) )))', ID="X_3453", classes=["selected", "target"])
    X_60 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(B - C))', ID="X_60", classes=["center", "incident"])
    X_386 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) + b*c + c*a + a*b)', ID="X_386", classes=["center", "incident"])
    central_line(model, X_60, X_386, 60, 386, incident=True)
    X_404 = eval_trilinear_point(model, A, B, C, '(b*c*(a + b + c) - a*(b**(2) + c**(2) - a**(2)))', ID="X_404", classes=["center", "incident"])
    X_849 = eval_trilinear_point(model, A, B, C, '(a/(b + c))**(2)', ID="X_849", classes=["center", "incident"])
    central_line(model, X_404, X_849, 404, 849, incident=True)
    X_261 = eval_trilinear_point(model, A, B, C, '(((csc(A))*(sec(B/2 - C/2)))**(2))', ID="X_261", classes=["center", "incident"])
    X_1078 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(2)*c**(2) + c**(2)*a**(2) + a**(2)*b**(2) - a**(4)))', ID="X_1078", classes=["center", "incident"])
    central_line(model, X_261, X_1078, 261, 1078, incident=True)
    return promote_point_to_top(model, X_3453)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3453 on the given reference triangle."""
    model = create_model('X_3453 = 1st SARAGOSSA POINT OF X_10')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03453(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03453.json"))
    write_center_svg(
        model_acute,
        here / "x-03453.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
