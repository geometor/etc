"""GEOMETOR construction model for X_2740 = SR(X_103, X_111)."""

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
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_02740(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2740 = SR(X_103, X_111) on reference triangle ABC."""
    X_2729 = point_from_barycentrics(model, A, B, C, 0.71174829, -0.30626744, 0.59451916, ID="X_2729", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_2740 = reflection_in_point(model, X_2729, X_3, ID="X_2740", classes=["selected", "target"], guide=False)
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X_103", classes=["center", "incident"])
    X_524 = eval_trilinear_point(model, A, B, C, '(2*a**(2) - b**(2) - c**(2))/a', ID="X_524", classes=["center", "incident"])
    central_line(model, X_103, X_524, 103, 524, incident=True)
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X_111", classes=["center", "incident"])
    X_516 = eval_trilinear_point(model, A, B, C, 'b*c*((a - b)*cot(C) + (a - c)*cot(B))', ID="X_516", classes=["center", "incident"])
    central_line(model, X_111, X_516, 111, 516, incident=True)
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    X_1499 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))*(b**(2) + c**(2) - 5*a**(2))', ID="X_1499", classes=["center", "incident"])
    central_line(model, X_101, X_1499, 101, 1499, incident=True)
    return promote_point_to_top(model, X_2740)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2740 on the given reference triangle."""
    model = create_model('X_2740 = SR(X_103, X_111)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02740(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02740.json"))
    write_center_svg(
        model_acute,
        here / "x-02740.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
