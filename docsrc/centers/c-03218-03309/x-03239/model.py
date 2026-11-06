"""GEOMETOR construction model for X_3239 = ISOGONAL CONJUGATE OF X_1461."""

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
    mittenpunkt_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03239(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3239 = ISOGONAL CONJUGATE OF X_1461 on reference triangle ABC."""
    X_1461 = point_from_barycentrics(model, A, B, C, 0.13227513, -0.16931217, 1.037037, ID="X_1461", classes=["center"])
    X_3239 = isogonal_conjugate(model, A, B, C, X_1461, ID="X_3239", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_652 = eval_trilinear_point(model, A, B, C, 'sec(B) - sec(C)', ID="X_652", classes=["center", "incident"])
    central_line(model, X_9, X_652, 9, 652, incident=True)
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center", "incident"])
    X_661 = eval_trilinear_point(model, A, B, C, 'cot(B) - cot(C)', ID="X_661", classes=["center", "incident"])
    central_line(model, X_514, X_661, 514, 661, incident=True)
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    X_1309 = eval_trilinear_point(model, A, B, C, '(csc(2*A))/(4*((sin(B))**(2) - (sin(C))**(2))*cos(B)*cos(C) + (sin(B))**(2)*cos(B) - (sin(C))**(2)*cos(C))', ID="X_1309", classes=["center", "incident"])
    central_line(model, X_101, X_1309, 101, 1309, incident=True)
    return promote_point_to_top(model, X_3239)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3239 on the given reference triangle."""
    model = create_model('X_3239 = ISOGONAL CONJUGATE OF X_1461')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03239(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03239.json"))
    write_center_svg(
        model_acute,
        here / "x-03239.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
