"""GEOMETOR construction model for X_2825 = ISOGONAL CONJUGATE OF X_2741."""

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


def construct_x_02825(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2825 = ISOGONAL CONJUGATE OF X_2741 on reference triangle ABC."""
    X_2741 = point_from_barycentrics(model, A, B, C, 1.0279659, 0.40414514, -0.43211102, ID="X_2741", classes=["center"])
    X_2825 = isogonal_conjugate(model, A, B, C, X_2741, ID="X_2825", classes=["selected", "target"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X_103", classes=["center", "incident"])
    central_line(model, X_58, X_103, 58, 103, incident=True)
    X_118 = point_from_barycentrics(model, A, B, C, 0.28918651, -0.056547619, 0.76736111, ID="X_118", classes=["center", "incident"])
    X_127 = eval_trilinear_point(model, A, B, C, 'b*c*(sin(2*B) - sin(2*C))*((b**(2) - c**(2))*sin(2*A) - b**(2)*sin(2*B) + c**(2)*sin(2*C))', ID="X_127", classes=["center", "incident"])
    central_line(model, X_118, X_127, 118, 127, incident=True)
    X_116 = eval_trilinear_point(model, A, B, C, 'b*c*((b - c)**(2)*(b**(2) + b*c + c**(2) - a*b - a*c))', ID="X_116", classes=["center", "incident"])
    X_132 = point_from_barycentrics(model, A, B, C, 0.11002416, 0.049913231, 0.84006261, ID="X_132", classes=["center", "incident"])
    central_line(model, X_116, X_132, 116, 132, incident=True)
    return promote_point_to_top(model, X_2825)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2825 on the given reference triangle."""
    model = create_model('X_2825 = ISOGONAL CONJUGATE OF X_2741')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02825(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02825.json"))
    write_center_svg(
        model_acute,
        here / "x-02825.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
