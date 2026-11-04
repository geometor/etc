"""GEOMETOR construction model for X_2736 = SR(X_103, X_105)."""

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


def construct_x_02736(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2736 = SR(X_103, X_105) on reference triangle ABC."""
    X_2725 = point_from_barycentrics(model, A, B, C, 0.76388889, -0.28333333, 0.51944444, ID="X_2725", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_2736 = reflection_in_point(model, X_2725, X_3, ID="X_2736", classes=["selected", "target"], guide=False)
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X_103", classes=["center", "incident"])
    X_518 = eval_trilinear_point(model, A, B, C, '(a*b + a*c - b**(2) - c**(2))', ID="X_518", classes=["center", "incident"])
    central_line(model, X_103, X_518, 103, 518, incident=True)
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center", "incident"])
    X_516 = eval_trilinear_point(model, A, B, C, 'b*c*((a - b)*cot(C) + (a - c)*cot(B))', ID="X_516", classes=["center", "incident"])
    central_line(model, X_105, X_516, 105, 516, incident=True)
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center", "incident"])
    X_1292 = eval_trilinear_point(model, A, B, C, '1/((b - c)*(a**(2) + b**(2) + c**(2) - 2*a*b - 2*a*c))', ID="X_1292", classes=["center", "incident"])
    central_line(model, X_514, X_1292, 514, 1292, incident=True)
    return promote_point_to_top(model, X_2736)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2736 on the given reference triangle."""
    model = create_model('X_2736 = SR(X_103, X_105)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02736(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02736.json"))
    write_center_svg(
        model_acute,
        here / "x-02736.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
