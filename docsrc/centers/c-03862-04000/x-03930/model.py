"""GEOMETOR construction model for X_3930 = X_672com[INVERSE(n(INCENTRAL TRIANGLE))]."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    mittenpunkt_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03930(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3930 = X_672com[INVERSE(n(INCENTRAL TRIANGLE))] on reference triangle ABC."""
    X_3930 = eval_barycentric_point(model, A, B, C, '(a*(b + c)*(b**(2) + c**(2) - a*b - a*c))', ID="X_3930", classes=["selected", "target"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    central_line(model, X_37, X_42, 37, 42, incident=True)
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X_226", classes=["center", "incident"])
    X_306 = eval_trilinear_point(model, A, B, C, '(b**(2)*c**(2))*(b + c)*cos(A)', ID="X_306", classes=["center", "incident"])
    central_line(model, X_226, X_306, 226, 306, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_1174 = point_from_barycentrics(model, A, B, C, 0.24963675, 0.33833122, 0.41203203, ID="X_1174", classes=["center", "incident"])
    central_line(model, X_9, X_1174, 9, 1174, incident=True)
    return promote_point_to_top(model, X_3930)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3930 on the given reference triangle."""
    model = create_model('X_3930 = X_672com[INVERSE(n(INCENTRAL TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03930(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03930.json"))
    write_center_svg(
        model_acute,
        here / "x-03930.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
