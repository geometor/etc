"""GEOMETOR construction model for X_1566 = ORTHOJOIN OF X_676."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01566(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1566 = ORTHOJOIN OF X_676 on reference triangle ABC."""
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center"])
    X_516 = eval_trilinear_point(model, A, B, C, 'b*c*((a - b)*cot(C) + (a - c)*cot(B))', ID="X_516", classes=["center"])
    X_1566 = crosspoint(model, A, B, C, X_514, X_516, ID="X_1566", classes=["selected", "target"])
    X_132 = point_from_barycentrics(model, A, B, C, 0.11002416, 0.049913231, 0.84006261, ID="X_132", classes=["center", "incident"])
    X_242 = eval_trilinear_point(model, A, B, C, '((sec(A))*((sin(A))**(2) - sin(B)*sin(C)))', ID="X_242", classes=["center", "incident"])
    central_line(model, X_132, X_242, 132, 242, incident=True)
    X_116 = eval_trilinear_point(model, A, B, C, 'b*c*((b - c)**(2)*(b**(2) + b*c + c**(2) - a*b - a*c))', ID="X_116", classes=["center", "incident"])
    central_line(model, X_116, X_514, 116, 514, incident=True)
    X_118 = point_from_barycentrics(model, A, B, C, 0.28918651, -0.056547619, 0.76736111, ID="X_118", classes=["center", "incident"])
    central_line(model, X_118, X_516, 118, 516, incident=True)
    return promote_point_to_top(model, X_1566)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1566 on the given reference triangle."""
    model = create_model('X_1566 = ORTHOJOIN OF X_676')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01566(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01566.json"))
    write_center_svg(
        model_acute,
        here / "x-01566.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
