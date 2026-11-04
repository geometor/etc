"""GEOMETOR construction model for X_2820 = ISOGONAL CONJUGATE OF X_2736."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02820(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2820 = ISOGONAL CONJUGATE OF X_2736 on reference triangle ABC."""
    X_2736 = point_from_barycentrics(model, A, B, C, 0.10416667, 1.075, -0.17916667, ID="X_2736", classes=["center"])
    X_2820 = isogonal_conjugate(model, A, B, C, X_2736, ID="X_2820", classes=["selected", "target"])
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X_103", classes=["center", "incident"])
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center", "incident"])
    central_line(model, X_103, X_105, 103, 105, incident=True)
    X_118 = point_from_barycentrics(model, A, B, C, 0.28918651, -0.056547619, 0.76736111, ID="X_118", classes=["center", "incident"])
    X_120 = eval_trilinear_point(model, A, B, C, 'b*c*(2*a*b*c - (b + c)*(a**(2) + (b - c)**(2)))*(b**(2) + c**(2) - a*b -a*c)', ID="X_120", classes=["center", "incident"])
    central_line(model, X_118, X_120, 118, 120, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    return promote_point_to_top(model, X_2820)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2820 on the given reference triangle."""
    model = create_model('X_2820 = ISOGONAL CONJUGATE OF X_2736')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02820(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02820.json"))
    write_center_svg(
        model_acute,
        here / "x-02820.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
