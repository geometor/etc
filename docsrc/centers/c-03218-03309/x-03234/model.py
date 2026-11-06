"""GEOMETOR construction model for X_3234 = VERTEX OF THE INSCRIBED YFF PARABOLA."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03234(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3234 = VERTEX OF THE INSCRIBED YFF PARABOLA on reference triangle ABC."""
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X_190", classes=["center"])
    X_2398 = point_from_barycentrics(model, A, B, C, -1.2222222, 0.33333333, 1.8888889, ID="X_2398", classes=["center"])
    X_3234 = ceva_conjugate(model, A, B, C, X_190, X_2398, ID="X_3234", classes=["selected", "target"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center", "incident"])
    central_line(model, X_101, X_514, 101, 514, incident=True)
    X_118 = point_from_barycentrics(model, A, B, C, 0.28918651, -0.056547619, 0.76736111, ID="X_118", classes=["center", "incident"])
    X_516 = eval_trilinear_point(model, A, B, C, 'b*c*((a - b)*cot(C) + (a - c)*cot(B))', ID="X_516", classes=["center", "incident"])
    central_line(model, X_118, X_516, 118, 516, incident=True)
    X_1633 = eval_trilinear_point(model, A, B, C, '((a**(2) + b**(2) + c**(2) - 2*b*c)/(b - c))', ID="X_1633", classes=["center", "incident"])
    X_2736 = point_from_barycentrics(model, A, B, C, 0.10416667, 1.075, -0.17916667, ID="X_2736", classes=["center", "incident"])
    central_line(model, X_1633, X_2736, 1633, 2736, incident=True)
    return promote_point_to_top(model, X_3234)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3234 on the given reference triangle."""
    model = create_model('X_3234 = VERTEX OF THE INSCRIBED YFF PARABOLA')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03234(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03234.json"))
    write_center_svg(
        model_acute,
        here / "x-03234.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
