"""GEOMETOR construction model for X_3508 = INTERSECTION OF LINES X_1X_6 AND X_76X_1423."""

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
    incenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03508(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3508 = INTERSECTION OF LINES X_1X_6 AND X_76X_1423 on reference triangle ABC."""
    X_385 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(4) - b**(2)*c**(2))', ID="X_385", classes=["center"])
    X_3507 = eval_trilinear_point(model, A, B, C, '(a**(3)*(b + c) - (a**(2) + b*c)*(b**(2) + b*c + c**(2)) + a*(b + c)*(b**(2) + c**(2)))', ID="X_3507", classes=["center"])
    X_3508 = ceva_conjugate(model, A, B, C, X_385, X_3507, ID="X_3508", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center", "incident"])
    X_813 = eval_trilinear_point(model, A, B, C, '1/(a**(-2)*(b**(1) - c**(1)) + a**(0)*(b**(-1) - c **(-1)))', ID="X_813", classes=["center", "incident"])
    central_line(model, X_98, X_813, 98, 813, incident=True)
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    X_983 = eval_trilinear_point(model, A, B, C, '(1/(b**(2) - b*c + c**(2)))', ID="X_983", classes=["center", "incident"])
    central_line(model, X_32, X_983, 32, 983, incident=True)
    return promote_point_to_top(model, X_3508)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3508 on the given reference triangle."""
    model = create_model('X_3508 = INTERSECTION OF LINES X_1X_6 AND X_76X_1423')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03508(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03508.json"))
    write_center_svg(
        model_acute,
        here / "x-03508.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
