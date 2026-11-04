"""GEOMETOR construction model for X_2684 = RS(X_99, X_101)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_02684(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2684 = RS(X_99, X_101) on reference triangle ABC."""
    X_2681 = point_from_barycentrics(model, A, B, C, 0.43640713, 0.023754536, 0.53983834, ID="X_2681", classes=["center"])
    X_118 = point_from_barycentrics(model, A, B, C, 0.28918651, -0.056547619, 0.76736111, ID="X_118", classes=["center"])
    X_2684 = reflection_in_point(model, X_2681, X_118, ID="X_2684", classes=["selected", "target"], guide=False)
    X_114 = eval_trilinear_point(model, A, B, C, 'b*c*(b*sec(B +  omega  ) + c*sec(C +  omega  ))', ID="X_114", classes=["center", "incident"])
    X_325 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)', ID="X_325", classes=["center", "incident"])
    central_line(model, X_114, X_325, 114, 325, incident=True)
    X_516 = eval_trilinear_point(model, A, B, C, 'b*c*((a - b)*cot(C) + (a - c)*cot(B))', ID="X_516", classes=["center", "incident"])
    central_line(model, X_118, X_516, 118, 516, incident=True)
    return promote_point_to_top(model, X_2684)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2684 on the given reference triangle."""
    model = create_model('X_2684 = RS(X_99, X_101)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02684(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02684.json"))
    write_center_svg(
        model_acute,
        here / "x-02684.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
