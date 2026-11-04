"""GEOMETOR construction model for X_1353 = REFLECTION OF X_5 IN X_6."""

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
    midpoint,
    nine_point_center_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01353(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1353 = REFLECTION OF X_5 IN X_6 on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_193 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cot(B) + cot(C) - cot(A))', ID="X_193", classes=["center"])
    X_1353 = midpoint(model, X_3, X_193, ID="X_1353", classes=["selected", "target"], guide=False)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_5, X_6, 5, 6, incident=True)
    central_line(model, X_3, X_193, 3, 193, incident=True)
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    X_140 = eval_trilinear_point(model, A, B, C, '2*cos(A) + cos(B - C)', ID="X_140", classes=["center", "incident"])
    central_line(model, X_69, X_140, 69, 140, incident=True)
    return promote_point_to_top(model, X_1353)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1353 on the given reference triangle."""
    model = create_model('X_1353 = REFLECTION OF X_5 IN X_6')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01353(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01353.json"))
    write_center_svg(
        model_acute,
        here / "x-01353.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
