"""GEOMETOR construction model for X_1261 = ISOGONAL CONJUGATE OF X_1122."""

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
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01261(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1261 = ISOGONAL CONJUGATE OF X_1122 on reference triangle ABC."""
    X_1122 = eval_trilinear_point(model, A, B, C, '((a*(b + c) + (b - c)**(2))/(b + c - a))', ID="X_1122", classes=["center"])
    X_1261 = isogonal_conjugate(model, A, B, C, X_1122, ID="X_1261", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    central_line(model, X_8, X_56, 8, 56, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_200 = eval_trilinear_point(model, A, B, C, '(cot(A/2))**(2)', ID="X_200", classes=["center", "incident"])
    central_line(model, X_31, X_200, 31, 200, incident=True)
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center", "incident"])
    X_728 = eval_trilinear_point(model, A, B, C, '((b + c - a)**(3))', ID="X_728", classes=["center", "incident"])
    central_line(model, X_41, X_728, 41, 728, incident=True)
    return promote_point_to_top(model, X_1261)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1261 on the given reference triangle."""
    model = create_model('X_1261 = ISOGONAL CONJUGATE OF X_1122')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01261(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01261.json"))
    write_center_svg(
        model_acute,
        here / "x-01261.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
